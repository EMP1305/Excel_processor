from streamlit_pages.df_show import data_frames
import streamlit
from data_analysis.files_db import data_frame_properties

for key in data_frames:
    streamlit.write(data_frame_properties(data_frames[key]))
    streamlit.divider()