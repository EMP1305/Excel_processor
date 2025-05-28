import streamlit
import os

if 'path' not in streamlit.session_state:
    streamlit.session_state.path = ''
if 'files' not in streamlit.session_state:
    streamlit.session_state.files = list()
if 'selected_file' not in streamlit.session_state:
    streamlit.session_state.selected_file = None

path = streamlit.text_input('Database path: ',streamlit.session_state.path)
if path != streamlit.session_state.path:
    if os.path.exists(path):
        streamlit.session_state.path = path
        streamlit.session_state.files = [file for file in os.listdir(streamlit.session_state.path) if file.endswith(('.xls','.xlsx','.xlm'))]

if streamlit.session_state.files:
    selected = streamlit.radio('Selecciona un archivo:',streamlit.session_state.files,index=None,key='radio_option')
    streamlit.session_state.selected_file = selected