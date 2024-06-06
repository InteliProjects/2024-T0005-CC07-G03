# app/controllers/pessoa_controller.py
from flask import abort
from ..models.pessoa_model import Pessoa,db
from .pre_pago_controller import criar_pre
from .pos_pago_controller import criar_pos
from sqlalchemy import func
from .pre_pago_controller import adicionar_consumo_atual
import bcrypt
import requests

url = "https://e1k9lobizj.execute-api.us-east-1.amazonaws.com/default/emailLambda?email=" #url filas

"""
Controlador de Pessoas

Este módulo contém funções para lidar com operações relacionadas a pessoas, como criação, obtenção,
atualização e exclusão de registros de pessoas no banco de dados. Além disso, inclui funções para autenticar
pessoas com base em seus números de telefone e endereços de e-mail.
"""



"""
        Cria uma nova pessoa com base nos dados fornecidos.

        Args:
            data (dict): Dicionário contendo os dados da pessoa.

        Returns:
            dict: Dicionário contendo os dados da pessoa criada.
"""
def criar_pessoa(data):
    pessoa = Pessoa(**data)
    senha_codificada = f'{pessoa.senha}'.encode('utf-8')
    print(senha_codificada)
    pessoa.senha = hash_senha(senha_codificada)
    print(url + pessoa.email)
    requests.get(url + pessoa.email)

    
    # se o tipo da pessoa for "pre" cria um pre pago para ela
    if pessoa.tipo == 'pre':
        pre = criar_pre(consumo_atual=0, consumo_total=200, valor=0, saldo=0)
        db.session.add(pre)
        db.session.commit()

        pessoa.id_pre = pre.id_prepago
    # se o tipo da pessoa for "pos" cria um pos pago para ela
    elif pessoa.tipo == 'pos':
        pos = criar_pos(consumo = 0,  valor=0)
        db.session.add(pos)
        db.session.commit()
        pessoa.id_pos = pos.id_pospago

    db.session.add(pessoa)
    db.session.commit()
    return pessoa_to_dict(pessoa)



"""
    Converte um objeto Pessoa em um dicionário serializável.

    Args:
        pessoa (Pessoa): Objeto da classe Pessoa.

    Returns:
        dict: Dicionário contendo os dados da pessoa.
"""
def pessoa_to_dict(pessoa): #necessário para serializar
    return {
        'id_pessoa': pessoa.id_pessoa,
        'nome': pessoa.nome,
        'email': pessoa.email,
        'cpf': pessoa.cpf,
        'numero': pessoa.numero,
        'tipo': pessoa.tipo,
        'id_pre': pessoa.id_pre,
        'id_pos': pessoa.id_pos,
        'senha': pessoa.senha
    }

"""
    Obtém uma pessoa pelo seu ID.

    Args:
        id_pessoa (int): ID da pessoa a ser obtida.

    Returns:
        dict: Dicionário contendo os dados da pessoa obtida.
"""
def obter_pessoa(id_pessoa):
    pessoa = Pessoa.query.get_or_404(id_pessoa)
    adicionar_consumo_atual(pessoa.id_pre,1)
    return pessoa_to_dict(pessoa)



"""
    Obtém uma pessoa pelo seu CPF.

    Args:
        cpf (str): CPF da pessoa a ser obtida.

    Returns:
        dict: Dicionário contendo os dados da pessoa obtida.
"""
def obter_pessoa_cpf(cpf):
    pessoa = Pessoa.query.filter_by(cpf=cpf).first()
    adicionar_consumo_atual(pessoa.id_pre,1)
    if pessoa is None:
        abort(404, description="Pessoa não encontrada")
    return pessoa_to_dict(pessoa)

"""
    Obtém uma pessoa pelo seu Número.

    Args:
        Número (INT): Número da pessoa a ser obtida.

    Returns:
        dict: Dicionário contendo os dados da pessoa obtida.
"""
def obter_pessoa_numero(numero):
    pessoa = Pessoa.query.filter_by(numero=numero).first()
    adicionar_consumo_atual(pessoa.id_pre,1)
    if pessoa is None:
        abort(404, description="Pessoa não encontrada")
    return pessoa_to_dict(pessoa)


"""
    Obtém uma pessoa pelo seu email.

    Args:
        email (str): email da pessoa a ser obtida.

    Returns:
        dict: Dicionário contendo os dados da pessoa obtida.
"""
def obter_pessoa_email(email):
    pessoa = Pessoa.query.filter_by(email = email).first()
    adicionar_consumo_atual(pessoa.id_pre,1)
    if pessoa is None:
        abort(404, description="Pessoa não encontrada")
    return pessoa_to_dict(pessoa)


"""
    Obtém todas as pessoas registradas no sistema.

    Returns:
        list: Lista contendo dicionários com os dados de todas as pessoas.
"""
def obter_todas_pessoas():
    pessoas = Pessoa.query.all()
    return [{'id_pessoa': pessoa.id_pessoa, 'nome': pessoa.nome, 'email': pessoa.email, 'cpf': pessoa.cpf, 'numero': pessoa.numero, 'tipo': pessoa.tipo,
        'id_pre': pessoa.id_pre, 'id_pos': pessoa.id_pos, 'senha': pessoa.senha} for pessoa in pessoas]



"""
    Atualiza os dados de uma pessoa existente.

    Args:
        id_pessoa (int): ID da pessoa a ser atualizada.
        data (dict): Dicionário contendo os novos dados da pessoa.

    Returns:
        dict: Dicionário contendo os dados atualizados da pessoa.
"""
def atualizar_pessoa(id_pessoa, data):
    pessoa = Pessoa.query.get_or_404(id_pessoa) #fazer get de pessoa que deseja alterar
    for key, value in data.items():
        setattr(pessoa, key, value)
    db.session.commit()
    return pessoa_to_dict(pessoa)


"""
    Deleta uma pessoa do sistema.

    Args:
        id_pessoa (int): ID da pessoa a ser deletada.

    Returns:
        str: String vazia indicando que a pessoa foi deletada com sucesso.
"""
def deletar_pessoa(id_pessoa):
    pessoa = Pessoa.query.get_or_404(id_pessoa)
    db.session.delete(pessoa)
    db.session.commit()
    return ''


"""
    Gera um hash seguro para uma senha.

    Args:
        senha (str): Senha a ser hasheada.

    Returns:
        str: Hash seguro gerado para a senha.
"""
def hash_senha(senha):
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(senha, salt)
    return hashed


"""
    Autentica uma pessoa com base em seu número de telefone e senha.

    Args:
        numero (str): Número de telefone da pessoa.
        senha (str): Senha da pessoa.

    Returns:
        bool: True se a autenticação for bem-sucedida, False caso contrário.
"""
def autenticar_pessoa_numero(numero, senha):
    pessoa = Pessoa.query.filter_by(numero=numero).first()
    print(f"senha: {senha}")
    print(f"hashed: {pessoa.senha.encode('utf-8')}")
    if pessoa is None:
        print("falso em pessoa is None")
        return False

    if bcrypt.checkpw(senha.encode('utf-8'), pessoa.senha.encode('utf-8')):
        print("autenticação efetuada com sucesso!!!")
        return True
    else:
        print("falso em bcrypt")
        return False

"""
    Autentica uma pessoa com base em seu endereço de e-mail e senha.

    Args:
        email (str): Endereço de e-mail da pessoa.
        senha (str): Senha da pessoa.

    Returns:
        bool: True se a autenticação for bem-sucedida, False caso contrário.
"""
def autenticar_pessoa_email(email, senha):
    pessoa = Pessoa.query.filter_by(email=email).first()
    print(f"senha: {senha}")
    print(f"hashed: {pessoa.senha.encode('utf-8')}")
    if pessoa is None:
        print("falso em pessoa is None")
        return False

    if bcrypt.checkpw(senha.encode('utf-8'), pessoa.senha.encode('utf-8')):
        print("autenticação efetuada com sucesso!!!")
        return True
    else:
        print("falso em bcrypt")
        return False
