from flask import Blueprint, Flask, jsonify, request
import time
import random
import redis
import json
# Assuming you've set up Redis connection elsewhere or you can set it up here
redis_conn = redis.Redis(host='clusterlive.2adguz.ng.0001.use1.cache.amazonaws.com', port=6379, decode_responses=True)


from ..controllers.pre_pago_controller import (adicionar_consumo_atual,
                                               criar_pre,
                                               adicionar_consumo_total,
                                               adicionar_saldo, atualizar_pre,
                                               criar_pre, deletar_pre,
                                               diminuir_saldo, obter_pre,
                                               obter_todos_pre)

bp = Blueprint('prepago',__name__)
"""
Rotas de planos Pré-Pagos

Este módulo contém as rotas para lidar com operações relacionadas a planos pré-pagos.
"""



# Define uma rota para obter um 'pre' específico pelo seu id
@bp.route('/prepago/<int:id_prepago>', methods=['GET'])
def obter(id_prepago):
    """
    Obtém os dados de um plano pré-pago pelo seu ID.

    Args:
        id_prepago (int): ID do plano pré-pago a ser obtido.

    Returns:
        dict: Dicionário contendo os dados do plano pré-pago.
    """
    # segundos = random.randint(20,30)
    # time.sleep(segundos)
    adicionar_consumo_atual(id_prepago, 1)
    pre = obter_pre(id_prepago)
    return jsonify(pre)

@bp.route('/prepago', methods=['POST'])
def criar():
    """
    Cria um novo plano pré-pago com valores padrão.

    Returns:
        dict: Dicionário contendo os dados do plano pré-pago criado.
    """
    data = request.json
    pre = criar_pre(0, 100, 0, 50)
    return jsonify(pre), 201

# Define uma rota para obter um 'pre'
@bp.route('/prepagos', methods=['GET'])
def obter_todos():
    """
    Obtém os dados de todos os pagamentos pré-pagos registrados no sistema.

    Returns:
        list: Lista contendo dicionários com os dados de todos os pagamentos pré-pagos.
    """
    pre = obter_todos_pre()
    return jsonify(pre)

# Define uma rota para atualizar um 'pre'
@bp.route('/prepago/<int:id_prepago>', methods=['PUT'])
def atualizar(id_prepago):
    """
    Atualiza os dados de um plano pré-pago existente com base nos dados fornecidos na solicitação.

    Args:
        id_prepago (int): ID do plano pré-pago a ser atualizado.

    Returns:
        dict: Dicionário contendo os dados atualizados do plano pré-pago.
    """
    #time.sleep(30)
    adicionar_consumo_atual(id_prepago, 1)
    data = request.json
    pre = atualizar_pre(id_prepago, data)
    return jsonify(pre)

# Define uma rota para deletar um 'pre'
@bp.route('/prepago/<int:id_prepago>', methods=['DELETE'])
def deletar(id_prepago):
    """
    Deleta um plano pré-pago do sistema.

    Args:
        id_prepago (int): ID do plano pré-pago a ser deletado.

    Returns:
        str: String vazia indicando que o plano pré-pago foi deletado com sucesso.
    """
    deletar_pre(id_prepago)
    return '', 204


# Define uma rota para adicionar consumo atual a um 'pre'
@bp.route('/prepago/adicionar_consumo_atual/<int:id_prepago>', methods=['PUT'])
def rota_adicionar_consumo_atual(id_prepago):
    """
    Adiciona consumo atual a um plano pré-pago específico.

    Args:
        id_prepago (int): ID do plano pré-pago a ter o consumo atual aumentado.

    Returns:
        dict: Dicionário contendo os dados atualizados do plano pré-pago.
    """
    #time.sleep(30)
    valor_adicionado = request.json.get("valor_adicionado")
    if not isinstance(valor_adicionado, (int, float)):
        return {'message': 'O valor fornecido não é um número válido'}, 400

    pre = adicionar_consumo_atual(id_prepago,valor_adicionado)
    return pre, 200


# Define uma rota para adicionar consumo total a um 'pre'
@bp.route('/prepago/adicionar_consumo_total/<int:id_prepago>', methods=['PUT'])
def rota_adicionar_consumo_total(id_prepago):
    """
    Adiciona consumo total a um plano pré-pago específico.

    Args:
        id_prepago (int): ID do plano pré-pago a ter o consumo total aumentado.

    Returns:
        dict: Dicionário contendo os dados atualizados do plano pré-pago.
    """
    #time.sleep(30)
    valor_adicionado = request.json.get("valor_adicionado")
    if not isinstance(valor_adicionado, (int, float)):
        return {'message': 'O valor fornecido não é um número válido'}, 400

    pre = adicionar_consumo_total(id_prepago,valor_adicionado)
    return pre, 200

# Define uma rota para adicionar saldo a um 'pre'
@bp.route('/prepago/adicionar_saldo/<int:id_prepago>', methods=['PUT'])
def rota_adicionar_saldo(id_prepago):
    """
    Adiciona saldo a um plano pré-pago específico.

    Args:
        id_prepago (int): ID do plano pré-pago a ter o saldo aumentado.

    Returns:
        dict: Dicionário contendo dados do plano pré pago
    """
    #time.sleep(30)
    valor_adicionado = request.json.get("valor_adicionado")
    if not isinstance(valor_adicionado, (int, float)):
        return {'message': 'O valor fornecido não é um número válido'}, 400

    pre = adicionar_saldo(id_prepago,valor_adicionado)
    return pre, 200


# Define uma rota para diminuir saldo a um 'pre'
@bp.route('/prepago/diminuir_saldo/<int:id_prepago>', methods=['PUT'])
def rota_diminuir_saldo(id_prepago):
    """
    Diminui saldo de um plano pré-pago específico.

    Args:
        id_prepago (int): ID do plano pré-pago a ter o saldo diminuído.

    Returns:
        dict: Dicionário contendo os dados atualizados do plano pré-pago.
    """
    #time.sleep(30)
    valor_diminuido = request.json.get("valor_diminuido")
    if not isinstance(valor_diminuido, (int, float)):
        return {'message': 'O valor fornecido não é um número válido'}, 400

    pre = diminuir_saldo(id_prepago,valor_diminuido)
    return pre, 200



# obter todos pre_pago pelo cache
@bp.route('/pre_pago/cache', methods=['GET'])
def obter_todos_pre_pago_cache():
    """
    Obtém os dados(do cache) de todos os pagamentos pré-pagos registrados no sistema.

    Returns:
        list: Lista contendo dicionários com os dados de todos os pagamentos pré-pagos.
    """
    pre_pago_json = redis_conn.get('PrePagoData')
    if pre_pago_json:
        return jsonify(json.loads(pre_pago_json)), 200
    return jsonify({"error": "No data found in cache."}), 404

#obter pre_pago por id do cache
@bp.route('/pre_pago/cache/id/<id>', methods=['GET'])
def obter_pre_pago_por_id_cache(id):
    """
    Obtém os dados(do cache) de um plano pré-pago pelo seu ID.

    Args:
        id_prepago (int): ID do plano pré-pago a ser obtido.

    Returns:
        dict: Dicionário contendo os dados do plano pré-pago.
    """
    pre_pago_json = redis_conn.get('PrePagoData')
    if pre_pago_json:
        pre_pago_data = json.loads(pre_pago_json)
        pre_pago_record = next((item for item in pre_pago_data if item["id_prepago"] == int(id)), None)
        if pre_pago_record:
            return jsonify(pre_pago_record), 200
    return jsonify({"error": "PrePago not found."}), 404

#obter pre_pago por numero do cache
@bp.route('/pre_pago/cache/numero/<numero>', methods=['GET'])
def obter_pre_pago_por_numero_cache(numero):
    """
    Obtém os dados de um plano pré-pago pelo seu numero.

    Args:
        numero (int): numero do plano pré-pago a ser obtido.

    Returns:
        dict: Dicionário contendo os dados do plano pré-pago.
    """
    pre_pago_json = redis_conn.get(f'PrePagoData:numero:{numero}')
    if pre_pago_json:
        return jsonify(json.loads(pre_pago_json)), 200
    return jsonify({"error": "PrePago not found."}), 404

#obter pre_pago por email do cache
@bp.route('/pre_pago/cache/email/<email>', methods=['GET'])
def obter_pre_pago_por_email_cache(email):
    """
    Obtém os dados de um plano pré-pago pelo seu email.

    Args:
        email (str): email do plano pré-pago a ser obtido.

    Returns:
        dict: Dicionário contendo os dados do plano pré-pago.
    """
    pre_pago_json = redis_conn.get(f'PrePagoData:email:{email}')
    if pre_pago_json:
        return jsonify(json.loads(pre_pago_json)), 200
    return jsonify({"error": "PrePago not found."}), 404

