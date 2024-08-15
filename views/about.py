import streamlit as st

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assests/ImageSInsight_2.png", width=280)

with col2:
    st.title("ImageSInsight", anchor=False)
    st.write(
        "**ImageInsight** is a cutting-edge application designed to revolutionize image analysis with advanced classification and segmentation capabilities for **study purpose only**. "
    )

# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.subheader("Details:", anchor=False)
st.write(
    """
    By leveraging state-of-the-art & modified algorithms, ImageInsight offers users an intuitive platform to analyze a variety of
      images. Whether it's identifying plant diseases, distinguishing between fractures and non-fractures, segmenting polyps, or 
      classifying agricultural leaves, ImageInsight delivers accurate and insightful results. This powerful tool combines ease of
        use with sophisticated technology to provide actionable insights from your images, making it an indispensable resource 
        for researchers, healthcare professionals, and agricultural experts.
    - **Comprehensive Image Analysis:** Classify and analyze plant diseases, fractures, polyps, and agricultural leaves.
    - **Advanced Algorithms:** Utilizes cutting-edge technology for precise and reliable results.
    - **User-Friendly Interface:** Intuitive design for easy navigation and quick access to results.
    - **Innovative Technology:** Combines modern AI techniques with a sleek user experience for enhanced functionality.
    """
)
