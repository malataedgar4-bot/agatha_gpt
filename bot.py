import streamlit as st
import folium
from streamlit_folium import st_folium

# 1. PAGE CONFIG
st.set_page_config(
    page_title="Agatha U-D GPT",
    page_icon="🛰️",
    layout="centered"
)

# 2. ELITE STYLING
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #ffffff; }
    header, footer { visibility: hidden; }
    .agatha-bubble {
        background: #161b22; padding: 25px; border-radius: 15px;
        border: 1px solid #30363d; color: #e6edf3; margin-bottom: 20px;
    }
    .user-msg { color: #58a6ff; font-weight: bold; margin-bottom: 5px; }
    </style>
    """, unsafe_allow_html=True
)

# 3. KNOWLEDGE DATABASE
KNOWLEDGE_BASE = {
    "vc": "Prof. William Anangisye is the Vice-Chancellor, heading all UDSM operations.",
    "chancellor": "Dr. Jakaya Kikwete is the Chancellor and titular head of UDSM.",
    "council": "The University Council is chaired by Judge (Rtd) Damian Lubuva.",
    "academic": "Prof. Bonaventure Rutinwa is the DVC (Academic).",
    "pfa": "Prof. Bernadeta Killian is the DVC (Planning, Finance and Administration).",
    "hall 1": {"info": "Hall 1 is the primary male hostel near the Admin block.", "lat": -6.7800, "lon": 39.2030},
    "hall 3": {"info": "Hall 3 is a male hostel located near the Yombo complex.", "lat": -6.7850, "lon": 39.2060},
    "hall 5": {"info": "Hall 5 is a female hostel near the Health Centre.", "lat": -6.7820, "lon": 39.2120},
    "library": {"info": "The Dr. Wilbert Chagula Library is the heart of UDSM research.", "lat": -6.7828, "lon": 39.2045},
    "coict": {"info": "College of ICT is located at Kijitonyama Campus.", "lat": -6.7725, "lon": 39.2355},
    "daruso": "DARUSO is the Dar es Salaam University Students' Organization.",
}

# 4. SIDEBAR
with st.sidebar:
    st.title("🛰️ Agatha Settings")
    lang = st.selectbox("Language", ["English", "Kiswahili"])
    voice_on = st.toggle("Voice Assistance")
    if st.button("Clear Chat"):
        st.rerun()

# 5. MAIN CHAT INTERFACE
st.title("🛰️ Agatha U-D GPT")

welcome_msg = (
    "I'm Agatha. Ask me about UDSM leadership or campus locations."
    if lang == "English"
    else "Mimi ni Agatha. Niulize kuhusu uongozi wa UDSM au miundombinu."
)
st.markdown(f"<div class='agatha-bubble'>{welcome_msg}</div>", unsafe_allow_html=True)

user_query = st.chat_input("Message Agatha...")

if user_query:
    st.markdown(f"<div class='user-msg'>You: {user_query}</div>", unsafe_allow_html=True)
    
    query_lower = user_query.lower()
    response = "I am scanning... Try asking about 'VC', 'Hall 1', or 'Library'."
    map_data = None

    for key, data in KNOWLEDGE_BASE.items():
        if key in query_lower:
            if isinstance(data, dict):
                response = data["info"]
                map_data = data
            else:
                response = data
            break

    st.markdown(f"<div class='agatha-bubble'>{response}</div>", unsafe_allow_html=True)

    if map_data:
        m = folium.Map(
            location=[map_data["lat"], map_data["lon"]],
            zoom_start=17,
            tiles="CartoDB dark_matter"
        )
        folium.Marker(
            [map_data["lat"], map_data["lon"]],
            popup=response
        ).add_to(m)
        st_folium(m, width=700, height=300)

    if voice_on:
        st.toast("Agatha is responding via voice...")