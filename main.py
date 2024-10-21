import streamlit as st
from transformers import pipeline  # Import the transformers library for Hugging Face
import os

# Text to Roman Urdu conversion using Hugging Face model
def convert_to_roman_urdu(text):
    try:
        translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-ur")
        result = translator(text)[0]['translation_text']
        return result
    except Exception as e:
        st.error(f"HuggingFace model error: {str(e)}")
        return None

# Streamlit UI
def main():
    st.title("AI Converter")

    # Roman Urdu Conversion Mode
    st.header("Text to Roman Urdu Converter")
    input_text = st.text_area("Enter text to convert:")

    if st.button("Convert"):
        if input_text:
            with st.spinner("Converting..."):
                result = convert_to_roman_urdu(input_text)
                if result:
                    st.success("Conversion Complete!")
                    st.write("Result:")
                    st.write(result)

if __name__ == "__main__":
    st.set_page_config(page_title="AI Converter", layout="wide")
    main()
