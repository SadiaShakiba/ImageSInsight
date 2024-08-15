import streamlit as st

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
        margin-top: 20px;
        background-color: #ffffff;
    }
    .image-box img {
        max-width: 100%;
        max-height: 100%;
    }
      .button-container {
        margin-top: 20px; 
    }
    </style>
""", unsafe_allow_html=True)


st.title("Polyp Segmentation 🏥")

test_image = st.file_uploader("Choose a Polyp Image:")

st.markdown('<button class="custom-button">Show Image</button>', unsafe_allow_html=True)

st.markdown("""
    <div class="image-box">
        <img id="image-preview" src="https://via.placeholder.com/268" alt="Image Preview">
    </div>
""", unsafe_allow_html=True)
    

st.markdown('<div class="button-container"><button class="custom-button">Segment</button></div>', unsafe_allow_html=True)
    
st.markdown("""
    <div class="image-box">
        <img id="image-preview" src="https://via.placeholder.com/388" alt="Image Preview">
    </div>
""", unsafe_allow_html=True)