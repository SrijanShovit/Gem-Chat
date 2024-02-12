from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
import time
from PIL import Image
import requests
from io import BytesIO
import hashlib


# Load environment variables
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load Gemini Pro model to get response
model = genai.GenerativeModel("gemini-pro-vision")

def get_gemini_resp(input, image):
    if input != "":
        resp = model.generate_content([input, image])
    else:
        resp = model.generate_content(image)
    return resp.text

# Function to generate a unique key for caching
def generate_cache_key(question, image):
    combined_data = f"{question}-{image}"
    return hashlib.md5(combined_data.encode()).hexdigest()


# Streamlit app
st.set_page_config(page_title="Gemini chat🔥")

st.header("Gem Chat App 🚀😎")

# Function to initialize or get session state
def get_session():
    return st.session_state

# Initialize or get session state
state = get_session()

# Initialize cache if not already
if 'cache' not in state:
    state.cache = {}

input_question = st.text_input("Input: ", key="input")

image_option = st.radio("Select image option:", ("Upload Image", "Embed Image Link"))

image = ""
if image_option == "Upload Image":
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image!!", use_column_width=True)
elif image_option == "Embed Image Link":
    image_link = st.text_input("Enter image URL:")
    if image_link:
        try:
            response = requests.get(image_link)
            if response.status_code == 200:
                image = Image.open(BytesIO(response.content))
                st.image(image, caption="Embedded Image!!", use_column_width=True)
            else:
                st.error("Failed to fetch image from URL. Please check the URL.")
        except Exception as e:
            st.error(f"Error loading image from URL: {e}")

submit = st.button("Go👍")

if submit:
    if input_question.strip() == "":
        st.warning("What do you want me to do?")
    else:
        # Check if question exists in cache
        # Generate cache key
        cache_key = (input_question, image.tobytes())

        # Check if question exists in cache
        if cache_key in state.cache:
            # Fetch response from cache
            start_time = time.time()
            response = state.cache[cache_key]
            st.subheader("Here's your answer (from cache) 🔄:")
            st.write(response)
            end_time = time.time()
            response_time = end_time - start_time
            st.write(f"Response time: {response_time:.3f} seconds ⏱️")
        else:
            # Fetch response from Gemini model
            start_time = time.time()
            response = get_gemini_resp(input_question, image)
            # Cache the question and response
            state.cache[cache_key] = response
            end_time = time.time()
            response_time = end_time - start_time

            st.subheader("💬Here's what I think🧠:")
            st.write(response)
            st.write(f"Response time: {response_time:.3f} seconds ⏱️")
