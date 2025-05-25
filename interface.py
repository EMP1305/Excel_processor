import streamlit
import os
from files_db import data_frame_maker

if 'path' not in streamlit.session_state:
    streamlit.session_state.path = ''
if 'files' not in streamlit.session_state:
    streamlit.session_state.files = list()
if 'selected_file' not in streamlit.session_state:
    streamlit.session_state.selected_file = None
streamlit.session_state.setdefault('data_frames',dict())
streamlit.session_state.setdefault('passed',False)

if not streamlit.session_state.passed:
    path = streamlit.text_input('Database path: ',streamlit.session_state.path)
    if path != streamlit.session_state.path:
        if os.path.exists(path):
            streamlit.session_state.path = path
            streamlit.session_state.files = [file for file in os.listdir(streamlit.session_state.path) if file.endswith(('.xls','.xlsx','.xlm'))]

    if streamlit.session_state.files:
        selected = streamlit.radio('Selecciona un archivo:',streamlit.session_state.files,index=None)
        streamlit.session_state.selected_file = selected

    if streamlit.session_state.selected_file:
        streamlit.write(os.path.join(streamlit.session_state.path,streamlit.session_state.selected_file))
        if streamlit.button('Procesar'):
            streamlit.session_state.data_frames = data_frame_maker(os.path.join(streamlit.session_state.path,streamlit.session_state.selected_file))
            streamlit.session_state.passed = True
            streamlit.rerun()

else:
    for key in streamlit.session_state.data_frames:
        streamlit.dataframe(streamlit.session_state.data_frames [key],hide_index=True)
        streamlit.divider()