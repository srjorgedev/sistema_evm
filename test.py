import interface.usuarios.Menu as _Usuarios
from interface.usuarios import fUsuarios

import interface.bitacoras.Menu as _Bitacoras
from controllers import bitacora_controller

import interface.vehiculos.Menu as _Vehiculos
#from controllers import fVehiculo

from db.conn import conn
print("prueba de conexion")
miConn = conn()
from interface.observacionymantenimiento import menu
from interface.observacionymantenimiento import fMantenimiento
from interface.observacionymantenimiento import fObservacion
#import sys
from interface.observacionymantenimiento import val

import interface.Menu as Menu
import interface.Val as Val

import os

os.system("cls")
print()

opc1 = 100
while True and opc1 != 9:
    opc1 = Val._SelectMenu("    Opcion: ", Menu.pricipal, 1, 9)

    match opc1:
        case 1:
            opc11 = 100

            while opc11 != 6:
                opc11 = Val._SelectMenu("    Opcion: ", _Bitacoras.principal, 1, 6)
                match opc11:
                    case 1:
                        bitacora_controller.lista()
                    case 2:
                        bitacora_controller.registrarSalida()
                    case 3:
                        bitacora_controller.registrarEntrada()
                    case 4:
                        bitacora_controller.modificar()
                    case 5:
                        bitacora_controller.eliminar()
                    case 6:
                        print("   Saliendo...")
                        break

    #    case 2:
    #        opc12 = 100
#
 #           while opc12 != 5:
  #              opc12 = Val._SelectMenu("    Opcion: ", _Vehiculos.menuVehiculos,
   #                                     1, 6)
    #            match opc12:
     #               case 1:
      #                  fVehiculo.listarVehiculos()
       #             case 2:
        #                fVehiculo.SolicitarDatos()
         #           case 3:
          #              fVehiculo.modificarMatricula()
          #          case 4:
          #              fVehiculo.borrarVehiculo()
          #          case 5:
          #              print("   Saliendo...")
          #              break


        case 3:
            opc13 = 100

            while opc13 != 6:
                opc13 = Val._SelectMenu("    Opcion: ", _Usuarios._Usuarios, 1, 6)
                match opc13:
                    case 1:
                        fUsuarios.createUser()
                    case 2:
                        fUsuarios.selectChofer()
                    case 3:
                        fUsuarios.empleados_contactos()
                    case 4:
                        fUsuarios.updateUser()
                    case 5:
                        fUsuarios.deleteUser()
                    case 6:
                        print("   Saliendo del Menu de Usuarios...")

        case 4: # MANTENIMIENTO
            opc1=0
            while (opc1!=9):
                opc1 = val.vOpciones("Opcion",1,9, menu.mMantenimiento)
                match opc1:
                    case 1: fMantenimiento.pedirDatos()
                    case 2: fMantenimiento.listaGeneral()
                    case 3: fMantenimiento.actualizarMantenimiento()
                    case 4: fMantenimiento.borrarMantenimiento()
        case 5: # OBSERVACIONES
            opc2=0
            while (opc2!=9):
                opc2 = val.vOpciones("Opcion",1,9, menu.mObservaciones)
                match opc2:
                    case 1: fObservacion.pedirDatos()
                    case 2: fObservacion.listaGeneral()
                    case 3: fObservacion.actualizarObservacion()
                    case 4: fObservacion.borrarObservacion()
        
        case 9:
            print("   Saliendo...")
            break
