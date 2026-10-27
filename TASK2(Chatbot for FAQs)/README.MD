# 🤖 FAQ Chatbot Using NLP and Streamlit

## 📌 Project Overview

The **FAQ Chatbot** is a web-based chatbot developed using Python, Natural Language Processing (NLP), and Streamlit. It answers frequently asked questions about Python, Machine Learning, Streamlit, and customer support.

The chatbot uses **TF-IDF vectorization** and **Cosine Similarity** to compare user questions with predefined FAQ questions and return the most relevant answer. It also includes basic text preprocessing techniques to improve question matching.

## 🎯 Project Objectives

- Develop an interactive FAQ chatbot using Python.
- Apply Natural Language Processing (NLP) techniques.
- Clean and preprocess text using NLTK.
- Convert text into numerical features using TF-IDF.
- Find the most relevant FAQ using Cosine Similarity.
- Build a user-friendly chat interface with Streamlit.
- Maintain conversation history during the session.

## ✨ Features

- 🤖 Interactive chatbot interface.
- 💬 Real-time question-and-answer functionality.
- 🧠 NLP-based question matching.
- 🔤 Text preprocessing and tokenization.
- ✂️ Punctuation and stopword removal.
- 📚 Word lemmatization using NLTK.
- 📊 TF-IDF text vectorization.
- 🎯 Cosine Similarity for matching questions.
- 👋 Basic greeting detection.
- 💬 Chat history using Streamlit session state.
- ⚙️ Similarity threshold to handle unmatched questions.
- 🚀 Simple and lightweight web application.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | Web-based chatbot interface |
| NLTK | Natural Language Processing |
| Scikit-learn | TF-IDF vectorization and similarity calculation |
| TF-IDF | Converts text into numerical vectors |
| Cosine Similarity | Measures similarity between questions |
| WordNetLemmatizer | Reduces words to their base forms |
| Git & GitHub | Version control and project hosting |

## 📂 Project Structure

```text
FAQ-Chatbot/
│
├── faq_chatbot.py
└── README.md
```

**File descriptions:**

- `faq_chatbot.py`: Contains the chatbot logic, FAQ dataset, NLP preprocessing, similarity matching, and Streamlit interface.
- `README.md`: Provides project documentation and installation instructions.

## ⚙️ Installation and Setup

### 1. Clone the Repository

Replace `YOUR_USERNAME` with your GitHub username and use your repository name.

```bash
git clone https://github.com/YOUR_USERNAME/FAQ-Chatbot.git
```

### 2. Open the Project Folder

```bash
cd FAQ-Chatbot
```

### 3. Create a Virtual Environment (Optional)

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

Create a file named `requirements.txt` and add:

```text
streamlit
nltk
scikit-learn
```

Install the libraries:

```bash
python -m pip install -r requirements.txt
```

### 5. Run the Application

Make sure your Python file is named `app.py`. Run:

```bash
python -m streamlit run app.py
```

The chatbot will open in your web browser.

## 🧠 How the Chatbot Works

The chatbot follows these steps:

### Step 1: FAQ Dataset

A predefined dataset stores frequently asked questions and their answers. The current dataset covers:

- Python
- Python package installation
- Machine Learning
- Python lists and tuples
- Customer support
- Streamlit

### Step 2: Text Preprocessing

The chatbot preprocesses questions using the following techniques:

1. **Lowercasing:** Converts text to lowercase.
2. **Punctuation Removal:** Removes punctuation marks.
3. **Tokenization:** Splits sentences into individual words.
4. **Stopword Removal:** Removes common English words.
5. **Lemmatization:** Reduces words to their base forms.

### Step 3: TF-IDF Vectorization

TF-IDF converts the preprocessed FAQ questions into numerical vectors. These vectors represent the importance of words within the FAQ dataset.

### Step 4: Cosine Similarity

When a user submits a question, the chatbot converts it into a TF-IDF vector and compares it with the stored FAQ question vectors using Cosine Similarity.

### Step 5: Answer Selection

The chatbot selects the FAQ question with the highest similarity score.

- If the score is **0.2 or higher**, it returns the corresponding answer.
- If the score is **below 0.2**, it returns a fallback message asking the user to rephrase the question or contact support.
- Basic greetings such as "Hi", "Hello", and "Assalam" receive a greeting response.

**Note:** The similarity threshold is configurable and may require testing to achieve appropriate matching behavior.

## 💬 Example Interaction

**User:**
```text
What is Python?
```

**Chatbot:**
```text
Python is a high-level, interpreted programming language known for its easy syntax and readability.
```

**User:**
```text
How do I install Python packages?
```

**Chatbot:**
```text
You can install Python packages using pip. For example:
'pip install package_name' in your terminal.
```

**User:**
```text
Hello
```

**Chatbot:**
```text
Hello! How can I help you today? You can ask me about Python, ML, or our services.
```

## 📊 NLP Techniques

| Technique | Description |
|---|---|
| Tokenization | Splits text into individual words |
| Lowercasing | Converts text to lowercase |
| Punctuation Removal | Removes punctuation marks |
| Stopword Removal | Filters common English words |
| Lemmatization | Converts words into their base forms |
| TF-IDF | Represents text as numerical vectors |
| Cosine Similarity | Measures similarity between text vectors |

## ⚠️ Limitations

- The chatbot uses a small, predefined FAQ dataset.
- It does not generate new answers like a generative AI chatbot.
- It may fail to recognize questions that use unfamiliar wording.
- Its matching accuracy depends on the FAQ content and similarity threshold.
- The chatbot currently supports English text processing.
- The customer support email and phone number are example contact details and should be replaced with valid information before deployment.
- NLTK resources must be downloaded successfully before text preprocessing can work.

## 🚀 Future Improvements

- Add more FAQs and categories.
- Support Urdu and other languages.
- Improve question matching using sentence embeddings.
- Add an admin interface to manage FAQs.
- Store chat history in a database.
- Integrate a real customer support system.
- Add user feedback to improve answer quality.
- Deploy the application online.

## 🎓 Learning Outcomes

Through this project, you can learn:

- Python application development.
- Basic Natural Language Processing.
- Text cleaning and preprocessing.
- TF-IDF feature extraction.
- Cosine Similarity calculations.
- FAQ-based chatbot development.
- Streamlit web application development.
- Python dependency management.

## 👩‍💻 Author

**Zarfshan  Attiq Khan**

