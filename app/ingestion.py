import pandas as pd

def import_dataset(path):
    df = pd.read_csv(path)

    return df
