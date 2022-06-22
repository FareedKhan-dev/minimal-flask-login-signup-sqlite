import pandas as pd
from io import BytesIO

def show_data(dats):
    df = pd.read_csv(BytesIO(dats))
    show_data.df = df
    headers = list(df.columns)
    data = df.head().values.tolist()
    return (headers, data)