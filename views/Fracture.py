import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
from io import BytesIO
import base64
import time

# CSS for styling
st.markdown("""
    <style>
    .custom-button {
        background-color: #1e8449;
        color: white;
        border: none; 
        padding: 10px 20px; 
        font-size: 16px; 
        cursor: pointer; 
        border-radius: 5px;
        transition: background-color 0.3s ease; 
    }
    .custom-button:hover {
        background-color: #145a32;
    }
    .image-box {
        width: 308px; 
        height: 308px;
        border: 2px dashed #000;
        border-radius: 5px; 
        display: flex;
        align-items: center;
        justify-content: center;
        margin-top: 15px;
        background-color: #ffffff;
        overflow: hidden;
        
    }
    .image-box img {
        max-width: 100%;
        max-height: 100%;
        object-fit: contain;
    }
    .button-container {
        margin-top: 20px; 
    }
     .predict-gap {
        margin-top: 25px;
    }
    </style>
""", unsafe_allow_html=True)

# TensorFlow Model Prediction
def model_prediction(test_image):
    model = tf.keras.models.load_model('trained_fracture_classification_model.keras')
    image = tf.keras.preprocessing.image.load_img(test_image, target_size=(288, 288))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr])  # Convert single image to batch
    predictions = model.predict(input_arr)
    return np.argmax(predictions)  # Return index of max element

st.title("Fracture Classification 🏥")

# Initialize session state
if "show_image_clicked" not in st.session_state:
    st.session_state.show_image_clicked = False

# Upload Image
test_image = st.file_uploader("Choose a Bone X-ray Image:")

# Convert image to base64
def image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# Display buttons and image preview area
if st.button("Show Image"):
    if test_image:
        st.session_state.show_image_clicked = True

if st.session_state.show_image_clicked:
    if test_image:
        img = Image.open(test_image)
        img_base64 = image_to_base64(img)
        img_html = f"""
            <div class="image-box">
                <img src="data:image/png;base64,{img_base64}" alt="Image Preview">
            </div>
        """
        st.markdown(img_html, unsafe_allow_html=True)
else:
    st.markdown("""
        <div class="image-box">
            <img id="image-preview" src="https://via.placeholder.com/268" alt="Image Preview">
        </div>
    """, unsafe_allow_html=True)

# Add gap before the Predict button
st.markdown('<div class="predict-gap"></div>', unsafe_allow_html=True)

# Display Predict button
if st.button("Predict"):
    if test_image:
        with st.spinner("Processing..."):
            time.sleep(0.05)  # Add a short delay for the spinner to show
            result_index = model_prediction(test_image)
            class_name = ['Fractured', 'Non_fractured']
            st.success(f"Model is Predicting it's a {class_name[result_index]}")
