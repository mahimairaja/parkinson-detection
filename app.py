import streamlit as st
from PIL import Image 
import os
import cv2
from modules import *


def processImage():
    """
        UI Part if the users chooses
        to proceess a image.
    """
    # load the model
    model = setup()
    # load the image
    image_file = st.file_uploader("Upload An Image",type=['png','jpeg','jpg'])
    # check if the image is uploaded
    if image_file is not None:
        # get the file details
        file_details = {"FileName":image_file.name,"FileType":image_file.type}
        file_type = (image_file.type).split('/')[1]
        # make a directory to store the image
        if not os.path.exists(os.path.join(os.getcwd(),"data")):
            os.makedirs(os.path.join(os.getcwd(),"data"))
        # save the image
        input_file_name = f"data/Input.{file_type}"
        with open(input_file_name,mode = "wb") as f: 
            f.write(image_file.getbuffer())    
        # predict the image and save it
        result_frame, labels = predict(input_file_name,model)
        cv2.imwrite('data/result.jpg', result_frame)
        # display the image and class
        img_ = Image.open(f"data/result.jpg")
        result_class = " ".join(labels).split()[0]
        confidence = float(" ".join(labels).split()[1])
        
        st.subheader(f"Result {result_class} with confidence {confidence * 100 :.2f}%")
        st.image(img_)
        # To download the image
        with open("data/result.jpg", "rb") as file:
            st.download_button(
                    label="Download image",
                    data=file,
                    file_name="predicted.jpg",
                    mime="image/jpg"
                ) 


def main():
        """
            UI Part of the entire application.
        """
        st.set_page_config(
            page_title ="Parkinson-X",
            page_icon = "🧊",
            menu_items={
        'About': "# Parkinson's Prediction"
            } 
        )    
        st.markdown("<h1 style='text-align: center;'>Parkinson's <span style='color: #9eeade;'>Prediction</span></h1>", unsafe_allow_html=True)  
        st.subheader("Early Parkinson's detection")

        st.title('Drawing Analysis')
        
        processImage()
        with st.expander("Parkinson's Prediction"):
            st.markdown( "<p style='font-size: 30px;'><strong>Welcome to the Parkinson's  \
                <span style='color: #9eeade;'>Prediction</span> App!</strong></p>", unsafe_allow_html= True)
            st.markdown("<p style = 'font-size : 20px; color : white;'>This application was \
                built  to analyse the <strong>spiral drawings</strong> \
                    to predict and suggest parkinson diagnosis.</p>", unsafe_allow_html=True)

if __name__ == '__main__':
    __author__ = 'Mahimai Raja J'
    __version__ = "1.0.0"
    main()

# 📌 NOTE :
# Do not modify the credits unless you have 
# legal permission from the authorizing authority .

# Thank you for helping to maintain the integrity of the 
# open source community by promoting fair and ethical 
# use of open source software 💎.