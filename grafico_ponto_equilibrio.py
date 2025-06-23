import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

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

df['GAO'] = df.apply(
    lambda row: (row['Receita de Contribuição'] / row['Lucro Operacional']) if row['Lucro Operacional'] > 0 else None,
    axis=1
)

print("\n✅ GAO para cada nível de produção (onde Lucro > 0):")
print(df[['Unidades Vendidas', 'Lucro Operacional', 'GAO']].dropna())

# ----------- Plotando o Gráfico com Melhorias Profissionais -----------

plt.figure(figsize=(12, 7))
plt.grid(True, linestyle='--', alpha=0.4)

# Linhas principais
plt.plot(df['Unidades Vendidas'], df['Receita Total'], label='Receita de Vendas', color='green', linewidth=2)
plt.plot(df['Unidades Vendidas'], df['Custo Total'], label='Custo Total', color='red', linewidth=2)
plt.hlines(custo_fixo_total, xmin=df['Unidades Vendidas'].min(), xmax=df['Unidades Vendidas'].max(),
           colors='orange', linestyles='dashed', linewidth=2, label='Custo Fixo Total')

# Áreas de Lucro e Prejuízo
plt.fill_between(df['Unidades Vendidas'], df['Receita Total'], df['Custo Total'],
                 where=(df['Receita Total'] >= df['Custo Total']), color='green', alpha=0.2, label='Área de Lucro')
plt.fill_between(df['Unidades Vendidas'], df['Receita Total'], df['Custo Total'],
                 where=(df['Receita Total'] < df['Custo Total']), color='red', alpha=0.2, label='Área de Prejuízo')

# Ponto de Equilíbrio - com marcação melhor
plt.scatter(ponto_equilibrio, valor_no_equilibrio, color='black', s=100, marker='*', zorder=5, label='Ponto de Equilíbrio')
plt.axvline(x=ponto_equilibrio, color='black', linestyle=':', linewidth=1)
plt.axhline(y=valor_no_equilibrio, color='black', linestyle=':', linewidth=1)

plt.annotate(f'Ponto de Equilíbrio\n({ponto_equilibrio:.0f} unidades / R${valor_no_equilibrio:,.0f})',
             xy=(ponto_equilibrio, valor_no_equilibrio),
             xytext=(ponto_equilibrio + 150, valor_no_equilibrio - 2000),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=9, weight='bold')

# Texto da Margem de Segurança
plt.text(df['Unidades Vendidas'].min() + 100, custo_fixo_total + 1500,
         f'Margem de Segurança: {margem_seguranca:.2f}%',
         fontsize=10, color='blue', weight='bold')

# Título Profissional
plt.title('Análise do Ponto de Equilíbrio com Margem de Segurança e GAO', fontsize=14, weight='bold')

# Eixos com formatação de milhar
plt.xlabel('Unidades Vendidas', fontsize=11)
plt.ylabel('Valor (R$)', fontsize=11)

formatter = ticker.FuncFormatter(lambda x, pos: f'R${x:,.0f}')
plt.gca().yaxis.set_major_formatter(formatter)

# Texto explicativo sobre áreas
plt.text(ponto_equilibrio + 300, valor_no_equilibrio + 3000, 'Zona de Lucro', color='green', fontsize=9, weight='bold')
plt.text(ponto_equilibrio - 600, custo_fixo_total - 1500, 'Zona de Prejuízo', color='red', fontsize=9, weight='bold')

# Melhorando a Legenda
plt.legend(loc='upper left', frameon=True, fontsize=9, title='Legenda')

# Limites dos eixos
plt.xlim(0, df['Unidades Vendidas'].max() + 200)
plt.ylim(0, df['Receita Total'].max() + 3000)

# Layout Final
plt.tight_layout()

# Exportar como PNG Alta Resolução (se quiser salvar)
# plt.savefig('grafico_ponto_equilibrio_profissional.png', dpi=300)

plt.show()
