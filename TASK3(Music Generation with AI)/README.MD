# 🎵 AI Music Generator Using LSTM and TensorFlow

## 📌 Project Overview

The **AI Music Generator** is a web-based application developed using Python, TensorFlow, and Streamlit. It uses a Long Short-Term Memory (LSTM) neural network to learn musical patterns from MIDI files and generate new music.

Users can upload MIDI files, train an AI model, generate a sequence of musical notes, and download the generated music as a MIDI file.

This project demonstrates how Deep Learning and Artificial Intelligence can be applied to music generation.

## 🎯 Project Objectives

- Develop an AI-powered music generation application.
- Use LSTM neural networks to learn musical sequences.
- Extract notes and chords from MIDI files.
- Preprocess musical data for model training.
- Train a deep learning model using TensorFlow.
- Generate new musical sequences using a trained model.
- Build an interactive interface using Streamlit.
- Allow users to download AI-generated music.

## ✨ Features

- 🎹 Upload multiple MIDI files.
- 🧠 Train an LSTM-based deep learning model.
- 🎼 Extract musical notes and chords using Music21.
- 🔢 Convert musical sequences into numerical data.
- 📊 Configure training epochs.
- ⚙️ Adjust the sequence length.
- 📈 Monitor training progress and loss.
- 🎵 Generate 100 musical notes.
- 💾 Export generated music as a MIDI file.
- 🌐 Use a simple, interactive Streamlit interface.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Streamlit | Web application interface |
| TensorFlow | Deep learning model development |
| Keras | LSTM model construction and training |
| NumPy | Numerical operations and data preprocessing |
| Music21 | MIDI parsing and musical note processing |
| LSTM | Learning sequential musical patterns |
| MIDI | Input and output music file format |

## 📂 Project Structure

```text
AI-Music-Generator/
│
├── app.py
├── requirements.txt
└── README.md
```

### File Description

- **`app.py`** — Contains the Streamlit application, MIDI processing, LSTM model, training process, and music generation logic.
- **`requirements.txt`** — Lists the Python libraries required to run the application.
- **`README.md`** — Provides project documentation and setup instructions.

## ⚙️ Installation and Setup

### Step 1: Clone the Repository

Replace `YOUR_USERNAME` with your GitHub username.

```bash
git clone https://github.com/YOUR_USERNAME/AI-Music-Generator.git
```

### Step 2: Open the Project Folder

```bash
cd AI-Music-Generator
```

### Step 3: Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### Step 4: Install Dependencies

Create a file named `requirements.txt` and add:

```text
streamlit
numpy
tensorflow
music21
```

Install the required libraries:

```bash
python -m pip install -r requirements.txt
```

**Note:** TensorFlow installation requirements depend on your Python version and operating system. Use a Python version supported by the TensorFlow release you install.

### Step 5: Run the Application

Make sure the Python file is named `app.py`.

Run the following command:

```bash
python -m streamlit run app.py
```

Streamlit will open the application in your web browser.

## 🧠 How It Works

The application follows these main steps.

### 1. Upload MIDI Files

Users upload one or more `.mid` or `.midi` files containing musical notes and chords.

### 2. Extract Musical Notes

The Music21 library parses the uploaded MIDI files and extracts musical information, including individual notes and chords.

- Individual notes are represented by pitch names.
- Chords are represented by their note numbers.

The extracted information becomes the dataset for training.

### 3. Prepare the Training Data

The application creates sequences of musical notes.

For example, if the sequence length is 4:

```text
Input:  [C4, D4, E4, G4]
Output: A4
```

The model learns to predict the next musical element based on the preceding sequence.

The input sequences are converted into numerical representations and reshaped for the LSTM network.

### 4. Build the LSTM Model

The model contains:

- **First LSTM layer:** Learns patterns in musical sequences.
- **Dropout layer:** Helps reduce overfitting.
- **Second LSTM layer:** Learns additional sequential patterns.
- **Dense layer:** Produces predictions for the possible musical elements.
- **Softmax activation:** Converts model outputs into a probability distribution.

The model is trained using categorical cross-entropy loss and the RMSprop optimizer.

### 5. Train the Model

Users can configure the number of training epochs through the Streamlit sidebar.

During training, the application displays:

- Current epoch.
- Total epochs.
- Training loss.
- Training progress.

### 6. Generate New Music

After training, the model uses an existing musical sequence as a starting point and repeatedly predicts the next musical element.

The application generates 100 notes or chord representations and converts the sequence into a MIDI file.

### 7. Download Generated Music

The generated music is saved as:

```text
generated_music.mid
```

Users can download the file through the Streamlit interface and play it using compatible MIDI software.

## 🎼 Model Architecture

The neural network uses the following architecture:

```text
Musical Note Sequences
          |
          v
     LSTM Layer
       (256)
          |
          v
    Dropout (0.3)
          |
          v
     LSTM Layer
       (256)
          |
          v
    Dropout (0.3)
          |
          v
     Dense Layer
    (Vocabulary Size)
          |
          v
  Softmax Activation
          |
          v
  Next Note Prediction
          |
          v
   Generated Music
```

## 🚀 How to Use the Application

1. Start the application using Streamlit.
2. Upload one or more MIDI files.
3. Select the training epochs from the sidebar.
4. Adjust the sequence length.
5. Click **Start Training & Generate Music**.
6. Wait for the application to extract notes and train the model.
7. Monitor the training progress.
8. Allow the application to generate a new musical sequence.
9. Click **Download Generated MIDI File**.
10. Open the downloaded file using MIDI-compatible software.

## 📁 Input and Output

| Type | Description |
|---|---|
| Input | MIDI files (`.mid`, `.midi`) |
| Training Data | Extracted musical notes and chords |
| AI Model | LSTM neural network |
| Output | Generated MIDI file |
| Output Filename | `ai_generated_music.mid` |

## ⚠️ Limitations

- The model requires suitable MIDI files for training.
- Training time depends on dataset size and available hardware.
- Music quality depends on the quantity and variety of training data.
- The current implementation generates a fixed sequence of 100 musical elements.
- The model predicts musical elements but does not explicitly model tempo, rhythm, or note duration.
- MIDI playback may not work directly in every web browser.
- The current implementation provides a MIDI download rather than a guaranteed playable audio preview.
- The model is trained from scratch whenever the training button is used; trained model weights are not saved for reuse.
- The generated output is a basic musical sequence and may need further editing.

## 🔮 Future Improvements

- Add a MIDI-to-WAV audio conversion feature.
- Add an in-browser audio player for generated music.
- Save trained models to avoid retraining.
- Support different musical genres.
- Improve the model using larger MIDI datasets.
- Add temperature-based sampling for more varied predictions.
- Include tempo, rhythm, and note duration in the training data.
- Add piano, guitar, and other instrument options.
- Deploy the application online.
- Improve error handling and input validation.

## 🎓 Learning Outcomes

This project helps demonstrate:

- Artificial Intelligence and Deep Learning.
- Recurrent Neural Networks (RNNs).
- Long Short-Term Memory (LSTM) networks.
- Sequential data processing.
- Musical note extraction from MIDI files.
- Data preprocessing with NumPy.
- Model training with TensorFlow and Keras.
- AI-based music generation.
- Streamlit application development.

## 👩‍💻 Author

**Zarfshan  ATTIQ Khan**

GitHub: Add your GitHub profile link here.

