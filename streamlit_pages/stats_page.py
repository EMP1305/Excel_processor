import streamlit
from data_analysis.statistic_data import statistic_data

session = streamlit.session_state
data_frames = session.get('data_frames',{})

for key, df in data_frames.items():
    streamlit.subheader(f"Hoja: {key}")
    streamlit.dataframe(statistic_data(df))
    streamlit.divider()
