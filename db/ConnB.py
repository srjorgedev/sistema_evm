import mysql.connector
from mysql.connector import Error


class Conn:

    def __init__(self):
        try:
            self.cnx = mysql.connector.connect(host="localhost",
                                               port=3306,
                                               user="root",
                                               password="root",
                                               db="evm")
        except Error as error:
            print("   Ha ocurrido un error al hacer la conexion.")
            print(error)

    def lista(self, comando):
        if self.cnx.is_connected():
            try:
                cursor = self.cnx.cursor()
                cursor.execute(comando)

                res = cursor.fetchall()

                return res
            except Error as valError:
                print("   Error: ")
                print(valError)

        return 0

    def registrar(self, query):
        lastid = 0
        if self.cnx.is_connected():
            try:
                cursor = self.cnx.cursor()
                cursor.execute(query)
                self.cnx.commit()

                lastid = cursor.lastrowid
            except Error as valError:
                print("   Error en conexion")
                lastid = -1
                print(valError)

        return lastid

    def actualizar(self, query):
        rowcount = 0
        if self.cnx.is_connected():
            try:
                cursor = self.cnx.cursor()
                cursor.execute(query)
                self.cnx.commit()

                rowcount = cursor.rowcount
            except Error as valError:
                print("   Error en conexion")
                rowcount = -1
                print(valError)

        return rowcount
