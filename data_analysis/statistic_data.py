import pandas

def statistic_data (df:pandas.DataFrame):
    return df.describe(include=['number'])