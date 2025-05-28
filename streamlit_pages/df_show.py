import os
from data_analysis.files_db import data_frame_maker
import streamlit

data_frames = data_frame_maker(os.path.join(streamlit.session_state.path,streamlit.session_state.selected_file))
for key in data_frames:
    streamlit.dataframe(data_frames [key],hide_index=True)
    streamlit.divider()