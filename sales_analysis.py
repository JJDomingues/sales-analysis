import sqlite3
import pandas as pd

conn = sqlite3.connect("sales.db")
cursor = conn.cursor()

# SQL
print("=== Todos os clientes: ===")
cursor.execute("SELECT * FROM customers")
for row in cursor.fetchall():
    print(row)

print("\n=== Clientes por cidade: ===")
cursor.execute("SELECT city, COUNT(*) FROM customers GROUP BY city")
for row in cursor.fetchall():
    print(row)

print("\n=== Média de idade: ===")
cursor.execute("SELECT AVG(age) FROM customers")
print(cursor.fetchone()[0])

# Pandas
print("\n=== DATAFRAME PANDAS ===")
df = pd.read_sql_query("SELECT * FROM customers", conn)
print(df)

print("\n=== ESTATÍSTICAS ===")
print(df.describe())

conn.close()
