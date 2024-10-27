from flask import Flask
from mysql.connector import connect
from conexao import conectar_banco  #Importa a função que conecta ao banco

app = Flask(__name__)

# Importa as rotas dos arquivos login e views
from login import login_page, login, cadastro_page, logout
from views import index, inserir, deletar, formulario_movimentacao, registrar_movimentacao, listar_historico

# Registrar as rotas no app
app.add_url_rule('/', 'login_page', login_page)
app.add_url_rule('/login', 'login', login, methods=['POST'])
app.add_url_rule('/cadastro', 'cadastro_page', cadastro_page, methods=['GET', 'POST'])
app.add_url_rule('/logout', 'logout')
app.add_url_rule('/index', 'index', index)
app.add_url_rule('/inserir', 'inserir', inserir, methods=['POST'])
app.add_url_rule('/deletar/<int:id>', 'deletar', deletar)
app.add_url_rule('/movimentacao', 'formulario_movimentacao', formulario_movimentacao, methods=['GET'])
app.add_url_rule('/registrar_movimentacao', 'registrar_movimentacao', registrar_movimentacao, methods=['POST'])
app.add_url_rule('/historico', 'listar_historico', listar_historico) 

if __name__ == '__main__':
    app.run(debug=True)
