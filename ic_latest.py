import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model


model = load_model('models/imageclassifier.h5')


classes = ['Happy', 'Sad']


def preprocess_image(image):
    image = tf.image.resize(image, (256, 256))
    image = tf.cast(image, tf.float32) / 255.0
    return tf.expand_dims(image, 0)


st.title("Image Classifier App")


uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True) 

    
    image = Image.open(uploaded_file)
    image = np.array(image)
    image = preprocess_image(image)

    
    prediction = model.predict(image)


    st.write(f"Prediction: {classes[int(prediction[0][0] > 0.5)]}")

