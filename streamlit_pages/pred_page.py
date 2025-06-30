import streamlit
import matplotlib.pyplot as plt
from data_analysis.predic_data import predict
import pandas as pd

session = streamlit.session_state
data_frames = session.get('data_frames', {})

n = streamlit.text_input('Cantidad de datos a predecir:', '')
num_pred = int(n) if n.isnumeric() else 10

for key, df in data_frames.items():
    streamlit.subheader(f"Hoja: {key}")
    pred_df = predict(df, num_pred)
    streamlit.dataframe(pred_df, hide_index=True)

    # Gráfico 1: comparación último 40% real vs predicción OLS sobre ese tramo
    if len(df) > 1:
        last_40 = max(2, int(len(df) * 0.4))  # al menos 2 puntos
        real = df.iloc[-last_40:]
        x_real = range(1,last_40+1)
        fig1, ax1 = plt.subplots()
        pred = predict(df.iloc[:last_40],last_40)
        for column in pred.select_dtypes(include='number').columns:
            ax1.plot(x_real, real[column], label=f"Real {column}")
            ax1.plot(x_real, pred[column], '--', label=f"OLS {column}")
        ax1.set_title("Comparación último 40% real vs OLS")
        ax1.legend()
        streamlit.pyplot(fig1)

    # Gráfico 2: todos los datos reales + predicción
    if len(df) > 0 and not pred_df.empty:
        fig2, ax2 = plt.subplots()
        for column in df.select_dtypes(include='number').columns:
            ax2.plot(range(1, len(df) + 1), df[column].values, label=f"Real {column}")
            x_pred = range(len(df) + 1, len(df) + 1 + len(pred_df))
            ax2.plot(x_pred, pred_df[column].values, '--', label=f"Predicción {column}")
        ax2.set_title("Datos reales + predicción futura")
        ax2.legend()
        streamlit.pyplot(fig2)

    streamlit.divider()
