import pandas as pd
import numpy as np

def categorize_by_age(df, evaluation_column):
    bins = [0, 18, 29, 37, np.inf]
    names = ["de_0_ate_18", "ate_29", "ate_37", "acima_37"]
    df["hma_cat"] = pd.cut(df[evaluation_column], bins, labels=names)

    return df

def categorize_by_region(df, evaluation_column):
    bins = [np.NINF, -119, np.inf]
    names = ["norte", "sul"]
    df["c_ns"] = pd.cut(df[evaluation_column], bins, labels=names)

    return df

def summary(df):
    labels = {"population": "s_population", "median_house_value": "m_median_house_value"}
    df_summary = df.groupby(["age", "california_region"]).agg({"population": "sum", "median_house_value": "mean"}).rename(columns=labels)

    return df_summary
