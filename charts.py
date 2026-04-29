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

# Gráfico 2 - Média de idade por cidade
media_idade = df.groupby('city')['age'].mean().round(1)

plt.figure(figsize=(8, 5))
plt.bar(media_idade.index, media_idade.values, color='coral')
plt.title('Média de Idade por Cidade')
plt.xlabel('Cidade')
plt.ylabel('Idade Média')
plt.tight_layout()
plt.savefig('media_idade_por_cidade.png')
plt.show()

print("Segundo gráfico salvo!")

# Gráfico 3 - Total de vendas por cidade
conn2 = sqlite3.connect('sales.db')
df_sales = pd.read_sql_query("SELECT city, SUM(amount) as total FROM sales GROUP BY city", conn2)
conn2.close()

plt.figure(figsize=(8, 5))
plt.bar(df_sales['city'], df_sales['total'], color='green')
plt.title('Total de Vendas por Cidade (R$)')
plt.xlabel('Cidade')
plt.ylabel('Total (R$)')
plt.tight_layout()
plt.savefig('vendas_por_cidade.png')
plt.show()
print("Terceiro gráfico salvo!")

# Gráfico 4 - Total de vendas por cliente (JOIN)
conn3 = sqlite3.connect('sales.db')
df_join = pd.read_sql_query("""
    SELECT c.name, SUM(s.amount) as total
    FROM sales s
    JOIN customers c ON s.customer_id = c.id
    GROUP BY c.name
    ORDER BY total DESC
""", conn3)
conn3.close()

plt.figure(figsize=(10, 6))
plt.barh(df_join['name'], df_join['total'], color='purple')
plt.title('Total de Vendas por Cliente (R$)')
plt.xlabel('Total (R$)')
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig('vendas_por_cliente.png')
plt.show()
print("Quarto gráfico salvo!")