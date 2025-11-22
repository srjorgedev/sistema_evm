from PyQt6.QtCore import QObject, pyqtSignal, pyqtSlot, QThread

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

class TaskRunner(QObject):
    """Gestor centralizado de tareas asíncronas"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self._threads = [] # Referencia para que el GC no los mate

    def run(self, func, on_success, on_error=None, *args, **kwargs):
        thread = QThread()
        worker = Fetch(func, *args, **kwargs)
        worker.moveToThread(thread)

        # Conexiones
        thread.started.connect(worker.run)
        worker.finished.connect(lambda res: self._cleanup(thread, worker))
        worker.finished.connect(on_success)
        
        if on_error:
            worker.error.connect(on_error)
        else:
            worker.error.connect(lambda e: print(f"Error asíncrono: {e}"))

        # Iniciar
        thread.start()
        self._threads.append((thread, worker))

    def _cleanup(self, thread, worker):
        thread.quit()
        thread.wait()
        # Remover de la lista de referencias
        self._threads = [t for t in self._threads if t[0] != thread]