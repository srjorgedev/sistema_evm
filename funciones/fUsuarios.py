import Validar, random
from menus import mUsuarios


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
                    print("Volviendo al menu de Usuarios...")
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
                    apellidoPaterno=input(" Ingrese su apellido paterno: ")
                    apellidoMaterno=input(" Ingrese su apellido materno: ")
                    nombre=nombrePila+ " " + apellidoPaterno + " " + apellidoMaterno
                    print("Su nombre es: " + nombre)
                    print()
                    number=input("Ingrese su numero telefonico (10 digitos): ")
                    Validar.valTelefono(number)
                    print()
                    while True:
                         password = input("Ingrese una contraseña: ")
                         if Validar.validate_password(password):
                              print(" Contraseña válida.")
                              print("Administrador registrado exitosamente. ")
                              numEmpleado = random.randint(100000, 999999)
                              print(f"Empleado: {nombre} | Número de Administrador: {numEmpleado}")
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
                    apellidoPaterno=input(" Ingrese su apellido paterno: ")
                    apellidoMaterno=input(" Ingrese su apellido materno: ")
                    nombre=nombrePila + " " + apellidoPaterno + " " + apellidoMaterno
                    print("Su nombre es: " + nombre)
                    print()
                    number=input("Ingrese su numero telefonico (10 digitos): ")
                    Validar.valTelefono(number)
                    print()
                    print("Seleccione el tipo de licencia del chofer: ")
                    print("Tipo A (Automovilista): Para la conducción de vehículos particulares, como autos, camionetas y motocicletas.")
                    print("Tipo B (Taxis y aplicaciones): Para conductores de taxis y servicios de transporte de pasajeros a través de plataformas tecnológicas.")
                    print("Tipo C (Transporte público): Para operar vehículos de transporte colectivo de pasajeros como microbuses, minibuses y vagonetas.")
                    print("Tipo D (Transporte de carga): Para la conducción de camiones de carga. ")
                    print("Tipo E (Servicios especializados y de carga pesada): Para transporte especializado, como pipas, o para carga pesada como tráileres y doble remolque. ")
                    licencia=input("Ingrese una opcion: ")
                    print("Eligio la opcion de licencia " + licencia +".")
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
                              print("Administrador registrado exitosamente. ")
                              numEmpleado = random.randint(100000, 999999)
                              print(f"Empleado: {nombre} | Número de Chofer: {numEmpleado}, numero de licencia: {numeroLicencia}")
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
                    apellidoPaterno=input(" Ingrese su apellido paterno: ")
                    apellidoMaterno=input(" Ingrese su apellido materno: ")
                    nombre=nombrePila + " " + apellidoPaterno + " " + apellidoMaterno
                    print("Su nombre es: " + nombre)
                    print()
                    number=input("Ingrese su numero telefonico (10 digitos): ")
                    Validar.valTelefono(number)
                    print()
                    while True:
                         password = input("Ingrese una contraseña: ")
                         if Validar.validate_password(password):
                              print(" Contraseña válida.")
                              print("Administrador registrado exitosamente. ")
                              numEmpleado = random.randint(100000, 999999)
                              print(f"Empleado: {nombre} | Número de Vigilante: {numEmpleado}")
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
                    apellidoPaterno=input(" Ingrese su apellido paterno: ")
                    apellidoMaterno=input(" Ingrese su apellido materno: ")
                    nombre=nombrePila + " " + apellidoPaterno + " " + apellidoMaterno
                    print("Su nombre es: " + nombre)
                    print()
                    number=input("Ingrese su numero telefonico (10 digitos): ")
                    Validar.valTelefono(number)
                    print()
                    while True:
                         password = input("Ingrese una contraseña: ")
                         if Validar.validate_password(password):
                              print(" Contraseña válida.")
                              print("Administrador registrado exitosamente. ")
                              numEmpleado = random.randint(100000, 999999)
                              print(f"Empleado: {nombre} | Número de Vigilante: {numEmpleado}")
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
