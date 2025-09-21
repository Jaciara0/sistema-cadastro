import sqlite3 as lite
from datetime import datetime

# Criando a conexão com o banco de dados
con = lite.connect('banco.db')

# Inserindo dados na tabela "inventario"
def inserir_form(i):
    with con:
        cur = con.cursor()
        query = """
            INSERT INTO inventario (
                nome, local, descricao, marca, data_daquisicao, 
                valor_da_compra, serie, imagem, quantidade
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        cur.execute(query, i)
        
# Deletar dados da tabela "inventario"
def deletar_form(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM inventario WHERE id = ?"
        cur.execute(query, i)
        
# Atualizar dados na tabela "inventario"
def atualizar_form(i):
    with con:
        cur = con.cursor()
        query = """
            UPDATE inventario 
            SET nome = ?, local = ?, descricao = ?, marca = ?, 
                data_daquisicao = ?, valor_da_compra = ?, 
                serie = ?, imagem = ?, quantidade = ? 
            WHERE id = ?
        """
        cur.execute(query, i)
        
# Ver todos os itens no inventário
def ver_form():
    lista_itens = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Inventario")
        rows = cur.fetchall()
        for row in rows:
            lista_itens.append(row)
    return lista_itens

# Ver um item específico no inventário
def ver_item(id):
    list_item = []
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Inventario WHERE id = ?", (id,))
        rows = cur.fetchall()
        for row in rows:
            list_item.append(row)
    return list_item