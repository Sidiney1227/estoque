import unittest
import mysql.connector
from conexao import conectar_banco  #Importa a função que conecta ao banco

class TestDatabaseConnection(unittest.TestCase):
    
    def test_conexao_banco(self):
        #Testa se a conexão com o banco de dados pode ser estabelecida. 
        try:
            conexao = conectar_banco()
            self.assertIsNotNone(conexao, "Falha ao conectar ao banco de dados.")
            conexao.close()
        except mysql.connector.Error as err:
            self.fail(f"Erro ao tentar conectar ao banco de dados: {err}")

if __name__ == '__main__':
    unittest.main()
#Retorna "OK" se a conexão for bem sucedida!