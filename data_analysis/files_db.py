import pandas as pd
import re
from io import StringIO
from typing import Dict, Union

def data_frame_maker(source: Union[str, StringIO]) -> Dict[str, pd.DataFrame]:
    """
    Lee un archivo Excel (ruta o buffer) y retorna un dict de DataFrames por hoja.
    Detecta automáticamente el separador decimal.
    """
    test = pd.read_excel(source, sheet_name=0)
    for row in test.values:
        for elem in row:
            if isinstance(elem, str) and re.search(r'\d+,\d+', elem):
                return pd.read_excel(source, sheet_name=None, decimal=',')
    return pd.read_excel(source, sheet_name=None)

def data_frame_properties(df: pd.DataFrame) -> str:
    """
    Devuelve información resumida del DataFrame como string.
    """
    buffer = StringIO()
    df.info(buf=buffer)
    return buffer.getvalue()