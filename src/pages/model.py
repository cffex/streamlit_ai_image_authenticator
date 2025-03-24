import numpy as np
import streamlit as st

from PIL import Image
from keras import models
import time

model: models.Sequential = models.load_model("src/model_file/model.keras")
image_shape = (768, 512, 3)

def show_model():
    st.title("Model 🤖")
    st.divider()

    st.header("Usage 🔧")
    st.write("Simply upload an image and the model will do the analysis.")
    st.divider()

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

            prob_not_ai = prediction[0][0]
            prob_ai = prediction[0][1]
            delta = prob_not_ai - prob_ai
            text = ""

            if delta > 0:
                text = "### :green[It is likely not A.I-generated.]"
            elif delta < 0:
                text = "### :red[It is likely A.I-generated.]"

            print(prob_not_ai, "not ai")
            print(prob_ai, "ai")
            
            st.write(text)
