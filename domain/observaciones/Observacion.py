# Observacion.py
class Observacion:
    def __init__(self, descripcion, tipoObservacion, bitacoraAsociada, numero=0):
        self.__numero = numero
        self.__descripcion = descripcion
        self.__tipoObservacion = tipoObservacion
        self.__bitacoraAsociada = bitacoraAsociada

    def __str__(self):
        return f"Folio: {self.__numero} | Tipo: {self.__tipoObservacion} | Descripción: {self.__descripcion[:50]}... | Bitácora: {self.__bitacoraAsociada}"

    # Getters
    def get_numero(self): return self.__numero
    def get_descripcion(self): return self.__descripcion
    def get_tipoObservacion(self): return self.__tipoObservacion
    def get_bitacoraAsociada(self): return self.__bitacoraAsociada

    # Setters
    def set_numero(self, numero): self.__numero = numero
    def set_descripcion(self, descripcion): self.__descripcion = descripcion
    def set_tipoObservacion(self, tipoObservacion): self.__tipoObservacion = tipoObservacion
    def set_bitacoraAsociada(self, bitacoraAsociada): self.__bitacoraAsociada = bitacoraAsociada

