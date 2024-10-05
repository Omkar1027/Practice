import google.generativeai as genai
import streamlit as st
import os

genai.configure(api_key=os.getenv("API Key"))
model = genai.GenerativeModel("gemini-pro")

def planner(strt, dest, budget, mot, about):
    prompt = "The start location is {}. The destination is {}. The budget is {}. The mode of transport {}. Further elaboration of journey is:{}.".format(strt, dest, budget, mot, about)
    response = model.generate_content(prompt)
    return response.text

# prepare empty web page
st.set_page_config(
    page_title = "Trip Planner",
    page_icon = ":plan:",
    layout = "centered",
    initial_sidebar_state = "collapsed"
)

st.header("Have professional planner at your fingertips!")
st.write("Desribe the details of your journey for a pre-planned travel.")

col1,col2=st.columns(2)

with col1:
    strt = st.text_input("Start location")
    dest= st.text_input("Destination")

with col2:
    budget = st.text_input("Budget for travel Eg. 100000-20000")
    mot = st.selectbox("Mode of travelling", ["Railways", "Airways", "Roadways"])

about = st.text_area("Describe your journey further")

send_request = st.button("Generate plan in a tabular format")

if send_request:
    if strt and dest and budget and mot and about:
        st.write(planner(strt, dest, budget, mot, about))
    else:
        st.error("Please fill all the fields.")