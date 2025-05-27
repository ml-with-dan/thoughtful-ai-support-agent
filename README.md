# Thoughtful AI Support Agent

A simple customer support AI agent built with Streamlit and scikit-learn to answer questions about Thoughtful AI's agents.

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
