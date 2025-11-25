class Usuario:
    def __init__(self, numEmpleado, nombrePila, apdPaterno, apdMaterno, tipo_empleado, activo, password, email):
        self.__numEmpleado = numEmpleado
        self.__nombrePila = nombrePila
        self.__apdPaterno = apdPaterno
        self.__apdMaterno = apdMaterno
        self.__tipo_empleado = tipo_empleado
        self.__activo = activo
        self.__password = password
        self.__email = email

    def __str__(self):
        return f" Numero de Empleado: {self.__numEmpleado}\n Nombre: {self.__nombrePila} {self.__apdPaterno} {self.__apdMaterno}\n Tipo de Empleado: {self.__tipo_empleado} "

    def get_numEmpleado(self):
        return self.__numEmpleado

    def set_numEmpleado(self, numEmpleado):
        self.__numEmpleado = numEmpleado

    def get_nombrePila(self):
        return self.__nombrePila
    def set_nombrePila(self, nombrePila):
        self.__nombrePila = nombrePila
        
    def get_tipo_empleado(self):
        return self.__tipo_empleado

    def set_tipo_empleado(self, tipo_empleado):
        self.__tipo_empleado = tipo_empleado

    def get_activo(self):
        return self.__activo

    def set_activo(self, activo):
        self.__activo = activo
        
    def get_password(self):
        return self.__password
    
    def set_password(self, password):
        self.__password = password
        
    def get_email(self):
        return self.__email
    
    def set_email(self, email):
        self.__email = email
        
    def get_nombrePila(self):
        return self.__nombrePila
    def set_nombrePila(self, nombrePila):
        self.__nombrePila = nombrePila
    
    def get_apdPaterno(self):
        return self.__apdPaterno
    def set_apdPaterno(self, apdPaterno):
        self.__apdPaterno = apdPaterno
    
    def get_apdMaterno(self):
        return self.__apdMaterno
    def set_apdMaterno(self, apdMaterno):
        self.__apdMaterno = apdMaterno

class Telefono:
    def __init__(self, num, numTelefono, empleado):
        self.__num = num
        self.__numTelefono = numTelefono
        self.__empleado = empleado

    def get_num(self):
        return self.__num

    def set_num(self, num):
        self.__num = num

    def get_empleado(self):
        return self.__empleado

    def set_empleado(self, empleado):
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

    def set_empleado(self, empleado):
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


class TipoLicencia:
    def __init__(self, numeroLic, codigoLic, descripcionLic):
        self.__numeroLic = numeroLic
        self.__codigoLic = codigoLic
        self.__descripcionLic = descripcionLic

    def get_codigoLic(self):
        return self.__codigoLic

    def set_codigoLic(self, codigoLic):
        self.__codigoLic = codigoLic
        
    def get_numeroLic(self):
        return self.__numeroLic

    def set_numeroLic(self, numeroLic):
        self.__numeroLic = numeroLic
        
    def get_descripcionLic(self):
        return self.__descripcionLic

    def set_descripcionLic(self, descripcionLic):
        self.__descripcionLic = descripcionLic
