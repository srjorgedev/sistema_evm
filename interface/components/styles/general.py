from enum import Enum

class COLORS(Enum):
    CREAR = "crear"
    MODIFICAR = "mod"
    ARCHIVAR = "archivar"
    BASE = "base"
    BG_OSCURO_1 = "bg_oscuro_og"
    BG_OSCURO_2 = "bg_oscuro_2"
    SIDE_OSCURO_1 = "side_oscuro_1"
    SIDE_OSCURO_2 = "side_oscuro_2"

COLORS_LIST = {
    COLORS.ARCHIVAR: "#EF4444",
    COLORS.CREAR: "#22C55E",
    COLORS.MODIFICAR: "#fbff85",
    COLORS.BASE: "#3498DB",
    COLORS.BG_OSCURO_2: "#192c3b",
    COLORS.BG_OSCURO_1: "#0f181f",
    COLORS.SIDE_OSCURO_1: "#131e24",
    COLORS.SIDE_OSCURO_2: "#1d323d"
    
}