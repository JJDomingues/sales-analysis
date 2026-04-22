import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect("sales.db")
cursor = conn.cursor()

# Todos os clientes
print("=== Todos os clientes: ===")
cursor.execute("SELECT * FROM customers")
for row in cursor.fetchall():
    print(row)

# Cliente por cidade
print("\n=== Clientes por cidade: ===")
cursor.execute("SELECT city, COUNT(*) FROM customers GROUP BY city")
for row in cursor.fetchall():
    print(row)

# Média de idade
print("\n=== Média de idade: ===")
cursor.execute("SELECT AVG(age) FROM customers")
print(cursor.fetchone()[0])

# Fechando a conexão
conn.close()
