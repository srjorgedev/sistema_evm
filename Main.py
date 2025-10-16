import Menu, Validar, FunBitacora, SubMenus

mantenimientos = []
observaciones = []

opc1 = 0
while opc1 != 8:
    opc1: int = Validar._SelectMenu("    Ingrese una opcion: ", Menu._Principal, 1, 8)

    match opc1:
        case 1: # -> Bitacoras
            opc11 = 0
            while opc11 != 4:
                opc11 = Validar._SelectMenu("\n    Ingrese una opcion: ", Menu._Bitacoras, 1, 4)
                match opc11:
                    case 1:
                        opc112 = 0
                        while opc112 != 4:
                            opc112 = Validar._SelectMenu("\n    Ingrese una opcion: ", Menu._CrearBitacora, 1, 4)
                            match opc112:
                                case 1: 
                                    FunBitacora._Salida()
                                case 2:
                                    FunBitacora._Entrada()
                                case 3:
                                    FunBitacora._Generar()
                                case 4: 
                                    print("Volver al menu de bitacora")
                    case 2:
                        FunBitacora._Listado()
                    case 3:
                        FunBitacora._Consulta()
                    case 4:
                        print("Volver al menu principal")
        case 2: # -> Vehiculos
            opc12 = 0
            while opc12 != 6:
                opc12 = Validar._SelectMenu("    Ingrese una opcion: ", Menu._Vehiculos, 1, 6)
                match opc12:
                    case 1:
                        print("Listado de vehiculos")
                        print("los vehiculos registrados son:")
                        print("En construccion...")
                    case 2:
                        print("Agregar vehiculo")
                        print("Ingresa el numero de serie del vehiculo: ")
                        num_serie = input()
                        print("Ingresa la matricula del vehiculo: ")
                        matricula = input()
                        print("Ingresa la marca del vehiculo: ")
                        marca = input()
                        print("Ingresa el modelo del vehiculo: ")
                        modelo = input()
                        print("Ingresa el color del vehiculo: ")
                        color = input()
                        print("Ingresa la fecha de fabricacion del vehiculo (dd/mm/aaaa): ")
                        fecha_fabricacion = input()
                        print("Ingresa la fecha de adquision del vehiculo (dd/mm/aaaa): ")
                        fecha_adquision = input()
                        print("Ingresa el tipo de vehiculo: ")
                        tipo = input()
                        print("Tipo de licencia requerida: ")
                        tipo_licencia = input()
                        print("Capacidad de pasajeros: ")
                        capacidad_pasajeros = input()
                        print("Utilidad del vehiculo: ")
                        utilidad = input()
                        print("comentarios adicionales: ")
                        comentarios = input()
                        print("El vehiculo ha sido registrado exitosamente.")
                        
                    case 3:
                        print("Modificar informacion de vehiculo")
                        print("Que vehiculo desea modificar?")
                        vehiculoMod = input()
                        print("Que dato desea modificar?")
                        datoMod = input()
                        print("Por favor ingrese el nuevo valor:")
                        nuevoValor = input()
                        print(f"El dato {datoMod} del vehiculo {vehiculoMod} ha sido modificado a {nuevoValor}.")
                    case 4:
                        print("Eliminar vehiculo")
                        print("Que vehiculo desea eliminar?")
                        vehiculoEli = input()
                        print("Cual es la razon de eliminar el vehiculo?")
                        razonEli = input()
                        print(f"El vehiculo {vehiculoEli} ha sido eliminado por la siguiente razon: {razonEli}.")
                    case 5:
                        print("Suspender vehiculo")
                        print("Que vehiculo desea suspender?")
                        vehiculoSus = input()
                        print("Cual es la razon de suspender el vehiculo?")
                        razonSus = input()
                        print("Fecha de inicio de suspension (dd/mm/aaaa): ")
                        fechaInicio = input()
                        print("fecha de fin de suspension (dd/mm/aaaa): ")
                        fechaFin = input()
                        print(f"El vehiculo {vehiculoSus} ha sido suspendido por la siguiente razon: {razonSus}.")
                        print(f"La suspension sera efectiva desde {fechaInicio} hasta {fechaFin}.")
                    case 6:
                        print("Volver al menu principal")
                print()
        case 6: # -> Mantenimiento
            opc13 = 0
            while opc13 != 6:
                opc13 = Validar._SelectMenu("    Ingrese una opcion: ", Menu._Mantenimiento, 1, 6)
                match opc13:
                    case 1:
                        print("Listado de mantenimientos")
                        print("En construccion...")
                    case 2:
                        print("Solicitar mantenimiento")
                        print("En construccion...")
                    case 6:
                        print("Volver al menu principal")
                print()
        case 7:  # -> Observaciones
            opc14 = 0
            while opc14 != 6:
                opc14 = Validar._SelectMenu("Ingrese una opcion: ", Menu._Observaciones, 1, 6)
                match opc14:
                    case 1:
                        print("\n--- Listado de observaciones ---")
                        if len(observaciones) == 0:
                            print("No hay observaciones registradas.")
                        else:
                            for i, obs in enumerate(observaciones, 1):
                                print(f"{i}. Vehiculo: {obs['vehiculo']} | Tipo: {obs['tipo']} | Descripcion: {obs['descripcion']} | Fecha: {obs['fecha']}")
                    case 2:
                        print("\n--- Registrar observacion ---")
                        vehiculo = input("Ingrese el nombre o ID del vehiculo: ")
                        tipo = input("Tipo de incidente/observacion (leve, media, grave): ")
                        descripcion = input("Descripcion detallada del incidente: ")
                        fecha = input("Ingrese la fecha (DD/MM/AAAA): ")

                        obs = {
                            "vehiculo": vehiculo,
                            "tipo": tipo,
                            "descripcion": descripcion,
                            "fecha": fecha
                        }
                        observaciones.append(obs)
                        print("Observacion registrada correctamente.")

                        respuesta = input("¿Desea registrar un mantenimiento relacionado? (S/N): ").strip().upper()
                        if respuesta == "S":
                            print("\nRedirigiendo al registro de mantenimiento...\n")
                            vehiculo_m = vehiculo
                            tipo_m = input("Ingrese el tipo de mantenimiento (preventivo/correctivo): ")
                            fecha_m = input("Ingrese la fecha del mantenimiento (DD/MM/AAAA): ")
                            observ_m = input("Ingrese observaciones generales: ")

                            mantenimiento = {
                                "vehiculo": vehiculo_m,
                                "tipo": tipo_m,
                                "fecha": fecha_m,
                                "observaciones": observ_m
                            }
                            mantenimientos.append(mantenimiento)
                            print("Mantenimiento registrado correctamente.")
                        else:
                            print("No se registró mantenimiento adicional.")
                    case 6:
                        print("Volver al menu principal")
                print()
        case 4: # -> Solicitudes
            opc15 = 0
            while opc15 != 6:
                opc15 = Validar._SelectMenu("    Ingrese una opcion: ", Menu._Solicitudes, 1, 6)
                match opc15:
                    case 1:
                        print("Listado de solicitudes")
                        print("solicitudes de vehiculos:")
                        print("En construccion...")
                        print("Solicitudes de mantenimiento:")
                        print("En construccion...")
                    case 2:
                        print("Levantar solicitud")
                        print("Tipo de solicitud (Mantenimiento/vehiculo): ")
                        tipo_solicitud = input()
                        print("Motivo de la solicitud: ")
                        motivo_solicitud = input()
                        print("Fecha de solicitud (dd/mm/aaaa): ")
                        fecha_solicitud = input()
                        print("Hora de solicitud (hh:mm): ")
                        hora_solicitud = input()
                        print("Nombre del solicitante: ")
                        nombreSoli = input()
                        print("Apellido paterno del solicitante: ")
                        apellidopSoli = input()
                        print("Apellido materno del solicitante: ")
                        apellidomSoli = input()
                        print("Numero de empleado del solicitante: ")
                        num_empleado = input()
                        print("Tipo de licencia del solicitante: ")
                        tipo_licencia_soli = input()
                        print("Fecha de vencimiento de la licencia (dd/mm/aaaa): ")
                        fecha_vencimiento = input()
                        print("Telefono del solicitante: ")
                        telefono = input()
                        print("Generar solicitud (1), modificar solicitud (2), cancelar (3): ")
                        solicitud = input()
                        if solicitud == "1":
                            print("La solicitud ha sido generada exitosamente.")
                        elif solicitud == "2":
                            print("Modificar solicitud")
                        else:
                            print("Cancelando...")
                            
                    case 3:
                        print("Modificar solicitud")
                        print("Que solicitud desea modificar?")
                        solicitudMod = input()
                        print("Que dato desea modificar?")
                        datoMod = input()
                        print("Motivo de la modificacion: ")
                        motivoMod = input()
                        print("Por favor ingrese el nuevo valor:")
                        nuevoValor = input()
                        print(f"El dato {datoMod} de la solicitud {solicitudMod} ha sido modificado a {nuevoValor} por la siguiente razon: {motivoMod}.")
                    
                    case 4:
                        print("Ver estado de la solicitud")
                        print("Que solicitud desea consultar?")
                        solicitudCon = input()
                        print(f"El estado actual de la solicitud {solicitudCon} es: En proceso.")
                        
                    case 5:
                        print("Eliminar solicitud")
                        print("Que solicitud desea eliminar?")
                        solicitudEli = input()
                        print("Cual es la razon de eliminar la solicitud?")
                        razonEli = input()
                        print(f"La solicitud {solicitudEli} ha sido eliminada por la siguiente razon: {razonEli}.")
                    case 6:
                        print("Volver al menu principal")
                print()
        case 5: # -> Ususarios
            opc16 = 0
            while opc16 != 6:
                opc16 = Validar._SelectMenu("    Ingrese una opcion: ", Menu._Usuarios, 1, 6)
                match opc16:
                    case 1:
                        print("    LISTADO DE USUARIOS")
                        SubMenus._listausuarios()
                    case 2:
                        print("    REGISTRAR USUARIO")
                        SubMenus._registrausuario()
                    case 6:
                        print("    Volver al menu principal")
                print()
        case 3: # -> Autorizar Solicitudes
            opc17 = 0
            while opc17 != 6:
                opc17 = Validar._SelectMenu("    Ingrese una opcion: ", Menu._Autorizar, 1, 6)
                match opc17:
                    case 1:
                        print("    LISTADO DE SOLICITUDES\n")
                        print("    No hay solicitudes")
                    case 2:
                        print("    LISTADO DE AUTORIZACIONES")
                        print("    No hay autorizaciones")
                    case 6:
                        print("    Volver al menu principal")
                print()
        case 8:
            print("    Salio del sistema.")
            print()