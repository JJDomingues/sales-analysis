import sqlite3
import pandas as pd

# Conexão
conn = sqlite3.connect("sales.db")

# Carrega tudo no Pandas
df = pd.read_sql_query("SELECT * FROM customers", conn)
conn.close()

print("=" * 40)
print("   RELATÓRIO DE CLIENTES - SALES ANALYSIS")
print("=" * 40)

# Visão geral
print(f"\nTotal de clientes: {len(df)}")
print(f"Idade média: {df['age'].mean():.1f} anos")
print(f"Mais novo: {df['age'].min()} anos")
print(f"Mais velho: {df['age'].max()} anos")

# Clientes por cidade
print("\n--- Clientes por Cidade ---")
print(df.groupby('city')['name'].count())

# Média de idade por cidade
print("\n--- Média de Idade por Cidade ---")
print(df.groupby('city')['age'].mean().round(1))

# Clientes acima da média
media = df['age'].mean()
print(f"\n--- Clientes Acima da Média ({media:.1f} anos) ---")
print(df[df['age'] > media][['name', 'city', 'age']])

print("\n" + "=" * 40)