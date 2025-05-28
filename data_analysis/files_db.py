import pandas
import re
from io import StringIO

def data_frame_maker (path:str)->list:
    test = pandas.read_excel(path,sheet_name=0)
    for colum in test.values:
        for elem in colum:
            if re.search(r'\d+\,\d+',elem):
                return pandas.read_excel(path,sheet_name=None,decimal=',')
    return pandas.read_excel(path,sheet_name=None)

def data_frame_properties (df:pandas.DataFrame)->str:
    buffer = StringIO()
    df.info(buf=buffer)
    return buffer.getvalue()