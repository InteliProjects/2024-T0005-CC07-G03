import pymysql

# Configuracao db
db_config = {
    "host": "live-db.cnk6ckkiqtey.us-east-1.rds.amazonaws.com",
    "user": "admin",
    "password": "live852741",
    "db": "sample"
}

try:
    # Conectar com banco de dados
    db_conn = pymysql.connect(**db_config)
    cursor = db_conn.cursor()

    # Executar uma query
    cursor.execute("SELECT * FROM Pessoa LIMIT 1")
    row = cursor.fetchone()
    
    if row:
        print("Successfully connected to the RDS database. Here's a sample record:", row)
    else:
        print("Connected to the RDS database, but no data was found.")

except pymysql.Error as e:
    print(f"Failed to connect to the database. Error: {e}")

finally:
    # Fechar o cursor e a conexão com o banco de dados
    if 'cursor' in locals():
        cursor.close()
    if 'db_conn' in locals():
        db_conn.close()
