from enum import Enum

class COLORS(Enum):
    CREAR = "crear"
    MODIFICAR = "mod"
    ARCHIVAR = "archivar"
    BASE = "base"
    BG_OSCURO_1 = "bg_oscuro_og"
    BG_OSCURO_2 = "bg_oscuro_2"
    BG_CLARO_1 = "bg_claro_1"
    SIDE_OSCURO_1 = "side_oscuro_1"
    SIDE_OSCURO_2 = "side_oscuro_2"
    SIDE_CLARO_1 = "side_claro_1"
    MODAL_1 = "modal_1"
    MODAL_CARD = "modal_card"
    MODAL_CARD_BORDER = "modal_card_border"
    MAL = "mal"

COLORS_LIST = {
    COLORS.ARCHIVAR: "#EF4444",
    COLORS.CREAR: "#22C55E",
    COLORS.MODIFICAR: "#fbff85",
    COLORS.BASE: "#3498DB",
    COLORS.BG_OSCURO_2: "#192c3b",
    COLORS.BG_OSCURO_1: "#0f181f",
    COLORS.BG_CLARO_1: "#fcfcfc",
    COLORS.SIDE_OSCURO_1: "#131e24",
    COLORS.SIDE_OSCURO_2: "#1d323d",
    COLORS.SIDE_CLARO_1: "#f5f5f5",
    COLORS.MODAL_1: "#1e293b",
    COLORS.MODAL_CARD: "#1f2e43",
    COLORS.MODAL_CARD_BORDER: "#234360",
    COLORS.MAL: "#EF4444"
}