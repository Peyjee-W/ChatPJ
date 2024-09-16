# Chat Assistant with Flask and OpenAI

## Overview

This project is a Flask web application that provides a chat assistant interface powered by OpenAI's GPT-4o-mini model. The application allows users to interact with an AI model to generate responses in a conversation format. It also includes features such as saving conversation history, switching between different conversations, and resetting the current conversation.

## Features

- **Chat with AI Assistant**: Users can interact with the AI assistant powered by OpenAI’s GPT-4o-mini model.
- **Conversation Management**: Start new conversations, switch between existing ones, or delete conversations.
- **Conversation History**: All previous conversations are stored and displayed in a sidebar for easy access.
- **Interactive Frontend**: The chat interface supports message display with a typewriter effect and uses Markdown for formatted text.

## Technologies Used

- **Flask**: A lightweight WSGI web application framework in Python.
- **OpenAI API**: GPT-4o-mini for generating chat responses.
- **HTML/CSS/JavaScript**: For the frontend user interface.
- **Marked.js**: Used for rendering Markdown content in the chat window.

## Prerequisites

- Python 3.7+
- An OpenAI API key

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/Peyjee-W/ChatPJ.git
   cd ChatPJ
   ```

2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

   If there is no `requirements.txt` file, you can install the required libraries manually by running:

   ```bash
   pip install Flask openai threading webbrowser
   ```

4. Obtain your OpenAI API key from [https://github.com/popjane/free_chatgpt_api](https://github.com/popjane/free_chatgpt_api) and set it in the `app.py` file:
   ```python
   openai.api_key = "your-api-key"
   ```

## Running the Application

1. Start the Flask application:
   ```bash
   python app.py
   ```

2. The app will automatically open a browser window pointing to `http://127.0.0.1:5000/`.

3. You can now interact with the assistant through the web interface.

## API Endpoints

- `GET /`: Loads the main chat interface.
- `POST /chat`: Sends a user's message and returns the AI's reply.
- `POST /reset`: Resets the current conversation.
- `POST /switch`: Switches to a different conversation based on the conversation ID.
- `GET /get_conversation/<conversation_id>`: Retrieves the conversation history for a given ID.

## Customization

- Modify the HTML and CSS in `index.html` to change the layout or styling of the chat interface.
- In `app.py`, you can adjust the assistant’s behavior by modifying the system message when a new conversation is initiated:
  ```python
  {"role": "system", "content": "You are a helpful and friendly assistant."}
  ```

## Security

Make sure to secure your OpenAI API key. Avoid hardcoding sensitive information into the code in a production environment. Use environment variables instead.

## License

This project is licensed under the MIT License.
