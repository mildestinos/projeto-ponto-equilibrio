import pandas as pd
import matplotlib.pyplot as plt

# Ler a base de dados já gerada anteriormente
df = pd.read_csv('data/base_exemplo.csv')

# Calcular Margem de Contribuição
df['Margem de Contribuição'] = df['Receita Total'] - df['Custo Variável Total']

# Calcular GAO apenas para os pontos com Lucro > 0 (evitar divisão por zero e resultados irrelevantes)
df['GAO'] = df.apply(lambda row: (row['Margem de Contribuição'] / row['Lucro Operacional'])
                     if row['Lucro Operacional'] > 0 else None, axis=1)

# Plotando o GAO
plt.figure(figsize=(10, 6))

# Filtrar só os pontos com GAO calculado
df_grafico = df[df['GAO'].notnull()]

plt.plot(df_grafico['Unidades Vendidas'], df_grafico['GAO'], marker='o', color='blue', label='GAO')

# Destaque do ponto de equilíbrio
ponto_equilibrio = 800  # Calculado anteriormente
plt.axvline(x=ponto_equilibrio, color='orange', linestyle='--', label='Ponto de Equilíbrio (800 unidades)')

# Ajustes visuais
plt.title('Grau de Alavancagem Operacional (GAO) ao Longo das Vendas')
plt.xlabel('Unidades Vendidas')
plt.ylabel('GAO (x)')
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.show()
