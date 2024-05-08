import pandas as pd
import numpy as np

# Define the size of the table
num_rows = 5
num_cols = 3

# Generate random data
np.random.seed(0)  # For reproducibility
random_data = np.random.randint(0, 100, size=(num_rows, num_cols))

# Creating a DataFrame with random data
df = pd.DataFrame(random_data, columns=['Column1', 'Column2', 'Column3'])

# Printing the DataFrame
print(df)