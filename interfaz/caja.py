import shutil, sys

ancho = shutil.get_terminal_size().columns
alto = shutil.get_terminal_size().lines
espacio = 4

horizontal = "\u2501"
esqinfizq = "\u2517"
esqinfder = "\u251B"
esqsupizq = "\u250F"
esqsupder = "\u2513"
vertical = "\u2503"
conexionizq = "\u2523"
conexionder = "\u252B"

print(f"""
     Alto: {alto}
     Ancho: {ancho}
     """)

def _Linea():
     """
     Imprime una horizontal recta.
     \nUtilizando el simbolo    \u2501
     """

     print(" " * espacio + horizontal * (ancho - espacio * 2))
     
def _LineaInf():
     """
     Imprime una horizontal recta con esquinas que conectan hacia arriba.
     \nUtilizando los simbolos    \u2517  \u2501  \u251B
     """
     
     print(" " * espacio + esqinfizq + horizontal * (ancho - 2 - espacio * 2) + esqinfder)
     
def _LineaSup():
     """
     Imprime una horizontal recta con esquinas que conectan hacia abajo.
     \nUtilizando los simbolos    \u250F  \u2501  \u2513
     """
     
     print(" " * espacio + esqsupizq + horizontal * (ancho - 2 - espacio * 2) + esqsupder)
     
def _BordeV():
     """
     Imprime un borde en los lados izquierdo y derecho con el centro vacio.
     \nUtilizando el simbolo    \u2503
     """
     
     print(" " * espacio + vertical + " " * (ancho - 2 - espacio * 2) + vertical)
     
def _BordeVN(n):
     for i in range(n + 1):
          _BordeV()
          
def _Conexion():
     """
     Imprime una linea horizontal recta cuyos bordes conectan con lineas verticales.
     \nUtilizando los simbolos    \u2523  \u252B
     """
     
     print(" " * espacio + conexionizq + horizontal * (ancho - 2 - espacio * 2) + conexionder)
     

def _TextoCentrado(txt):
     """
     Imprime un texto centrado. SIN BORDE LATERAL.
     """
     espacio_libre_total = (ancho - espacio * 2) - len(txt)
     vacio_izquierdo = espacio_libre_total // 2
     vacio_derecho = espacio_libre_total - vacio_izquierdo
     
     linea = " " * espacio + " " * vacio_izquierdo + txt + " " * vacio_derecho + " " * espacio
     print(linea)
     
def _TextoCentradoBorde(txt):
     """
     Imprime un texto centrado. CON BORDE LATERAL.
     """
     espacio_libre_interno = (ancho - 2 - espacio * 2) - len(txt)
     vacio_izquierdo = espacio_libre_interno // 2
     vacio_derecho = espacio_libre_interno - vacio_izquierdo 

     linea = " " * espacio + vertical + " " * vacio_izquierdo + txt + " " * vacio_derecho + vertical + " " * espacio
     print(linea)
     
def _GuardarCursor():
     """
     Guarda la posicion actual del cursor.
     """
     print("\x1b[s", end="")
     
def _RecuperarCursor():
     """
     Mueve el cursor a la posicion guardada.
     """
     print("\x1b[u", end="")
     
def _MoverCursor(y, x):
     """ 
     Mueve el cursor a la posición (y, x) en la terminal. 
     
     args: 
          - x
          - y
     """
     _GuardarCursor()
     print(f"\x1b[{y};{x}H", end="")
     sys.stdout.flush()
     
def _Titulo(txt):
     _LineaSup()
     _BordeV()
     _TextoCentradoBorde(txt)
     _BordeV()
     _Conexion()

_Linea()
_LineaInf()
_LineaSup()
_BordeV()
_BordeVN(8)
_TextoCentrado("Hola")
_TextoCentradoBorde("Hola")
_MoverCursor(10, 8)
print("Hola sobrinos")
_RecuperarCursor()
_Conexion()
_Titulo("PEPEEEEEEEEEEEEEA")