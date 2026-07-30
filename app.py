"""
GET 324 Mini-Project (CE4)
Fresh Apple vs Formalin-mixed Apple Classifier
Streamlit web application

Deployment: Streamlit Community Cloud (https://share.streamlit.io)
"""

import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# -----------------------------------------------------------------
# IMPORTANT: This must match the class_names order printed at the end
# of train_model.py / your notebook (Cell 13). Example:
# ['formalin_apple', 'fresh_apple']
# -----------------------------------------------------------------
CLASS_NAMES = ["formalin_apple", "fresh_apple"]  # <-- CONFIRM/EDIT THIS

MODEL_PATH = "ce4_apple_model.keras"
IMG_SIZE = (224, 224)

st.set_page_config(page_title="CE4: Fresh vs Formalin-mixed Apple", page_icon="🍎")


@st.cache_resource
def load_model():
    return tf.keras.models.load_model(MODEL_PATH)


def preprocess_image(image: Image.Image):
    image = image.convert("RGB")
    image = image.resize(IMG_SIZE)
    img_array = tf.keras.utils.img_to_array(image)
    img_array = tf.expand_dims(img_array, 0)  # create batch axis
    img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)
    return img_array


def main():
    st.title("🍎 Fresh Apple vs Formalin-mixed Apple Classifier")
    st.write(
        "Upload an image of an apple, and this app will predict whether it "
        "is **fresh** or **formalin-mixed**, using a CNN (MobileNetV2 transfer "
        "learning) trained for GET 324 Mini-Project (Group CE4)."
    )

    model = load_model()

    uploaded_file = st.file_uploader(
        "Upload an apple image (JPG or PNG)", type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)

        with st.spinner("Classifying..."):
            processed = preprocess_image(image)
            prediction = model.predict(processed)[0][0]

            # prediction is a sigmoid output between 0 and 1
            predicted_class = CLASS_NAMES[1] if prediction > 0.5 else CLASS_NAMES[0]
            confidence = prediction if prediction > 0.5 else 1 - prediction

        st.subheader("Result")
        if predicted_class == "fresh_apple":
            st.success(f"✅ Prediction: **Fresh Apple** ({confidence * 100:.2f}% confidence)")
        else:
            st.error(f"⚠️ Prediction: **Formalin-mixed Apple** ({confidence * 100:.2f}% confidence)")

        st.progress(float(confidence))

    st.markdown("---")
    st.caption(
        "GET 324 Laboratory Exercise 10 (Mini-Project) | Group CE4 | "
        "Chemical Engineering"
    )


if __name__ == "__main__":
    main()
