import streamlit as st
import folium
from streamlit_folium import st_folium

# 1. ELITE PAGE SETUP
st.set_page_config(page_title="Agatha U-D GPT", page_icon="🛰️", layout="centered")

# 2. CSS KILL-SWITCH (Zero 'Ugly' Boxes) [cite: 2026-02-06, 2026-02-10]
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #ffffff; }
    header, footer, .stExpander { visibility: hidden !important; display: none !important; }
    .agatha-bubble {
        background: #161b22; padding: 25px; border-radius: 15px;
        border: 1px solid #30363d; color: #e6edf3; margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);
    }
    .user-msg { color: #58a6ff; font-weight: bold; margin-bottom: 5px; }
    </style>
    """, unsafe_allow_html=True)

# 3. POLYGLOT KNOWLEDGE DATABASE [cite: 2026-02-06]
# Intelligence covers: Admin, Chain of Command, Offices, Hostels, Cafes, Rooms, Emergency
KNOWLEDGE = {
    "admin": {
        "en": "UDSM Chain of Command: 1. Chancellor (Titular Head), 2. Vice-Chancellor (Chief Executive), 3. Deputy Vice-Chancellors (Academic and PFA).",
        "sw": "Uongozi wa UDSM: 1. Kansela (Mkuu wa Heshima), 2. Makamu wa Kansela (Mtendaji Mkuu), 3. Naibu Makamu wa Kansela (Taaluma na PFA)."
    },
    "vc": {
        "en": "The Vice-Chancellor is Prof. William Anangisye. He oversees all university operations.",
        "sw": "Makamu wa Kansela ni Prof. William Anangisye. Anasimia shughuli zote za chuo."
    },
    "chancellor": {
        "en": "The Chancellor is Dr. Jakaya Mrisho Kikwete, the former President of Tanzania.",
        "sw": "Kansela ni Dr. Jakaya Mrisho Kikwete, Rais mstaafu wa Tanzania."
    },
    "offices": {
        "en": "Main administration offices are located in the Administration Block near the main entrance.",
        "sw": "Ofisi kuu za utawala zipo jengo la Utawala (Admin Block) karibu na geti kuu."
    },
    "hostels": {
        "en": "Hostels include Hall 1-6 (Main Campus), Mabibo Hostels, and Dr. John Joseph Pombe Magufuli Hostels.",
        "sw": "Hosteli ni pamoja na Hall 1-6 (Kampasi Kuu), Hosteli za Mabibo, na Hosteli za Dr. John Joseph Pombe Magufuli."
    },
    "hall 1": {"info": "Hall 1: Primary male hostel near Admin.", "lat": -6.7800, "lon": 39.2030},
    "hall 5": {"info": "Hall 5: Female hostel near Health Centre.", "lat": -6.7820, "lon": 39.2120},
    "cafes": {
        "en": "Major cafes: Mlimani Main Cafeteria, CoET Cafe, and various vendors at Yombo and UDBS.",
        "sw": "Migahawa mikuu: Mlimani Main Cafeteria, CoET Cafe, na vibanda vya Yombo na UDBS."
    },
    "yombo": {"info": "Yombo: Largest complex for lecture rooms and exam halls.", "lat": -6.7845, "lon": 39.2065},
    "health": {"info": "UDSM Health Centre: Medical and Emergency services near the main gate.", "lat": -6.7815, "lon": 39.2100},
    "emergency": {
        "en": "EMERGENCY: Contact UDSM Health Centre or Campus Security immediately.",
        "sw": "DHARURA: Wasiliana na Kituo cha Afya cha UDSM au Ulinzi wa Kampasi haraka."
    }
}

# 4. SIDEBAR SETTINGS [cite: 2026-02-06, 2026-02-07]
with st.sidebar:
    st.title("🛰️ Agatha Settings")
    lang_choice = st.radio("Language / Lugha", ["English", "Kiswahili"])
    l_key = "en" if lang_choice == "English" else "sw"
    voice_on = st.toggle("Voice Assistance / Sauti")
    if st.button("Reset Chat"):
        st.rerun()

# 5. INTERFACE
st.title("🛰️ Agatha U-D GPT")
intro = "I am Agatha. Ask me about UDSM's command, hostels, cafes, or emergency services." if l_key == "en" else "Mimi ni Agatha. Niulize kuhusu uongozi wa UDSM, hosteli, migahawa, au dharura."
st.markdown(f"<div class='agatha-bubble'>{intro}</div>", unsafe_allow_html=True)

# 6. POLYGLOT CHAT LOGIC
user_query = st.chat_input("Message Agatha...")

if user_query:
    st.markdown(f"<div class='user-msg'>You: {user_query}</div>", unsafe_allow_html=True)
    q = user_query.lower()
    response = "I am scanning... try 'VC', 'Hostels', or 'Yombo'." if l_key == "en" else "Natafuta... jaribu 'VC', 'Hosteli', au 'Yombo'."
    map_data = None

    for key, data in KNOWLEDGE.items():
        if key in q:
            if "lat" in str(data): # Map data
                response, map_data = data["info"], data
            else: # Multilingual text
                response = data[l_key]
            break

    st.markdown(f"<div class='agatha-bubble'>{response}</div>", unsafe_allow_html=True)

    if map_data:
        m = folium.Map(location=[map_data["lat"], map_data["lon"]], zoom_start=17, tiles="CartoDB dark_matter")
        folium.Marker([map_data["lat"], map_data["lon"]], popup=response).add_to(m)
        st_folium(m, width=700, height=300)

    if voice_on:
        st.toast("🔊 Agatha speaking..." if l_key == "en" else "🔊 Agatha anaongea...")