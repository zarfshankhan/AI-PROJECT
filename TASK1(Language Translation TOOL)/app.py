import streamlit as st
import streamlit.components.v1 as components
from googletrans import Translator
import json
import html
import time
import asyncio

# =====================================
# PAGE CONFIGURATION
# =====================================
st.set_page_config(
    page_title="Language Translation Tool",
    page_icon="🌍",
    layout="centered"
)

# =====================================
# CACHED TRANSLATION FUNCTION
# =====================================
@st.cache_data(ttl=86400, max_entries=200, show_spinner=False)
def translate_text(text, source_code, target_code):
    """Cache successful translations for 24 hours."""
    # googletrans needs asyncio in some environments
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

    translator = Translator()
    
    # If source is 'auto', googletrans uses 'auto'
    if source_code == "auto":
        source_code = "auto"

    result = translator.translate(text, src=source_code, dest=target_code)

    if not result or not result.text:
        raise ValueError("No translation was returned.")

    return result.text

# =====================================
# CUSTOM DESIGN
# =====================================
st.markdown("""
<style>
.stApp {
    background-color: #f5f7ff;
}
.title {
    text-align: center;
    font-size: 36px;
    font-weight: bold;
    color: #5947d9;
}
.subtitle {
    text-align: center;
    color: #555;
    margin-bottom: 25px;
}
.result {
    background-color: white;
    border: 2px solid #7967f5;
    border-radius: 12px;
    padding: 20px;
    font-size: 20px;
    white-space: pre-wrap;
    overflow-wrap: anywhere;
    color: black; 
}

/* YEH NAYA CODE ADD KAREIN */
h1, h2, h3, h4, h5, h6, p, span {
    color: #333333 !important; 
}
</style>
""", unsafe_allow_html=True)

# =====================================
# TITLE
# =====================================
st.markdown('<div class="title">🌍 Language Translation Tool</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Translate text between multiple languages</div>', unsafe_allow_html=True)

# =====================================
# SUPPORTED LANGUAGES
# =====================================
languages = {
    "Arabic": "ar", "Chinese": "zh-CN", "English": "en", "French": "fr",
    "German": "de", "Hindi": "hi", "Italian": "it", "Japanese": "ja",
    "Korean": "ko", "Persian": "fa", "Punjabi": "pa", "Russian": "ru",
    "Spanish": "es", "Turkish": "tr", "Urdu": "ur"
}

# =====================================
# LANGUAGE SELECTION
# =====================================
col1, col2 = st.columns(2)
with col1:
    source_language = st.selectbox("Source Language", ["Auto Detect"] + list(languages.keys()))
with col2:
    target_language = st.selectbox("Target Language", list(languages.keys()), index=list(languages.keys()).index("Urdu"))

# =====================================
# TEXT INPUT
# =====================================
input_text = st.text_area("Enter text to translate", placeholder="Type your text here...", height=160, max_chars=5000)
st.caption(f"Characters: {len(input_text)} / 5000")

# =====================================
# SESSION STATE
# =====================================
if "last_translation_time" not in st.session_state:
    st.session_state["last_translation_time"] = 0.0
if "translated_text" not in st.session_state:
    st.session_state["translated_text"] = ""
if "target_code" not in st.session_state:
    st.session_state["target_code"] = "ur"

# =====================================
# BUTTONS
# =====================================
col_translate, col_clear = st.columns(2)
with col_translate:
    translate_clicked = st.button("🌐 Translate", type="primary", use_container_width=True)
with col_clear:
    clear_clicked = st.button("🗑️ Clear", use_container_width=True)

if clear_clicked:
    st.session_state["translated_text"] = ""
    st.session_state["target_code"] = "ur"
    st.session_state["last_translation_time"] = 0.0
    st.rerun()

# =====================================
# TRANSLATION LOGIC
# =====================================
if translate_clicked:
    if not input_text.strip():
        st.warning("Please enter text first.")
    elif source_language != "Auto Detect" and source_language == target_language:
        st.warning("Select two different languages.")
    else:
        now = time.time()
        last_time = st.session_state["last_translation_time"]

        # 4 seconds delay to prevent rate limiting
        if now - last_time < 4:
            st.warning("Please wait a few seconds before translating again.")
        else:
            st.session_state["last_translation_time"] = now
            source_code = "auto" if source_language == "Auto Detect" else languages[source_language]
            target_code = languages[target_language]

            try:
                with st.spinner("Translating text..."):
                    result = translate_text(input_text.strip(), source_code, target_code)

                st.session_state["translated_text"] = result
                st.session_state["target_code"] = target_code
                st.success("Translation completed!")

            except Exception as e:
                error_msg = str(e).lower()
                if "too many requests" in error_msg or "429" in error_msg:
                    st.error("Google Translate is temporarily limiting requests. Please wait a few minutes and try again, or switch to a different internet connection (like Mobile Hotspot).")
                else:
                    st.error(f"Translation failed: {type(e).__name__}: {e}")

# =====================================
# DISPLAY RESULT
# =====================================
translated_text = st.session_state["translated_text"]
target_code = st.session_state["target_code"]

if translated_text:
    st.divider()
    st.subheader("📄 Translated Text")
    st.markdown('<div class="result">' + html.escape(translated_text) + '</div>', unsafe_allow_html=True)

    # COPY BUTTON
    st.markdown("### 📋 Copy Translation")
    copy_html = f"""
    <button id="copyButton" style="width:100%; padding:12px; background:#5947d9; color:white; border:none; border-radius:8px; cursor:pointer; font-size:16px;">
        Copy Translated Text
    </button>
    <p id="copyMessage" style="color: #198754; font-size: 14px; font-weight: bold;"></p>
    <script>
    const translatedText = {json.dumps(translated_text, ensure_ascii=False)};
    document.getElementById("copyButton").onclick = async function() {{
        const message = document.getElementById("copyMessage");
        try {{
            await navigator.clipboard.writeText(translatedText);
            message.textContent = "✅ Copied successfully!";
        }} catch (e) {{
            message.textContent = "❌ Copy unavailable. Please select manually.";
        }}
    }};
    </script>
    """
    components.html(copy_html, height=100)
    
    # TEXT TO SPEECH
    st.markdown("### 🔊 Listen to Translation")
    # Map language codes for speech synthesis
    speech_lang_map = {"zh-CN": "zh-CN", "ur": "ur-PK", "ar": "ar-SA", "fa": "fa-IR", "pa": "pa-IN"}
    speech_lang = speech_lang_map.get(target_code, target_code)

    speech_html = f"""
    <button id="speakButton" style="padding:12px 22px; background:#198754; color:white; border:none; border-radius:8px; cursor:pointer; font-weight: bold;">
        🔊 Speak
    </button>
    <button id="stopButton" style="padding:12px 22px; margin-left:8px; border:1px solid #888; border-radius:8px; cursor:pointer; background: #f0f0f0; font-weight: bold;">
        ⏹ Stop
    </button>
    <script>
    const textToSpeak = {json.dumps(translated_text, ensure_ascii=False)};
    const languageCode = {json.dumps(speech_lang)};

    document.getElementById("speakButton").onclick = function() {{
        if (!window.speechSynthesis) {{
            alert("Speech is not supported by this browser.");
            return;
        }}
        window.speechSynthesis.cancel();
        const speech = new SpeechSynthesisUtterance(textToSpeak);
        speech.lang = languageCode;
        window.speechSynthesis.speak(speech);
    }};

    document.getElementById("stopButton").onclick = function() {{
        if (window.speechSynthesis) {{
            window.speechSynthesis.cancel();
        }}
    }};
    </script>
    """
    components.html(speech_html, height=60)

# =====================================
# FOOTER
# =====================================
st.divider()
st.caption("Language Translation Tool | Python + Streamlit")