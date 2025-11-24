# fObservacion.py
from interface.observacionymantenimiento import val
from domain.observaciones import crudObservacion
from domain.observaciones.Observacion import Observacion
from interface.observacionymantenimiento import fMantenimiento

def pedirDatos():
    print(" ----- Registrar Observación -----")
    tipoObservacion = val.vSeleccion("Tipo de Observación", ["General", "Seguridad", "Calidad", "Personal"])
    
    descripcion = val.Str("Descripción de la Observación")
    bitacoraAsociada = val.vEmpresa("Bitácora asociada")
    
    nuevaObservacion = Observacion(descripcion, tipoObservacion, bitacoraAsociada)
    crudObservacion.alta(nuevaObservacion)

    while True:
        respuesta = val.vSeleccion("¿Desea registrar un nuevo MANTENIMIENTO?", ["si", "no"]).lower()
        if respuesta == "si":
            print("\n** Redirigiendo a registro de Mantenimiento **")
            fMantenimiento.pedirDatos()
            break
        elif respuesta == "no":
            break

def listaGeneral():
    crudObservacion.lista()
    
def actualizarObservacion():
    print(" ----- Modificar Observación -----")
    numero = val.vInt("Folio de la Observación a modificar")
    tempObservacion = Observacion("", "", "", numero)
    
    objObservacion = crudObservacion.buscar(tempObservacion)
    
    if objObservacion:
        print("\n-- Ingrese nuevos datos --")
        
        # Actualizar Descr
        nuevaDescripcion = val.Str(f"Nueva Descripción (actual: {objObservacion.get_descripcion()})")
        objObservacion.set_descripcion(nuevaDescripcion)
        
        # Actualizar Bitácora
        nuevaBitacora = val.vEmpresa(f"Nueva Bitácora Asociada (actual: {objObservacion.get_bitacoraAsociada()})")
        objObservacion.set_bitacoraAsociada(nuevaBitacora)
        
        crudObservacion.actualizar(objObservacion)

def borrarObservacion():
    print(" ----- Eliminar Observación -----")
    numero = val.vInt("Folio de la Observación a eliminar")
    tempObservacion = Observacion("", "", "", numero)
    
    objObservacion = crudObservacion.buscar(tempObservacion)
    
    if objObservacion:
        confirma = val.vSeleccion("Confirme eliminación", ["si", "no"])
        if confirma.lower() == "si":
            crudObservacion.borrar(objObservacion)
        else:
            print("Eliminación cancelada.")