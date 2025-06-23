import pandas as pd
import numpy as np
import os

# Criar a pasta /data se ela não existir
if not os.path.exists('data'):
    os.makedirs('data')

# ----------- Criando a Base de Dados Exemplo -----------

unidades = np.arange(0, 2001, 100)  # De 0 até 2000 unidades (de 100 em 100)
preco_unitario = 10
custo_variavel_unitario = 5
custo_fixo_total = 4000

df = pd.DataFrame({
    'Unidades Vendidas': unidades,
    'Receita Total': preco_unitario * unidades,
    'Custo Variável Total': custo_variavel_unitario * unidades,
    'Custo Fixo Total': custo_fixo_total,
})

df['Custo Total'] = df['Custo Variável Total'] + df['Custo Fixo Total']
df['Lucro Operacional'] = df['Receita Total'] - df['Custo Total']

# ----------- Salvando como CSV -----------

caminho_csv = 'data/base_exemplo.csv'
df.to_csv(caminho_csv, index=False)

print(f'Arquivo CSV criado com sucesso em: {caminho_csv}')
print(df)
