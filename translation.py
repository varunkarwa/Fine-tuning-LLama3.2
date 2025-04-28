
import streamlit as st
import textwrap
import numpy as np
from peft import AutoPeftModelForCausalLM
from transformers import AutoTokenizer
import torch
import re

# Load selected model
@st.cache_resource
def get_model(model_name):
    model = AutoPeftModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16, load_in_4bit=True)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    return tokenizer, model

def main():
    # Set page title and icon
    st.set_page_config(page_title="German-French Translator", page_icon="🌍")

    # Add a title with custom styling
    st.markdown(
        "<h1 style='text-align: center; color: #4CAF50;'>German-French Translations</h1>",
        unsafe_allow_html=True,
    )

    # Load the model
    model_name = "/content/MODEL_C"
    tokenizer, model = get_model(model_name)

    # User input
    st.markdown("### Enter a German Sentence")
    user_input = st.text_area("", placeholder="Type your German sentence here...")

    # Translate button
    if st.button("Translate", key="translate_button"):
        if user_input:
            # Show a progress bar
            with st.spinner("Translating..."):
                # Prepare the prompt
                prompt = f"Translate the following German sentence to French:\n\nGerman: {user_input}\nFrench:"
                input_ids = tokenizer(prompt, return_tensors='pt', padding=True, truncation=True).to("cuda")

                # Generate output
                with torch.no_grad():
                    outputs = model.generate(**input_ids, max_new_tokens=50, temperature=0.7, top_p=0.6)

                # Decode and clean output
                output = tokenizer.decode(outputs[0][len(input_ids["input_ids"][0]):], skip_special_tokens=True)
                translated_text = output.strip()

            # Display the translation
            st.markdown("### French Translation")
            st.success(translated_text)
        else:
            st.warning("Please enter a German sentence to translate.")

if __name__ == "__main__":
    main()
