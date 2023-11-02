import streamlit as st
import pandas as pd

url_data = (r'https://github.com/andyen11821/xcalsizer/blob/main/Cap%20Rates.csv')
capratelist = pd.read_csv('url_data', encoding = 'ISO-8859-1', names = col_names)

st.write('X-Caliber Capital Automatic Sizer')

#projectname = st.text_input("Enter the project name:")
#projectcity = st.text_input("Enter the project city:")
#projectstate = st.text_input("Enter the project state:")

#ogname = st.text_input("Enter the originator:")
#ogphone = st.text_input("Enter the originator's phone number:")
#ogemail = st.text_input("Enter the originator's email address:")

#uwname = st.text_input("Enter the underwriter's name:")
#uwphone = st.text_input("Enter the underwriter's phone number:")
#uwemail = st.text_input("Enter the underwriter's email address:")

#schedballoon = st.text_input("Enter the Scheduled Balloon (USD):")
#cutoffnoi = st.text_input("Enter the Cutoff NOI (USD):")
#units= st.text_input("Enter the number of units :")
#recentval = st.text_input("Enter the recent valuation (USD):")

#loantypes = ["Market", 'Affordable', 'Green']
#loantype = st.selectbox("Choose a type:", loantypes)

cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]  # Add more cities as needed
city = st.selectbox("Choose a city:", cities)

if st.button("Get Cap Rates"):
    

  
