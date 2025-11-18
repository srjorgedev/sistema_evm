from domain.bitacoras.CRUD import listaGeneral

print("Ejecutando listaGeneral en hilo principal (prueba)...")
try:
    res = listaGeneral()
    print("Resultado (sync):", type(res), "len:", len(res) if hasattr(res, '__len__') else "n/a")
except Exception as e:
    print("Exception en hilo principal:", e)