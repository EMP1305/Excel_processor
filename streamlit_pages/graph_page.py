import matplotlib.pyplot
from df_show import data_frames
import streamlit
import pandas

fig,ax = matplotlib.pyplot.subplots()
for key in data_frames:
    data_frame: pandas.DataFrame = data_frames [key]
    x = data_frame.index.values
    for column in data_frame.columns:
        if pandas.api.types.is_numeric_dtype(data_frame [column]):
            ax.plot(x,data_frame [column],label=column)
    ax.legend()
    streamlit.pyplot(fig)
    streamlit.divider()