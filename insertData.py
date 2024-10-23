import sqlite3

class InseridorDadosSQLite:
    def __init__(self, nome_banco):
        self.nome_banco = nome_banco

    def inserir_dados(self, nome, idade):
        conexao = sqlite3.connect(self.nome_banco)
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", (nome, idade))
        conexao.commit()
        conexao.close()

inseridor_dados = InseridorDadosSQLite('banco_dados.db')
inseridor_dados.inserir_dados('Alice', 30)
