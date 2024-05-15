import pandas as pd

# Create a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'Salary': [50000, 60000, 70000, 80000]
}

df = pd.DataFrame(data)

# Display the DataFrame
print("DataFrame:")
print(df)
print()

# Accessing columns
print("Accessing columns:")
print(df['Name'])
print()

# Accessing rows
print("Accessing rows:")
print(df.iloc[0])  # Access first row by index
print(df.loc[1])   # Access second row by label
print()

# Adding a new column
df['Department'] = ['HR', 'Finance', 'IT', 'Marketing']
print("DataFrame with new column:")
print(df)
print()

# Summary statistics
print("Summary statistics:")
print(df.describe())
