import pandas as pd
import numpy as np

df = pd.read_csv('Health Dataset.csv')

print("original dataset info:")
print(f"shape: {df.shape}")
print(f"missing values:\n{df.isnull().sum()}\n")


# simplify column names

newColumnNames = {
    'Country': 'Country',
    'State': 'State',
    'Year': 'Year',
    'Gender': 'Gender',
    'Type Of Disease': 'DiseaseType',
    'Cases (UOM:Number), Scaling Factor:1': 'Cases',
    'Deaths (UOM:Number), Scaling Factor:1': 'Deaths'
}

df.rename(columns=newColumnNames, inplace=True)
print("column names changed:")
print(df.columns.tolist())


# fill missing values in gender

df = df.dropna(subset=['Gender'])
print(f"\nafter removing rows with missing gender: {df.shape}")



# fill missing values in cases

if df['Cases'].isnull().sum() > 0:
    cases_mean = df['Cases'].mean()
    df['Cases'] = df['Cases'].fillna(cases_mean)
    print(f"filled missing values with mean: {cases_mean:.2f}")

# fill missing values in deaths

if df['Deaths'].isnull().sum() > 0:
    deaths_mean = df['Deaths'].mean()
    df['Deaths'] = df['Deaths'].fillna(deaths_mean)
    print(f"filled missing values with mean: {deaths_mean:.2f}")


# verify data

print(f"\ncleaned dataset info:")
print(f"shape: {df.shape}")
print(f"missing values:\n{df.isnull().sum()}\n")
print("first few rows of cleaned data:")
print(df.head(10))

# save the cleaned dataset

output_file = 'Health Dataset Cleaned.csv'
df.to_csv(output_file, index=False)
print(f"\ncleaned dataset saved to: {output_file}")
