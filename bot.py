import streamlit as st
import folium
from streamlit_folium import st_folium

# 1. PAGE CONFIG
st.set_page_config(page_title="Agatha U-D GPT", page_icon="🛰️", layout="centered")

# 2. THE DARK LOOK: CSS STYLING
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    .chat-wrapper { max-width: 850px; margin: auto; padding-top: 50px; }
    .agatha-msg {
        background-color: #1e2530; padding: 20px; border-radius: 15px;
        border-left: 4px solid #4a90e2; margin-bottom: 25px;
        font-size: 18px; line-height: 1.6; color: #e6edf3 !important;
    }
    section[data-testid="stSidebar"] { background-color: #161b22 !important; }
    h1, h2, h3, p, span, stMarkdown { color: #e6edf3 !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. KNOWLEDGE BASE
KNOWLEDGE_IQ = {
    "council": "Judge (Rtd) Damian Lubuva chairs the University Council.",
    "chancellor": "Dr. Jakaya Kikwete is the Chancellor.",
    "vc": "Prof. William Anangisye is the Vice-Chancellor.",
    "academic": "Prof. Bonaventure Rutinwa (DVC-Academic) oversees research.",
    "finance": "Prof. Bernadeta Killian (DVC-PFA) manages resources.",
    "hall 1": "Hall 1 is near the main administration area.",
    "hall 3": "Hall 3 is located near the Yombo complex.",
    "coict": "The College of ICT is located at the Kijitonyama Campus.",
    "library": "The Dr. Wilbert Chagula Library is at the campus center.",
    "health": "The University Health Centre is near the main gate."
}

# 4. SIDEBAR & VOICE SETTINGS
with st.sidebar:
    st.markdown("### Agatha Core")
    lang = st.selectbox("Language / Lugha", ["English", "Kiswahili", "Chinese", "French"])
    voice_on = st.toggle("Voice Assistance")
    st.divider()
    st.markdown("U-D GPT: Elite Edition")

# 5. THE INTERFACE FLOW
st.markdown("<div class='chat-wrapper'>", unsafe_allow_html=True)
st.title("🛰️ Agatha U-D GPT")

welcome_text = {
    "English": "I'm Agatha. Ask me anything about UDSM's leadership or campus infrastructure.",
    "Kiswahili": "Mimi ni Agatha. Niulize lolote kuhusu uongozi wa UDSM au miundombinu ya kampasi.",
    "Chinese": "我是艾格峰。询问我有关 UDSM 领导层或校园基础设施的任何信息。",
    "French": "Je suis Agatha. Posez-moi des questions sur la direction ou l'infrastructure de l'UDSM."
}
st.markdown(f"<div class='agatha-msg'>{welcome_text[lang]}</div>", unsafe_allow_html=True)

# Quick Info & Map
col1, col2 = st.columns(2)
with col1:
    with st.expander("🎓 Institutional IQ"):
        st.write("**VC:** Prof. William Anangisye")
        st.write("**Council:** Judge Damian Lubuva")
with col2:
    with st.expander("📍 Geospatial View"):
        m = folium.Map(location=[-6.7828, 39.2045], zoom_start=16, tiles="CartoDB dark_matter")
        folium.Marker([-6.7828, 39.2045], popup="Admin Block").add_to(m)
        st_folium(m, width=350, height=250)

# 6. CHAT LOGIC
user_query = st.chat_input("Ask about leaders, offices, or campus locations...")

if user_query:
    st.markdown(f"**You:** {user_query}")
    query = user_query.lower()
    
    response = "I am processing that. Try asking about the 'VC', 'Council', or 'Hall 3'."
    for key, info in KNOWLEDGE_IQ.items():
        if key in query:
            response = info
            break
    
    st.markdown(f"<div class='agatha-msg'>{response}</div>", unsafe_allow_html=True)

    if voice_on:
        st.info("Voice Assistant is Active. (Agatha is speaking...)")

st.markdown("</div>", unsafe_allow_html=True)