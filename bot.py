import streamlit as st

# 1. ELITE PAGE CONFIG
st.set_page_config(page_title="Agatha U-D GPT", page_icon="🛰️", layout="centered")

# 2. CSS KILL-SWITCH (Clean & Professional)
st.markdown("""
    <style>
    .stApp { background-color: #0d1117; color: #ffffff; }
    header, footer, .stExpander { visibility: hidden !important; display: none !important; }
    .agatha-bubble {
        background: #161b22; padding: 25px; border-radius: 15px;
        border-left: 5px solid #58a6ff; color: #e6edf3; margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.5);
    }
    .user-msg { color: #58a6ff; font-weight: bold; margin-bottom: 5px; }
    </style>
    """, unsafe_allow_html=True)

# 3. MASTER QUADRILINGUAL VAULT (Restored IQ)
VAULT = {
    "vc": {
        "en": "The Vice-Chancellor is Prof. William Anangisye, the chief executive officer of UDSM.",
        "sw": "Makamu wa Kansela ni Prof. William Anangisye, mtendaji mkuu wa UDSM.",
        "zh": "副校长是 William Anangisye 教授。",
        "ar": "نائب المستشار هو الأستاذ ويليام أنانيسي."
    },
    "admin": {
        "en": "Chain of Command: Chancellor (Dr. Kikwete), Vice-Chancellor (Prof. Anangisye), and Deputy Vice-Chancellors.",
        "sw": "Uongozi: Kansela (Dr. Kikwete), Makamu wa Kansela (Prof. Anangisye), na Manaibu wake.",
        "zh": "领导层：校监（Kikwete）、副校长（Anangisye）及副职。",
        "ar": "الهيكل الإداري: المستشار (كيكويت) ونائب المستشار (أنانيسي)."
    },
    "semester 1": {
        "en": "Semester 1 (2025/2026) starts on 24 November 2025 and ends on 20 March 2026.",
        "sw": "Muhula wa Kwanza unaanza 24 Novemba 2025 na kuisha 20 Machi 2026.",
        "zh": "第一学期：2025年11月24日至2026年3月20日。",
        "ar": "الفصل الأول: ٢٤ نوفمبر ٢٠٢٥ إلى ٢٠ مارس ٢٠٢٦."
    },
    "exams": {
        "en": "Semester 1 exams are scheduled from 06 March to 20 March 2026.",
        "sw": "Mitihani ya Muhula wa 1 ni kuanzia tarehe 06 hadi 20 Machi 2026.",
        "zh": "第一学期考试：2026年3月6日至20日。",
        "ar": "امتحانات الفصل الدراسي الأول: من ٠٦ مارس إلى ٢٠ مارس ٢٠٢٦."
    },
    "graduation": {
        "en": "The 56th Graduation Ceremony (Cluster I) is on Friday, 29 May 2026.",
        "sw": "Mahafali ya 56 (Kundi la I) ni Ijumaa, tarehe 29 Mei 2026.",
        "zh": "第 56 届毕业典礼定于 2026 年 5 月 29 日。",
        "ar": "حفل التخرج السادس والخمسون في ٢٩ مايو ٢٠٢٦."
    }
}

# 4. SIDEBAR SETTINGS
with st.sidebar:
    st.title("🛰️ Agatha Settings")
    lang_choice = st.radio("Language", ["English", "Kiswahili", "Chinese", "Arabic"])
    l_key = {"English": "en", "Kiswahili": "sw", "Chinese": "zh", "Arabic": "ar"}[lang_choice]
    voice_on = st.toggle("Voice Assistance")

# 5. MAIN INTERFACE
st.title("🛰️ Agatha U-D GPT")
intros = {
    "en": "I am Agatha. How can I help you today?",
    "sw": "Mimi ni Agatha. Nikusaidie nini leo?",
    "zh": "我是 Agatha。我今天能为您提供什么帮助？",
    "ar": "أنا أجاثا. كيف يمكنني مساعدتك اليوم؟"
}
st.markdown(f"<div class='agatha-bubble'>{intros[l_key]}</div>", unsafe_allow_html=True)

# 6. LOGIC
user_query = st.chat_input("Message Agatha...")
if user_query:
    st.markdown(f"<div class='user-msg'>You: {user_query}</div>", unsafe_allow_html=True)
    res = "I don't have that data yet. Try 'VC' or 'Semester 1'."
    for k in VAULT:
        if k in user_query.lower():
            res = VAULT[k][l_key]
    st.markdown(f"<div class='agatha-bubble'>{res}</div>", unsafe_allow_html=True)
    if voice_on:
        st.toast("🔊 Responding...")