import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Hardcoded dataset
knowledge_base = {
    "What does the eligibility verification agent (EVA) do?":
        "EVA automates the process of verifying a patient’s eligibility and benefits information in real-time, eliminating manual data entry errors and reducing claim rejections.",
    "What does the claims processing agent (CAM) do?":
        "CAM streamlines the submission and management of claims, improving accuracy, reducing manual intervention, and accelerating reimbursements.",
    "How does the payment posting agent (PHIL) work?":
        "PHIL automates the posting of payments to patient accounts, ensuring fast, accurate reconciliation of payments and reducing administrative burden.",
    "Tell me about Thoughtful AI's Agents.":
        "Thoughtful AI provides a suite of AI-powered automation agents designed to streamline healthcare processes. These include Eligibility Verification (EVA), Claims Processing (CAM), and Payment Posting (PHIL), among others.",
    "What are the benefits of using Thoughtful AI's agents?":
        "Using Thoughtful AI's Agents can significantly reduce administrative costs, improve operational efficiency, and reduce errors in critical processes like claims management and payment posting."
}

questions = list(knowledge_base.keys())
answers = list(knowledge_base.values())

# Vectorize questions
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)

def find_best_match(user_input):
    user_vec = vectorizer.transform([user_input])
    similarities = cosine_similarity(user_vec, X)
    best_idx = similarities.argmax()
    best_score = similarities[0, best_idx]
    if best_score > 0.5:
        return answers[best_idx]
    else:
        return "I'm sorry, I don't have an answer for that yet. Please reach out to our support team for more assistance!"

# Streamlit UI
st.set_page_config(page_title="Thoughtful AI Support Agent", page_icon="🤖")
st.title("🧠 Thoughtful AI Support Assistant")
st.write("Ask me anything about Thoughtful AI's agents!")

user_input = st.text_input("You:", "")

if user_input:
    response = find_best_match(user_input)
    st.markdown(f"**Agent:** {response}")
