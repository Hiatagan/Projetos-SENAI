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

