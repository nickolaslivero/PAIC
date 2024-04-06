import streamlit as st
import google.generativeai as genai
import PIL.Image

genai.configure(api_key="AIzaSyDfHJ_KcI9td-9z8M_b23sjtxPpJBwkGJk")

INPUT = \
    """
    Retorne um audio com a musica dessa partitura.
    """

MODEL_VISION = genai.GenerativeModel('gemini-pro-vision')
MODEL_TEXT = genai.GenerativeModel('gemini-pro')


def generate_description_from_image(image, model):
    description = model.generate_content([INPUT, image])
    return description.text


def generate_description_from_text(prompt, model):
    description = model.generate_content(prompt)
    return description.text


def main():
    st.title("Generative AI Web App")

    uploaded_image = st.file_uploader("Carregar imagem", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        image = PIL.Image.open(uploaded_image)
        st.image(image, caption="Imagem Carregada", use_column_width=True)

        with st.spinner("Processando imagem..."):
            description = generate_description_from_image(image, MODEL_VISION)
            st.subheader("Resultado:")
            st.write(description)


if __name__ == "__main__":
    main()
