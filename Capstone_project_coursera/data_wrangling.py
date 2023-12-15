import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # Seaborn for improved aesthetics
import matplotlib.ticker as ticker

pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 500)

# Assuming 'df' is your DataFrame
df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m2_survey_data.csv")

# Filter out missing values in the 'ConvertedComp' column
# filtered_df = df.dropna(subset=['ConvertedComp'])

#
# Plot the distribution curve using Seaborn
# plt.figure(figsize=(10, 6))
# sns.histplot(filtered_df['ConvertedComp'], kde=True, bins=30, color='skyblue')
# plt.title('Distribution of Converted Compensation')
# plt.xlabel('Converted Compensation (USD)')
# plt.ylabel('Density')
# plt.grid(True)

#
#
# # Plot only the KDE curve
# plt.figure(figsize=(10, 6))
# sns.kdeplot(filtered_df['ConvertedComp'], color='red')
# plt.title('Kernel Density Estimate (KDE) of Converted Compensation')
# plt.xlabel('Converted Compensation (USD)')
# plt.ylabel('Density')
# plt.grid(True)
#
# formatter = ticker.ScalarFormatter(useMathText=False)
# formatter.set_scientific(False)
# plt.gca().xaxis.set_major_formatter(formatter)
#
# plt.show()

# p = df['ConvertedComp'].median()
# m = df['ConvertedComp'].mean()
# q = df['ConvertedComp'].quantile(0.50)
# print(df['Gender'].value_counts())
#
# women_df = df[df['Gender'] == 'Woman']
# median_converted_comp = women_df['ConvertedComp'].median()
# print(f"median_converted_comp: {p},meanconverted_comp = {m},q5={q}, median women_df  {median_converted_comp}")
#
# min_age = df['Age'].min()
# max_age = df['Age'].max()
# median_age = df['Age'].median()
# q1_age = df['Age'].quantile(0.25)
# q3_age = df['Age'].quantile(0.75)

# print(f'min_age = {min_age},\n max_age = {max_age},\n median_age = {median_age}, \n q1_age = {q1_age} \n q3_age = {q3_age}')

# Plot the distribution curve using Seaborn
# plt.figure(figsize=(10, 6))
# sns.histplot(df['Age'], kde=True, bins=30, color='skyblue')
# plt.title('Age Distribution')
# plt.xlabel('Age')
# plt.ylabel('Density')
# plt.grid(True)
# plt.show()



Q1 = df['ConvertedComp'].quantile(0.25)
Q3 = df['ConvertedComp'].quantile(0.75)
# IQR = Q3 - Q1
# print('IQR ConvertedComp' , IQR)
print(df.shape)
print('ConvertedComp_shape', df['ConvertedComp'].shape)

Q4 = df['ConvertedComp'].quantile(1)
print('q4',Q4)
print('q3',Q3)
print('q1',Q1)
outliers = df[df['ConvertedComp'] > Q4]
print('количество вилетов', outliers.shape[0])
print(outliers.head())

# Print the results

df_ConvertedComp_no_out = df[df['ConvertedComp']<Q4]
print('df_ConvertedComp_no_out', df_ConvertedComp_no_out.shape)

plt.figure(figsize=(10, 6))
sns.boxplot(y=df['ConvertedComp'])

# Set the plot title and labels
plt.title('Box Plot of Converted Compensation')
plt.xlabel('Converted Compensation (USD)')
plt.show()