from df_show import data_frames
import streamlit
from data_analysis.statistic_data import statistic_data

for key in data_frames:
    streamlit.write(key)
    streamlit.dataframe(statistic_data(data_frames [key]))
    streamlit.divider()