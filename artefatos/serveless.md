# Serveless
AWS Lambda é um serviço de computação sem servidor oferecido pela Amazon Web Services (AWS) que permite executar código em resposta a eventos sem precisar gerenciar a infraestrutura subjacente. É escalável automaticamente e você paga apenas pelo tempo de execução do código.

Serverless é um modelo de computação em que o provedor de nuvem (como a AWS) é responsável pela execução, dimensionamento e gerenciamento da infraestrutura, permitindo que os desenvolvedores se concentrem apenas no código de aplicativo. Isso elimina a necessidade de provisionar e gerenciar servidores, tornando o desenvolvimento e a implantação de aplicativos mais rápidos e eficientes.

O grupo LIVE utilizou AWS LAMBDA para armazenar os logs de acessos enviados do frontend para o cloudwatch dentro de um bucket do S3.
abaixo segue o código do grupo:

```
import boto3
from datetime import datetime, timedelta
import time

def lambda_handler(event, context):
    # Cria um cliente S3
    logs_client = boto3.client('logs')
    s3 = boto3.client('s3')
    
    # Especifica o nome do bucket, o nome do arquivo no S3 e o caminho local do arquivo
    bucket_name = 'bucketdomaiamarcelo'
    s3_file_name = 'teste.txt'

    # Especifica o grupo de logs do CloudWatch e o intervalo de tempo
    log_group_name = 'access.log'
   # Define o intervalo de tempo para os últimos 15 minutos
    end_time = int(datetime.now().timestamp() * 1000)  # Tempo atual em milissegundos
    start_time = end_time - (365 * 24 * 60 * 60 * 1000)  # 365 dias antes do tempo atual em milissegundos
    
    
    # Faz a consulta para coletar os logs
    query = "fields @timestamp, @message | sort @timestamp desc | limit 20"
    start_query_response = logs_client.start_query(
        logGroupName=log_group_name,
        startTime=start_time,
        endTime=end_time,
        queryString=query,
    )
    
    query_id = start_query_response['queryId']
    
    # Aguardar até que a consulta seja concluída
    response = None
    while response is None or response['status'] == 'Running':
        time.sleep(1)  # Adiciona um delay para evitar excesso de requisições
        response = logs_client.get_query_results(queryId=query_id)
    
    # Processar os resultados da consulta, se houver
    log_lines = []
    if 'results' in response and response['results']:
        for result in response['results']:
            timestamp = next(item['value'] for item in result if item['field'] == '@timestamp')
            message = next(item['value'] for item in result if item['field'] == '@message')
            log_lines.append(f"{timestamp} {message}")
    else:
        log_lines.append("Nenhum log encontrado no intervalo especificado.")

    log_content = "\n".join(log_lines)
    
    print(log_content)

    # Caminho para o arquivo temporário no ambiente Lambda
    local_file_path = '/tmp/teste.txt'
    
    # Gerando um arquivo temporário
    with open(local_file_path, 'w') as f:
        f.write(log_content)
        
    # Faz o upload do arquivo para o bucket especificado
    try:
        s3.upload_file(local_file_path, bucket_name, s3_file_name)
        return_message = f"Arquivo enviado com sucesso: {s3_file_name}"
    except Exception as e:
        return_message = f"Erro ao fazer upload do arquivo: {e}"
    
    return {
        'statusCode': 200,
        'body': return_message
    }
```

obs: O aws lambda estava na conta antiga dda aws do grupo o saldo ultrapassou os 100 dólares e o laboratório não pode ser acessado, na nova conta do grupo aws lambda está com acesso negado ao S3.