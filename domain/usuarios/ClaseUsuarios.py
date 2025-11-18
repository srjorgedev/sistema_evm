class Usuario:
    def __init__(self, numEmpleado, nombre, tipo_empleado, activo):
        self.__numEmpleado = numEmpleado
        self.__tipo_empleado = tipo_empleado
        self.__nombre = nombre
        self.__activo = activo

    def __str__(self):
        return f" Numero de Empleado: {self.__numEmpleado}\n Nombre: {self.__nombre}\n  "

    def get_numEmpleado(self):
        return self.__numEmpleado

    def set_numEmpleado(self, numEmpleado):
        self.__numEmpleado = numEmpleado
        
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_tipo_empleado(self):
        return self.__tipo_empleado

    def set_tipo_empleado(self, tipo_empleado):
        self.__tipo_empleado = tipo_empleado

    def get_activo(self):
        return self.__activo

    def set_activo(self, activo):
        self.__activo = activo

class Telefono:
    def __init__(self, num, numTelefono, empleado):
        self.__num = num
        self.__numTelefono = numTelefono
        self.__empleado = empleado

    def get_num(self):
        return self.__num

    def set_(self, num):
        self.__num = num

    def get_empleado(self):
        return self.__empleado

    def set_(self, empleado):
        self.__empleado = empleado

    def get_numTelefono(self):
        return self.__numTelefono

    def set_numTelefono(self, numTelefono):
        self.__numTelefono = numTelefono

class Licencia:
    def __init__(self, num, fechaExpedicion, fechaVencimiento, empleado, tipoLicencia):
        self.__num = num
        self.__fechaExpedicion = fechaExpedicion
        self.__fechaVencimiento = fechaVencimiento
        self.__empleado = empleado
        self.__tipoLicencia = tipoLicencia

    def get_num(self):
        return self.__num

    def set_num(self, num):
        self.__num = num

    def get_fechaExpedicion(self):
        return self.__fechaExpedicion

    def set_fechaExpedicion(self, fechaExpedicion):
        self.__fechaExpedicion = fechaExpedicion

    def get_fechaVencimiento(self):
        return self.__fechaVencimiento

    def set_fechaVencimiento(self, fechaVencimiento):
        fechaVencimiento = fechaVencimiento

    def get_empleado(self):
        return self.__empleado

    def set_(self, empleado):
        self.__empleado = empleado

    def get_tipoLicencia(self):
        return self.__tipoLicencia

    def set_tipoLicencia(self, tipoLicencia):
        self.__tipoLicencia = tipoLicencia

class TipoEmpleado:
    def __init__(self, codigo, descripcion):
        self.__codigo = codigo
        self.__descripcion = descripcion

    def get_codigo(self):
        return self.__codigo

    def set_codigo(self, codigo):
        self.__codigo = codigo

    def get_descripcion(self):
        return self.__descripcion

    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion