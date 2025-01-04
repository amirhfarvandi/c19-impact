import pandas as pd

file_path = 'Data/WPP2024_GEN_F01_DEMOGRAPHIC_INDICATORS_COMPACT.xlsx'
country_code = 364  

df1 = pd.read_excel(file_path, sheet_name='Estimates', header=16)
df2 = pd.read_excel(file_path, sheet_name='Medium variant', header=16)
df = pd.concat([df1, df2], ignore_index=True)
df['Year'] = df['Year'].astype('Int64') 

filtered_data = df[
    (df['Location code'] == country_code) & 
    (df['Year'].between(2010, 2060))  
]
selected_data = filtered_data[['Year', 'Net Migration Rate (per 1,000 population)']].reset_index(drop=True)

print(selected_data)
selected_data.to_csv('Data/net-migration.csv', index=False)