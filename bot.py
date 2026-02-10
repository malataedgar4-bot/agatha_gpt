import streamlit as st

# 1. ELITE CONFIG
st.set_page_config(page_title="Agatha U-D GPT", page_icon="🛰️", layout="centered")

# 2. CSS KILL-SWITCH (Clean, Professional Dark Mode)
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

# 3. QUADRILINGUAL KNOWLEDGE VAULT (Admin, Hostels, Medical, Study)
VAULT = {
    "vc": {
        "en": "The Vice-Chancellor is Prof. William Anangisye, the chief executive officer of UDSM.",
        "sw": "Makamu wa Kansela ni Prof. William Anangisye, mtendaji mkuu wa UDSM.",
        "zh": "副校长是 William Anangisye 教授，达累斯萨拉姆大学的首席执行官。",
        "ar": "نائب المستشار هو الأستاذ ويليام أنانيسي، الرئيس التنفيذي لجامعة دار السلام."
    },
    "admin": {
        "en": "UDSM Chain of Command: Chancellor (Dr. Kikwete), Vice-Chancellor (Prof. Anangisye), and Deputy Vice-Chancellors.",
        "sw": "Uongozi wa UDSM: Kansela (Dr. Kikwete), Makamu wa Kansela (Prof. Anangisye), na Manaibu wake.",
        "zh": "学校领导层：校监（Kikwete 博士）、副校长（Anangisye 教授）及各副职。",
        "ar": "الهيكل الإداري: المستشار (د. كيكويت)، ونائب المستشار (أ.د. أنانيسي)، ونوابه."
    },
    "hostels": {
        "en": "UDSM offers various student hostels including Hall 1-6, Mabibo, and Dr. J.P. Magufuli hostels.",
        "sw": "UDSM inatoa hosteli mbalimbali ikiwemo Hall 1-6, Mabibo, na hosteli za Dr. J.P. Magufuli.",
        "zh": "大学提供多种宿舍，包括 Hall 1-6、Mabibo 以及 Magufuli 博士宿舍。",
        "ar": "توفر الجامعة سكناً طلابياً متنوعاً يشمل Hall 1-6، مابيبو، وسكن الدكتور ماغوفولي."
    },
    "emergency": {
        "en": "For medical emergencies, visit the UDSM Health Centre near the main gate.",
        "sw": "Kwa dharura ya matibabu, fika Kituo cha Afya cha UDSM karibu na geti kuu.",
        "zh": "如有医疗紧急情况，请前往校门附近的达大健康中心。",
        "ar": "في حالات الطوارئ الطبية، يرجى زيارة المركز الصحي بالجامعة بالقرب من البوابة الرئيسية."
    },
    "library": {
        "en": "The Dr. Wilbert Chagula Library is the primary research facility on the main campus.",
        "sw": "Maktaba ya Dr. Wilbert Chagula ndicho kituo kikuu cha utafiti kampasi kuu.",
        "zh": "Wilbert Chagula 博士图书馆是主校区的主要研究设施。",
        "ar": "مكتبة الدكتور ويلبرت تشاغولا هي مرفق البحث الرئيسي في الحرم الجامعي."
    }
}

# 4. QUADRILINGUAL SIDEBAR
with st.sidebar:
    st.title("🛰️ Agatha Translator")
    lang_choice = st.radio("Select Language / 选择语言 / اختر اللغة", ["English", "Kiswahili", "Chinese", "Arabic"])
    
    # Mapping keys
    lang_map = {"English": "en", "Kiswahili": "sw", "Chinese": "zh", "Arabic": "ar"}
    l_key = lang_map[lang_choice]
    
    voice_on = st.toggle("Voice Assistance")

# 5. INTERFACE
st.title("🛰️ Agatha U-D GPT")
intros = {
    "en": "I am Agatha. How may I assist you with University information?",
    "sw": "Mimi ni Agatha. Nikusaidie nini kuhusu taarifa za Chuo?",
    "zh": "我是 Agatha。我能为您提供哪些关于大学的信息？",
    "ar": "أنا أجاثا. كيف يمكنني مساعدتك في الحصول على معلومات الجامعة؟"
}
st.markdown(f"<div class='agatha-bubble'>{intros[l_key]}</div>", unsafe_allow_html=True)

# 6. SEARCH LOGIC
user_query = st.chat_input("Message Agatha...")

if user_query:
    st.markdown(f"<div class='user-msg'>You: {user_query}</div>", unsafe_allow_html=True)
    q = user_query.lower()
    
    # Default Not Found
    nf = {
        "en": "Information not found. Please try 'VC', 'Admin', or 'Emergency'.",
        "sw": "Taarifa haijapatikana. Jaribu 'VC', 'Admin', au 'Dharura'.",
        "zh": "未找到信息。请尝试搜索 'VC'、'Admin' 或 'Emergency'。",
        "ar": "لم يتم العثور على المعلومات. يرجى تجربة 'VC' أو 'Admin' أو 'Emergency'."
    }
    response = nf[l_key]
    
    for key in VAULT:
        if key in q:
            response = VAULT[key][l_key]
            break
            
    st.markdown(f"<div class='agatha-bubble'>{response}</div>", unsafe_allow_html=True)

    if voice_on:
        st.toast("🔊 Agatha speaking...")

