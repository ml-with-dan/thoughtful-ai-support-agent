# Thoughtful AI Support Agent

A simple customer support AI agent assistant built with Streamlit and scikit-learn to answer questions about Thoughtful AI's agents using a hardcoded FAQ-style knowledge base.

## Objective
Imagine you are working at Thoughtful AI. The team has tasked you with building a simple customer support AI Agent to assist users with basic questions about Thoughtful AI. The agent will use predefined, hardcoded responses to answer common questions.

### Rules

Your agent should follow these guidelines:

- The agent must accept user input and answer the question like a conversational AI Agent.
- The agent should retrieve the most relevant answer from a hardcoded set of responses about Thoughtful AI.
- The agent should display the answer to the user in a user-friendly format.

## Features
- Answers common questions about Thoughtful AI Agents
- Uses TF-IDF + cosine similarity to find the best answer
- Graceful fallback for unknown questions
- Simple web interface via Streamlit

## How to Run Locally

1. Clone this repository.
2. Install the dependencies:  
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:  
   ```bash
   streamlit run app.py
   ```

**Note**: This app uses `st.chat_message`, which is available in Streamlit 1.18.0 and later. Make sure you have a compatible version installed.

## How to Deploy on Streamlit Cloud

1. Go to [Streamlit Cloud](https://share.streamlit.io/) and log in or sign up.
2. Connect your GitHub account.
3. Select this repository and the main branch.
4. Choose `app.py` as the entry point.
5. Deploy the app.

You will get a public URL where you can share the app.
