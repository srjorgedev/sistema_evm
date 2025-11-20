from enum import Enum

class ColorKeys(Enum):
    CREAR = "crear"
    MODIFICAR = "mod"
    ARCHIVAR = "archivar"
    BASE = "base"

colors = {
    ColorKeys.ARCHIVAR: "#EF4444",
    ColorKeys.CREAR: "#22C55E",
    ColorKeys.MODIFICAR: "#fbff85",
    ColorKeys.BASE: "#343434"
}
