# Unit Converter and ChatBot Application

This project is a Streamlit web application that combines a versatile unit converter with an interactive chatbot powered by Google's Gemini AI model. The unit converter allows users to convert between various units across different categories, while the chatbot can answer questions about the unit converter's functionality and the creator of the website.

## Features

-   **Unit Converter:**
    -   Supports conversions between units in the following categories:
        -   Length
        -   Mass
        -   Temperature (Celsius, Fahrenheit, Kelvin)
        -   Volume
        -   Time
    -   User-friendly interface for selecting categories, units, and entering quantities.
    -   Clear display of conversion results.
-   **ChatBot:**
    -   Powered by Google's Gemini AI model (`gemini-2.0-flash`).
    -   Context-aware: The chatbot is designed to answer questions specifically about the unit converter's features, usage, and supported units.
    -   It will only answer the question regarding unit converter.
    -   Provides information about the website's creator (Abdul Samad Siddiqui) when asked.
    -   Handles out-of-context questions politely.
    -   Uses streaming to provide smooth, real-time responses.
-   **Smooth Response:**
    - Response from the chatbot is in smooth way.
- **Error handling:**
    - If there is any error in the unit converter it will show error.
    - If the api key is not present in .env it show the error.
- **Clean Code**:
    - The code is clean and easy to understand.
- **Well Structure**:
    - The code is well structure.

## Project Structure

The project is organized into the following components:

