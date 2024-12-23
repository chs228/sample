import streamlit as st
from googletrans import Translator

# Set page configuration for a beautiful UI
st.set_page_config(page_title="Real-Time Language Translator", layout="wide")

# Header and description
st.title("Real-Time Language Translator")
st.markdown("### Translate text between multiple languages in real-time using Google Translate.")

# Create a translator object
translator = Translator()

# Input from user
source_text = st.text_area("Enter text to translate", "Hello, how are you?", height=150)

# Language selection
languages = ['en', 'fr', 'es', 'de', 'it', 'pt', 'ru', 'ja', 'zh-cn']
source_lang = st.selectbox("Select source language", languages, index=languages.index('en'))
target_lang = st.selectbox("Select target language", languages, index=languages.index('fr'))

# Button to trigger translation
if st.button('Translate'):
    if source_text:
        # Perform translation
        translated = translator.translate(source_text, src=source_lang, dest=target_lang)
        
        # Display translation result
        st.success(f"Translated text: {translated.text}")
    else:
        st.error("Please enter some text to translate.")

# Display the languages available for reference
st.markdown("### Available Languages:")
st.write({
    'en': 'English',
    'fr': 'French',
    'es': 'Spanish',
    'de': 'German',
    'it': 'Italian',
    'pt': 'Portuguese',
    'ru': 'Russian',
    'ja': 'Japanese',
    'zh-cn': 'Chinese'
})

# Footer
st.markdown("#### Made with ❤️ using Streamlit and Google Translate API.")
