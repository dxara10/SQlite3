import sqlite3

class ExcluidorDadosSQLite:
    def __init__(self, nome_banco):
        self.nome_banco = nome_banco

    def excluir_dados(self, id):
        conexao = sqlite3.connect(self.nome_banco)
        cursor = conexao.cursor()
        cursor.execute("DELETE FROM usuarios WHERE id = ?", (id,))
        conexao.commit()
        conexao.close()

excluidor_dados = ExcluidorDadosSQLite('banco_dados.db')
excluidor_dados.excluir_dados(1)
