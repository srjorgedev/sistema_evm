from domain.mantenimiento import crudMantenimiento
from domain.mantenimiento.Mantenimiento import Mantenimiento

def lista() -> list[Mantenimiento]:
    return crudMantenimiento.lista()