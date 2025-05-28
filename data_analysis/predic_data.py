import numpy as np
import pandas as pd
import statsmodels.api as sm
from pandas.api.types import is_numeric_dtype

def predict(df: pd.DataFrame, n: int = 10) -> pd.DataFrame:
    df = df.dropna(how='any')  # Elimina filas completamente vacías
    X = sm.add_constant(np.arange(1, len(df)+1).reshape(-1, 1))
    df_f = pd.DataFrame()

    for column in df.columns:
        if is_numeric_dtype(df[column]):
            model = sm.OLS(df[column], X).fit()
            new_X = np.arange(len(df)+1, len(df)+1+n).reshape(-1, 1)
            new_X = sm.add_constant(new_X)
            pred = model.predict(new_X)
            df_f[column + '_pred'] = pred

    return df_f
