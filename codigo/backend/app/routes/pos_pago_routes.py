from flask import Blueprint,Flask, jsonify, request
from ..controllers.pos_pago_controller import criar_pos, atualizar_pos, obter_pos, obter_todos_pos, deletar_pos, aumentar_consumo, diminuir_consumo, criar_pos
import time
import random

bp = Blueprint('pospago',__name__)
"""
Rotas de planos Pós-Pagos

Este módulo contém as rotas para lidar com operações relacionadas a planos pós-pagos.
"""




# rota para criar um pos pago
@bp.route('/pospago', methods=['POST'])
def criar():
    """
    Cria um novo plano pós-pago com base nos dados fornecidos na solicitação.

    Returns:
        dict: Dicionário contendo os dados do plano pós-pago criado.
    """
    data = request.json 
    pos = criar_pos(data)
    return jsonify(pos), 201


# rota para obter um pos pago
@bp.route('/pospago/<int:id_pospago>', methods=['GET'])
def obter(id_pospago):
    """
    Obtém os dados de um plano pós-pago pelo seu ID.

    Args:
        id_pospago (int): ID do plano pós-pago a ser obtido.

    Returns:
        dict: Dicionário contendo os dados do plano pós-pago.
    """
    # segundos = random.randint(20,30)
    # time.sleep(segundos)
    pos = obter_pos(id_pospago)
    return jsonify(pos)

# rota para obter todos os pos pagos
@bp.route('/pospagos', methods=['GET'])
def obter_todos():
    """
    Obtém os dados de todos os pagamentos pós-pagos registrados no sistema.

    Returns:
        list: Lista contendo dicionários com os dados de todos os pagamentos pós-pagos.
    """
    pos = obter_todos_pos()
    return jsonify(pos)

# rota para atualizar um pos pago
@bp.route('/pospago/<int:id_pospago>',methods=['PUT'])
def atualizar(id_pospago):
    """
    Atualiza os dados de um plano pós-pago existente com base nos dados fornecidos na solicitação.

    Args:
        id_pospago (int): ID do plano pós-pago a ser atualizado.

    Returns:
        dict: Dicionário contendo os dados atualizados do plano pós-pago.
    """
    data = request.json
    pos = atualizar_pos(id_pospago,data)
    return jsonify(pos)

# rota para deletar um pos pago
@bp.route('/pospago/<int:id_pospago>', methods=['DELETE'])
def deletar(id_pospago):
    """
    Deleta um plano pós-pago do sistema.

    Args:
        id_pospago (int): ID do plano pós-pago a ser deletado.

    Returns:
        str: String vazia indicando que o plano pós-pago foi deletado com sucesso.
    """
    deletar_pos(id_pospago)
    return ' ', 204

# rota para aumentar o consumo atual de um pos pago
@bp.route('/pospago/aumentar_consumo_atual/<int:id_pospago>', methods=['PUT'])
def aumentar_consumo_atual(id_pospago):
    """
    Aumenta o consumo atual de um plano pós-pago.

    Args:
        id_pospago (int): ID do plano pós-pago a ter o consumo atual aumentado.

    Returns:
        dict: Dicionário contendo os dados atualizados do plano pós-pago.
    """
    data = request.json
    valor = data.get('valor')
    if not isinstance(valor, (int, float)):
        return {'message': 'O valor fornecido não é um número válido'}, 400
    pos = aumentar_consumo(id_pospago, valor)
    return pos, 200

# rota para diminuir o consumo atual de um pos pago
@bp.route('/pospago/diminuir_consumo_atual/<int:id_pospago>', methods=['PUT'])
def diminuir_consumo_atual(id_pospago):
    """
    Diminui o consumo atual de um plano pós-pago.

    Args:
        id_pospago (int): ID do plano pós-pago a ter o consumo atual diminuído.

    Returns:
        dict: Dicionário contendo os dados atualizados do plano pós-pago.
    """
    data = request.json
    valor = data.get('valor')
    if not isinstance(valor, (int, float)):
        return {'message': 'O valor fornecido não é um número válido'}, 400
    pos = diminuir_consumo(id_pospago, valor)
    return jsonify(pos), 200
