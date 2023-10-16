# Import necessary libraries
import streamlit as st

# Title of our app
st.title("Streamlit Interactivity Demo")

# Sidebar header
st.sidebar.header("Options")

# Simple Slider Widget
slider_val = st.slider('Choose a value', min_value=1, max_value=100, value=25)

# Display the slider value in the main area
st.write(f"You selected {slider_val} using the slider.")

# Sidebar Checkbox to toggle information
if st.sidebar.checkbox("Show More Info"):
    st.write("This is some additional info displayed based on checkbox choice!")

# Using Selectbox for Dropdown options
option = st.selectbox("Choose an option:", ["Option 1", "Option 2", "Option 3"])
st.write(f"You selected: {option}")

# Display a date input widget in the sidebar
date = st.sidebar.date_input("Pick a Date")
st.write(f"Selected Date: {date}")

# Multi-page layout simulation using radio buttons
page = st.radio("Choose a Page:", ["Home", "About", "Contact"])
if page == "Home":
    st.write("Welcome to the Home Page!")
elif page == "About":
    st.write("This is the About Section!")
else:
    st.write("Feel free to Contact Us!")

