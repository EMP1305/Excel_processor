import numpy as np
import pandas as pd
import statsmodels.api as sm
from pandas.api.types import is_numeric_dtype

def predict(df: pd.DataFrame, n: int = 10) -> pd.DataFrame:
    """
    Predice los siguientes n valores para cada columna numérica usando regresión lineal OLS.
    """
    df = df.dropna(how='any')
    X = sm.add_constant(np.arange(1, len(df) + 1).reshape(-1, 1))
    result = {}
    for column in df.select_dtypes(include='number').columns:
        model = sm.OLS(df[column], X).fit()
        new_X = sm.add_constant(np.arange(len(df) + 1, len(df) + n + 1).reshape(-1, 1))
        result[column] = model.predict(new_X)
    return pd.DataFrame(result)
