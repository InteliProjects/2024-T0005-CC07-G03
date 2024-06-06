# app/controllers/pre_pago_controller.py
from ..models.pessoa_model import Pessoa,PosPago,PrePago,db

"""
Controlador de planos Pré-Pagos

Este módulo contém funções para lidar com operações relacionadas a planos pré-pagos.
"""



"""
    Cria um novo plano pré-pago com base nos dados fornecidos.

    Args:
        consumo_atual (float): O consumo atual do plano pré-pago.
        consumo_total (float): O consumo total do plano pré-pago.
        valor (float): O valor do plano pré-pago.
        saldo (float): O saldo do plano pré-pago.

    Returns:
        PrePago: O objeto do plano pré-pago criado.
"""
def criar_pre(consumo_atual, consumo_total, valor, saldo):
    pre = PrePago(consumo_atual=consumo_atual, consumo_total=consumo_total, valor=valor, saldo = saldo)
    db.session.add(pre)
    db.session.commit()
    return pre



"""
    Converte um objeto plano Pré-Pago em um dicionário serializável.

    Args:
        pre (PrePago): Objeto da classe plano Pré-Pago.

    Returns:
        dict: Dicionário contendo os dados do plano pré-pago.
"""
def pre_to_dict(pre):
    return {
        'id_prepago' : pre.id_prepago,
        'consumo_atual' : pre.consumo_atual,
        'consumo_total' : pre.consumo_total,
        'valor' : pre.valor,
        'saldo' : pre.saldo,
        'pessoas': [pessoa.nome for pessoa in pre.pessoas]
    }


"""
    Obtém um plano pré-pago pelo seu ID.

    Args:
        id_prepago (int): ID do plano pré-pago a ser obtido.

    Returns:
        dict: Dicionário contendo os dados do plano pré-pago obtido.
"""
def obter_pre(id_prepago):
    pre = PrePago.query.get_or_404(id_prepago)
    return pre_to_dict(pre)


"""
    Obtém todos os pagamentos pré-pagos registrados no sistema.

    Returns:
        list: Lista contendo dicionários com os dados de todos os pagamentos pré-pagos.
"""
def obter_todos_pre():
    pres = PrePago.query.all()
    return [{'id_prepago' : pre.id_prepago, 'consumo_atual' : pre.consumo_atual,'consumo_total' : pre.consumo_total, 'valor' : pre.valor, 'saldo' : pre.saldo,} for pre in pres]

"""
    Atualiza os dados de um plano pré-pago existente.

    Args:
        id_prepago (int): ID do plano pré-pago a ser atualizado.
        data (dict): Dicionário contendo os novos dados do plano pré-pago.

    Returns:
        dict: Dicionário contendo os dados atualizados do plano pré-pago.
"""
def atualizar_pre(id_prepago,data):
    pre = PrePago.query.get_or_404(id_prepago) #fazer get de pre que deseja alterar
    for key, value in data.items():
        setattr(pre, key, value)
    db.session.commit()
    return pre_to_dict(pre)




"""
    Deleta um plano pré-pago do sistema.

    Args:
        id_prepago (int): ID do plano pré-pago a ser deletado.

    Returns:
        str: String vazia indicando que o plano pré-pago foi deletado com sucesso.
"""
def deletar_pre(id_prepago):
    pre = PrePago.query.get_or_404(id_prepago)
    db.session.delete(pre)
    db.session.commit()
    return''


"""
    Adiciona consumo atual a um plano pré-pago.

    Args:
        id_prepago (int): ID do plano pré-pago a ter o consumo atual adicionado.
        valor_adicionado (float): Valor a ser adicionado ao consumo atual.

    Returns:
        dict: Dicionário contendo os dados atualizados do plano pré-pago.
"""
def adicionar_consumo_atual(id_prepago, valor_adicionado):
    pre = PrePago.query.get_or_404(id_prepago)
    pre.consumo_atual += valor_adicionado
    db.session.commit()
    return pre_to_dict(pre)


"""
    Adiciona consumo total a um plano pré-pago.

    Args:
        id_prepago (int): ID do plano pré-pago a ter o consumo total adicionado.
        valor_adicionado (float): Valor a ser adicionado ao consumo total.

    Returns:
        dict: Dicionário contendo os dados atualizados do plano pré-pago.
"""
def adicionar_consumo_total(id_prepago, valor_adicionado):
    pre = PrePago.query.get_or_404(id_prepago)
    pre.consumo_total += valor_adicionado
    db.session.commit()
    return pre_to_dict(pre)


"""
    Adiciona saldo a um plano pré-pago.

    Args:
        id_prepago (int): ID do plano pré-pago a ter o saldo adicionado.
        valor_adicionado (float): Valor a ser adicionado ao saldo.

    Returns:
        dict: Dicionário contendo os dados atualizados do plano pré-pago.
"""
def adicionar_saldo(id_prepago, valor_adicionado):
    pre = PrePago.query.get_or_404(id_prepago)
    print(f"pre: {pre.saldo}")
    print(f"valor_adicionado: {valor_adicionado}")
    pre.saldo += valor_adicionado
    db.session.commit()
    return pre_to_dict(pre)


"""
    Diminui saldo de um plano pré-pago.

    Args:
        id_prepago (int): ID do plano pré-pago a ter o saldo diminuído.
        valor_diminuido (float): Valor a ser subtraído do saldo.

    Returns:
        dict: Dicionário contendo os dados atualizados do plano pré-pago.
"""
def diminuir_saldo(id_prepago, valor_diminuido):
    pre = PrePago.query.get_or_404(id_prepago)
    pre.saldo -= valor_diminuido
    db.session.commit()
    return pre_to_dict(pre)
