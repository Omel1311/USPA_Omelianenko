import pandas as pd

# Assuming df1 and df2 are your DataFrames
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'j': [5, 6], 'B': [7, 8]})

# Using pd.concat instead of df1.append(df2)
df_combined = pd.concat([df1, df2], ignore_index=True)

# Display the combined DataFrame
print(df_combined)
