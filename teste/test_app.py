import pandas as pd
import numpy as np
import openpyxl
import os

# definir o caminho do arquivo Excel

## Usa a função read_excel do pandas para ler o arquivo
## O resultado é armazenado em um objeto chamado DataFrame
caminho_arquivo = 'data\\acoes-listadas-b3.csv'

try:
    # ler o arquivo Excel
    df = pd.read_csv(caminho_arquivo, sep=',')

    print("✅ Arquivo Excel lido com sucesso!")
    print("\nConteúdo do arquivo:")

except FileNotFoundError:
    print(f"❌ ERRO: O arquivo '{caminho_arquivo}' não foi encontrado.")
    print("Verifique se o nome e o caminho do arquivo estão corretos.")
except Exception as e:
    print(f"❌ ERRO: Ocorreu um problema ao ler o arquivo Excel.")
    print(f"Detalhes do erro: {e}")

# acessar colunas específicas
coluna_interesse = df['Ticker']

print(f'{df.loc[0]}')
for acao in coluna_interesse:
 
     print(f'Ações: {acao}')
