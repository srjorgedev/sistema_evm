class Vehiculo:
    def __init__(self, numero, asunto, horaSolicitud, fechaSolicitud, vehiculo, edoSolicitud,
                 solicitante, autorizador):
        self.__numero = numero
        self.__asunto = asunto  
        self.__horaSolicitud = horaSolicitud
        self.__fechaSolicitud = fechaSolicitud
        self.__vehiculo = vehiculo
        self.__edoSolicitud = edoSolicitud
        self.__solicitante = solicitante
        self.__autorizador = autorizador
        
        
    def __str__(self):
        return f"ID Solicitud: {self.__numero}  Asunto: {self.__asunto}  Hora Solicitud: {self.__horaSolicitud}  Fecha Solicitud: {self.__fechaSolicitud}  Vehiculo: {self.__vehiculo}  Estado Solicitud: {self.__edoSolicitud}  Solicitante: {self.__solicitante}  Autorizador: {self.__autorizador}"
        

    #gets
    def get_numero(self, ):
        return self.__numero
    def get_asunto(self):
        return self.__asunto
    def get_horaSolicitud(self):
        return self.__horaSolicitud
    def get_fechaSolicitud(self):
        return self.__fechaSolicitud
    def get_vehiculo(self):
        return self.__vehiculo
    def get_edoSolicitud(self):
        return self.__edoSolicitud
    def get_solicitante(self):
        return self.__solicitante
    def get_autorizador(self):
        return self.__autorizador
    
    #sets
    def set_numero(self, numero):
        self.__numero = numero
    def set_asunto(self, asunto):
        self.__asunto = asunto
    def set_horaSolicitud(self, horaSolicitud):
        self.__horaSolicitud = horaSolicitud
    def set_fechaSolicitud(self, fechaSolicitud):
        self.__fechaSolicitud = fechaSolicitud
    def set_vehiculo(self, vehiculo):
        self.__vehiculo = vehiculo
    def set_edoSolicitud(self, edoSolicitud):
        self.__edoSolicitud = edoSolicitud
    def set_solicitante(self, solicitante):
        self.__solicitante = solicitante
    def set_autorizador(self, autorizador):
        self.__autorizador = autorizador
        
    



