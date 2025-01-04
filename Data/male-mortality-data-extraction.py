import pandas as pd


file_path = 'Data/WPP2024_MORT_F03_2_DEATHS_PERCENTAGE_SELECT_AGE_GROUPS_MALE.xlsx'
country_code = 364  


df1 = pd.read_excel(file_path, sheet_name='Estimates', header=16)
df2 = pd.read_excel(file_path, sheet_name='Medium variant', header=16)
df = pd.concat([df1, df2], ignore_index=True)

df['Year'] = df['Year'].astype('Int64') 


filtered_data = df[
    (df['Location code'] == country_code) & 
    (df['Year'].between(2010, 2060))  
]

selected_data = filtered_data[['Year', '0-14', '15-49']].reset_index(drop=True)
selected_data['50-64'] = (filtered_data['50+'] - filtered_data['65+']).reset_index(drop=True)
selected_data['65-79'] = (filtered_data['65+'] - filtered_data['80+']).reset_index(drop=True)
selected_data['80+'] = filtered_data['80+'].reset_index(drop=True)
print(selected_data)
selected_data.to_csv('Data/male-mortality.csv', index=False)