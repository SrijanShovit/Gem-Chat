from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
import time

# Load environment variables
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load Gemini Pro model to get response
model = genai.GenerativeModel("gemini-pro")

# Function to get Gemini response
def get_gemini_resp(question):
    start_time = time.time()
    resp = model.generate_content(question)
    end_time = time.time()
    response_time = end_time - start_time
    return resp.text, response_time

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
submit = st.button("Ask the question❓")

if submit:
    if input_question.strip() == '':
        st.warning("Please input a question.")
    else:
        # Check if question exists in cache
        if input_question in state.cache:
            # Fetch response from cache
            start_time = time.time()
            response = state.cache[input_question]
            st.subheader("Here's your answer (from cache) 🔄:")
            st.write(response)
            end_time = time.time()
            response_time = end_time - start_time
            st.write(f"Response time: {response_time:.3f} seconds ⏱️")
        else:
            # Fetch response from Gemini model
            response, response_time = get_gemini_resp(input_question)
            # Cache the question and response
            state.cache[input_question] = response

            st.subheader("💬Here's your answer:")
            st.write(response)
            st.write(f"Response time: {response_time:.3f} seconds ⏱️")

        