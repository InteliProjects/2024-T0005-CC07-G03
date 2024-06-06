# app/models/pre_pago_model.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship

"""
Módulo de Modelos para usuário(Pessoa) e tipos de plano (pré e pós-pago)

Este módulo contém os modelos de dados para tipos de plano pré e pós-pagos, 
bem como informações de pessoas associadas a esses pagamentos.
"""

db = SQLAlchemy()


"""
Modelo de dados para planos pós-pagos.

Este modelo define a estrutura de dados para pagamentos pós-pagos, 
incluindo informações de consumo, valor e associação com pessoas.
"""
class PosPago(db.Model):
    __tablename__ = 'pos_pago'
    id_pospago = db.Column(db.Integer, primary_key=True, autoincrement=True)
    consumo = db.Column(db.DOUBLE)
    valor = db.Column(db.DOUBLE)
    pessoas = relationship("Pessoa", backref="pos_pagos") 


"""
Modelo de dados para planos pré-pagos.

Este modelo define a estrutura de dados para planos pré-pagos, 
incluindo informações de consumo atual, consumo total, valor, saldo e associação com pessoas.
"""
class PrePago(db.Model):
    __tablename__ = 'pre_pago'
    id_prepago = db.Column(db.Integer, primary_key=True, autoincrement=True)
    consumo_atual = db.Column(db.DOUBLE)
    consumo_total = db.Column(db.DOUBLE)
    valor = db.Column(db.DOUBLE)
    saldo = db.Column(db.DOUBLE)
    pessoas = relationship("Pessoa", backref="pre_pagos")



"""
    Modelo de dados para informações de pessoas associadas aos planos.

    Este modelo define a estrutura de dados para informações de pessoas, 
    incluindo nome, email, CPF, número, tipo de pagamento (pré ou pós) e associação com planos.
"""
class Pessoa(db.Model):
    __tablename__ = 'Pessoa'
    id_pessoa = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(60))
    cpf = db.Column(db.String(45))
    numero = db.Column(db.String(45))
    tipo = db.Column(db.String(45))
    id_pre = db.Column(db.Integer, db.ForeignKey('pre_pago.id_prepago'))
    id_pos = db.Column(db.Integer, db.ForeignKey('pos_pago.id_pospago'))
    senha = db.Column(db.String(256))
