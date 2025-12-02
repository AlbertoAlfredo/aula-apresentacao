import sqlite3

conn = sqlite3.connect("banco.db")

cursor = conn.cursor()

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        preco INTEGER,
        detalhes TEXT
    )
    """
)

def preco_para_banco(prec):
    preco = int(prec * 100 )
    return preco

def preco_para_soft(prec):
    preco = float(prec)/100
    return preco




def create(nome, preco, detalhes):
    cursor.execute(
    f"""
    INSERT INTO produtos ( nome, preco, detalhes)
    VALUES ('{nome}', '{preco_para_banco(preco)}', '{detalhes}');
    """
    )
    conn.commit()
    return

def read(id = False):
    if id:
        cursor.execute(
            f"""
                SELECT * FROM produtos WHERE id = '{id}';
            """
        )
        rows = cursor.fetchall()
        return rows
    else:
        cursor.execute(
            f"""
                SELECT * FROM produtos;
            """
        )
        rows = cursor.fetchall()
        return rows
    

def update(id, nome, preco, detalhes):
    cursor.execute(
        f"""
            UPDATE produtos
            SET nome = '{nome}', preco = {preco_para_banco(preco)}, detalhes = '{detalhes}' 
            WHERE id = {id};
        """
    )
    return

def delete(id):
    cursor.execute(
        f"""
           DELETE FROM produtos
           WHERE id = {id} 
        """
    )
    return