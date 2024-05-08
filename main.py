import pandas as pd
import numpy as np

# Generate random data
np.random.seed(0)  # For reproducibility
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': np.random.randint(20, 40, size=3),
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# Sort DataFrame by 'City' column
sorted_df = df.sort_values(by='City')

# Print sorted DataFrame
print(sorted_df)

print('test_conf')
