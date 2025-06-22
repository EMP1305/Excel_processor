import streamlit
from streamlit_pages.df_show import data_frames
from data_analysis.statistic_data import statistic_data

for key, df in data_frames.items():
    streamlit.write(key)
    streamlit.dataframe(statistic_data(df))
    streamlit.divider()