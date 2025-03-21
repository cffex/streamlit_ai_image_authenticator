import numpy as np
import streamlit as st

from PIL import Image
from keras import models

import time

model: models.Sequential = models.load_model("src/model_file/model.keras")
image_shape = (768, 512, 3)

def show_model():
    st.header("Description 📝")
    st.write(
        """
        This is a **Convolutional Neural Network (C.N.N)** that processes images.
        """
    )
    st.divider()

    st.header("Clarification ℹ️")
    st.write(
        """
        The file type should be: PNG, JPEG, JPG.
        \nThe file size should be: (width, height) = (768, 512) *(This is optional, but works best as the model was trained on this particular dimension)*
        """
    )
    st.divider()

    st.header("Usage 🔧")
    st.write("Simply upload an image and the model will do the analysis.")
    st.divider()

    ##
    ##
    ##

    uploaded_file = st.file_uploader("Choose an image file", type=["png", "jpeg", "jpg"])

    if uploaded_file is not None:
        with Image.open(uploaded_file) as pil_image:
            #st.image(image, caption="Uploaded image.")

            global prediction

            with st.spinner("Processing the image..."):
                resized_image = pil_image.resize((image_shape[0], image_shape[1]))

                if resized_image.mode != "RGB":
                    resized_image = resized_image.convert('RGB')

                np_image = np.array(resized_image).astype("float32")
                np_image /= 255.0

                reshaped_image_array = np.expand_dims(np_image.transpose((1,0,2)), axis=0)
                prediction = model.predict(x=reshaped_image_array)
                time.sleep(2)

            success_placeholder = st.empty()
            success_placeholder.success(body="Completed.", icon="✅")
            
            with st.spinner("Visualizing results..."):
                time.sleep(2)
                success_placeholder.empty()
