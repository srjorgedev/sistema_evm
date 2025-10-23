class Administrador:

    def __init__(self, nombre, number, password, numEmpleado):
        self.__nombre = nombre
        self.__number = number
        self.__password = password
        self.__numEmpleado = numEmpleado

    def __str__(self):
        return f" Nombre: {self.__nombre}\n Telefono: {self.__number}\n Numero de Empleado: {self.__numEmpleado} "
        
    def get_nombre(self):
        return self.__nombre
        
    def set_nombre(self, nombre):
        self.__nombre = nombre
        
    def get_number(self):
        return self.__number

    def set_number(self, number):
        self.__number = number
        
    def get_password(self):
        return self.__password
    
    def set_number(self, password):
        self.__password = password
    
    def get_numEmpleado(self):
        return self.__numEmpleado
    
    def get_number(self, numEmpleado):
        self.__numEmpleado = numEmpleado
        
    

class Chofer:
    def __init__(self, nombre, number, password, licencia, numeroLicencia, numEmpleado):
        self.__nombre = nombre
        self.__number = number
        self.__password = password
        self.__licencia = licencia
        self.__numeroLicencia = numeroLicencia
        self.__numEmpleado = numEmpleado

    def __str__(self):
        return f" Nombre: {self.__nombre}\n Telefono: {self.__number}\n Tipo de Licencia: {self.__licencia}\n Numero de Licencia: {self.__numeroLicencia}\n Numero de Empleado: {self.__numEmpleado} "

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_number(self):
        return self.__number

    def set_number(self, number):
        self.__number = number

    def get_password(self):
        return self.__password
    
    def set_number(self, password):
        self.__password = password
        
    def get_licencia(self):
        return self.__licencia
    
    def get_licencia(self, licencia):
        self.__licencia = licencia
        
    def get_numeroLicencia(self):
        return self.__numeroLicencia
    
    def get_licencia(self, numeroLicencia):
        self.__numeroLicencia = numeroLicencia
    
    def get_numEmpleado(self):
        return self.__numEmpleado
    
    def get_number(self, numEmpleado):
        self.__numEmpleado = numEmpleado

class Vigilante:
    def __init__(self, nombre, number, password, numEmpleado):
        self.__nombre = nombre
        self.__number = number
        self.__password = password
        self.__numEmpleado = numEmpleado

    def __str__(self):
        return f" Nombre: {self.__nombre}\n Telefono: {self.__number}\n Numero de Empleado: {self.__numEmpleado} "
        
    def get_nombre(self):
        return self.__nombre
        
    def set_nombre(self, nombre):
        self.__nombre = nombre
        
    def get_number(self):
        return self.__number

    def set_number(self, number):
        self.__number = number
        
    def get_password(self):
        return self.__password
    
    def set_number(self, password):
        self.__password = password
    
    def get_numEmpleado(self):
        return self.__numEmpleado
    
    def get_number(self, numEmpleado):
        self.__numEmpleado = numEmpleado

class Usuarios:
    def __init__(self, nombre, number, password, numEmpleado):
        self.__nombre = nombre
        self.__number = number
        self.__password = password
        self.__numEmpleado = numEmpleado

    def __str__(self):
        return f" Nombre: {self.__nombre}\n Telefono: {self.__number}\n Numero de Empleado: {self.__numEmpleado} "
        
    def get_nombre(self):
        return self.__nombre
        
    def set_nombre(self, nombre):
        self.__nombre = nombre
        
    def get_number(self):
        return self.__number

    def set_number(self, number):
        self.__number = number
        
    def get_password(self):
        return self.__password
    
    def set_number(self, password):
        self.__password = password
    
    def get_numEmpleado(self):
        return self.__numEmpleado
    
    def get_number(self, numEmpleado):
        self.__numEmpleado = numEmpleado
