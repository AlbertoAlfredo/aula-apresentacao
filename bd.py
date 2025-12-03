import sqlite3

conn = sqlite3.connect("banco.db", check_same_thread=False)

cursor = conn.cursor()
cursor.execute(
    """
    PRAGMA foreign_keys = ON   
    """
)
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS setores(
            id INTEGER PRIMARY KEY,
            nome TEXT NOT NULL 
        )
    """
)
cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS patrimonios (
            id INTEGER PRIMARY KEY,
            nome TEXT,
            patrimonio INTEGER,
            
            id_setor INTEGER NOT NULL,
            FOREIGN KEY (id_setor) REFERENCES setores(id)
            ON DELETE RESTRICT
            ON UPDATE CASCADE
            
        )
        """
    )

class Setor():
    @staticmethod
    def create(nome:str):
        cursor.execute(
        f"""
        INSERT INTO setores ( nome )
        VALUES ('{nome}');
        """
        )
        
        conn.commit()
        return
    @staticmethod
    def read(id = False):
        if id:
            cursor.execute(
                f"""
                    SELECT * FROM setores WHERE id = '{id}';
                """
            )
            rows = cursor.fetchall()
            return rows
        else:
            cursor.execute(
                f"""
                    SELECT * FROM setores;
                """
            )
            rows = cursor.fetchall()
            return rows
        
    @staticmethod
    def update(id:int, nome:str):
        cursor.execute(
            f"""
                UPDATE setores
                SET nome = '{nome}'
                WHERE id = {id};
            """
        )
        return
    @staticmethod
    def delete(id:int):
        try:
            cursor.execute(
                f"""
                DELETE FROM setores
                WHERE id = {id} 
                """
            )
            conn.commit()
            return True # Sucesso na exclusão
            
        except Exception as e:
            # Trata qualquer erro inesperado (ex: ID não existe)
            conn.rollback()
            print(f"Erro inesperado ao deletar setor: {e}")
            return False





class Patrimonio():
    @staticmethod
    def create(nome:str, patrimonio:int, id_setor:int):
        cursor.execute(
        f"""
        INSERT INTO patrimonios ( nome, patrimonio, id_setor)
        VALUES ('{nome}', '{patrimonio}', '{id_setor}');
        """
        )
        
        conn.commit()
        return
    
    @staticmethod
    def read(id = False):
        if id:
            cursor.execute(
                f"""
                    SELECT * FROM patrimonios WHERE id = '{id}';
                """
            )
            rows = cursor.fetchall()
            return rows
        else:
            cursor.execute(
                f"""
                    SELECT * FROM patrimonios;
                """
            )
            rows = cursor.fetchall()
            return rows
        
    @staticmethod
    def update(id:int, nome:str, patrimonio:int, id_setor:int):
        cursor.execute(
            f"""
                UPDATE patrimonios
                SET nome = '{nome}', patrimonio = {patrimonio}, id_setor = '{id_setor}' 
                WHERE id = {id};
            """
        )
        return
    @staticmethod
    def delete(id:int):
        cursor.execute(
            f"""
            DELETE FROM patrimonios
            WHERE id = {id} 
            """
        )
        return



