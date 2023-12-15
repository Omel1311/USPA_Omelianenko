import pandas as pd


pd.set_option('display.max_columns', 100)
pd.set_option('display.width', 1000)
pd.set_option('display.max_rows', 500)

dataset_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/LargeData/m1_survey_data.csv"

df = pd.read_csv(dataset_url)
#
# print(df.shape)
# print(df.dtypes)
# print('dddd', df.duplicated().sum())
#
# mean_age = df['Age'].mean()
# print(mean_age)
# unique_countries = df["Country"].unique()
# print(len(unique_countries))
# df.drop_duplicates
# print(df.shape)
# print('rrr', df['Respondent'].duplicated().sum())
#
# missing_workloc_count = df['WorkLoc'].isnull().sum()
# print(missing_workloc_count)
#
# for column_name in df.columns:
#     missing_count = df[column_name].isnull().sum()
#     print(f"Column: {column_name} -- {missing_count}")
#
#
# workloc_value_counts = df['WorkLoc'].value_counts()
#
# # Display the value counts for the 'WorkLoc' column
# print("Value counts for the 'WorkLoc' column:")
# print(workloc_value_counts)
#
# workloc_mode = df['WorkLoc'].mode()
# print(workloc_mode)
#
# df2 = df[["CompFreq", "CompTotal"]]
# print(df2["CompFreq"].value_counts())
# # print(df2.head(30))
#
#
#
compfreq_mapping = {'Yearly': 1, 'Monthly': 12, 'Weekly': 52}
df['NormalizedAnnualCompensation'] = df['CompTotal'] * df['CompFreq'].map(compfreq_mapping)

# print(df[['CompFreq', 'CompTotal', 'NormalizedAnnualCompensation']].head(30))
duplicate_rows = df[df.duplicated()]
print(duplicate_rows)
nun3 = df['CompFreq'].value_counts()
print(nun3)

missing_n = df.isnull().sum().sum()
df.drop_duplicates(inplace=True)

print(df.shape)

nun2 = df['CompFreq'].value_counts()
print(nun2)
nun = df['CompFreq'].nunique()
print(nun)

compfreq_mapping = {'Yearly': 1, 'Monthly': 12, 'Weekly': 52}
df['NormalizedAnnualCompensation'] = df['CompTotal'] * df['CompFreq'].map(compfreq_mapping)
f = df['NormalizedAnnualCompensation'].median()
print(f)

