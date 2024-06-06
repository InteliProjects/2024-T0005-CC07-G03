# app/controllers/pos_pago_controller.py
from ..models.pessoa_model import Pessoa,PosPago,PrePago,db

"""
Controlador de planos Pós-Pagos

Este módulo contém funções para lidar com operações relacionadas a planos pós-pagos.
"""



"""
    Cria um novo plano pós-pago com base nos dados fornecidos.

    Args:
        data (dict): Dicionário contendo os dados do plano pós-pago.

    Returns:
        dict: Dicionário contendo os dados do plano pós-pago criado.
"""
def criar_pos(data):
    pos = PosPago(**data)
    db.session.add(pos)
    db.session.commit()
    return pos_to_dict(pos)


"""
    Converte um objeto plano Pós-Pago em um dicionário serializável.

    Args:
        pos (PosPago): Objeto da classe plano Pós-Pago.

    Returns:
        dict: Dicionário contendo os dados do plano pós-pago.
"""
def pos_to_dict(pos):
    return {
        'id_pospago' : pos.id_pospago,
        'consumo' : pos.consumo,
        'valor' : pos.valor,
        'pessoas': [pessoa.nome for pessoa in pos.pessoas]
    }


"""
    Obtém um plano pós-pago pelo seu ID.

    Args:
        id_pospago (int): ID do plano pós-pago a ser obtido.

    Returns:
        dict: Dicionário contendo os dados do plano pós-pago obtido.
"""
def obter_pos(id_pospago):
    pos = PosPago.query.get_or_404(id_pospago)
    return pos_to_dict(pos)


"""
    Obtém todos os pagamentos pós-pagos registrados no sistema.

    Returns:
        list: Lista contendo dicionários com os dados de todos os pagamentos pós-pagos.
"""
def obter_todos_pos():
    pos = PosPago.query.all()
    return [{'id_pospago' : pos.id_pospago, 'consumo' : pos.consumo, 'valor' : pos.valor} for pos in pos]



"""
    Atualiza os dados de um plano pós-pago existente.

    Args:
        id_pospago (int): ID do plano pós-pago a ser atualizado.
        data (dict): Dicionário contendo os novos dados do plano pós-pago.

    Returns:
        dict: Dicionário contendo os dados atualizados do plano pós-pago.
"""
def atualizar_pos(id_pospago,data):
    pos = PosPago.query.get_or_404(id_pospago)
    for key, value in data.items():
        setattr(pos,key,value)
    db.session.commit()
    return pos_to_dict(pos)


"""
    Deleta um plano pós-pago do sistema.

    Args:
        id_pospago (int): ID do plano pós-pago a ser deletado.

    Returns:
        str: String vazia indicando que o plano pós-pago foi deletado com sucesso.
"""
def deletar_pos(id_pospago):
    pos = PosPago.query.get_or_404(id_pospago)
    db.session.delete(pos)
    db.session.commit


"""
    Aumenta o consumo atual de um plano pós-pago.

    Args:
        id_pospago (int): ID do plano pós-pago a ter o consumo aumentado.
        valor (float): Valor a ser adicionado ao consumo atual.

    Returns:
        dict: Dicionário contendo os dados atualizados do plano pós-pago.
"""
def aumentar_consumo(id_pospago, valor):
    pos = PosPago.query.get_or_404(id_pospago)
    pos.consumo += valor
    db.session.commit()
    return pos_to_dict(pos)

"""
    Diminui o consumo atual de um plano pós-pago.

    Args:
        id_pospago (int): ID do plano pós-pago a ter o consumo diminuído.
        valor (float): Valor a ser subtraído do consumo atual.

    Returns:
        dict: Dicionário contendo os dados atualizados do plano pós-pago.
"""
def diminuir_consumo(id_pospago, valor):
    pos = PosPago.query.get_or_404(id_pospago)
    pos.consumo -= valor
    db.session.commit()
    return pos_to_dict(pos)