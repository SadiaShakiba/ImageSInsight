# ImageSInsight (OVERVIEW)

This is a cutting-edge application designed to revolutionize image analysis with advanced classification and segmentation capabilities for study purpose only. By leveraging state-of-the-art & modified algorithms, ImageInsight offers users an intuitive platform to analyze a variety of images. Whether it's identifying plant diseases, distinguishing between fractures and non-fractures, segmenting polyps, or classifying agricultural leaves, ImageInsight delivers accurate and insightful results. This powerful tool combines ease of use with sophisticated technology to provide actionable insights from your images, making it an indispensable resource for researchers, healthcare professionals, and agricultural experts.

**Feature's:-**
* __Comprehensive Image Analysis:__ Classify and analyze plant diseases, fractures, polyps, and agricultural leaves.
* __Advanced Algorithms:__ Utilizes cutting-edge technology for precise and reliable results.
* __User-Friendly Interface:__ Intuitive design for easy navigation and quick access to results.
* __Innovative Technology:__ Combines modern AI techniques with a sleek user experience for enhanced functionality.

# Implementation
* __Frontend:__ **Streamlit** is used to build the frontend of ImageInsight, providing a user-friendly interface for image upload, visualization, and prediction. The interface includes features like image previews, 
                custom-styled buttons, and progress indicators to enhance user experience.
* __Backend:__ The backend of ImageInsight is integrated directly into the Streamlit frontend. The model, trained to classify plant diseases, is loaded and used for predictions within the same script that powers 
                the Streamlit application. 
    * __Machine Learning:__ TensorFlow
    * __Image Processing:__ PIL, OpenCV

# Interface Design
__Homepage__
![alt_img](https://github.com/SadiaShakiba/ImageSInsight/blob/db50bffff782553013e2a3578eaae9cc4e561b65/image7.png)
__Menubar__
![alt_img1](https://github.com/SadiaShakiba/ImageSInsight/blob/e95d5173c3efb6f82ad2d2e574470f604a848764/image3.png)
__PlantDiseasePrediction__
![alt_img2](https://github.com/SadiaShakiba/ImageSInsight/blob/e95d5173c3efb6f82ad2d2e574470f604a848764/image4.png)
__PlantDiseasePrediction(after show button)__
![alt_img3](https://github.com/SadiaShakiba/ImageSInsight/blob/52aa343e74c46cee724c39a3a9d80150c8643426/image8.png)
__PlantDiseasePrediction(after predict button)__
![alt_img4](https://github.com/SadiaShakiba/ImageSInsight/blob/52aa343e74c46cee724c39a3a9d80150c8643426/image9.png)
__FractureClassification__
![alt_img5](https://github.com/SadiaShakiba/ImageSInsight/blob/29f1f8a7cfff4b0c82e3b8aba35a7ffb0ac2b66b/image10.png)
__PolypSegmentation__
![alt_img6](https://github.com/SadiaShakiba/ImageSInsight/blob/e95d5173c3efb6f82ad2d2e574470f604a848764/image6.png)

# Reference Papers
* [Fracture Classification](https://ieeexplore.ieee.org/abstract/document/10534439)
* [Polyp Segmentation](https://arxiv.org/abs/2407.19327)
