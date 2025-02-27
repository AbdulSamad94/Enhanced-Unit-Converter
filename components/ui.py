import streamlit as st
from utils.config import UNITS


def sidebar_options():
    """Displays the sidebar options for app mode selection."""
    st.sidebar.header("Conversion Options")
    app_mode = st.sidebar.selectbox(
        "Choose the App mode", ["Unit Converter", "ChatBot"]
    )
    return app_mode


def unit_converter_ui(category, category_units):
    """Displays the UI elements for the unit converter."""
    st.header(f"{category} Conversion")
    quantity = st.number_input(
        f"Enter the quantity to convert (in {category})", value=1.0
    )
    from_unit = st.selectbox(f"Select the unit to convert from", category_units)
    to_unit = st.selectbox(
        f"Select the unit to convert to",
        category_units,
        index=1 if len(category_units) > 1 else 0,
    )
    return quantity, from_unit, to_unit


def display_chat_history():
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
