import pandas as pd

def statistic_data(df: pd.DataFrame) -> pd.DataFrame:
    """Devuelve estadísticas descriptivas solo para columnas numéricas."""
    return df.describe(include='number')