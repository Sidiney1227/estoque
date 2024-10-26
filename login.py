from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from werkzeug.security import check_password_hash, generate_password_hash
from conexao import conectar_banco  # Importa a função que conecta ao banco

app = Flask(__name__)

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    conexao = conectar_banco()
    cursor = conexao.cursor(dictionary=True)

    # Consulta o usuário no banco de dados
    query = "SELECT * FROM usuarios WHERE username = %s"
    cursor.execute(query, (username,))
    user = cursor.fetchone()

#Verifica se o usuario foi encontrado
    if not user:
        cursor.close()
        conexao.close()
        return 'Usuário não encontrado.'
    
#Verifica se o hash da senha é igual ao do banco de dados, caso não seja redireciona a pagina de login novamente
    if not check_password_hash(user['password'], password):
        cursor.close()
        conexao.close()
        #return 'Senha incorreta.'
        return redirect(url_for('login_page'))

    cursor.close()
    conexao.close()

    # Redireciona para a página inicial
    return redirect(url_for('index'))

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro_page():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conexao = conectar_banco()
        cursor = conexao.cursor()

        # Verifica se o usuário já existe
        query = "SELECT * FROM usuarios WHERE username = %s"
        cursor.execute(query, (username,))
        user = cursor.fetchone()

        if user:
            cursor.close()
            conexao.close()
            return 'Usuário já existe. Faça login.'

        # Insere o novo usuário com senha hash
        senha_hash = generate_password_hash(password)
        query = "INSERT INTO usuarios (username, password) VALUES (%s, %s)"
        cursor.execute(query, (username, senha_hash))
        conexao.commit()

        cursor.close()
        conexao.close()

        return redirect(url_for('login_page'))

    return render_template('cadastro.html')

@app.route('/logout')
def logout():
    return redirect(url_for('login_page'))

