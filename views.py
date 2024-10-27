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

# Rota para exibir o formulário de movimentação
def formulario_movimentacao():
    return render_template('movimentacao.html')

# Rota para processar o formulário e registrar a movimentação
def registrar_movimentacao():
    tipo_movimentacao = request.form['tipo_movimentacao']
    id_produto = request.form['id_produto']
    quantidade = int(request.form['quantidade'])
    valor_unitario = float(request.form['valor_unitario'])
    responsavel = request.form['responsavel']
    observacoes = request.form.get('observacoes', '')

    # Conexão com o banco de dados
    conexao = conectar_banco()
    cursor = conexao.cursor()

    # Inserindo a movimentação na tabela movimentacoes_estoque
    query = """
    INSERT INTO movimentacoes_estoque 
    (tipo_movimentacao, id_produto, quantidade, valor_unitario, responsavel, observacoes)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    valores = (tipo_movimentacao, id_produto, quantidade, valor_unitario, responsavel, observacoes)

    cursor.execute(query, valores)

    # Atualizar a quantidade na tabela produtos
    if tipo_movimentacao == 'entrada':
        cursor.execute("UPDATE produtos SET estoque = estoque + %s WHERE id = %s", (quantidade, id_produto))
    elif tipo_movimentacao == 'saida':
        cursor.execute("UPDATE produtos SET estoque = estoque - %s WHERE id = %s", (quantidade, id_produto))

    conexao.commit()

    cursor.close()
    conexao.close()

    return redirect(url_for('formulario_movimentacao'))

# Função para listar as movimentações
def listar_historico():
    # Conectar ao banco de dados
    conexao = conectar_banco()
    cursor = conexao.cursor()

    # Executar a consulta
    cursor.execute("SELECT * FROM movimentacoes_estoque")
    historico = cursor.fetchall()

    # Fechar a conexão
    cursor.close()
    conexao.close()

    # Renderizar o template com o histórico
    return render_template('historico.html', historico=historico)
