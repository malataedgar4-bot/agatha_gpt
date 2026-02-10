import streamlit as st
import folium
from streamlit_folium import st_folium

# 1. PAGE CONFIG
st.set_page_config(page_title="Agatha U-D GPT", page_icon="🛰️", layout="centered")

# 2. THE AGATHA AESTHETIC (Elite Dark Mode)
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #ffffff; }
    .agatha-bubble {
        background: #161b22;
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #30363d;
        margin-bottom: 20px;
        color: #e6edf3;
        line-height: 1.6;
    }
    .user-msg {
        color: #58a6ff;
        font-weight: bold;
        margin-top: 10px;
    }
    /* Hide the ugly sidebar scroll and standard headers */
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# 3. FULL KNOWLEDGE BASE [cite: 2026-02-06]
KNOWLEDGE_IQ = {
    "council": "Judge (Rtd) Damian Lubuva chairs the University Council, our top policy body.",
    "chancellor": "Dr. Jakaya Kikwete is the Chancellor, representing the university's vision.",
    "vc": "Prof. William Anangisye is the Vice-Chancellor, heading all operations.",
    "academic": "Prof. Bonaventure Rutinwa (DVC-Academic) oversees research and studies.",
    "finance": "Prof. Bernadeta Killian (DVC-PFA) manages resources and planning.",
    "hall 1": {"info": "Hall 1 is near the main administration area.", "lat": -6.7800, "lon": 39.2030},
    "hall 3": {"info": "Hall 3 is located near the Yombo complex.", "lat": -6.7850, "lon": 39.2060},
    "library": {"info": "The Dr. Wilbert Chagula Library is at the campus center.", "lat": -6.7828, "lon": 39.2045}
}

# 4. SIDEBAR (Tucked away settings) [cite: 2026-02-06, 2026-02-07]
with st.sidebar:
    st.title("🛰️ Agatha Core")
    lang = st.selectbox("Language / Lugha", ["English", "Kiswahili", "Chinese", "French"])
    voice_on = st.toggle("Voice Assistance")
    st.divider()
    st.markdown("U-D GPT: Elite Edition")

# 5. HEADER
st.title("🛰️ Agatha U-D GPT")

# 6. CHAT LOGIC & MAP INTEGRATION
user_query = st.chat_input("Ask Agatha about UDSM...")

if user_query:
    st.markdown(f"<div class='user-msg'>You: {user_query}</div>", unsafe_allow_html=True)
    query = user_query.lower()
    
    response = "I am processing that request. Try asking about the 'VC', 'Library', or 'Hall 1'."
    map_data = None

    # Search through the knowledge base
    for key, data in KNOWLEDGE_IQ.items():
        if key in query:
            if isinstance(data, dict):
                response = data["info"]
                map_data = data
            else:
                response = data
            break

    # Display Agatha's bubble
    st.markdown(f"<div class='agatha-bubble'>{response}</div>", unsafe_allow_html=True)

    # If the response includes a location, show the map ONLY then
    if map_data:
        st.markdown("### 📍 Geospatial Context")
        m = folium.Map(location=[map_data["lat"], map_data["lon"]], zoom_start=17, tiles="CartoDB dark_matter")
        folium.Marker([map_data["lat"], map_data["lon"]], popup=response).add_to(m)
        st_folium(m, width=700, height=300)

    # Voice Notification [cite: 2026-02-07]
    if voice_on:
        st.toast("Agatha is speaking...")
else:
    # Initial Welcome (when no query is active)
    welcome = {
        "English": "I'm Agatha. Ask me anything about UDSM's leadership or campus infrastructure.",
        "Kiswahili": "Mimi ni Agatha. Niulize lolote kuhusu uongozi wa UDSM au miundombinu."
    }
    st.markdown(f"<div class='agatha-bubble'>{welcome.get(lang, welcome['English'])}</div>", unsafe_allow_html=True)