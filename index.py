import pandas as pd

# 1. CARREGA O ARQUIVO CSV  
df = pd.read_csv('BaseVarejo.csv', sep=';', encoding='utf-8')

# 2. REMOVE COLUNAS VAZIAS OU DO TIPO UNNAMED
df = df.loc[:, ~df.columns.str.contains('^Unnamed')].dropna(how='all', axis=1)

# 3. CONVERTE A COLUNA DE DATA PARA O FORMATO DATETIME
df['DATA'] = pd.to_datetime(df['DATA'], format='%d/%m/%Y')
print(df.head())
#----------------------------------------------------------
