from io import BytesIO
import pandas as pd

def mydata(dats):
    df = pd.read_csv(BytesIO(dats))
    df = df.head()
    mydata.headers = list(df.columns)
    mydata.data = df.values.tolist()
