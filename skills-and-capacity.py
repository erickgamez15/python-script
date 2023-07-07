import pandas as pd

path = r'dataSource/Skills_y_Capacity V8.xlsm'
hr = (1,2)
df_Conocimiento = pd.read_excel(path, sheet_name ='Conocimiento', header = hr, engine='openpyxl')
df_Herramientas = pd.read_excel(path, sheet_name ='Herramientas', header = hr, engine='openpyxl')

df_Conocimiento= df_Conocimiento.dropna().reset_index(drop=True)

df_list_Conocimiento = []

areas_Conocimiento = df_Conocimiento.columns.get_level_values(0)[2:]
skills_Conocimiento = df_Conocimiento.columns.get_level_values(1)[2:]

for _, row in df_Conocimiento.iterrows():
    id = row['Unnamed: 0_level_0', 'ID']
    nombre = row['Unnamed: 1_level_0', 'Nombre']
    
    for area in areas_Conocimiento:
        area_info = row[area]
        
        for skill in skills_Conocimiento:
            try:
                score = area_info[skill]
                df_list_Conocimiento.append([id, nombre, area, skill, score])
            except KeyError:
                continue

df_csv_Conocimiento = pd.DataFrame(df_list_Conocimiento, columns=['ID', 'Nombre', 'Area', 'Skill', 'Score'])
df_csv_Conocimiento = df_csv_Conocimiento.drop_duplicates(keep='first')
df_csv_Conocimiento.to_csv(r'processedData/conocimientos.csv', encoding='utf-8-sig', index=False)

df_Herramientas = df_Herramientas.dropna().reset_index(drop=True)

df_list_Herramientas = []

areas_Herramientas = df_Herramientas.columns.get_level_values(0)[2:]
skills_Herramientas= df_Herramientas.columns.get_level_values(1)[2:]

for _, row in df_Herramientas.iterrows():
    id = row['Unnamed: 0_level_0', 'ID']
    nombre = row['Unnamed: 1_level_0', 'Nombre']
    
    for area in areas_Herramientas:
        area_info = row[area]
        
        for skill in skills_Herramientas:
            try:
                score = area_info[skill]
                df_list_Herramientas.append([id, nombre, area, skill, score])
            except KeyError:
                continue

df_csv_Herramientas = pd.DataFrame(df_list_Herramientas, columns=['ID', 'Nombre', 'Area', 'Skill', 'Score'])
df_csv_Herramientas = df_csv_Herramientas.drop_duplicates(keep='first')
df_csv_Herramientas.to_csv(r'processedData/herramientas.csv', encoding='utf-8-sig', index=False)
