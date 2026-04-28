import matplotlib.pyplot as plt
import pandas as pd
import sqlite3

# Conectando ao banco
conn = sqlite3.connect('sales.db')

# Carregando dados
df = pd.read_sql_query("SELECT * FROM customers", conn)
conn.close()

# Gráfico de barras - clientes por cidade
cidades = df.groupby('city')['name'].count()

plt.figure(figsize=(8, 5))
plt.bar(cidades.index, cidades.values, color='steelblue')
plt.title('Clientes por Cidade')
plt.xlabel('Cidade')
plt.ylabel('Quantidade')
plt.tight_layout()
plt.savefig('clientes_por_cidade.png')
plt.show()

print("Gráfico salvo!")