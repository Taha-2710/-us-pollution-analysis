import pandas as pd  # Import the pandas library for data manipulation and analysis
import matplotlib.pyplot as plt  # Import matplotlib for plotting graphs
import seaborn as sn  # Import seaborn for advanced statistical data visualization
sn.set()  # Set seaborn’s default style for plots

df = pd.read_csv('/pollution_us_2000_2016.csv')  # Read the CSV file containing pollution data into a DataFrame called df
df.head()  # Display the first 5 rows of the DataFrame to inspect data structure

del df['Unnamed: 0']  # Delete the unwanted 'Unnamed: 0' column from the DataFrame
df.info()  # Display concise summary of the DataFrame, including column names, non-null counts, and datatypes
df.isnull().sum()  # Count and display the number of missing values in each column
df.duplicated().sum()  # Count and display the number of duplicate rows in the DataFrame
df.describe(include='all')  # Generate descriptive statistics for all columns including categorical features
for col in df.columns:  # Loop through every column in the DataFrame
    print(f"{col}: {df[col].nunique()} unique values")  # Print the column name and the number of unique values in that column

df1 = df.dropna()  # Create a new DataFrame df1 by dropping all rows with any missing values from df
df1.isnull().sum()  # Count and display the number of missing values in each column of the cleaned DataFrame
df1.describe(include='all')  # Generate descriptive statistics for all columns in the cleaned DataFrame