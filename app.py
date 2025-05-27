import streamlit as st
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Function to clean text: remove punctuation and convert to lowercase
def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

# Predefined dataset
qa_data = {
    "questions": [
        {
            "question": "What does the eligibility verification agent (EVA) do?",
            "answer": "EVA automates the process of verifying a patient’s eligibility and benefits information in real-time, eliminating manual data entry errors and reducing claim rejections."
        },
        {
            "question": "What does the claims processing agent (CAM) do?",
            "answer": "CAM streamlines the submission and management of claims, improving accuracy, reducing manual intervention, and accelerating reimbursements."
        },
        {
            "question": "How does the payment posting agent (PHIL) work?",
            "answer": "PHIL automates the posting of payments to patient accounts, ensuring fast, accurate reconciliation of payments and reducing administrative burden."
        },
        {
            "question": "Tell me about Thoughtful AI's Agents.",
            "answer": "Thoughtful AI provides a suite of AI-powered automation agents designed to streamline healthcare processes. These include Eligibility Verification (EVA), Claims Processing (CAM), and Payment Posting (PHIL), among others."
        },
        {
            "question": "What are the benefits of using Thoughtful AI's agents?",
            "answer": "Using Thoughtful AI's Agents can significantly reduce administrative costs, improve operational efficiency, and reduce errors in critical processes like claims management and payment posting."
        }
    ]
}

# Extract specific agent answers
agents = {
    "eva": qa_data["questions"][0]["answer"],
    "cam": qa_data["questions"][1]["answer"],
    "phil": qa_data["questions"][2]["answer"]
}

# Extract all questions for TF-IDF vectorization
questions = [q["question"] for q in qa_data["questions"]]

# Initialize TF-IDF vectorizer
vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(questions)

# Generic fallback response
generic_response = (
    "I'm sorry, I don't have specific information on that question. "
    "However, Thoughtful AI provides AI-powered automation agents for healthcare, "
    "such as EVA for eligibility verification, CAM for claims processing, and PHIL for payment posting. "
    "If you have any other questions about these agents, feel free to ask!"
)

# Function to get the most relevant answer
def get_answer(user_question):
    user_question_clean = clean_text(user_question)
    
    # Check for specific agents (keyword matching)
    if "eva" in user_question_clean:
        return agents["eva"]
    elif "cam" in user_question_clean:
        return agents["cam"]
    elif "phil" in user_question_clean:
        return agents["phil"]
    
    # Use TF-IDF and cosine similarity for general questions
    user_query_tfidf = vectorizer.transform([user_question])
    similarities = cosine_similarity(user_query_tfidf, tfidf_matrix)
    
    # Find the index of the most similar question
    best_match_idx = similarities.argmax()
    similarity_score = similarities[0][best_match_idx]
    
    # If similarity is above threshold, return the best match; otherwise, fallback
    if similarity_score >= 0.5:
        return qa_data["questions"][best_match_idx]["answer"]
    else:
        return generic_response

# Streamlit app
st.title("Thoughtful AI Support Agent")
st.write("Ask me anything about Thoughtful AI's agents!")

if 'messages' not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is your question?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        answer = get_answer(prompt)
        st.markdown(answer)
        st.session_state.messages.append({"role": "assistant", "content": answer})
