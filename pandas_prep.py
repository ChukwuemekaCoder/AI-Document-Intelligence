#Bank Loan Data Cleaning

import kagglehub
import pandas as pd

# Download latest version
path = kagglehub.dataset_download("arezalo/bank-personal-loan")

print("Path to dataset files:", path)

#Upload the CSV file and read it into a DataFrame
from google.colab import files
uploaded = files.upload()

df = pd.read_csv('archive.zip')

# Inspect the first few rows of the DataFrame
print("First five rows of the dataset:")
print(df.head())

# Get a summary of the DataFrame
print("\nDataFrame summary:")
print(df.info())

#Find null values
print("\nNull values in each column:")
print(df.isnull())
print(df.notnull())

#Drop missing values
print(df.dropna())

# Identify duplicates
duplicates = df.duplicated()

# Remove duplicates
df_no_duplicates = df.drop_duplicates()
print("DataFrame after removing duplicates:\n", df_no_duplicates)


