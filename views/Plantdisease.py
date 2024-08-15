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
        width: 288px; 
        height: 288px;
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
    cnn = tf.keras.models.load_model('trained_plant_disease_model.keras')
    image = tf.keras.preprocessing.image.load_img(test_image, target_size=(128, 128))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.array([input_arr])  # Convert single image to batch
    predictions = cnn.predict(input_arr)
    return np.argmax(predictions)  # Return index of max element

st.title("Plant Disease Prediction 🌿")

# Initialize session state
if "show_image_clicked" not in st.session_state:
    st.session_state.show_image_clicked = False

# Upload Image
test_image = st.file_uploader("Choose a Plant Leaf Image:")

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
            class_name = ['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
                          'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 
                          'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 
                          'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 
                          'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 
                          'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot',
                          'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 
                          'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy', 
                          'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 
                          'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 
                          'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 
                          'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 
                          'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus',
                          'Tomato___healthy']
            st.success(f"Model is Predicting it's a {class_name[result_index]}")
