import pandas as pd
import sqlite3

# Conectando ao banco
conn = sqlite3.connect('sales.db')

# JOIN: cruzando customers com sales
df = pd.read_sql_query("""
    SELECT c.name, c.city, s.amount, s.sale_date
    FROM sales s
    JOIN customers c ON s.customer_id = c.id
""", conn)
conn.close()

# Mostrando o resultado completo
print("=== VENDAS POR CLIENTE ===")
print(df)

# Total gasto por cliente
print("\n=== TOTAL GASTO POR CLIENTE ===")
print(df.groupby('name')['amount'].sum().sort_values(ascending=False))

# Total de vendas por cidade
print("\n=== TOTAL DE VENDAS POR CIDADE ===")
print(df.groupby('city')['amount'].sum().sort_values(ascending=False))