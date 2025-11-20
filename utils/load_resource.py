from pathlib import Path

direction = Path(__file__)
folder = direction.parent.parent

def ruta_svg(icono):
    return folder / "interface" / "assets" / "icons" / f"{icono}.svg"    # Ruta del svg

def ruta_img_png(img):
    return folder / "interface" / "assets" / "images" / f"{img}.png"

def ruta_img_jpg(img):
    return folder / "interface" / "assets" / "images" / f"{img}.jpg"