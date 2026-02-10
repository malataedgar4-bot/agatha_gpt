import streamlit as st

# 1. PAGE SETUP
st.set_page_config(page_title="Agatha U-D GPT", page_icon="🛰️", layout="centered")

# 2. CSS KILL-SWITCH (Clean Professional Look)
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #ffffff; }
    header, footer, .stExpander { visibility: hidden !important; display: none !important; }
    .agatha-bubble {
        background: #161b22; padding: 25px; border-radius: 15px;
        border-left: 5px solid #58a6ff; color: #e6edf3; margin-bottom: 20px;
    }
    .user-msg { color: #58a6ff; font-weight: bold; margin-bottom: 5px; }
    </style>
    """, unsafe_allow_html=True)

# 3. QUADRILINGUAL KNOWLEDGE (Almanac + Admin)
VAULT = {
    "vc": {
        "en": "The Vice-Chancellor is Prof. William Anangisye.",
        "sw": "Makamu wa Kansela ni Prof. William Anangisye.",
        "zh": "副校长是 William Anangisye 教授。",
        "ar": "نائب المستشار هو الأستاذ ويليام أنانيسي."
    },
    "semester 1": {
        "en": "Starts: 24 Nov 2025 | Ends: 20 March 2026.",
        "sw": "Inaanza: 24 Nov 2025 | Inatamatika: 20 Machi 2026.",
        "zh": "开始：2025年11月24日 | 结束：2026年3月20日。",
        "ar": "البداية: ٢٤ نوفمبر ٢٠٢٥ | النهاية: ٢٠ مارس ٢٠٢٦."
    },
    "exams": {
        "en": "Sem 1 Exams: 06-20 March 2026.",
        "sw": "Mitihani Sem 1: 06-20 Machi 2026.",
        "zh": "第一学期考试：2026年3月6日至20日。",
        "ar": "امتحانات الفصل الدراسي الأول: ٠٦-٢٠ مارس ٢٠٢٦."
    }
}

# 4. SIDEBAR
with st.sidebar:
    st.title("🛰️ Agatha Settings")
    lang = st.radio("Language", ["English", "Kiswahili", "Chinese", "Arabic"])
    l_key = {"English": "en", "Kiswahili": "sw", "Chinese": "zh", "Arabic": "ar"}[lang]

# 5. INTERFACE
st.title("🛰️ Agatha U-D GPT")
st.markdown(f"<div class='agatha-bubble'>Agatha Navigator Ready ({lang})</div>", unsafe_allow_html=True)

# 6. LOGIC
query = st.chat_input("Ask Agatha...")
if query:
    st.markdown(f"<div class='user-msg'>You: {query}</div>", unsafe_allow_html=True)
    res = "Data not found. Try 'VC' or 'Exams'."
    for k in VAULT:
        if k in query.lower():
            res = VAULT[k][l_key]
    st.markdown(f"<div class='agatha-bubble'>{res}</div>", unsafe_allow_html=True)