from df_show import data_frames
import streamlit
from data_analysis.predic_data import predict

n = streamlit.text_input('Cantidad de datos a predecir: ',str())
for key in data_frames:
    streamlit.dataframe(predict(data_frames[key],int(n) if n.isnumeric() else 10),hide_index=True)
    streamlit.divider()