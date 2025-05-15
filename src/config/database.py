import sqlite3
from pathlib import Path
import os

class Database:
    def __init__(self, path_db):
        self.__conn = sqlite3.connect(path_db, check_same_thread=False)
        self.__conn.row_factory = sqlite3.Row
        self.__cursor = self.__conn.cursor()
    
    def create_table_data(self):
        table = f"""
        CREATE TABLE IF NOT EXISTS datos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT,
            categoria TEXT,
            pago TEXT,
            monto INTEGER
        )
        """
        self.__cursor.execute(table)
    
    def create_table_totales(self):
        table = """
        CREATE TABLE IF NOT EXISTS totales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT,
            total INTEGER,
            total_efectivo INTEGER,
            total_virtual INTEGER
        )
        """
        self.__cursor.execute(table)
    
    def add_data(self, data: dict):
        add_data = """
        INSERT INTO datos (fecha, categoria, pago, monto) VALUES (?,?,?,?)
        """
        value = (
            data['fecha'],
            data['categoria'],
            data['pago'],
            data['monto'],
        )
        self.__cursor.execute(add_data, value)
        self.__conn.commit()

    def get_all_data(self):
        query = """
        SELECT * FROM datos
        """
        row = self.__cursor.execute(query)
        return [dict(item) for item in row.fetchall()]

    def sum_mont_data(self):
        query = """
        SELECT SUM(monto) as total FROM datos
        """
        row = self.__cursor.execute(query)
        return [dict(row.fetchone())]
    
    def sum_total_tranfer(self):
        query = """
        SELECT SUM(monto) as total_tranfer FROM datos WHERE pago = 'Transferencia'
        """
        row = self.__cursor.execute(query)
        return [dict(row.fetchone())]

    def sum_total_cash(self):
        query = """
        SELECT SUM(monto) as total_efectivo FROM datos WHERE pago = 'Efectivo'
        """
        row = self.__cursor.execute(query)
        return [dict(row.fetchone())]
    
    def update_data(self, new_data: dict, id: int):
        add_new_data = """
        UPDATE datos SET categoria = ?,
        pago = ?, monto = ? WHERE id = ?
        """
        values = (
            new_data['categoria'],
            new_data['pago'],
            new_data['monto'],
            id,
        )
        self.__cursor.execute(add_new_data, values)
        self.__conn.commit()
    
    def get_data_for_id(self, id: int):
        query = """
        SELECT * FROM datos WHERE id = ?
        """
        row = self.__cursor.execute(query, (id,))
        return [dict(row.fetchone())]
    
    def delete_data(self, id: int):
        delete = """
        DELETE FROM datos WHERE id = ?
        """
        self.__cursor.execute(delete, (id,))
    
    def save_day_sales(self, data: dict):
        insert = """
        INSERT INTO totales (fecha, total, total_efectivo, total_virtual) VALUES (?,?,?,?)
        """
        values =(
            data['fecha'],
            data['total'],
            data['efectivo'],
            data['virtual'],
        )
        self.__cursor.execute(insert, values)
        self.__conn.commit()
    
    def get_totales(self):
        query = """
        SELECT * FROM totales
        """
        row = self.__cursor.execute(query)
        return [dict(item) for item in row.fetchall()]

    def delete_all_data(self):
        delete = """
        DELETE FROM datos
        """
        self.__cursor.execute(delete)
        self.__conn.commit()

    
    def close(self):
        self.__conn.close()


        

create_path = Path(os.getenv('APPDATA')) / 'gestor ventas'
create_path.mkdir(parents=True, exist_ok=True)

path = create_path / 'database.db'
db = Database(path_db=path)
db.create_table_data()
db.create_table_totales()