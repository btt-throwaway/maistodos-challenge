from ingestion import import_dataset
from analysis import categorize_by_age, categorize_by_region, summary
from persistence import save_to_parquet

# Importing dataset into DataFrame

df = import_dataset("dataset/california_housing_train.csv")


# 1. Column with highest standard deviation

df_std = df.std()

name = df_std[df_std == max(df_std)].index[0]
value = df_std[df_std == max(df_std)].values[0]

print (f"Column with highest standard deviation: {name} - stddev={value}")

# 2. Maximum and minimum values

maximum = max(df.max())
minimum = min (df.min())

print(f"Max value of dataset: {maximum}")
print(f"Min value of dataset: {minimum}")

# 3. Categorize by age
df_with_ages = categorize_by_age(df, "housing_median_age")

# 4. Categorize by 
df_with_ages_and_regions = categorize_by_region(df, "longitude")

df_final = df_with_ages_and_regions

df_final.rename(columns={"hma_cat": "age", "c_ns": "california_region"}, inplace=True)

# write parquet file with df_final

save_to_parquet(df_final, "results")

#Summary

df_summary = summary(df_final)

# Write parquet file with aggregate dataframe

save_to_parquet(df_summary, "summary")