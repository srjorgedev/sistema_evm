def _SelectMenu(msg: str, menu, inf: int, sup: int):
    """
    Imprime un menu mediante una lista.
    Solicita un numero con un mensaje personalizado dentro de un rango.
    Retorna el numero ingresado.

    args:
        - msg (str): Mensaje que aparecera en el input que solicita la opcion seleccionada.
        - menu (funcion): Opciones del menu
        - inf (int): Limite inferior del rango.
        - sup (int): Limite superior del rango.

    return:
        - int: Numero entero ingresado. Entre inf y sup.
    """
    while True:
        menu()
        opc = _IntRange(msg, inf, sup)
        print()

        if opc:
            return opc


def _IntRange(msg: str, inf: int, sup: int):
    """
    Solcita un numero dentro de un rango con un mensaje personalizado.
    Retorna el numero ingresado.

    args:
        - msg (str): Mensaje que aparecera en el input que solicita la opcion seleccionada.
        - inf (int): Limite inferior del rango.
        - sup (int): Limite superior del rango.

    return:
        - int: Numero entero ingresado. Entre inf y sup.
    """
    opc = input(msg)

    if not opc.isdigit():
        print()
        print("   Solo numeros enteros.")
    elif opc.isdigit() and inf <= int(opc) <= sup:
        return int(opc)
    elif opc.isdigit() and int(opc) > sup or int(opc) < inf:
        print()
        print(f"Fuera de rango. Rango: {inf} - {sup}")
