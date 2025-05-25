import pandas

def data_frame_maker (path:str)->list:
    return pandas.read_excel(path,sheet_name=None)