# Importing required libraries
from openai import OpenAI
import streamlit as st
import os

# Setting up the title of the web application using Streamlit
st.title("ChatGPT-like clone")

# Letting the user select the model provider
model_provider = st.selectbox(
    "Select the model provider",
    ("OpenAI", "Anyscale", "Together AI")
)

# Initializing the client based on the user's choice
if model_provider == "OpenAI":
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"], base_url=None)
elif model_provider == "Anyscale":
    client = OpenAI(api_key=st.secrets["ANYSCALE_API_KEY"], base_url=os.environ.get("ANYSCALE_BASE_URL"))
    st.session_state["openai_model"] = "mistralai/Mixtral-8x7B-Instruct-v0.1"
elif model_provider == "Together AI":
    client = OpenAI(api_key=st.secrets["TOGETHER_API_KEY"], base_url=os.environ.get("TOGETHER_BASE_URL"))
    st.session_state["openai_model"] = "mistralai/Mixtral-8x7B-Instruct-v0.1"

# Ensuring that the OpenAI model is set in the session state; defaulting to 'gpt-3.5-turbo'
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

# Ensuring that there is a message list in the session state for storing conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Displaying each message in the session state using Streamlit's chat message display
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Handling user input through Streamlit's chat input box
if prompt := st.chat_input("What is up?"):
    # Appending the user's message to the session state
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Displaying the user's message in the chat interface
    with st.chat_message("user"):
        st.markdown(prompt)

    # Preparing to display the assistant's response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()  # Placeholder for assistant's response
        full_response = ""  # Initializing a variable to store the full response

        # Generating a response from the OpenAI model
        for response in client.chat.completions.create(
            model=st.session_state["openai_model"],  # Using the model specified in the session state
            messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],  # Passing the conversation history
            stream=True,  # Enabling real-time streaming of the response
        ):
            # Updating the response as it is received
            full_response += (response.choices[0].delta.content or "")
            message_placeholder.markdown(full_response + "▌")  # Displaying the response as it's being 'typed'

        # Updating the placeholder with the final response once fully received
        message_placeholder.markdown(full_response)
    
    # Appending the assistant's response to the session's message list
    st.session_state.messages.append({"role": "assistant", "content": full_response})
