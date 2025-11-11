class Usuario:
    def __init__(self, nombre, telefono, tipoEmpleado, licencia, numeroLicencia, numEmpleado, activo):
        self.__nombre = nombre
        self.__telefono = telefono
        self.__tipoEmpleado = tipoEmpleado
        self.__licencia = licencia
        self.__numeroLicencia = numeroLicencia
        self.__numEmpleado = numEmpleado
        self.__activo = activo

    def __str__(self):
        return f" Nombre: {self.__nombre}\n Telefono: {self.__telefono}\n Tipo de Empleado: {self.__tipoEmpleado}\n Tipo de Licencia: {self.__licencia}\n Numero de Licencia: {self.__numeroLicencia}\n Numero de Empleado: {self.__numEmpleado} "

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_telefono(self):
        return self.__telefono

    def set_telefono(self, telefono):
        self.__telefono = telefono

    def get_tipoEmpleado(self):
        return self.__tipoEmpleado

    def set_tipoEmpleado(self, tipoEmpleado):
        self.__tipoEmpleado = tipoEmpleado

    def get_licencia(self):
        return self.__licencia

    def set_licencia(self, licencia):
        self.__licencia = licencia

    def get_numeroLicencia(self):
        return self.__numeroLicencia

    def set_numerolicencia(self, numeroLicencia):
        self.__numeroLicencia = numeroLicencia

    def get_numEmpleado(self):
        return self.__numEmpleado

    def set_numEmpleado(self, numEmpleado):
        self.__numEmpleado = numEmpleado
    
    def get_activo(self):
        return self.__activo

    def set_activo(self, activo):
        self.__activo = activo