import pandas as pd

# Creating a dictionary with table elements
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

# Creating a DataFrame
df = pd.DataFrame(data)

# Printing the DataFrame
print(df)