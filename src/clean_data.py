import pandas as pd

def load_and_clean(path):
    df = pd.read_csv(path)
    df.columns = [col.lower().replace(" ", "_") for col in df.columns]
    df.dropna(inplace=True)
    return df