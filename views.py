from flask import render_template, request, redirect, url_for
from conexao import conectar_banco

# Página inicial mostrando produtos
def index():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM produtos;')
    produtos = cursor.fetchall()
    cursor.close()
    conexao.close()
    return render_template('index.html', produtos=produtos)

# Inserir um novo produto
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

# Deletar um produto por ID
def deletar(id):
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('DELETE FROM produtos WHERE id = %s', (id,))
    conexao.commit()
    cursor.close()
    conexao.close()
    return redirect(url_for('index'))

