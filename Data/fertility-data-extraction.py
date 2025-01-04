import pandas as pd

file_path = 'Data/WPP2024_FERT_F02_FERTILITY_RATES_BY_5-YEAR_AGE_GROUPS_OF_MOTHER.xlsx'
country_code = 364  

df1 = pd.read_excel(file_path, sheet_name='Estimates', header=16)
df2 = pd.read_excel(file_path, sheet_name='Medium variant', header=16)
df = pd.concat([df1, df2], ignore_index=True)
df['Year'] = df['Year'].astype('Int64') 

filtered_data = df[
    (df['Location code'] == country_code) & 
    (df['Year'].between(2010, 2060))  
]
selected_data = filtered_data[['Year']].reset_index(drop=True)
selected_data['0-14'] = filtered_data['10-14'].reset_index(drop=True)
selected_data['15-49'] = (filtered_data['15-19']+filtered_data['20-24']+filtered_data['25-29']+filtered_data['30-34']+filtered_data['35-39']+filtered_data['40-44']+filtered_data['45-49']).reset_index(drop=True)
selected_data['50-64'] = filtered_data['50-54'].reset_index(drop=True)
selected_data['65-79'] = 0
selected_data['80+'] = 0

print(selected_data.reset_index(drop=True))
selected_data.to_csv('Data/fertility.csv', index=False)