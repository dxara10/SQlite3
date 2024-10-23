import sqlite3

class AtualizadorDadosSQLite:
    def __init__(self, nome_banco):
        self.nome_banco = nome_banco

    def atualizar_dados(self, id, novo_nome):
        conexao = sqlite3.connect(self.nome_banco)
        cursor = conexao.cursor()
        cursor.execute("UPDATE usuarios SET nome = ? WHERE id = ?", (novo_nome, id))
        conexao.commit()
        conexao.close()

atualizador_dados = AtualizadorDadosSQLite('banco_dados.db')
atualizador_dados.atualizar_dados(1, 'Bob')
