import streamlit as st
import numpy as np
import tensorflow as tf

from PIL import Image

interpreter = tf.lite.Interpreter(model_path="src/model_file/model_quantized.tflite")
interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

def render_home():
    st.set_page_config(
        page_title="A.I Image Authenticator",
        page_icon="🤖",
    )

    st.write("# AI Image Authenticator")

    with st.expander("Description", expanded=True):
        st.write(
            """
            This is a simple web application that uses a pre-trained model to determine whether an image is likely to be generated by A.I. or not.
            """
        )
        st.write("### How to use")
        st.write(
            """
            1. Upload an image file in PNG or JPEG format.
            2. The model will process the image and provide a prediction.
            3. The result will indicate whether the image is likely to be A.I.-generated or not, along with the probabilities (how likely a prediction is).
            """
        )

    uploader = st.file_uploader("Choose an image file", type=["png", "jpeg", "jpg"])

    st.divider()

    if uploader is not None:
        with Image.open(uploader) as pil_image:
            with st.expander("Preview image"):
                st.image(pil_image, caption="Uploaded Image", use_container_width=True)

            st.success("Image uploaded successfully!")

            with st.spinner("Processing the image..."):
                resized_image = pil_image.resize((224, 224))

                if resized_image.mode != "RGB":
                    resized_image = resized_image.convert('RGB')

                np_image = np.array(resized_image).astype("float32")
                np_image /= 255.0

                input_data = np.expand_dims(np_image.transpose((1, 0, 2)), axis=0).astype(np.float32)
                interpreter.set_tensor(input_details[0]['index'], input_data)
                interpreter.invoke()

                prediction = interpreter.get_tensor(output_details[0]['index'])

                non_ai_prob = prediction[0][0]
                ai_prob = prediction[0][1]
                delta = non_ai_prob - ai_prob
                text = ""

                if delta >= 0:
                    text = "### :green[It is likely not A.I-generated.]"
                elif delta < 0:
                    text = "### :red[It is likely A.I-generated.]"

                st.markdown(text)
                st.write(f"Probability of not A.I-generated: {non_ai_prob*100:.2f}%")
                st.write(f"Probability of A.I-generated: {ai_prob*100:.2f}%")


render_home()