# val.py
from datetime import date
import sys

# Menu
def vOpciones(msg, inf, sup, funcion):
    while True:
        funcion()
        valor = input(msg + ": ")
        if valor.isdigit() != True:
            print("Solo números enteros")
        else:
            valor = int(valor)
            if (valor >= inf and valor <= sup):
                break
            else:
                print("Opción fuera de rango")
        
    return valor

# 2. Validación de Teléfono
def vPhone(msg):
    while True:
        valor = input(msg + ": ").strip()
        if valor.isdigit() != True:
            print("Solo números enteros")
        else:
            if (len(valor) == 10):
                break
            else:
                print("Número inválido (debe tener 10 dígitos)")
    return valor

def vEmpresa(msg):
    while True:
        nombre = input(msg + ": ").strip()
        if len(nombre) < 2:
            print("Nombre corto o vacío")
        else:
            break
    
    return nombre

def vIntRange(msg, inf, sup):
    while True:
        valor = input(msg + ": ").strip()
        if valor.isdigit() != True:
            print("Solo números enteros")
        else:
            valor = int(valor)
            if (valor >= inf and valor <= sup):
                break
            else:
                print("Valor fuera de rango")
        
    return valor

def Str(msg):
    while True:
        valor = input(msg + ": ").strip()
        if len(valor) == 0:
            print("Debe escribir algo")
        else:
            if len(valor) < 2:
                print("Mínimo 2 letras o caracteres")
            else:
                break
    return valor

def vNombre(msg):
    while True:
        nombre = input(msg + ": ").strip()
        if nombre[0] == " ":
            print("Omita los espacios iniciales")
        else:
            aux = nombre.replace(" ","")
            if aux.isalpha() == False:
                print("Solo letras")
            else:
                if len(aux) < 2:
                    print("Nombre corto o vacío")
                else:
                    break
    
    return nombre

#Validación de Entero
def vInt(msg):
    while True:
        valor = input(msg + ": ").strip()
        if not valor.isdigit():
            print("Solo números enteros")
        else:
            return int(valor)

#Validación de Fecha
def vFecha(msg):
    """ Valida la fecha en formato YYYY-MM-DD. """
    while True:
        fecha_str = input(msg + " (YYYY-MM-DD): ").strip() 
        if len(fecha_str) != 10:
            print("Formato incorrecto. Use YYYY-MM-DD.")
            continue
        try:
            fecha = date.fromisoformat(fecha_str)
            return fecha.strftime('%Y-%m-%d')
        except ValueError:
            print("Fecha no válida o formato incorrecto.")

#Validación de Selección
def vSeleccion(msg, opciones):
    """ Muestra opciones numeradas (1, 2, 3...) y valida la entrada numérica. """
    num_opciones = len(opciones)
    while True:
        print(f"\n--- {msg} ---")
        for i, opcion in enumerate(opciones):
            print(f"   {i + 1}. {opcion}")
        
        valor = input("Ingrese el número de su elección: ").strip()
        
        if valor.isdigit():
            opc_num = int(valor)
            if 1 <= opc_num <= num_opciones:
                return opciones[opc_num - 1]
            else:
                print("Opción fuera de rango. Ingrese un número entre 1 y " + str(num_opciones))
        else:
            print("Entrada no válida. Por favor, ingrese un número.")