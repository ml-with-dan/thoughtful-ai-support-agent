# Thoughtful AI Support Agent

A simple customer support AI agent assistant built with Streamlit and scikit-learn to answer questions about Thoughtful AI's agents using a hardcoded FAQ-style knowledge base.

## Objective
Imagine you are working at Thoughtful AI. The team has tasked you with building a simple customer support AI Agent to assist users with basic questions about Thoughtful AI. The agent will use predefined, hardcoded responses to answer common questions.

### Rules

Your agent should follow these guidelines:

- The agent must accept user input and answer the question like a conversational AI Agent.
- The agent should retrieve the most relevant answer from a hardcoded set of responses about Thoughtful AI.
- The agent should display the answer to the user in a user-friendly format.

### Implementation

- You may use any programming language and framework you're comfortable with. This is an opportunity to showcase your skills in a language you are proficient in.
- For the chat UI, you can use any CLI or web-based framework, such as Gradio, Streamlit, Chainlit, etc.
- The agent should use the predefined dataset to answer the questions about Thoughtful AI and fallback to generic LLM responses for everything else.

### **Predefined Data**

Here’s a sample dataset of questions and answers about Thoughtful AI’s Agents that your agent should be able to respond to:
```json
{
    "questions": [
        {
            "question": "What does the eligibility verification agent (EVA) do?",
            "answer": "EVA automates the process of verifying a patient’s eligibility
and benefits information in real-time, eliminating manual data entry errors and reducing claim rejections."
        },
        {
            "question": "What does the claims processing agent (CAM) do?",
            "answer": "CAM streamlines the submission and management of claims,
improving accuracy, reducing manual intervention, and accelerating reimbursements."
        },
        {
            "question": "How does the payment posting agent (PHIL) work?",
            "answer": "PHIL automates the posting of payments to patient accounts,
ensuring fast, accurate reconciliation of payments and reducing administrative burden."
        },
        {
            "question": "Tell me about Thoughtful AI's Agents.",
            "answer": "Thoughtful AI provides a suite of AI-powered automation agents
designed to streamline healthcare processes. These include Eligibility Verification (EVA), Claims Processing (CAM),
and Payment Posting (PHIL), among others."
        },
        {
            "question": "What are the benefits of using Thoughtful AI's agents?",
            "answer": "Using Thoughtful AI's Agents can significantly reduce
administrative costs, improve operational efficiency, and reduce errors in critical processes like
claims management and payment posting."
        }
    ]
}
```

### Evaluation Criteria

1. **Functionality**: The code correctly implements the conversation logic.
2. **Code Quality**: The code is clean, readable, and well-structured, demonstrating knowledge of current tools and technologies.
3. **Robustness**: The code includes error handling for invalid or unexpected inputs. It gracefully handles scenarios where no search results are found.

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
