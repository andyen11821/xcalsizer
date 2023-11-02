import streamlit as st

st.write('Hello world')

cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]  # Add more cities as needed
city = st.selectbox("Choose a city:", cities)

st.button("Get Cap Rates")
# Code to fetch and display cap rates
  
