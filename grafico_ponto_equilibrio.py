import pandas as pd
import matplotlib.pyplot as plt

# ----------- Lendo a Base de Dados -----------

caminho_csv = 'data/base_exemplo.csv'
df = pd.read_csv(caminho_csv)

# ----------- Parâmetros usados na base -----------

preco_unitario = 10
custo_variavel_unitario = 5
custo_fixo_total = 4000

# ----------- Cálculo do Ponto de Equilíbrio -----------

ponto_equilibrio = custo_fixo_total / (preco_unitario - custo_variavel_unitario)
valor_no_equilibrio = preco_unitario * ponto_equilibrio

# ----------- Cálculo da Margem de Segurança -----------

vendas_atuais = df['Unidades Vendidas'].max()
margem_seguranca = ((vendas_atuais - ponto_equilibrio) / vendas_atuais) * 100

print(f"\n✅ Margem de Segurança: {margem_seguranca:.2f}%")

# ----------- Cálculo do GAO (Grau de Alavancagem Operacional) -----------

df['Receita de Contribuição'] = df['Receita Total'] - df['Custo Variável Total']

# Para evitar divisão por zero ou GAO com lucro negativo, vamos calcular apenas onde o Lucro > 0
df['GAO'] = df.apply(
    lambda row: (row['Receita de Contribuição'] / row['Lucro Operacional']) if row['Lucro Operacional'] > 0 else None,
    axis=1
)

print("\n✅ GAO para cada nível de produção (onde Lucro > 0):")
print(df[['Unidades Vendidas', 'Lucro Operacional', 'GAO']].dropna())

# ----------- Plotando o Gráfico -----------

plt.figure(figsize=(10, 6))

# Linhas principais
plt.plot(df['Unidades Vendidas'], df['Receita Total'], label='Receita de Vendas', color='green')
plt.plot(df['Unidades Vendidas'], df['Custo Total'], label='Custo Total', color='red')
plt.hlines(custo_fixo_total, xmin=df['Unidades Vendidas'].min(), xmax=df['Unidades Vendidas'].max(),
           colors='orange', linestyles='dashed', label='Custo Fixo Total')

# Áreas de Lucro e Prejuízo
plt.fill_between(df['Unidades Vendidas'], df['Receita Total'], df['Custo Total'],
                 where=(df['Receita Total'] >= df['Custo Total']), color='green', alpha=0.3, label='Área de Lucro')
plt.fill_between(df['Unidades Vendidas'], df['Receita Total'], df['Custo Total'],
                 where=(df['Receita Total'] < df['Custo Total']), color='red', alpha=0.3, label='Área de Prejuízo')

# Ponto de Equilíbrio
plt.scatter(ponto_equilibrio, valor_no_equilibrio, color='black', zorder=5)
plt.annotate('Ponto de Equilíbrio',
             xy=(ponto_equilibrio, valor_no_equilibrio),
             xytext=(ponto_equilibrio + 100, valor_no_equilibrio - 1000),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=9)

# Exibir Margem de Segurança no gráfico
plt.text(100, custo_fixo_total + 1000, f'Margem de Segurança: {margem_seguranca:.2f}%', fontsize=9, color='blue')

plt.title('Gráfico de Ponto de Equilíbrio com Margem de Segurança e GAO')
plt.xlabel('Unidades Vendidas')
plt.ylabel('Valor (R$)')
plt.legend()
plt.grid(True)
plt.xlim(0, df['Unidades Vendidas'].max())
plt.ylim(0, df['Receita Total'].max() + 2000)

plt.tight_layout()
plt.show()
