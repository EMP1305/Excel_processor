import matplotlib.pyplot
from streamlit_pages.df_show import data_frames
import streamlit
import pandas

for key in data_frames:
    fig,ax = matplotlib.pyplot.subplots()
    data_frame: pandas.DataFrame = data_frames [key]
    x = data_frame.index.values
    for column in data_frame.columns:
        if pandas.api.types.is_numeric_dtype(data_frame [column]):
            ax.plot(x,data_frame [column],label=column)
    ax.legend()
    streamlit.pyplot(fig)
    streamlit.divider()