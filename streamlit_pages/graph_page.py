import streamlit
import matplotlib.pyplot as plt
import pandas as pd
from streamlit_pages.df_show import data_frames

for key, df in data_frames.items():
    fig, ax = plt.subplots()
    x = df.index.values
    for column in df.select_dtypes(include='number').columns:
        ax.plot(x, df[column], label=column)
    ax.set_title(key)
    ax.legend()
    streamlit.pyplot(fig)
    streamlit.divider()