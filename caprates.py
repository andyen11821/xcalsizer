import streamlit as st

st.write('Hello world')

projectname = st.text_input("Enter the project name:")
projectcity = st.text_input("Enter the project city:")
projectstate = st.text_input("Enter the project state:")

ogname = st.text_input("Enter the originator:")
ogphone = st.text_input("Enter the originator's phone number:")
ogemail = st.text_input("Enter the originator's email address:")

uwname = st.text_input("Enter the underwriter's name:")
uwphone = st.text_input("Enter the underwriter's phone number:")
uwemail = st.text_input("Enter the underwriter's email address:")

schedballoon = st.text_input("Enter the Scheduled Balloon (USD):")
cutoffnoi = st.text_input("Enter the Cutoff NOI (USD):")
units= st.text_input("Enter the number of units :")
recentval = = st.text_input("Enter the recent valuation (USD):")

loantypes = ["Market", 'Affordable', 'Green']
loantype = st.selectbox("Choose a type:", loantypes)

cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]  # Add more cities as needed
city = st.selectbox("Choose a city:", cities)

st.button("Get Cap Rates")
# Code to fetch and display cap rates
  
