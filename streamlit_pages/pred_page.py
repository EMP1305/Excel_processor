import streamlit
from streamlit_pages.df_show import data_frames
from data_analysis.predic_data import predict

n = streamlit.text_input('Cantidad de datos a predecir:', '')
num_pred = int(n) if n.isnumeric() else 10

for key, df in data_frames.items():
    streamlit.dataframe(predict(df, num_pred), hide_index=True)
    streamlit.divider()