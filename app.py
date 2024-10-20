from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Função de conexão com o banco
def conectar_banco():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='loja',
    )
"""
# Rota para o arquivo index
@app.route('/index')
def index():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM produtos')
    produtos = cursor.fetchall()
    cursor.close()
    conexao.close()
    return render_template('index.html', produtos=produtos)

@app.route('/inserir', methods=['POST'])
def inserir():
    nome = request.form['nome']
    preco = float(request.form['preco'])
    estoque = int(request.form['estoque'])
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('INSERT INTO produtos (nome, preco, estoque) VALUES (%s, %s, %s)', (nome, preco, estoque))
    conexao.commit()
    cursor.close()
    conexao.close()

    return redirect(url_for('index'))

@app.route('/deletar/<int:id>')
def deletar(id):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('DELETE FROM produtos WHERE id = %s', (id,))
    conexao.commit()
    cursor.close()
    conexao.close()

    return redirect(url_for('index'))"""

if __name__ == '__main__':
    app.run(debug=True)  #Debug automático