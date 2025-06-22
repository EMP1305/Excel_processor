import streamlit
import os

# Inicialización de session_state
session = streamlit.session_state
if 'uploaded_file' not in session:
    session.uploaded_file = None

uploaded_file = streamlit.file_uploader(
    'Sube un archivo Excel',
    type=['xls', 'xlsx', 'xlm'],
    key='excel_uploader'
)

if uploaded_file:
    session.uploaded_file = uploaded_file
    streamlit.success(f'Archivo "{uploaded_file.name}" subido correctamente.')
else:
    streamlit.info('Por favor, sube un archivo Excel para continuar.')