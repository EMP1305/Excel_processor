# Excel Processor

Una aplicación web interactiva para el análisis de bases de datos en archivos Excel, desarrollada con Streamlit. Permite explorar, visualizar, obtener estadísticas y realizar predicciones sobre los datos de tus hojas de cálculo de manera sencilla y rápida.

## Características principales

- 📂 **Explora cualquier carpeta** de tu sistema y detecta automáticamente todos los archivos Excel compatibles (`.xls`, `.xlsx`, `.xlm`).
- 📰 **Visualiza los datos** de cada hoja de tus archivos Excel como DataFrames de pandas.
- 💻 **Consulta propiedades técnicas** de los DataFrames (útil para programadores y análisis avanzado).
- 💾 **Obtén estadísticas descriptivas** de tus datos (media, desviación estándar, percentiles, etc.).
- 🧮 **Predice valores futuros** usando un modelo de regresión lineal OLS (Ordinary Least Squares).
- 📉 **Genera gráficos** automáticamente para el análisis visual de tus datos.

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu_usuario/Excel_processor.git
   cd Excel_processor
   ```
2. Instala las dependencias necesarias:
   ```bash
   pip install -r requirements.txt
   ```
   Si no existe `requirements.txt`, instala manualmente:
   ```bash
   pip install streamlit pandas numpy matplotlib statsmodels openpyxl
   ```

## Uso

1. Ejecuta la aplicación con:
   ```bash
   streamlit run main.py
   ```
2. En la interfaz web:
   - Ingresa la ruta de la carpeta donde están tus archivos Excel.
   - Selecciona el archivo y la hoja que deseas analizar.
   - Navega entre las diferentes páginas para ver los datos, estadísticas, predicciones y gráficos.

## Estructura del proyecto

```
Excel_processor/
├── main.py                  # Punto de entrada de la app Streamlit
├── data_analysis/           # Lógica de análisis de datos
│   ├── files_db.py
│   ├── predic_data.py
│   └── statistic_data.py
├── streamlit_pages/         # Páginas individuales de la app
│   ├── interface.py
│   ├── df_show.py
│   ├── df_page.py
│   ├── stats_page.py
│   ├── pred_page.py
│   └── graph_page.py
├── example/                 # Ejemplo de archivo Excel
│   └── Libro1.xlsx
└── README.md
```

## Dependencias principales
- [Streamlit](https://streamlit.io/)
- [pandas](https://pandas.pydata.org/)
- [numpy](https://numpy.org/)
- [matplotlib](https://matplotlib.org/)
- [statsmodels](https://www.statsmodels.org/)
- [openpyxl](https://openpyxl.readthedocs.io/)