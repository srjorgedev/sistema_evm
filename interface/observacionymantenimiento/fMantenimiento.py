# fMantenimiento.py
from interface.observacionymantenimiento import val
from domain.mantenimiento import crudMantenimiento
from domain.mantenimiento.Mantenimiento import Mantenimiento

def pedirDatos():
    print(" ----- Solicitar Nuevo Mantenimiento -----")
    razon = val.vEmpresa("Razón de la solicitud")
    tipoMantenimiento = val.vSeleccion("Tipo de Mantenimiento", ["Correctivo", "Preventivo", "Superficial"])
    importancia = val.vSeleccion("Importancia", ["Alta", "Media", "Baja"])
    vehiculo = val.vEmpresa("Vehículo Asociado (ID-vehiculo) (Esta opción estará validada pero es foránea y no tengo la tabla Vehículos)")
    fechaProgramada = val.vFecha("Fecha Programada")
    comentarios = val.Str("Comentarios generales")
    
    estatus = "ABIERTO"
    estadoMantenimiento = "PENDIENTE DE ASIGNACIÓN"
    
    nuevoMantenimiento = Mantenimiento(razon, estatus, importancia, fechaProgramada, comentarios, tipoMantenimiento, vehiculo, estadoMantenimiento)
    crudMantenimiento.alta(nuevoMantenimiento)

def listaGeneral():
    crudMantenimiento.lista()
    
def actualizarMantenimiento():
    print(" ----- Actualizar Mantenimiento -----")
    folio = val.vInt("Folio del Mantenimiento a modificar")
    tempMantenimiento = Mantenimiento("", "", "", "", "", "", "", "", folio)
    
    objMantenimiento = crudMantenimiento.buscar(tempMantenimiento)
    
    if objMantenimiento:
        
        #Actualizar Estatus)
        estatusOpciones = ["ABIERTO", "CERRADO", "ASIGNADO"]
        # El estatus actual ya se muestra al listar el mantenimiento
        nuevoEstatus = val.vSeleccion("Seleccione el Nuevo Estatus", estatusOpciones)
        objMantenimiento.set_estatus(nuevoEstatus)
        
        if nuevoEstatus == "ABIERTO":
            objMantenimiento.set_estadoMantenimiento("PENDIENTE DE ASIGNACIÓN")
            print("\nEstatus cambiado a PENDIENTE.")
            crudMantenimiento.actualizar(objMantenimiento)
            
            
            print("\n-- Ingrese nuevos datos --")

            #Actualizar Importancia
            importanciaOpciones = ["Alta", "Media", "Baja"]
            nuevaImportancia = val.vSeleccion(f"Nueva Importancia (actual: {objMantenimiento.get_importancia()})", importanciaOpciones)
            objMantenimiento.set_importancia(nuevaImportancia)

            #Actualizar Fecha Programada
            nuevaFecha = val.vFecha(f"Nueva Fecha Programada (actual: {objMantenimiento.get_fechaProgramada()})")
            objMantenimiento.set_fechaProgramada(nuevaFecha)
            
            #Actualizar Comentarios
            nuevoComentarios = val.Str(f"Nuevos Comentarios (actual: {objMantenimiento.get_comentarios()})")
            objMantenimiento.set_comentarios(nuevoComentarios)

            #Actualizar Estado Mantenimiento
            #nuevoEstado = val.Str(f"Nuevo Estado (actual: {objMantenimiento.get_estadoMantenimiento()})")
            #objMantenimiento.set_estadoMantenimiento(nuevoEstado)

            crudMantenimiento.actualizar(objMantenimiento)
            return
        
        if nuevoEstatus == "CERRADO":
            objMantenimiento.set_estadoMantenimiento("FINALIZADO")
            print("\nEstatus cambiado a CERRADO. No se solicita más información.")
            crudMantenimiento.actualizar(objMantenimiento)
            return
        if nuevoEstatus == "ASIGNADO":
            objMantenimiento.set_estadoMantenimiento("EN PROGRESO")
            print("\nEstatus cambiado a ASIGNADO.")
            crudMantenimiento.actualizar(objMantenimiento)
            
            
            print("\n-- Ingrese nuevos datos --")

            #Actualizar Importancia
            importanciaOpciones = ["Alta", "Media", "Baja"]
            nuevaImportancia = val.vSeleccion(f"Nueva Importancia (actual: {objMantenimiento.get_importancia()})", importanciaOpciones)
            objMantenimiento.set_importancia(nuevaImportancia)

            #Actualizar Fecha Programada
            nuevaFecha = val.vFecha(f"Nueva Fecha Programada (actual: {objMantenimiento.get_fechaProgramada()})")
            objMantenimiento.set_fechaProgramada(nuevaFecha)
            
            #Actualizar Comentarios
            nuevoComentarios = val.Str(f"Nuevos Comentarios (actual: {objMantenimiento.get_comentarios()})")
            objMantenimiento.set_comentarios(nuevoComentarios)

            #Actualizar Estado Mantenimiento
            #nuevoEstado = val.Str(f"Nuevo Estado (actual: {objMantenimiento.get_estadoMantenimiento()})")
            #objMantenimiento.set_estadoMantenimiento(nuevoEstado)

            crudMantenimiento.actualizar(objMantenimiento)
            return
        
def borrarMantenimiento():
    print(" ----- Eliminar Mantenimiento -----")
    folio = val.vInt("Folio del Mantenimiento a eliminar")
    tempMantenimiento = Mantenimiento("", "", "", "", "", "", "", "", folio)
    
    objMantenimiento = crudMantenimiento.buscar(tempMantenimiento)
    
    if objMantenimiento:
        confirma = val.vSeleccion("Confirme eliminación", ["si", "no"])
        if confirma.lower() == "si":
            crudMantenimiento.borrar(objMantenimiento)
        else:
            print("Eliminación cancelada.")