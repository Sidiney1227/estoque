from flask import Flask
from mysql.connector import connect
from conexao import conectar_banco  # Importa a função que conecta ao banco

app = Flask(__name__)

# Importa as rotas de outros arquivos
from login import login_page, login, cadastro_page, logout
from views import index, inserir, deletar

# Registrar as rotas no app
app.add_url_rule('/', 'login_page', login_page)
app.add_url_rule('/login', 'login', login, methods=['POST'])
app.add_url_rule('/cadastro', 'cadastro_page', cadastro_page, methods=['GET', 'POST'])
app.add_url_rule('/logout', 'logout', logout)
app.add_url_rule('/index', 'index', index)
app.add_url_rule('/inserir', 'inserir', inserir, methods=['POST'])
app.add_url_rule('/deletar/<int:id>', 'deletar', deletar)

if __name__ == '__main__':
    app.run(debug=True)