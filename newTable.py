import sqlite3

class CriadorTabelaSQLite:
    def __init__(self, nome_banco):
        self.nome_banco = nome_banco

    def criar_tabela(self):
        conexao = sqlite3.connect(self.nome_banco)
        cursor = conexao.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios
                          (id INTEGER PRIMARY KEY, nome TEXT, idade INTEGER)''')
        conexao.commit()
        conexao.close()

criador_tabela = CriadorTabelaSQLite('banco_dados.db')
criador_tabela.criar_tabela()
