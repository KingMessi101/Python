import streamlit as st
from huggingface_hub import InferenceClient
import config
from hf import generate_response

client = InferenceClient (
    provider="hf-inference",
    api_key=config.HF_API_KEY
)
MODEL = "stabilityai/stable-diffusion-3-medium-diffusers"
st.title("AI Image Generator")
prompt = st.text_input("Enter image description")
if st.button("Generate Image"):
    if prompt:
        enhanced_prompt = generate_response(
            f"Improve this image: {prompt}"
        )
        st.write("### Enchanted Prompt")
        st.write(enhanced_prompt)
        image = client.text_to_text(
            prompt=enhanced_prompt,
            model=MODEL
        )
        st.image(image, caption="Generated Image")
    else:
        st.warning("Please enter a prompt.")