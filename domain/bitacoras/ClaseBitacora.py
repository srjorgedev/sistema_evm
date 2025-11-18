from datetime import datetime

class Registro:
    # Clase Registro
    # Su proposito es ser utilizada como un registro de
    # Entrada y Salida

    def __init__(self):
        self.__fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.__hora = datetime.now().strftime("%H:%M:%S")
        self.__kilometraje = ""
        self.__gasolina = ""

    def set_fecha(self, fecha):
        self.__fecha = datetime.strftime(fecha, "%Y-%m-%d")

    def set_hora(self, hora):
        self.__hora = datetime.strftime(hora, "%H:%M:%S")

    def set_kilometraje(self, kilometraje):
        self.__kilometraje = kilometraje

    def set_gasolina(self, gasolina):
        self.__gasolina = gasolina

    def get_fecha(self):
        return self.__fecha

    def get_hora(self):
        return self.__hora

    def get_kilometraje(self):
        return self.__kilometraje

    def get_gasolina(self):
        return self.__gasolina

    def __str__(self):
        return f"""
- Fecha: {self.__fecha} \tHora: {self.__hora}
- Kilometraje: {self.__kilometraje} \tGasolina: {self.__gasolina}
"""


class Bitacora:
    # Clase Bitacora

    def __init__(self):
        self.__numControl = 0
        self.__asunto = "Sin registrar"
        self.__destino = "Sin registrar"
        self.__responsable = 1
        self.__autorizador = 10
        self.__vehiculo = "1G4AL5E85SZ100001"
        self.__salida = "Sin registrar"
        self.__entrada = "Sin registrar"
        self.__kilometrajeTotal = "Sin registrar"
        self.__gasolinaConsumida =  "Sin registrar"
        self.__gasolinaRendimiento = "Sin registrar"
        self.__salidaBool = ""
        self.__entradaBool = ""

    def registrar_salida(self, kilometraje, gasolina):
        self.__salida = Registro()
        self.__salida.set_kilometraje(kilometraje)
        self.__salida.set_gasolina(gasolina)

    def registrar_entrada(self, kilometraje, gasolina):
        self.__entrada = Registro()
        self.__entrada.set_kilometraje(kilometraje)
        self.__entrada.set_gasolina(gasolina)

    def set_numControl(self, numControl):
        self.__numControl = numControl

    def set_asunto(self, asunto):
        self.__asunto = asunto

    def set_destino(self, destino):
        self.__destino = destino

    def set_responsable(self, usuario):
        self.__responsable = usuario

    def set_autorizador(self, autorizador):
        self.__autorizador = autorizador
        
    def set_gasolinaConsumida(self, gasolinaConsumida):
        self.__gasolinaConsumida = gasolinaConsumida

    def set_gasolinaRendimiento(self, gasolinaRendimiento):
        self.__gasolinaRendimiento = gasolinaRendimiento
        
    def set_kilometrajeTotal(self, kilometrajeTotal):
        self.__kilometrajeTotal = kilometrajeTotal

    def set_vehiculo(self, vehiculo):
        self.__vehiculo = vehiculo
        
    def set_entradaBool(self, entradaBool):
        self.__entradaBool = entradaBool
        
    def set_salidaBool(self, salidaBool):
        self.__salidaBool = salidaBool

    def get_numControl(self):
        return self.__numControl

    def get_vehiculo(self):
        return self.__vehiculo

    def get_asunto(self):
        return self.__asunto

    def get_destino(self):
        return self.__destino

    def get_responsable(self):
        return self.__responsable

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
    
    def get_gasolinaConsumida(self):
        return self.__gasolinaConsumida
    
    def get_entradaBool(self):
        return self.__entradaBool
    
    def get_salidaBool(self):
        return self.__salidaBool
    
    def calcular_gasolinaConsumida(self):
        self.set_gasolinaConsumida(self.__salida.get_gasolina() - self.__entrada.get_gasolina())

    def calcular_kilometrajeTotal(self):
        self.set_kilometrajeTotal(self.__entrada.get_kilometraje() - self.__salida.get_kilometraje())

    def calcular_gasolinaRendimiento(self):
        self.set_gasolinaRendimiento(self.__gasolinaConsumida / self.__kilometrajeTotal)

    def __str__(self):
        return f"""
Numero de control: {self.__numControl}
Asunto: {self.__asunto} Destino: {self.__destino} Responsable: {self.__responsable} Autorizador: {self.__autorizador}
Vehiculo: {self.__vehiculo}
Salida: {str(self.__salida)}
Entrada: {str(self.__entrada)}
Kilometraje Total: {self.__kilometrajeTotal}
Gasolina Rendimiento: {self.__gasolinaRendimiento}  
"""
