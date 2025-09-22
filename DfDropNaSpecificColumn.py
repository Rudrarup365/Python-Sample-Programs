import pandas as pd
import numpy as np

# Create a sample DataFrame
df = pd.DataFrame({
    'A': [1, 2, np.nan, 4],
    'B': [5, np.nan, 7, 8],
    'C': [9, 10, 11, np.nan]
})

print("Original DataFrame:")
print(df)

# Drop rows where 'A' or 'B' columns have missing values
df_cleaned = df.dropna(subset=['A', 'B'])

print("\nDataFrame after dropping rows with NaN in 'A' or 'B':")
print(df_cleaned)

# To modify the DataFrame in place without creating a new one:
# df.dropna(subset=['A', 'B'], inplace=True)