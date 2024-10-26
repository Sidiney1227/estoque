from flask import Flask
from mysql.connector import connect

app = Flask(__name__)

# Função para conectar ao banco de dados
def conectar_banco():
    return connect(
        host='localhost',
        user='root',
        password='',
        database='loja'
    )