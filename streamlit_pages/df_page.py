import streamlit
from data_analysis.files_db import data_frame_properties

session = streamlit.session_state
data_frames = session.get('data_frames', {})

for key, df in data_frames.items():
    streamlit.subheader(f"Hoja: {key}")
    info = data_frame_properties(df)
    # Procesar y mostrar cada línea con encabezado
    for line in info.strip().split('\n'):
        if ':' in line:
            k, v = line.split(':', 1)
            streamlit.markdown(f"**{k.strip()}:** {v.strip()}")
        else:
            streamlit.text(line)
    streamlit.divider()