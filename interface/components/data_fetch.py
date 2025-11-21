from PyQt6.QtCore import QObject, pyqtSignal, pyqtSlot

# Definicion del worker
# El objetivo de un worker es ejecutar una tarea en un hilo
# separado al hilo principal para evitar congelar la interfaz de usuario.
class Fetch(QObject): # Para poder usar Signal y Slot debemos heredar de QObject
    
    # Se definen Signals, que son lineas mediante las cuales el worker emite 
    # mensajes al hilo principal
    finished = pyqtSignal(object)   # Señal que se encarga de enviar el resultado
    error = pyqtSignal(str)         # Señal que se encarga de enviar el error
    
    def __init__(self, fn, *args, **kwargs): 
        super().__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    # Marca la funcion a la cual una Señal de Qt se puede conectar
    @pyqtSlot()
    
    # El trabajo que el worker debe realizar
    def run(self):
        try:
            # print("Ejecutando función dentro del worker...")
            # print("Voy a ejecutar fn =", fn)
            
            print("[FETCH]: Worker iniciando operacion.")
            # Ejecuta la funcion pasada por parametros
            data = self.fn(*self.args, **self.kwargs)
            # print("Función ejecutada correctamente.")
            
            print("[FETCH]: Worker operacion terminada.")
            
            print("[FETCH]: Worker enviando datos.")
            # El worker emite los datos obtenidos de la funcion 
            # al hilo pricipal
            self.finished.emit(data)
        except Exception as e:
            print(f"[FETCH]: Error con el worker -> {e}")
            # El worker emite el error  al hilo principal
            self.error.emit(str(e))
