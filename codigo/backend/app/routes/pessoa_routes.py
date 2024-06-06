from flask import Blueprint, jsonify, request
import redis
import json
import random
import time
# Assuming you've set up Redis connection elsewhere or you can set it up here
redis_conn = redis.Redis(host='clusterlive.2adguz.ng.0001.use1.cache.amazonaws.com', port=6379, decode_responses=True)

from ..controllers.pessoa_controller import criar_pessoa, obter_pessoa_numero, obter_pessoa, obter_pessoa_cpf, obter_todas_pessoas, atualizar_pessoa, deletar_pessoa, obter_pessoa_email, autenticar_pessoa_numero, autenticar_pessoa_email

bp = Blueprint('pessoa', __name__)

"""
Rotas de Pessoa

Este módulo contém as rotas para lidar com operações presente em pessoa_controler.
"""


# rota para criar uma pessoa
@bp.route('/pessoa', methods=['POST'])
def criar():
    """
    Cria uma nova pessoa com base nos dados fornecidos na solicitação.

    Returns:
        dict: Dicionário contendo os dados da pessoa criada.
    """
    data = request.json
    pessoa = criar_pessoa(data)
    return jsonify(pessoa), 201

# rota para obter uma pessoa
@bp.route('/pessoa/<int:id_pessoa>', methods=['GET'])
def obter(id_pessoa):
    """
    Obtém os dados de uma pessoa pelo seu ID.

    Args:
        id_pessoa (int): ID da pessoa a ser obtida.

    Returns:
        dict: Dicionário contendo os dados da pessoa.
    """
    # segundos = random.randint(20,30)
    # time.sleep(segundos)
    pessoa = obter_pessoa(id_pessoa)
    return jsonify(pessoa)

# rota para obter uma pessoa por cpf
@bp.route('/pessoa/cpf/<cpf>', methods=['GET'])
def obter_cpf(cpf):
    """
    Obtém os dados de uma pessoa pelo seu CPF.

    Args:
        cpf (str): CPF da pessoa a ser obtida.

    Returns:
        dict: Dicionário contendo os dados da pessoa.
    """
    # segundos = random.randint(20,30)
    # time.sleep(segundos)
    pessoa = obter_pessoa_cpf(cpf)
    return jsonify(pessoa)

# rota para obter uma pessoa por numero
@bp.route('/pessoa/numero/<numero>', methods=['GET'])
def obter_numero(numero):
    """
    Obtém os dados de uma pessoa pelo seu numero.

    Args:
        numero (int): numero da pessoa a ser obtida.

    Returns:
        dict: Dicionário contendo os dados da pessoa.
    """
    # segundos = random.randint(20,30)
    # time.sleep(segundos)
    pessoa = obter_pessoa_numero(numero)
    return jsonify(pessoa)

# rota para obter uma pessoa por email
@bp.route('/pessoa/email/<email>', methods=['GET'])
def obter_email(email):
    """
    Obtém os dados de uma pessoa pelo seu endereço de e-mail.

    Args:
        email (str): Endereço de e-mail da pessoa a ser obtida.

    Returns:
        dict: Dicionário contendo os dados da pessoa.
    """
    # segundos = random.randint(20,30)
    # time.sleep(segundos)
    pessoa = obter_pessoa_email(email)
    return jsonify(pessoa)



# Get pessoas Cache
@bp.route('/pessoas/cache', methods=['GET'])

def obter_todas_pessoas():
    """
    Obtém os dados(no cache) de todas as pessoas registradas no sistema.

    Returns:
        list: Lista contendo dicionários com os dados de todas as pessoas.
    """
    pessoas_json = redis_conn.get('PessoaData')
    if pessoas_json:
        return jsonify(json.loads(pessoas_json)), 200
    return jsonify({"error": "No data found in cache."}), 404

# Get ultima atualizacao
@bp.route('/ultima_atualizacao', methods=['GET'])
def obter_ultima_atualizacao():
    """
    Obtém o horário da última atualização realizada no cache.

    Returns:
        str: O horário da última atualização no cache.
    """
    ultima_atualizacao = redis_conn.get('UltimaAtualizacao')
    if ultima_atualizacao:
        return jsonify({"ultima_atualizacao": ultima_atualizacao}), 200
    else:
        return jsonify({"error": "Última atualização não encontrada no cache."}), 404



# obter pessoa por numero pelo cache
@bp.route('/pessoas/cache/numero/<numero>', methods=['GET'])
def obter_pessoa_por_numero_cache(numero):
    """
    Obtém os dados(no cache) de uma pessoa pelo seu numero.

    Args:
        numero (int): numero da pessoa a ser obtida.

    Returns:
        dict: Dicionário contendo os dados da pessoa.
    """
    pessoas_json = redis_conn.get('PessoaData')
    if pessoas_json:
        pessoas_data = json.loads(pessoas_json)
        for pessoa in pessoas_data:
            if pessoa.get('numero') == numero:
                return jsonify(pessoa), 200
        return jsonify({"error": "No matching pessoa found for the given number."}), 404
    return jsonify({"error": "No data found in cache."}), 404

# obter pessoa por email pelo cache
@bp.route('/pessoas/cache/email/<email>', methods=['GET'])
def obter_pessoa_por_email_cache(email):
    """
    Obtém os dados(no cache) de uma pessoa pelo seu endereço de e-mail.

    Args:
        email (str): Endereço de e-mail da pessoa a ser obtida.

    Returns:
        dict: Dicionário contendo os dados da pessoa.
    """
    pessoas_json = redis_conn.get('PessoaData')
    if pessoas_json:
        pessoas_data = json.loads(pessoas_json)
        for pessoa in pessoas_data:
            if pessoa.get('email') == email:
                return jsonify(pessoa), 200
        return jsonify({"error": "No matching pessoa found for the given email."}), 404
    return jsonify({"error": "No data found in cache."}), 404


@bp.route('pessoa/id/<id>', methods = ['GET'])
def obter_pessoa_por_id(id):
    """
    Obtém os dados de uma pessoa pelo seu ID.

    Args:
        id_pessoa (int): ID da pessoa a ser obtida.

    Returns:
        dict: Dicionário contendo os dados da pessoa.
    """
    pessoa_json = redis_conn.get(f'PessoaData:id:{id}')
    if pessoa_json:
        return jsonify(json.loads(pessoa_json)), 200
    return jsonify({"error": "Pessoa not found."}), 404



# rota para atualizar uma pessoa
@bp.route('/pessoa/<int:id_pessoa>', methods=['PUT'])
def atualizar(id_pessoa):
    """
    Atualiza os dados de uma pessoa existente com base nos dados fornecidos na solicitação.

    Args:
        id_pessoa (int): ID da pessoa a ser atualizada.

    Returns:
        dict: Dicionário contendo os dados atualizados da pessoa.
    """
    data = request.json
    pessoa = atualizar_pessoa(id_pessoa, data)
    return jsonify(pessoa)

# rota para deletar uma pessoa
@bp.route('/pessoa/<int:id_pessoa>', methods=['DELETE'])
def deletar(id_pessoa):
    """
    Deleta uma pessoa do sistema.

    Args:
        id_pessoa (int): ID da pessoa a ser deletada.

    Returns:
        str: String vazia indicando que a pessoa foi deletada com sucesso.
    """
    deletar_pessoa(id_pessoa)
    return '', 204

@bp.route('/pessoa/autenticar_numero/<numero>', methods=['POST'])
def autenticar_numero(numero):
    """
    Autentica uma pessoa com base no número de telefone e senha fornecidos na solicitação.

    Returns:
        str: Mensagem de sucesso ou falha na autenticação.
    """
    senha = request.json.get("senha")
    result = autenticar_pessoa_numero(numero, senha)
    if result:
        return jsonify(result), 201
    else:
        return jsonify({'message': 'Autenticação falhou'}), 401


@bp.route('/pessoa/autenticar_email/<email>', methods=['POST'])

def autenticar_email(email):
    """
    Autentica uma pessoa com base no endereço de e-mail e senha fornecidos na solicitação.

    Returns:
        str: Mensagem de sucesso ou falha na autenticação.
    """
    senha = request.json.get("senha")
    result = autenticar_pessoa_email(email, senha)
    if result:
        return jsonify(result), 201
    else:
        return jsonify({'message': 'Autenticação falhou'}), 401

# Health check route
@bp.route('/health_check', methods=['GET'])
def check():
    return jsonify("OK"), 201
