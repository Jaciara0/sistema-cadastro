# Importando o SQLite3
import sqlite3 as lite 

# Conectando ao banco de dados (ou criando, caso não exista)
con = lite.connect('banco.db')


# Criando a tabela "inventario"
with con:
    cur = con.cursor()

# Remove a tabela se ela já existir
    cur.execute("DROP TABLE IF EXISTS inventario")
    
    # Cria a nova tabela com a estrutura atualizada
    cur.execute("""
        CREATE TABLE inventario (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            local TEXT,
            descricao TEXT,
            marca TEXT,
            data_daquisicao DATE,
            valor_da_compra DECIMAL,
            serie TEXT,
            imagem TEXT,
            quantidade INTEGER
        )
    """)

