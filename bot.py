import streamlit as st

# 1. PAGE SETUP (The "Look")
st.set_page_config(page_title="Agatha U-D GPT", page_icon="🛰️", layout="centered")

# 2. CSS (Hides the "Ugly" parts and the Vault)
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

# 3. THE HIDDEN VAULT (Merged Intel)
VAULT = {
    "vc": {
        "en": "The Vice-Chancellor is Prof. William Anangisye. He is the CEO of UDSM.",
        "sw": "Makamu wa Kansela ni Prof. William Anangisye. Ndiye mtendaji mkuu wa UDSM.",
        "zh": "副校长是 William Anangisye 教授。",
        "ar": "نائب المستشار هو الأستاذ ويليام أنانيسي."
    },
    "semester 1": {
        "en": "Semester 1 (2025/2026) starts 24 Nov 2025 and ends 20 March 2026.",
        "sw": "Muhula wa 1 unaanza 24 Nov 2025 na kuisha 20 Machi 2026.",
        "zh": "第一学期：2025年11月24日至2026年3月20日。",
        "ar": "يبدأ الفصل الدراسي الأول في 24 نوفمبر 2025."
    },
    "postgraduate": {
        "en": "Apply via UDSM-OAS. GPA Requirements: 2.7 for Coursework, 3.5 for Thesis.",
        "sw": "Omba kupitia UDSM-OAS. Sifa za GPA: 2.7 (masomo) na 3.5 (tasnifu).",
        "zh": "研究生申请：课程硕士 GPA 2.7，论文硕士 GPA 3.5。",
        "ar": "متطلبات الدراسات العليا: معدل ٢.٧ للمقررات و٣.٥ للبحث."
    },
    "fees": {
        "en": "PGDE fees: 2.1M TZS (Res) / $3,055 (Non-Res). Other Masters average 3M to 9M TZS.",
        "sw": "Ada za PGDE: TZS Milioni 2.1. Shahada nyingine za uzamili ni kati ya Milioni 3 hadi 9.",
        "zh": "学费：PGDE 为 210 万先令。其他硕士课程在 300 万至 900 万先令之间。",
        "ar": "رسوم الدبلوم التربوي ٢.١ مليون شلن. تتراوح رسوم الماجستير بين ٣ إلى ٩ ملايين شلن."
    },
    "graduation": {
        "en": "The 56th Graduation (Cluster I) is Friday, 29 May 2026.",
        "sw": "Mahafali ya 56 ni Ijumaa, tarehe 29 Mei 2026.",
        "zh": "第 56 届毕业典礼定于 2026 年 5 月 29 日。",
        "ar": "حفل التخرج السادس والخمسون في ٢٩ مايو ٢٠٢٦."
    }
}

# 4. THE VISIBLE SIDEBAR
with st.sidebar:
    st.title("🛰️ Agatha Settings")
    lang = st.radio("Language", ["English", "Kiswahili", "Chinese", "Arabic"])
    l_key = {"English": "en", "Kiswahili": "sw", "Chinese": "zh", "Arabic": "ar"}[lang]

# 5. THE VISIBLE CHAT
st.title("🛰️ Agatha U-D GPT")
st.markdown(f"<div class='agatha-bubble'>Navigator Active: {lang}</div>", unsafe_allow_html=True)

query = st.chat_input("Ask about UDSM...")
if query:
    st.markdown(f"<div class='user-msg'>You: {query}</div>", unsafe_allow_html=True)
    res = "Data not found. Try 'Postgraduate' or 'Semester 1'."
    for k in VAULT:
        if k in query.lower():
            res = VAULT[k][l_key]
    st.markdown(f"<div class='agatha-bubble'>{res}</div>", unsafe_allow_html=True)