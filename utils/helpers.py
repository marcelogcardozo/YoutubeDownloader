from wtforms import StringField, PasswordField, BooleanField, RadioField
from wtforms.validators import DataRequired, Email, Length
from flask_wtf import FlaskForm

class FormularioLogin(FlaskForm):
    email = StringField('E-mail', validators=[DataRequired(), Email(), Length(min=1, max=100)])
    senha = PasswordField('Senha', validators=[DataRequired()])
    lembrar = BooleanField('Lembre-me')

class FormularioCadastro(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired(), Length(min=1, max=30)])
    sobrenome = StringField('Sobrenome', validators=[DataRequired(), Length(min=1, max=30)])
    email = StringField('E-mail', validators=[DataRequired(), Email(), Length(min=1, max=100)])
    senha = PasswordField('Senha', validators=[DataRequired()])
    receber_emails = BooleanField('Desejo receber e-mails de novidades')

class FormularioPesquisa(FlaskForm):
    pesquisa = StringField('URL ou Texto de Busca', validators=[DataRequired(), Length(min=1, max=255)])
    baixar_video = RadioField('Baixar Vídeo', choices=[(1, 'Baixar Vídeo'), (2, 'Baixar Áudio')], default=1)