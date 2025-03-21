import streamlit as st

def show_home():
    st.title("Welcome! 🚀")
    st.divider()

    st.header("Concept 💡")
    st.write(
        """
        This is an interactive website where you gain access to a **Convolutional Neural Network (C.N.N)**. Its job is to process images then evaluate whether or not they are *likely* to be A.I-generated.
        """
    )
    st.divider()

    st.header("Why? 🤔")
    st.write(
        """
        With the rising trend of **A.I** as technology advances, we gain a number of benefits coming from it. But there can also be involved drawbacks as A.I has been seen with its deceitful usage (fake videos, fake voice recordings, fake images, ...)
        \nNot only was this project created to mitigate such occurences (fake images), but also to challenge myself with my abilities.
        """
    )
    st.divider()

    st.header("Where can I start using the model? 😵‍💫")
    st.write(
        """
        There is a navigation bar at the top of the page, where many buttons are to be found. Simply clicking them will allow you to move through the website.
        """
    )
    st.divider()