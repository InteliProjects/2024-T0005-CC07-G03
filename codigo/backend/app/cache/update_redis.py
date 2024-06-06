import pymysql
import redis
import json
from datetime import datetime
import pytz  # Import the pytz library

# Configuracao banco de dados
db_config = {
    "host": "live-db-sprint5.cqjeaemyz0rx.us-east-1.rds.amazonaws.com",
    "user": "admin",
    "password": "live852741",
    "db": "sample"
}

# Conectar com banco de dados
db_conn = pymysql.connect(**db_config)
cursor = db_conn.cursor()

# funcao para obter dados
def fetch_data(table_name):
    cursor.execute(f"SELECT * FROM {table_name}")
    columns = [col[0] for col in cursor.description]
    rows = cursor.fetchall()
    return [dict(zip(columns, row)) for row in rows]

# Obter dados
pessoa_data = fetch_data("Pessoa")
pos_pago_data = fetch_data("pos_pago")
pre_pago_data = fetch_data("pre_pago")

# Configuracao redis
redis_conn = redis.Redis(
    host='clusterlive.2adguz.ng.0001.use1.cache.amazonaws.com',
    port=6379,
    decode_responses=True
)

# configuracao de fuso horario
sao_paulo_horario = pytz.timezone('America/Sao_Paulo')
horario_atual = datetime.now(sao_paulo_horario)
time_string = horario_atual.strftime('%H:%M:%S')
redis_conn.set('UltimaAtualizacao', time_string)


# Atualizar cache
redis_conn.set('PessoaData', json.dumps(pessoa_data))
redis_conn.set('PosPagoData', json.dumps(pos_pago_data))
redis_conn.set('PrePagoData', json.dumps(pre_pago_data))

# Fechar o cursor e a conexão com o banco de dados
cursor.close()
db_conn.close()
print("cache atualizado")
