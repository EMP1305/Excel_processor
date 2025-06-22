import streamlit
from data_analysis.files_db import data_frame_maker

session = streamlit.session_state

data_frames = {}
if hasattr(session, 'uploaded_file') and session.uploaded_file:
    # Solo cargar si no está en session_state o si el archivo cambió
    if 'data_frames' not in session or session.get('last_uploaded_name') != session.uploaded_file.name:
        session.data_frames = data_frame_maker(session.uploaded_file)
        session.last_uploaded_name = session.uploaded_file.name
    data_frames = session.data_frames

for key, df in data_frames.items():
    streamlit.dataframe(df, hide_index=True)
    streamlit.divider()