# views.py
from django.shortcuts import render
from .forms import ClassificationForm
import cv2
import numpy as np
from joblib import load
import os

# Get the path to the models folder
models_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'classifier', 'models')
svm_classifier = load(os.path.join(models_path, 'emotion_classifier.joblib'))

# Assuming you have defined 'width' and 'height' for resizing
width = 100
height = 100

# Define the predict_class function
def predict_class(image):
    new_image = cv2.imdecode(np.frombuffer(image.read(), np.uint8), cv2.IMREAD_GRAYSCALE)

    if new_image is not None:
        new_image = cv2.resize(new_image, (width, height))  # Resize
        new_feature = new_image.flatten() / 255.0  # Normalize and Flatten
        new_feature = np.array([new_feature])  # Convert to NumPy array
        predicted_class = svm_classifier.predict(new_feature)[0]

        if predicted_class == 0:
            return "Sad"
        elif predicted_class == 1:
            return "Happy"
    else:
        return "Error: Could not process the image."

def classify(request):
    if request.method == 'POST':
        form = ClassificationForm(request.POST, request.FILES)
        if form.is_valid():
            prediction = predict_class(request.FILES['image'])

            # Render the result template with predicted class
            return render(request, 'classifier/result.html', {'predicted_class': prediction})
    else:
        form = ClassificationForm()
        
    return render(request, 'classifier/index.html', {'form': form})
