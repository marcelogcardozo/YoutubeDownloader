from flask import render_template, request, redirect, url_for, session, send_file
from utils.helpers import FormularioLogin, FormularioCadastro, FormularioPesquisa
from utils.models import Usuario, InformacoesAdicionais, HistoricoPesquisa
from pytube import YouTube
from app import app, db
from io import BytesIO

@app.route('/')
def home():

    if 'usuario_logado' in session and session['usuario_logado'] != None:
        user = Usuario.query.filter_by(email=session['usuario_logado']).first()
        nome = InformacoesAdicionais.query.filter_by(id_usuario=user.id).order_by(InformacoesAdicionais.data_alteracao.desc()).first().nome
        usuario = {'nome': nome, 'status': 'logout'}
    else:
        usuario = {'nome' : 'Visitante', 'status' : 'login'}

    form = FormularioPesquisa()
    return render_template('home.html', titulo='Ytb Downloader', usuario=usuario, form=form)

@app.route('/login')
def login():
    form = FormularioLogin()
    mensagem = '' if 'mensagem' not in request.args else request.args['mensagem']
    return render_template('login.html', titulo='Login', mensagem=mensagem, form=form)

@app.route('/autenticar', methods=['POST'])
def autenticar():

    form = FormularioLogin(request.form)

    if not form.validate_on_submit():
        return redirect(url_for('login', mensagem='E-mail e/ou senha inválido(s)!', form=form))

    usuario_input = form.email.data
    senha_input = form.senha.data
    
    usuario = Usuario.query.filter_by(email=usuario_input, senha=senha_input).first()

    if usuario is None:
        return redirect(url_for('login', mensagem='E-mail e/ou senha inválido(s)!', form=form))
    
    session['usuario_logado'] = usuario.email
    return redirect(url_for('home'))
       
@app.route('/cadastro')
def cadastro():
    form = FormularioCadastro()
    mensagem = '' if 'mensagem' not in request.args else request.args['mensagem']
    return render_template('cadastro.html', titulo='Cadastro', mensagem=mensagem, form=form)

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    form = FormularioCadastro(request.form)

    if not form.validate_on_submit():
        return redirect(url_for('cadastro', mensagem='Dados inválidos!', form=form))

    usuario_input = form.email.data
    senha_input = form.senha.data
    nome_input = form.nome.data
    sobrenome_input = form.sobrenome.data
    foto_url_input = ''

    usuario = Usuario.query.filter_by(email=usuario_input).first()

    if usuario is not None:
        return redirect(url_for('cadastro', mensagem='E-mail já cadastrado!', form=form))

    usuario = Usuario(email=usuario_input, senha=senha_input)
    db.session.add(usuario)
    user_id = Usuario.query.filter_by(email=usuario_input).first().id
    informacoes_adicionais = InformacoesAdicionais(id_usuario=user_id, nome=nome_input, sobrenome=sobrenome_input, foto_url=foto_url_input)
    
    db.session.add(informacoes_adicionais)
    db.session.commit()

    return redirect(url_for('login', mensagem='Cadastro realizado com sucesso!'))

@app.route('/download', methods=['POST'])
def download():

    if 'usuario_logado' not in session:
        return redirect(url_for('login', mensagem='Faça login para continuar!'))

    form = FormularioPesquisa(request.form)

    if not form.validate_on_submit():
        return redirect(url_for('home'))

    buffer = BytesIO()

    string_pesquisa = form.pesquisa.data
    #audio_video = form.baixar_video.data
    audio_video = '1'

    usuario = Usuario.query.filter_by(email=session['usuario_logado']).first()
    historico = HistoricoPesquisa(id_usuario=usuario.id, string_pesquisa=string_pesquisa)

    db.session.add(historico)
    db.session.commit()

    ytb = YouTube(string_pesquisa)

    if str(audio_video) == '1':
        midia = ytb.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()[0]
        extension = '.mp4'
    else:
        midia = ytb.streams.filter(only_audio=True).first()
        extension = '.mp3'

    midia.stream_to_buffer(buffer)
    buffer.seek(0)
    return send_file(buffer, as_attachment=True, download_name=midia.title + extension)
    
@app.route('/logout')
def logout():
    if 'usuario_logado' in session:
        del session['usuario_logado']
        return redirect(url_for('home'))
    else:
        return redirect(url_for('login'))