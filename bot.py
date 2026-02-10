import streamlit as st
import folium
from streamlit_folium import st_folium

# 1. PAGE CONFIG
st.set_page_config(page_title="Agatha U-D GPT", page_icon="🛰️", layout="centered")

# 2. ELITE STYLING (Hiding all the 'ugly' boxes)
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #ffffff; }
    header, footer {visibility: hidden;}
    .agatha-bubble {
        background: #161b22; padding: 25px; border-radius: 15px;
        border: 1px solid #30363d; color: #e6edf3; margin-bottom: 20px;
    }
    .user-msg { color: #58a6ff; font-weight: bold; margin-bottom: 5px; }
    </style>
    """, unsafe_allow_html=True)

# 3. HIGH-IQ DATABASE [cite: 2026-02-06]
KNOWLEDGE_IQ = {
    "vc": "Prof. William Anangisye is the Vice-Chancellor, heading all UDSM operations.",
    "chancellor": "Dr. Jakaya Kikwete is the Chancellor and titular head of UDSM.",
    "council": "The University Council is chaired by Judge (Rtd) Damian Lubuva.",
    "library": {"info": "The Dr. Wilbert Chagula Library is the heart of UDSM research.", "lat": -6.7828, "lon": 39.2045},
    "hall 1": {"info": "Hall 1 is the primary male hostel near the Admin block.", "lat": -6.7800, "lon": 39.2030},
    "hall 5": {"info": "Hall 5 is a female hostel near the Health Centre.", "lat": -6.7820, "lon": 39.2120},
    "daruso": "DARUSO is the Dar es Salaam University Students' Organization.",
    "coict": {"info": "College of ICT is located at Kijitonyama Campus.", "lat": -6.7725, "lon": 39.2355}
}

# 4. SIDEBAR & VOICE SETTINGS [cite: 2026-02-06, 2026-02-07]
with st.sidebar:
    st.title("🛰️ Agatha Settings")
    lang = st.selectbox("Language", ["English", "Kiswahili"])
    voice_on = st.toggle("Voice Assistance")
    if st.button("Clear Chat"):
        st.rerun()

# 5. MAIN CHAT
st.title("🛰️ Agatha U-D GPT")
welcome = "I'm Agatha. Ask me about UDSM leadership or locations." if lang == "English" else "Mimi ni Agatha. Niulize kuhusu UDSM."
st.markdown(f"<div class='agatha-bubble'>{welcome}</div>", unsafe_allow_html=True)

user_query = st.chat_input("Message Agatha...")

if user_query:
    st.markdown(f"<div class='user-msg'>You: {user_query}</div>", unsafe_allow_html=True)
    query = user_query.lower()
    response = "I'm still learning that. Try 'VC' or 'Hall 1'."
    map_data = None

    for key, data in KNOWLEDGE_IQ.items():
        if key in query:
            if isinstance(data, dict):
                response, map_data = data["info"], data
            else:
                response = data
            break

    st.markdown(f"<div class='agatha-bubble'>{response}</div>", unsafe_allow_html=True)

    if map_data:
        m = folium.Map(location=[map_data["lat"], map_data["lon"]], zoom_start=17, tiles="CartoDB dark_matter")
        folium.Marker([map_data["lat"], map_data["lon"]]).add_to(m)
        st_folium(m, width=700, height=300)

    # Voice Discipline [cite: 2026-02-07]
    if voice_on:
        st.toast("Agatha is speaking...")