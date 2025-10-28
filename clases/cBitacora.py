from datetime import datetime

class Registro: 
    # Clase Registro
    # Su proposito es ser utilizada como un registro de 
    # Entrada y Salida
    
    def __init__(self):
        self.__fecha = datetime.now().strftime("%d/%m/%Y").date
        self.__hora = datetime.now().strftime("%h:%m:%s").time
        self.__kilometraje = ""
        self.__gasolima = ""
        
    def set_fecha(self, fecha):
        self.__fecha = datetime.strftime(fecha, "%d/%m/%Y")
        
    def set_hora(self, hora):
        self.__hora = datetime.strftime(hora, "%h:%m:%s")

    def set_kilometraje(self, kilometraje):
        self.__kilometraje = kilometraje
        
    def set_gasolima(self, gasolina):
        self.__gasolima = gasolina
        
    def get_fecha(self):
        return self.__fecha
    
    def get_hora(self):
        return self.__hora
    
    def get_kilometraje(self):
        return self.__kilometraje
    
    def get_hora(self):
        return self.__gasolima 

class Bitacora:
    # Clase Bitacora
    
    def __init__(self):
        self.__asunto = ""
        self.__destino = ""
        self.__usuario = ""
        self.__autorizador = ""
        self.__salida = Registro()
        self.__entrada = Registro()
        self.__kilometrajeTotal = ""
        self.__gasolinaRendimiento = ""
        
    def set_asunto(self, asunto):
        self.__asunto = asunto
        
    def set_destino(self, destino):
        self.__destino = destino
        
    def set_usuario(self, usuario):
        self.__usuario = usuario
    
    def set_autorizador(self, autorizador):
        self.__autorizador = autorizador
        
    def set_kilometrajeTotal(self, kilometraje):
        self.__kilometrajeTotal = kilometraje
    
    def set_gasolinaRendimiento(self, gasolina):
        self.__gasolinaRendimiento = gasolina
        
    def get_asunto(self):
        return self.__asunto
    
    def get_destino(self):
        return self.__destino
    
    def get_usuario(self):
        return self.__usuario
    
    def get_autorizador(self):
        return self.__autorizador
    
    def get_salida(self):
        return self.__salida
    
    def get_entrada(self):
        return self.__entrada
    
    def get_kilometrajeTotal(self):
        return self.__kilometrajeTotal
    
    def get_gasolinaRendimiento(self):
        return self.__gasolinaRendimiento   