import os
import google.generativeai as genai
from dotenv import load_dotenv
import streamlit as st

load_dotenv()


def load_api_key():
    """Loads the GOOGLE_API_KEY from environment variables and configures the API."""
    try:
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY not found in environment variables.")
        genai.configure(api_key=api_key)
        return api_key
    except (KeyError, ValueError) as e:
        st.error(
            f"Error: {e}. Please ensure the GOOGLE_API_KEY is set correctly in your .env file."
        )
        st.stop()


# Constants
UNITS = {
    "Length": {
        "meter": 1,
        "kilometer": 1000,
        "centimeter": 0.01,
        "millimeter": 0.001,
        "micrometer": 0.000001,
        "nanometer": 0.000000001,
        "mile": 1609.34,
        "yard": 0.9144,
        "foot": 0.3048,
        "inch": 0.0254,
        "nautical mile": 1852,
    },
    "Mass": {
        "kilogram": 1,
        "gram": 0.001,
        "milligram": 0.000001,
        "metric ton": 1000,
        "pound": 0.453592,
        "ounce": 0.0283495,
    },
    "Temperature": {
        "celsius": "celsius",
        "fahrenheit": "fahrenheit",
        "kelvin": "kelvin",
    },
    "Volume": {
        "liter": 1,
        "milliliter": 0.001,
        "cubic meter": 1000,
        "gallon": 3.78541,
        "quart": 0.946353,
        "pint": 0.473176,
    },
    "Time": {
        "second": 1,
        "minute": 60,
        "hour": 3600,
        "day": 86400,
        "week": 604800,
        "year": 31536000,
    },
}

ABOUT_ME = """
This website was created by Abdul Samad Siddiqui. I am a full-stack developer with skills-set in Next.js, React, Tailwind CSS, JavaScript, TypeScript, Node.js, Express.js, MongoDB, HTML, CSS, and Python. I'm 17 years old, currently learning Agentic AI at the Governor IT Initiative, and I live in Karachi, Pakistan.
"""
