import pandas as pd

# 1. CARREGA O ARQUIVO CSV  
df = pd.read_csv('BaseVarejo.csv', sep=';', encoding='utf-8')

# 2. REMOVE COLUNAS VAZIAS OU DO TIPO UNNAMED
df = df.loc[:, ~df.columns.str.contains('^Unnamed')].dropna(how='all', axis=1)

# 3. CONVERTE A COLUNA DE DATA PARA O FORMATO DATETIME
df['DATA'] = pd.to_datetime(df['DATA'], format='%d/%m/%Y')
print(df.head())
#----------------------------------------------------------
#-------- UTILIZANDO FUNÇÕES CONDICIONAIS -----------------
import re

def limpar_texto(valor):#PADRONIZAR E LIMPAR VALORES DE TEXTO COM SUPORTE A CONDICIONAIS
    
    if pd.isna(valor):
        return None
    else:
        texto = str(valor)
        if texto == "":
            return None
        else:
            #PARA REMOVER CARACTERES ESPECIAIS 
            texto_limpo = re.sub(r'[^a-zA-Z0-9\sà-úÀ-Ú]', '', texto)         
            if texto_limpo == "":
                return None
            else:
                #REMOVE MUTIPLOS ESPAÇOS INTEIROS
                texto_limpo = re.sub(r'\s+', ' ', texto_limpo).strip()                
                if texto_limpo == "":
                    return None
                else:
                    return texto_limpo.upper()
#----------------
def limpar_inteiro(valor):#EXTRAI E CONVERTE VALORES PARA INTEIRO COM CONDICIONAIS
    
    if pd.isna(valor):
        return None
    else:
        texto = str(valor)
        if texto == "":
            return None
        else:
            # Busca por sequência numérica
            match = re.search(r'(\d+)', texto)
            if match:
                numero_str = match.group(1)
                return int(numero_str)
            else:
                return None
#=================
def limpar_decimal(valor):#NORMAIZA E CONVERTE FORMATOS MONETÁRIOS
    
    if pd.isna(valor):
        return None
    else:
        texto = str(valor)
        if texto == "":
            return None
        else:
            #FILTRA APENAS DIGITOS, VÍRGULA E SINA DE MENOS
            texto_limpo = re.sub(r'[^\d,-]', '', texto)           
            if texto_limpo == "" or texto_limpo == "-":
                return None
            else:
                if ',' in texto_limpo:
                    texto_limpo = texto_limpo.replace(',', '.')
                else:
                    pass
                
                try:
                    return float(texto_limpo)
                except ValueError:
                    return None

#CARREGAMENTO E ESTRUTURAÇÃO DA BASE DE DADOS
#CARREGA O ARQUIVO CSV
df = pd.read_csv('BaseVarejo.csv', sep=';', encoding='utf-8')
df = df.loc[:, ~df.columns.str.contains('^Unnamed')].dropna(how='all', axis=1)

#APLICAÇÃO DAS FUNÇÕES DE LIMPEZA E PADRONIZAÇÃO
df['PR_NOME'] = df['PR_NOME'].apply(limpar_texto)
df['PR_CAT'] = df['PR_CAT'].apply(limpar_texto)
df['CO_ID'] = df['CO_ID'].apply(limpar_inteiro)
df['CL_ID'] = df['CL_ID'].apply(limpar_inteiro)

#----------ESTATÍSTICA DESCRITIVA--------------
# AGRUPAENTO POR CLIENTE UNICO
df_clientes = df.groupby('CL_ID')['CL_FHL'].first()

#QUARTIS 0.25 E 0.75
q1 = df_clientes.quantile(0.25)
q3 = df_clientes.quantile(0.75)

#ESTRUTURAÇÃO COM ESTATÍSTICA
estatisticas_filhos = pd.DataFrame({
    'Parâmetro Estatístico': [
        'Contagem (Count)',
        'Média',
        'Mediana',
        'Moda',
        'Desvio Padrão',
        'Variância',
        'Mínimo',
        '1º Quartil (Q1 - 25%)',
        '3º Quartil (Q3 - 75%)',
        'Intervalo Interquartil (IQR)',
        'Máximo',
        'Amplitude Total',
        'Assimetria (Skewness)',
        'Curtose (Kurtosis)'
    ],
    'Valor': [
        len(df_clientes),                             # Contagem
        round(df_clientes.mean(), 4),                # Média
        round(df_clientes.median(), 4),              # Mediana
        int(df_clientes.mode()[0]),                  # Moda
        round(df_clientes.std(), 4),                 # Desvio Padrão
        round(df_clientes.var(), 4),                 # Variância
        int(df_clientes.min()),                      # Mínimo
        round(q1, 4),                                # Q1
        round(q3, 4),                                # Q3
        round(q3 - q1, 4),                           # IQR
        int(df_clientes.max()),                      # Máximo
        int(df_clientes.max() - df_clientes.min()),  # Amplitude Total
        round(df_clientes.skew(), 4),                # Assimetria
        round(df_clientes.kurt(), 4)                 # Curtose
    ]
})

#PRINT FINAL   
print(estatisticas_filhos.to_string(index=False))