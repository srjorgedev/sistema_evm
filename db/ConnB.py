import mysql.connector
from mysql.connector import Error

class Conn:
    def conectar(self):
        return mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="root",
            db="evm_db",
            use_pure=True
        )

    def lista(self, comando):
        try:
            cnx = self.conectar()
            cursor = cnx.cursor()
            cursor.execute(comando)
            res = cursor.fetchall()
            cursor.close()
            cnx.close()
            return res
        except Error as error:
            return -1, error

    def registrar(self, query) -> int:
        try:
            cnx = self.conectar()
            cursor = cnx.cursor()
            cursor.execute(query)
            cnx.commit()
            lastid = cursor.lastrowid
            cursor.close()
            cnx.close()
            return lastid
        except Error as error:
            print("Error:", error)
            return -1

    def actualizar(self, query):
        try:
            cnx = self.conectar()
            cursor = cnx.cursor()
            cursor.execute(query)
            cnx.commit()
            count = cursor.rowcount
            cursor.close()
            cnx.close()
            return count
        except Error as error:
            print("Error:", error)
            return -1
