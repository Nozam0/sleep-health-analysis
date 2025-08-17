import pandas as pd

def load_raw_data(filepath: str) -> pd.DataFrame:
    return pd.read_csv(filepath)
    
def load_and_clean(filepath):
    df = pd.read_csv(filepath)
    df.columns = [col.lower().replace(" ", "_") for col in df.columns]
    df = fill_values(df)
    df[['systolic','diastolic']] = df['blood_pressure'].str.split('/', expand=True)
    df['systolic'] = pd.to_numeric(df['systolic'], errors='coerce')
    df['diastolic'] = pd.to_numeric(df['diastolic'], errors='coerce')
    obj_cols = df.select_dtypes(include='object').columns
    df[obj_cols] = df[obj_cols].astype('string')
    return df

def fill_values(dataframe) -> pd.DataFrame:
    for column in dataframe.columns:
        if column == "sleep_disorder":
            dataframe[column] = dataframe[column].fillna('NO')
    return dataframe
    
def look_dtype(df, value: str):
    d_list = []
    for i in df.columns:
        if df[i].dtype == str(value):
            d_list.append(i)
    return df[d_list]