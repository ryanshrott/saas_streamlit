# Import necessary libraries
import streamlit as st

# Title of our app
st.title("Streamlit Interactivity and Session Demo")

# Sidebar header
st.sidebar.header("Options")

# Simple Slider Widget
slider_val = st.slider('Choose a value', min_value=1, max_value=100, value=25)
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
page = st.radio("Choose a Page:", ["Home", "About", "Contact"], horizontal=True)
if page == "Home":
    st.write("Welcome to the Home Page!")
elif page == "About":
    st.write("This is the About Section!")
else:
    st.write("Feel free to Contact Us!")

# Using st.session_state for a simple counter
if 'counter' not in st.session_state:
    st.session_state.counter = 0

increment = st.button('Increment Counter')
if increment:
    st.session_state.counter += 1

st.write(f"Counter Value: {st.session_state.counter}")
