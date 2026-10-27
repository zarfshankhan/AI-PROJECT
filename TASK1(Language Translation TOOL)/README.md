# 🌍 Language Translation Tool

A web-based Language Translation Tool built with Python and Streamlit that allows users to translate text between multiple languages. The application uses Google Translate through the `googletrans` Python library and provides a simple, interactive user interface.

## ✨ Features

- 🌐 **Multiple Language Support:** Translate text between 15 languages.
- 🔍 **Automatic Language Detection:** Automatically detect the source language.
- 🎯 **Language Selection:** Select source and target languages.
- ⚡ **Text Translation:** Translate text with a single click.
- 📋 **Copy Translation:** Copy translated text using the built-in copy button.
- 🔊 **Text-to-Speech:** Listen to translations using your browser's speech synthesis.
- ⏹️ **Stop Speech:** Stop audio playback whenever needed.
- 🗑️ **Clear Button:** Clear the previous translation.
- 💾 **Translation Caching:** Cache successful translations for 24 hours to reduce repeated API requests.
- ⏳ **Request Rate Limiting:** Add a delay between translation attempts to help reduce excessive requests.
- 🎨 **Custom UI:** Purple-themed interface with a clean layout.
- 📏 **Character Limit:** Accept up to 5,000 characters per translation.

## 🛠️ Technologies Used

- Python
- Streamlit
- Googletrans
- HTML
- CSS
- JavaScript
- JSON

## 🌎 Supported Languages

The application supports the following 15 languages:

| Language | Language Code |
|---|---|
| Arabic | `ar` |
| Chinese | `zh-CN` |
| English | `en` |
| French | `fr` |
| German | `de` |
| Hindi | `hi` |
| Italian | `it` |
| Japanese | `ja` |
| Korean | `ko` |
| Persian | `fa` |
| Punjabi | `pa` |
| Russian | `ru` |
| Spanish | `es` |
| Turkish | `tr` |
| Urdu | `ur` |

The source language can also be set to **Auto Detect**.

## 📂 Project Structure

```text
Language-Translation-Tool/
│
├── app.py
├── README.md
└── requirements.txt
```

- `app.py`: Contains the Streamlit application and translation functionality.
- `README.md`: Provides project documentation.
- `requirements.txt`: Lists the Python dependencies.

## ⚙️ Installation and Setup

### Step 1: Clone the Repository

If your project is available on GitHub, clone it using:

```bash
git clone YOUR_REPOSITORY_URL
```

Alternatively, download the project and open its folder in VS Code.

### Step 2: Open the Project Folder

Open the project folder in Visual Studio Code.

Open the terminal using:

**Terminal → New Terminal**

### Step 3: Create a Virtual Environment

Run:

```bash
python -m venv .venv
```

### Step 4: Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Step 5: Install Dependencies

Create a `requirements.txt` file containing:

```text
streamlit
googletrans==4.0.0-rc1
```

Install the dependencies:

```bash
python -m pip install -r requirements.txt
```

If you encounter dependency conflicts, check the installed Python version and the compatibility of the Googletrans dependencies.

### Step 6: Run the Application

Execute the following command:

```bash
python -m streamlit run app.py
```

### Step 7: Open in Your Browser

Streamlit will provide a local address, usually:

```text
http://localhost:8501
```

Open the address in your browser to use the application.

## 🚀 How to Use

1. Run the application.
2. Select the source language or choose **Auto Detect**.
3. Select the target language.
4. Enter your text in the input field.
5. Click **🌐 Translate**.
6. View the translated text.
7. Click **Copy Translated Text** to copy the result.
8. Click **🔊 Speak** to listen to the translation if your browser supports the selected language.
9. Click **⏹ Stop** to stop speech playback.
10. Click **🗑️ Clear** to clear the current translation.

## 🧠 How It Works

### 1. User Input

The user enters text and selects the source and target languages.

### 2. Language Detection

When Auto Detect is selected, Googletrans attempts to identify the source language automatically.

### 3. Translation

The application sends the translation request through Googletrans and receives the translated text.

### 4. Caching

The application uses Streamlit's `st.cache_data` to cache successful translation results for up to 24 hours. Repeated requests with the same text and language settings can reuse cached results.

### 5. Copy Functionality

JavaScript's Clipboard API allows users to copy the translated text when browser permissions and security requirements permit it.

### 6. Text-to-Speech

The browser's Web Speech API converts translated text into speech when a compatible speech voice is available.

## ⚠️ Limitations

- Googletrans relies on an unofficial interface to Google Translate and may stop working temporarily.
- Excessive requests can trigger rate limits.
- An active internet connection is generally required for translation requests that are not cached.
- Browser speech support and voice availability vary by language and device.
- The application supports a maximum input length of 5,000 characters.
- The current request delay is a basic per-session safeguard, not a global rate limiter across all users.
- Translation accuracy may vary depending on language, context, and sentence structure.

## 🔧 Troubleshooting

### Error: ModuleNotFoundError

Install the required libraries:

```bash
python -m pip install -r requirements.txt
```

### Error: Google Translate Is Temporarily Limiting Requests

Wait before trying again. Avoid repeatedly clicking the Translate button, and reuse cached translations where possible.

### Error: Streamlit Command Not Found

Run:

```bash
python -m streamlit run app.py
```

### Text-to-Speech Is Not Working

Check your browser's speech support, system volume, and availability of a voice for the selected language.

### Application Is Not Opening

Confirm that Streamlit has started successfully and open the local address shown in the terminal.

## 🔮 Future Improvements

- Add more languages.
- Integrate a translation service with an official API.
- Add translation history.
- Support document translation.
- Add speech-to-text input.
- Improve error handling and retry mechanisms.
- Add a downloadable translation feature.
- Deploy the application online.

## 🎯 Project Objectives

- Develop a simple and user-friendly translation application.
- Demonstrate Python and Streamlit development skills.
- Integrate a translation library into a web application.
- Provide convenient copy and speech functionality.
- Reduce unnecessary translation requests through caching.

## 👩‍💻 Author

**Zarfshan  Attiq Khan**

Project: Language Translation Tool

Technologies: Python | Streamlit | Googletrans | HTML | CSS | JavaScript

