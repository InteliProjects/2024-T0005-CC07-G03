# app/__init__.py

from flask import Flask
from .models.pessoa_model import db
from flask_cors import CORS, cross_origin
"""
Inicialização da Aplicação

Este módulo contém a função responsável por criar e configurar a aplicação Flask.
"""
#from .models.models import db

def create_app():
    """
    Cria e configura a aplicação Flask.

    Returns:
        Flask: Objeto representando a aplicação Flask configurada.
    """
    app = Flask(__name__)
    CORS(app,origins='*')
    
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://admin:live852741@live-db-sprint5.cqjeaemyz0rx.us-east-1.rds.amazonaws.com:3306/sample'
    
    db.init_app(app)
    
    
    # from .routes.test_route import bp as example_bp
    # app.register_blueprint(example_bp, url_prefix='/api')
    from .routes.pessoa_routes import bp as pessoa_bp
    from .routes.pre_pago_routes import bp as pre_pago_bp
    from .routes.pos_pago_routes import bp as pos_pago_bp
    app.register_blueprint(pessoa_bp, url_prefix='/api')
    app.register_blueprint(pre_pago_bp, url_prefix='/api')
    app.register_blueprint(pos_pago_bp, url_prefix='/api')
    
    return app
