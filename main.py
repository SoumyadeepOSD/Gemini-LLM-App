import google.generativeai as genai
import streamlit as st

API_KEY = st.secrets["API_KEY"]

model = genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')

new_title = '<p style="font-family:sans-serif; color:Green; font-size: 42px;">LLM App, powered by Gemini-pro</p>'
st.markdown(new_title, unsafe_allow_html=True)

prompt = st.text_input("Enter your query here")
if (st.button("Submit") and prompt): 
    try:
        response = model.generate_content(prompt)
        st.write(response.text)
    except Exception as e:
        st.write("An error occured", e)