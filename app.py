import streamlit as st
from components.converter import unit_converter
from components.chatbot import get_chatbot_prompt, display_streaming_response
from components.ui import sidebar_options, unit_converter_ui, display_chat_history
from utils.config import load_api_key, UNITS
import google.generativeai as genai


# Load the API key
load_api_key()


# --- Main App ---
def main():
    st.title("Unit Converter and ChatBot")
    st.write("A versatile unit converter and chat bot with streaming responses.")

    # Sidebar
    app_mode = sidebar_options()

    # --- Unit Converter Mode ---
    if app_mode == "Unit Converter":
        category = st.sidebar.selectbox("Select a Category", list(UNITS.keys()))
        category_units = list(UNITS[category].keys())

        quantity, from_unit, to_unit = unit_converter_ui(category, category_units)

        if st.button("Convert"):
            try:
                result = unit_converter(quantity, from_unit, to_unit, category)
                if category == "Temperature":
                    st.success(
                        f"{quantity} {from_unit.capitalize()} is equal to {result:.2f} {to_unit.capitalize()}"
                    )
                else:
                    st.success(
                        f"{quantity} {from_unit} is equal to {result:.2f} {to_unit}"
                    )
            except KeyError:
                st.error(
                    f"Invalid unit selection. Please ensure both '{from_unit}' and '{to_unit}' are valid units within the selected category '{category}'."
                )
            except Exception as e:
                st.error(f"An error occurred: {e}")

    # --- ChatBot Mode ---
    elif app_mode == "ChatBot":
        st.header("Chat with AI")

        # Initialize the model outside of the loop
        model = genai.GenerativeModel("gemini-2.0-flash")

        # Initialize chat history
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []

        # Display chat history
        display_chat_history()

        # Get user input
        user_prompt = st.chat_input("Type your message here...")

        if user_prompt:
            with st.chat_message("user"):
                st.markdown(user_prompt)
            st.session_state.chat_history.append(
                {"role": "user", "content": user_prompt}
            )

            # Display the assistant's response in a streaming way
            with st.chat_message("assistant"):
                final_prompt = get_chatbot_prompt(user_prompt)
                full_response = display_streaming_response(model, final_prompt)

            st.session_state.chat_history.append(
                {"role": "assistant", "content": full_response}
            )

    st.write("---")
    st.markdown("##### Created by Abdul Samad")


if __name__ == "__main__":
    main()
