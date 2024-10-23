import sqlite3

class SelecionadorDadosSQLite:
    def __init__(self, nome_banco):
        self.nome_banco = nome_banco

    def selecionar_dados(self):
        conexao = sqlite3.connect(self.nome_banco)
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM usuarios")
        dados = cursor.fetchall()
        conexao.close()
        return dados

selecionador_dados = SelecionadorDadosSQLite('banco_dados.db')
dados = selecionador_dados.selecionar_dados()
print("Dados da tabela:", dados)
