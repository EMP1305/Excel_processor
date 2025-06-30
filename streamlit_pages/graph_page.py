import streamlit
import matplotlib.pyplot as plt
import pandas as pd

session = streamlit.session_state
data_frames = session.get('data_frames',{})

for key, df in data_frames.items():
    fig, ax = plt.subplots()
    x = df.index.values
    for column in df.select_dtypes(include='number').columns:
        ax.plot(x, df[column], label=column)
    ax.set_title(f"Hoja: {key}")
    ax.legend()
    streamlit.pyplot(fig)
    streamlit.divider()
