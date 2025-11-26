from enum import Enum

class COLORS(Enum):
    CREAR = "crear"
    MODIFICAR = "mod"
    ARCHIVAR = "archivar"
    BASE = "base"
    BASE_OSCURO = "base_oscuro"
    BASE_CLARO = "base_claro"
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
    ADVERTENCIA = "advertencia"
    TEXTO_CLARO = "texto_claro"
    TEXTO_OSCURO = "texto_oscuro"
    TABLA_CLARO = "tabla_claro"
    TABLA_OSCURO = "tabla_oscuro"
    BG_CLARO_2 = "bg_claro_2"
    BG_CLARO_4 = "bg_claro_4"

COLORS_LIST = {
    COLORS.ARCHIVAR: "#EF4444",
    COLORS.CREAR: "#22C55E",
    COLORS.MODIFICAR: "#ffd335",
    COLORS.BASE: "#3498DB",
    COLORS.BASE_OSCURO: "#277EB8",
    COLORS.BASE_CLARO: "#9fd9ef",
    COLORS.BG_OSCURO_2: "#192c3b",
    COLORS.BG_OSCURO_1: "#0f181f",
    COLORS.BG_CLARO_1: "#f0f6fa",
    COLORS.BG_CLARO_2: "#f2f2f2",
    COLORS.BG_CLARO_4: "#c1c1c1",
    COLORS.SIDE_OSCURO_1: "#131e24",
    COLORS.SIDE_OSCURO_2: "#1d323d",
    COLORS.SIDE_CLARO_1: "#f5f5f5",
    COLORS.MODAL_1: "#1e293b",
    COLORS.MODAL_CARD: "#1f2e43",
    COLORS.MODAL_CARD_BORDER: "#234360",
    COLORS.MAL: "#EF4444",
    COLORS.TEXTO_CLARO: "#f1f1f1",
    COLORS.TEXTO_OSCURO: "#242424",
    COLORS.TABLA_CLARO: "#ededed",
    COLORS.TABLA_OSCURO: "#343434"
}