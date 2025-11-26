from vehiculo  import fVehiculo as fVehiculo
from vehiculo import menu as menu
from vehiculo import val as val

opc = 0
while opc != 5:    
    opc = val.vOpciones("Ingrese una opción: ", 1, 5, menu.menuVehiculos)
    
    match opc:
        case 1:
            fVehiculo.listarVehiculos() 
        case 2:
            fVehiculo.SolicitarDatos()
        case 3:
            fVehiculo.modificarMatricula()
        case 4:
            fVehiculo.borrarVehiculo()
        case 5:
            print("Saliendo...")
            break 
        


