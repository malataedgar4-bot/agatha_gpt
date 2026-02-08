import streamlit as st
import requests
import json
import streamlit as st
import folium
from streamlit_folium import st_folium

st.title("Agatha U-D GPT 🛰️")
st.subheader("UDSM Campus Navigator")

# Language Toggle
lang = st.sidebar.radio("Chagua Lugha / Select Language", ["Kiswahili", "English"])

# Voice Toggle
voice = st.sidebar.checkbox("Voice Assistance (Agatha)")

# UDSM Map Logic
m = folium.Map(location=[-6.7797, 39.2040], zoom_start=15)
folium.Marker([-6.7797, 39.2040], popup="UDSM Main Campus", tooltip="Hapa ni Mlimani").add_to(m)

st_folium(m, width=700)

if lang == "Kiswahili":
    st.write("Karibu! Mimi ni Agatha. Nitakusaidia kufika unapoenda.")
else:
    st.write("Welcome! I am Agatha. I will help you find your destination.")

# Load API keys from Streamlit secrets
API_KEY = st.secrets['https://api.render.com/deploy/srv-d64ani4r85hc73bogtm0?key=GBsmPegI4Gk]

# Multilingual support
# Expanded Language Support for Agatha
SUPPORTED_LANGUAGES = {
    'en': 'English', 
    'sw': 'Kiswahili', 
    'zh': 'Chinese (中文)',
    'ar': 'Arabic (العربية)',
    'pt': 'Portuguese',
    'hi': 'Hindi (हिन्दी)',
    'ja': 'Japanese (日本語)',
    'fr': 'French', 
    'es': 'Spanish'
}
def get_response_from_api(user_input, language):
    headers = {'Authorization': f'Bearer {API_KEY}', 'Content-Type': 'application/json'}
    payload = json.dumps({'input': user_input, 'language': language})
    response = requests.post('https://api.example.com/process', headers=headers, data=payload)
    if response.status_code == 200:
        return response.json()
    else:
        st.error(f'Error fetching data: {response.status_code} {response.text}')
        return None

# Enhanced RAG pipeline (Retrieval-Augmented Generation)
def rag_pipeline(user_query):
    # Add logic for retrieving relevant information and generating responses
    pass  # Placeholder for the RAG implementation

# Main Streamlit app
def main():
    st.title('Multilingual Bot')
    language = st.selectbox('Choose your language:', list(SUPPORTED_LANGUAGES.keys()))
    user_input = st.text_input('Enter your query:')
    if st.button('Submit') and user_input:
        response = get_response_from_api(user_input, language)
        if response:
            st.write(response['output'])

if __name__ == '__main__':
    main()import pandas as pd
import json

# Handle the uploaded files
if uploaded_files:
    for uploaded_file in uploaded_files:
        if uploaded_file.name.endswith('.json') or uploaded_file.name.endswith('.geojson'):
            # Load Map Data into memory
            map_data = json.load(uploaded_file)
            st.success(f"Map '{uploaded_file.name}' loaded into Agatha's memory.")
            # Visualize the map
            render_map(map_data)
            
        elif uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
            st.dataframe(df.head()) # Preview the data
            st.success(f"Data from {uploaded_file.name} indexed.")import pandas as pd
import json
import os

def rag_pipeline(user_query):
    # Agatha looks for the files you uploaded to GitHub
    # Let's assume you uploaded 'map_data.geojson'
    file_path = 'map_data.geojson' 
    
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            data = json.load(f)
            # Short, precise logic:
            return f"Agatha Memory: Found map data with {len(data['features'])} locations. How can I help with these?"
    else:
        return "Agatha: I can't see the files yet. Ensure they are in the root folder of your GitHub repo."