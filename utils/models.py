from datetime import datetime as dt
from app import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    __table_args__ = {'schema': 'ytb_downloader'}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(50), nullable=False)
    data_cadastro = db.Column(db.DateTime, nullable=False)

    def __init__(self, email, senha):
        self.email = email
        self.senha = senha
        self.data_cadastro = dt.now()

    def __repr__(self):
        return '<Usuario %r>' % self.email

class InformacoesAdicionais(db.Model):
    __tablename__ = 'informacoes_adicionais'
    __table_args__ = {'schema': 'ytb_downloader'}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_usuario = db.Column(db.Integer, nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    sobrenome = db.Column(db.String(100), nullable=False)
    foto_url = db.Column(db.String(100))
    data_alteracao = db.Column(db.DateTime, nullable=False)
    
    def __init__(self, id_usuario, nome, sobrenome, foto_url):
        self.id_usuario = id_usuario
        self.nome = nome
        self.sobrenome = sobrenome
        self.foto_url = foto_url
        self.data_alteracao = dt.now()

    def __repr__(self):
        return '<InformacoesAdicionais %r>' % self.nome

class HistoricoPesquisa(db.Model):
    __tablename__ = 'historico_pesquisa'
    __table_args__ = {'schema': 'ytb_downloader'}

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_usuario = db.Column(db.Integer, nullable=False)
    string_pesquisa = db.Column(db.String(255), nullable=False)
    data_pesquisa = db.Column(db.DateTime, nullable=False)

    def __init__(self, id_usuario, string_pesquisa):
        self.id_usuario = id_usuario
        self.string_pesquisa = string_pesquisa
        self.data_pesquisa = dt.now()

    def __repr__(self):
        return '<HistoricoPesquisa %r>' % self.pesquisa