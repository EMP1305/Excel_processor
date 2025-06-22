import streamlit
from data_analysis.files_db import data_frame_properties

session = streamlit.session_state
data_frames = session.get('data_frames', {})

for key, df in data_frames.items():
    streamlit.write(data_frame_properties(df))
    streamlit.divider()