# conn.py
import mysql.connector
from mysql.connector import Error

class conn:
    def __init__(self):
        self.conexion = None
        try:
            self.conexion = mysql.connector.connect(
                host="localhost",
                port=3306,
                user="root",
                password="",
                database="evm_db")
            print("Conectado a Enterprise Vehicle Manager")
        except Error as variable:
            print("Error en conexion")
            print(variable)
            
    def lista(self, comando):
        if self.conexion and self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute(comando)
                reultados = cursor.fetchall()
                # print("Listado correcto")
                return reultados
            except Error as valError:
                print("Error al listar:")
                print(valError)
        return 0
    
    def registrar(self, comando):
        if self.conexion and self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute(comando)
                self.conexion.commit()
                print("Registrado correctamente")
                return cursor.rowcount
            except Error as valError:
                print("Error en el registro:")
                print(valError)
        return -1
                
    def actualizar(self, comando):
        contador = -1
        if self.conexion and self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute(comando)
                self.conexion.commit()
                contador = cursor.rowcount
            except Error as valError:
                print("Error en conexión o actualización:")
                print(valError)
                contador = -1
            
            return contador
        return contador