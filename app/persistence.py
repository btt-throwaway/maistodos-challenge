def save_to_parquet(df, filename):
    df.to_parquet(f"outputs/{filename}.parquet")
