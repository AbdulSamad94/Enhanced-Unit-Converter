import google.generativeai as genai
import streamlit as st
import time
from utils.config import ABOUT_ME


def get_chatbot_prompt(user_prompt):
    """Creates the prompt for the chatbot, including context and instructions."""
    prompt_engineering = f"""
    You are a helpful chatbot designed to answer questions specifically about a unit converter website.
    Your knowledge is limited to the functionalities and usage of this unit converter.
    You can answer questions like:
    - What categories of units does this website support?
    - How do I use the unit converter?
    - What is the formula for converting between different temperature units?
    - How many units are in each category?
    - How can I convert from one unit to another unit in this website?
    - Can you show me how to convert a unit?
    - What is the history of unit conversion?
    - This website only include these categories of units: Length, Mass, Temperature, Volume, and Time.

    If a user asks about the creator of the site, please use the following information:
    {ABOUT_ME}

    If a user asks a question that is completely outside of this context, you should politely respond with "I'm sorry, I can only answer questions about the unit converter website."
    """
    return prompt_engineering + "\n\n" + "User Query: " + user_prompt


def display_streaming_response(model, final_prompt):
    """Displays the chatbot's response in a streaming way."""
    message_placeholder = st.empty()
    full_response = ""
    try:
        chat = model.start_chat(history=[])
        for chunk in chat.send_message(final_prompt, stream=True):
            for word in chunk.text.split():  # Iterate over words
                full_response += word + " "
                time.sleep(0.05)  # add a delay
                message_placeholder.markdown(full_response + "▌")  # Update placeholder
        message_placeholder.markdown(full_response)
    except Exception as e:
        st.error(f"An error occurred: {e}")
    return full_response
