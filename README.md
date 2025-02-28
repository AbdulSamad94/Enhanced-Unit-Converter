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


-   **`app.py`:** The main entry point for the Streamlit application. It orchestrates the overall flow and imports functions from other modules.
-   **`components/`:** A directory containing modules that define different parts of the application's functionality.
    -   **`converter.py`:** Contains the logic for unit conversions (e.g., `unit_converter`, `convert_temperature`).
    -   **`chatbot.py`:** Implements the chatbot's features, including generating prompts and handling streaming responses.
    -   **`ui.py`:** Contains functions for creating Streamlit UI elements (e.g., sidebar, input fields, displaying chat history).
-   **`utils/`:** A directory for utility functions and configuration.
    -   **`config.py`:** Loads the API key from environment variables, defines constants like `UNITS` (supported units) and `ABOUT_ME` (creator information).
- **`.env`**: Containe the api key in it.
- **`readme.md`**: It will tell you about the project.

## Setup and Installation

1.  **Clone the repository:**

    ```bash
    git clone <your-repository-url>
    cd unit_converter
    ```

2.  **Install dependencies:**

    ```bash
    pip install streamlit google-generativeai python-dotenv
    ```

3.  **Create a `.env` file:**
    - Create a `.env` file in the root directory of the project (`unit_converter/`).
    - Add your Google Gemini API key to this file:

    ```properties
    GOOGLE_API_KEY="YOUR_API_KEY_HERE"
    ```

    - **Replace `YOUR_API_KEY_HERE` with your actual API key.**

4.  **Run the application:**

    ```bash
    streamlit run app.py
    ```

    This will open the application in your web browser.

## Usage

1.  **Unit Converter:**
    -   Select the "Unit Converter" option in the sidebar.
    -   Choose a category of units.
    -   Enter the quantity you want to convert.
    -   Select the "from" unit and the "to" unit.
    -   Click the "Convert" button.
    -   The result will be displayed.
2.  **ChatBot:**
    -   Select the "ChatBot" option in the sidebar.
    -   Type your question about the unit converter in the chat input box.
    -   The chatbot will respond in a streaming manner.
    -   Ask "who made this website?" to know more about the creator of this website.

## Key Technologies

-   **Streamlit:** For creating the interactive web application.
-   **Google's Gemini AI Model:** For the chatbot's conversational abilities.
-   **Python:** The programming language used for the entire project.
-   **python-dotenv:** For managing the API key securely.

## Contributing

Contributions to this project are welcome! If you find any bugs or have suggestions for new features, please open an issue or a pull request on the GitHub repository.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

