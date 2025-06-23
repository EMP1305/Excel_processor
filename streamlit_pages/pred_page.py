import streamlit
import matplotlib.pyplot as plt
from data_analysis.predic_data import predict
import numpy as np
import statsmodels.api as sm

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
        x_real = np.arange(len(df) - last_40 + 1, len(df) + 1)
        fig1, ax1 = plt.subplots()
        for col in real.select_dtypes(include='number').columns:
            # Ajustar modelo OLS sobre el tramo real
            y = real[col].values
            X = sm.add_constant(np.arange(1, len(y) + 1).reshape(-1, 1))
            model = sm.OLS(y, X).fit()
            y_pred = model.predict(X)
            ax1.plot(x_real, y, label=f"Real {col}")
            ax1.plot(x_real, y_pred, '--', label=f"OLS {col}")
        ax1.set_title("Comparación último 40% real vs OLS")
        ax1.legend()
        streamlit.pyplot(fig1)

    # Gráfico 2: todos los datos reales + predicción
    if len(df) > 0 and not pred_df.empty:
        fig2, ax2 = plt.subplots()
        for col in df.select_dtypes(include='number').columns:
            ax2.plot(range(1, len(df) + 1), df[col].values, label=f"Real {col}")
            if col + '_pred' in pred_df:
                x_pred = range(len(df) + 1, len(df) + 1 + len(pred_df))
                ax2.plot(x_pred, pred_df[col + '_pred'].values, '--', label=f"Predicción {col}")
        ax2.set_title("Datos reales + predicción futura")
        ax2.legend()
        streamlit.pyplot(fig2)

    streamlit.divider()