# Import necessary libraries
from django.shortcuts import render
from .models import Image
from .forms import ImageForm
import cv2
import numpy as np
from joblib import load
import os

# Get the path to the models folder
models_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'models')
svm_classifier = load(os.path.join(models_path, 'emotion_classifier.joblib'))

# Assuming you have defined 'width' and 'height' for resizing
width = 100
height = 100

# Define the predict_class function
def predict_class(image_path):
    # Load the new image
    new_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

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
        return "Error: Could not load the new image. Please check the file path."

# Define the classify view
def classify(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()
            predicted_class = predict_class(image.image.path)  # Use the predict_class function

            # Render the result template with predicted class and image URL
            return render(request, 'emotion_classifier/result.html', {'predicted_class': predicted_class, 'image_url': image.image.url})
    else:
        form = ImageForm()
        
    return render(request, 'emotion_classifier/index.html', {'form': form})  # Update template name to 'index.html'
