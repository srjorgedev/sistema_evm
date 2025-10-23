import random
from menus import mUsuarios
from Utils import Validar
from clases.cUsuarios import Administrador, Chofer, Vigilante, Usuarios


#0.6.1
def _Listado():
     opc26=0
     while opc26 != 5:
          mUsuarios._Listado()
          opc26=int(input("  Seleccione el tipo de usuario: "))
          match opc26:
               case 1:
                    print(" No hay Aministradores.")
                    print()
               case 2:
                    print(" No hay choferes.")
                    print()
               case 3:
                    print(" No hay vigilantes.")
                    print()
               case 4:
                    print(" No hay usuarios.")
                    print()
               case 5:
                    print(" Volviendo al menu de Usuarios...")
     print()

#0.6.2
def _Registrar():
     opc36=0
     while opc36 != 5:
          mUsuarios._Tipos()
          opc36=int(input("  Seleccione el tipo de usuario que desea registrar: "))
          match opc36:
               case 1:
                    print()
                    nombrePila=input(" Ingrese su nombre de pila: ")
                    if Validar.valTexto(nombrePila):
                         print()
                    else:
                         _Registrar()
                    apellidoPaterno=input(" Ingrese su apellido paterno: ")
                    if Validar.valTexto(apellidoPaterno):
                         print()
                    else:
                         _Registrar()
                    apellidoMaterno=input(" Ingrese su apellido materno: ")
                    if Validar.valTexto(apellidoMaterno):
                         print()
                    else:
                         _Registrar()
                    nombre=nombrePila+ " " + apellidoPaterno + " " + apellidoMaterno
                    print("   Su nombre es: " + nombre)
                    print()
                    number=input("Ingrese su numero telefonico (10 digitos): ")
                    Validar.valTelefono(number)
                    print()
                    while True:
                         password = input("Ingrese una contraseña: ")
                         if Validar.validate_password(password):
                              print(" Contraseña válida.")
                              print("Administrador registrado exitosamente: ")
                              numEmpleado = random.randint(100000, 999999)
                              nuevoAdmin = Administrador(nombre, number, password, numEmpleado)
                              print()
                              print(nuevoAdmin)
                              print()
                              break
                         else:
                              print("- Contraseña inválida. Debe tener:")
                              print("- Al menos 8 caracteres")
                              print("- Una letra mayúscula")
                              print("- Una letra minúscula")
                              print("- Un número\n")
                    print()
               case 2:
                    print()
                    nombrePila=input(" Ingrese su nombre de pila: ")
                    if Validar.valTexto(nombrePila):
                         print()
                    else:
                         _Registrar()
                    apellidoPaterno=input(" Ingrese su apellido paterno: ")
                    if Validar.valTexto(apellidoPaterno):
                         print()
                    else:
                         _Registrar()
                    apellidoMaterno=input(" Ingrese su apellido materno: ")
                    if Validar.valTexto(apellidoMaterno):
                         print()
                    else:
                         _Registrar()
                    nombre=nombrePila + " " + apellidoPaterno + " " + apellidoMaterno
                    print(" Su nombre es: " + nombre)
                    print()
                    number=input("Ingrese su numero telefonico (10 digitos): ")
                    Validar.valTelefono(number)
                    print()
                    print("Seleccione el tipo de licencia del chofer: ")
                    print("Tipo A (Automovilista): Para la conducción de vehículos particulares, como autos, camionetas y motocicletas.")
                    print()
                    print("Tipo B (Taxis y aplicaciones): Para conductores de taxis y servicios de transporte de pasajeros a través de plataformas tecnológicas.")
                    print()
                    print("Tipo C (Transporte público): Para operar vehículos de transporte colectivo de pasajeros como microbuses, minibuses y vagonetas.")
                    print()
                    print("Tipo D (Transporte de carga): Para la conducción de camiones de carga. ")
                    print()
                    print("Tipo E (Servicios especializados y de carga pesada): Para transporte especializado, como pipas, o para carga pesada como tráileres y doble remolque. ")
                    print()
                    licencia=input("Ingrese una opcion: ")
                    print()
                    print(" Eligio la opcion de licencia " + licencia +".")
                    print()
                    while True:
                         numeroLicencia = input("Ingrese el número de licencia (Ejemplo: A123456789): ")
                         if Validar.valLicencia(numeroLicencia):
                              print(" Número de licencia válido.")
                              break
                         else:
                              print(" Número de licencia inválido. Debe comenzar con una letra mayúscula seguida de 9 o 10 dígitos.\n")
                    print()
                    while True:
                         password = input("Ingrese una contraseña: ")
                         if Validar.validate_password(password):
                              print(" Contraseña válida.")
                              print(" Chofer registrado exitosamente. ")
                              numEmpleado = random.randint(100000, 999999)
                              nuevoChofer = Chofer(nombre, number, password, licencia, numeroLicencia, numEmpleado)
                              print()
                              print(nuevoChofer)
                              print()
                              break
                         else:
                              print("- Contraseña inválida. Debe tener:")
                              print("- Al menos 8 caracteres")
                              print("- Una letra mayúscula")
                              print("- Una letra minúscula")
                              print("- Un número\n")
                    print()
               case 3:
                    print()
                    nombrePila=input(" Ingrese su nombre de pila: ")
                    if Validar.valTexto(nombrePila):
                         print()
                    else:
                         _Registrar()
                    apellidoPaterno=input(" Ingrese su apellido paterno: ")
                    if Validar.valTexto(apellidoPaterno):
                         print()
                    else:
                         _Registrar()
                    apellidoMaterno=input(" Ingrese su apellido materno: ")
                    if Validar.valTexto(apellidoMaterno):
                         print()
                    else:
                         _Registrar()
                    nombre=nombrePila + " " + apellidoPaterno + " " + apellidoMaterno
                    print(" Su nombre es: " + nombre)
                    print()
                    number=input("Ingrese su numero telefonico (10 digitos): ")
                    Validar.valTelefono(number)
                    print()
                    while True:
                         password = input("Ingrese una contraseña: ")
                         if Validar.validate_password(password):
                              print(" Contraseña válida.")
                              print(" Vigilante registrado exitosamente. ")
                              numEmpleado = random.randint(100000, 999999)
                              nuevoVigilante = Vigilante(nombre,number, password, numEmpleado)
                              print()
                              print(nuevoVigilante)
                              print()
                              break
                         else:
                              print("- Contraseña inválida. Debe tener:")
                              print("- Al menos 8 caracteres")
                              print("- Una letra mayúscula")
                              print("- Una letra minúscula")
                              print("- Un número\n")
                    print()
               case 4:
                    print()
                    nombrePila=input(" Ingrese su nombre de pila: ")
                    if Validar.valTexto(nombrePila):
                         print()
                    else:
                         _Registrar()
                    apellidoPaterno=input(" Ingrese su apellido paterno: ")
                    if Validar.valTexto(apellidoPaterno):
                         print()
                    else:
                         _Registrar()
                    apellidoMaterno=input(" Ingrese su apellido materno: ")
                    if Validar.valTexto(apellidoMaterno):
                         print()
                    else:
                         _Registrar()
                    nombre=nombrePila + " " + apellidoPaterno + " " + apellidoMaterno
                    print(" Su nombre es: " + nombre)
                    print()
                    number=input("Ingrese su numero telefonico (10 digitos): ")
                    Validar.valTelefono(number)
                    print()
                    while True:
                         password = input("Ingrese una contraseña: ")
                         if Validar.validate_password(password):
                              print(" Contraseña válida.")
                              print(" Usuario registrado exitosamente. ")
                              numEmpleado = random.randint(100000, 999999)
                              nuevoUsuario = Usuarios(nombre,number, password, numEmpleado)
                              print()
                              print(nuevoUsuario)
                              print()
                              break
                         else:
                              print("- Contraseña inválida. Debe tener:")
                              print("- Al menos 8 caracteres")
                              print("- Una letra mayúscula")
                              print("- Una letra minúscula")
                              print("- Un número\n")
                    print()
               case 5:
                    print("Volviendo al menu de Usuarios...")
     print()
