import streamlit as st
import nltk
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# =====================================
# NLTK SETUP (Fast Loading & Error Handling)
# =====================================
@st.cache_resource
def download_nltk_data():
    try:
        # Check if data is already present
        nltk.data.find('tokenizers/punkt')
        nltk.data.find('tokenizers/punkt_tab')
        nltk.data.find('corpora/stopwords')
        nltk.data.find('corpora/wordnet')
    except LookupError:
        # If not present, download it
        nltk.download('punkt')
        nltk.download('punkt_tab')
        nltk.download('stopwords')
        nltk.download('wordnet')

download_nltk_data()

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# =====================================
# FAQ DATASET
# =====================================
faqs = [
    {
        "question": "What is Python?",
        "answer": "Python is a high-level, interpreted programming language known for its easy syntax and readability."
    },
    {
        "question": "How do I install Python packages?",
        "answer": "You can install Python packages using pip. For example: 'pip install package_name' in your terminal."
    },
    {
        "question": "What is Machine Learning?",
        "answer": "Machine Learning is a branch of AI that allows systems to learn and improve from experience without being explicitly programmed."
    },
    {
        "question": "What is the difference between list and tuple in Python?",
        "answer": "Lists are mutable (can be changed) and use square brackets [], while tuples are immutable (cannot be changed) and use parentheses ()."
    },
    {
        "question": "How can I contact customer support?",
        "answer": "You can contact our customer support by emailing support@example.com or calling 1-800-123-4567."
    },
    {
        "question": "What is Streamlit?",
        "answer": "Streamlit is an open-source Python library used to create beautiful, custom web apps for machine learning and data science in minutes."
    }
]

# =====================================
# NLP PREPROCESSING
# =====================================
lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    # 1. Lowercase
    text = text.lower()
    # 2. Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # 3. Tokenize
    tokens = word_tokenize(text)
    # 4. Remove stopwords and lemmatize
    cleaned_tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stop_words]
    
    return " ".join(cleaned_tokens)

# Preprocess all FAQ questions
faq_questions = [faq["question"] for faq in faqs]
processed_questions = [preprocess_text(q) for q in faq_questions]

# =====================================
# VECTORIZATION (TF-IDF)
# =====================================
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(processed_questions)

# =====================================
# MATCHING FUNCTION
# =====================================
def get_best_answer(user_query):
    # Preprocess the user query
    processed_query = preprocess_text(user_query)
    
    # --- BONUS: Handle Greetings ---
    greetings = ["hi", "hello", "hey", "salam", "assalam", "aoa"]
    if any(word in processed_query.split() for word in greetings):
        return "Hello! How can I help you today? You can ask me about Python, ML, or our services."
    # --------------------------------
    
    # Convert user query to vector
    query_vector = vectorizer.transform([processed_query])
    
    # Calculate Cosine Similarity
    similarity_scores = cosine_similarity(query_vector, tfidf_matrix).flatten()
    
    # Get the index of the highest score
    best_match_index = similarity_scores.argmax()
    best_score = similarity_scores[best_match_index]
    
    # If the similarity is too low, we don't have a good answer
    if best_score < 0.2: # You can adjust this threshold
        return "Sorry, I couldn't find a matching answer. Please try rephrasing or contact support."
    
    return faqs[best_match_index]["answer"]

# =====================================
# STREAMLIT UI CONFIGURATION
# =====================================
st.set_page_config(page_title="FAQ Chatbot", page_icon="🤖", layout="centered")

st.title("🤖 FAQ Chatbot")
st.markdown("Ask me anything about Python, ML, or our services!")

# =====================================
# CHAT INTERFACE
# =====================================
# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Type your question here..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
        
    # Get bot response
    bot_response = get_best_answer(prompt)
    
    # Display bot response
    with st.chat_message("assistant"):
        st.markdown(bot_response)
        
    # Add bot response to chat history
    st.session_state.messages.append({"role": "assistant", "content": bot_response})