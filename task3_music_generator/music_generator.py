import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.utils import to_categorical
from music21 import converter, instrument, note, chord, stream
import glob
import os
import time

# Page Config
st.set_page_config(page_title="AI Music Generator", page_icon="🎵", layout="centered")
st.title("🎵 AI Music Generator")
st.markdown("Upload MIDI files, train the AI, and generate new music!")

# =====================================
# SIDEBAR FOR SETTINGS
# =====================================
st.sidebar.header("Settings")
epochs = st.sidebar.slider("Training Epochs", min_value=5, max_value=50, value=15, step=5)
sequence_length = st.sidebar.slider("Sequence Length", min_value=10, max_value=50, value=30, step=5)

# =====================================
# HELPER FUNCTIONS
# =====================================
def get_notes_from_files(file_paths):
    notes = []
    for file in file_paths:
        try:
            midi = converter.parse(file)
            parts = instrument.partitionByInstrument(midi)
            notes_to_parse = parts.parts[0].recurse() if parts else midi.flat.notes
            for element in notes_to_parse:
                if isinstance(element, note.Note):
                    notes.append(str(element.pitch))
                elif isinstance(element, chord.Chord):
                    notes.append('.'.join(str(n) for n in element.normalOrder))
        except Exception as e:
            st.warning(f"Error parsing {file}: {e}")
    return notes

def prepare_sequences(notes, n_vocab, seq_len):
    pitchnames = sorted(set(item for item in notes))
    note_to_int = dict((note, number) for number, note in enumerate(pitchnames))
    network_input, network_output = [], []
    
    for i in range(0, len(notes) - seq_len, 1):
        seq_in = notes[i:i + seq_len]
        seq_out = notes[i + seq_len]
        network_input.append([note_to_int[char] for char in seq_in])
        network_output.append(note_to_int[seq_out])
        
    n_patterns = len(network_input)
    network_input = np.reshape(network_input, (n_patterns, seq_len, 1))
    network_input = network_input / float(n_vocab)
    network_output = to_categorical(network_output, num_classes=n_vocab)
    return network_input, network_output, note_to_int, pitchnames

def generate_and_save_music(model, network_input, int_to_note, n_vocab, seq_len):
    start = np.random.randint(0, len(network_input)-1)
    pattern = network_input[start]
    prediction_output = []

    # Progress bar for generation
    progress_bar = st.progress(0)
    status_text = st.empty()

    for note_index in range(100): # Generate 100 notes
        prediction_input = np.reshape(pattern, (1, len(pattern), 1))
        prediction_input = prediction_input / float(n_vocab)
        prediction = model.predict(prediction_input, verbose=0)
        index = np.argmax(prediction)
        result = int_to_note[index]
        prediction_output.append(result)
        pattern = np.append(pattern, index)
        pattern = pattern[1:len(pattern)]
        
        # Update progress
        progress_bar.progress((note_index + 1) / 100)
        status_text.text(f"Generating notes... {note_index + 1}/100")

    # Convert to MIDI
    offset = 0
    output_notes = []
    for pattern in prediction_output:
        if ('.' in pattern) or pattern.isdigit():
            notes_in_chord = pattern.split('.')
            notes = []
            for current_note in notes_in_chord:
                new_note = note.Note(int(current_note))
                new_note.storedInstrument = instrument.Piano()
                notes.append(new_note)
            new_chord = chord.Chord(notes)
            new_chord.offset = offset
            output_notes.append(new_chord)
        else:
            new_note = note.Note(pattern)
            new_note.offset = offset
            new_note.storedInstrument = instrument.Piano()
            output_notes.append(new_note)
        offset += 0.5

    midi_stream = stream.Stream(output_notes)
    output_file = "generated_music.mid"
    midi_stream.write('midi', fp=output_file)
    return output_file

# =====================================
# MAIN UI LOGIC
# =====================================
uploaded_files = st.file_uploader("Upload MIDI Files (.mid)", type=["mid", "midi"], accept_multiple_files=True)

if uploaded_files:
    st.success(f"{len(uploaded_files)} files uploaded successfully!")
    
    if st.button("🚀 Start Training & Generate Music", type="primary"):
        # Save uploaded files to a temp directory
        os.makedirs("temp_midi", exist_ok=True)
        file_paths = []
        for uploaded_file in uploaded_files:
            file_path = os.path.join("temp_midi", uploaded_file.name)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            file_paths.append(file_path)
            
        with st.spinner("Extracting notes from MIDI files..."):
            notes = get_notes_from_files(file_paths)
            
        if len(notes) < sequence_length:
            st.error("Not enough notes in the uploaded files. Please upload more or longer MIDI files.")
        else:
            st.info(f"Total notes extracted: {len(notes)} | Unique notes: {len(set(notes))}")
            
            with st.spinner("Preparing data for training..."):
                n_vocab = len(set(notes))
                network_input, network_output, note_to_int, pitchnames = prepare_sequences(notes, n_vocab, sequence_length)
                int_to_note = dict((number, note) for number, note in enumerate(pitchnames))
            
            # Build Model
            model = Sequential([
                LSTM(256, input_shape=(network_input.shape[1], network_input.shape[2]), return_sequences=True),
                Dropout(0.3),
                LSTM(256),
                Dropout(0.3),
                Dense(n_vocab),
                tf.keras.layers.Activation('softmax')
            ])
            model.compile(loss='categorical_crossentropy', optimizer='rmsprop')
            
            # Train Model with Progress Bar
            st.write("### 🧠 Training the AI Model...")
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            class StreamlitCallback(tf.keras.callbacks.Callback):
                def on_epoch_end(self, epoch, logs=None):
                    progress_bar.progress((epoch + 1) / epochs)
                    status_text.text(f"Epoch {epoch + 1}/{epochs} - Loss: {logs['loss']:.4f}")
            
            model.fit(network_input, network_output, epochs=epochs, batch_size=64, callbacks=[StreamlitCallback()], verbose=0)
            
            st.success("Training Completed! Generating new music...")
            
            # Generate Music
            output_file = generate_and_save_music(model, network_input, int_to_note, n_vocab, sequence_length)
            
            st.write("### 🎶 Listen to your AI-Generated Music")
            
            # Convert MIDI to Audio (WAV) for browser playback using pygame (if installed)
            try:
                import pygame
                # Pygame needs some setup to work in Streamlit environment
                # For simplicity, we'll provide the MIDI file for download and a basic audio player attempt
                with open(output_file, "rb") as f:
                    st.audio(f.read(), format="audio/midi") # This might not play in all browsers
            except Exception as e:
                st.warning("Your browser might not support MIDI playback directly.")
                
            # Always provide a download button
            with open(output_file, "rb") as f:
                st.download_button(
                    label="⬇️ Download Generated MIDI File",
                    data=f,
                    file_name="ai_generated_music.mid",
                    mime="audio/midi"
                )
            st.balloons()