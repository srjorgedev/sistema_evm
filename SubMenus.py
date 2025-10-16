import Menu, Validar, random

#0.6.1 SubMenu Usuarios
def _listausuarios():
    opc26=0
    while opc26 != 5:
        print("  Listado de usuarios")
        print("  1. Administradores ")
        print("  2. Choferes")
        print("  3. Vigilante ")
        print("  4. Usuario ")
        print("  5. Volver ")
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
                Menu._Usuarios()
    print()


#0.6.2
def _registrausuario():
    opc36=0
    while opc36 != 5:
        print("  Tipos de Usuario: ")
        print("  1. Administradores ")
        print("  2. Choferes")
        print("  3. Vigilante ")
        print("  4. Usuario ")
        print("  5. Volver ")
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
                password=input("Inregese una contrasena: ")
                valpassword=input("Repita la contrasena: ")
                if valpassword!=password:
                    print("Contrasena incorrecta")
                    print()
                else:
                    print("Administrador registrado exitosamente. ")
                    numAdmin = random.randint(100000, 999999)
                    print(f"Empleado: {nombre} | Número de Administrador: {numAdmin}")
                    print()
            case 2:
                print()
                nombrePila=input(" Ingrese su nombre de pila: ")
                apellidoPaterno=input(" Ingrese su apellido paterno: ")
                apellidoMaterno=input(" Ingrese su apellido materno: ")
                nombre=nombrePila+apellidoPaterno+apellidoMaterno
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
                print()
                password=input("Inregese una contrasena: ")
                valpassword=input("Repita la contrasena: ")
                if valpassword!=password:
                    print("Contrasena incorrecta")
                    print()
                else:
                    print("Chofer registrado exitosamente. ")
                    numChofer = random.randint(100000, 999999)
                    print(f"Empleado: {nombre} | Número de Chofer: {numChofer}")
                    print()
            case 3:
                print()
                nombrePila=input(" Ingrese su nombre de pila: ")
                apellidoPaterno=input(" Ingrese su apellido paterno: ")
                apellidoMaterno=input(" Ingrese su apellido materno: ")
                nombre=nombrePila+apellidoPaterno+apellidoMaterno
                print("Su nombre es: " + nombre)
                print()
                number=input("Ingrese su numero telefonico (10 digitos): ")
                Validar.valTelefono(number)
                print()
                password=input("Inregese una contrasena: ")
                valpassword=input("Repita la contrasena: ")
                if valpassword!=password:
                    print("Contrasena incorrecta")
                    print()
                else:
                    print("Vigilante registrado exitosamente. ")
                    numVig = random.randint(100000, 999999)
                    print(f"Empleado: {nombre} | Número de Vigilante: {numVig}")
                    print()
            case 4:
                print()
                nombrePila=input(" Ingrese su nombre de pila: ")
                apellidoPaterno=input(" Ingrese su apellido paterno: ")
                apellidoMaterno=input(" Ingrese su apellido materno: ")
                nombre=nombrePila+apellidoPaterno+apellidoMaterno
                print("Su nombre es: " + nombre)
                print()
                number=input("Ingrese su numero telefonico (10 digitos): ")
                Validar.valTelefono(number)
                print()
                password=input("Inregese una contrasena: ")
                valpassword=input("Repita la contrasena: ")
                if valpassword!=password:
                    print("Contrasena incorrecta")
                    print()
                else:
                    print("Usuario registrado exitosamente. ")
                    numUsuario = random.randint(100000, 999999)
                    print(f"Empleado: {nombre} | Número de Usuario: {numUsuario}")
                    print()
            case 5:
                Menu._Usuarios()
    print()

