import re

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

def _Int(msg: str):
    """
    Solicita un numero con un mensaje personalizado..
    Retorna el numero ingresado.

    args:
        - msg (str): Mensaje que aparecera en el input que solicita la opcion seleccionada.

    return:
        - int: Numero entero ingresado.
    """
    opc = input(msg)

    if not opc.isdigit():
        print()
        print("Solo numeros enteros.")
    elif opc.isdigit():
        return int(opc)

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
        print("Solo numeros enteros.")
    elif opc.isdigit() and inf <= int(opc) <= sup:
        return int(opc)
    elif opc.isdigit() and int(opc) > sup or int(opc) < inf:
        print()
        print(f"Fuera de rango. Rango: {inf} - {sup}")


def valTelefono(number):
    pattern = r"^\d{10}$"
    if re.fullmatch(pattern, number):
        print(f"{number}: Numero valido")
    else:
        print(f"{number}: numero invalido")

def validate_password(password):
    # define our regex pattern for validation
    pattern = r"^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$"

    # We use the re.match function to test the password against the pattern
    match = re.match(pattern, password)
    return bool(match)


def valLicencia(numeroLicencia):
    regex_federal = r'^[A-Z]\d{9,10}$'
    return re.match(regex_federal, numeroLicencia)


def valTexto(texto):
    """
    Valida que el texto solo contenga letras (incluye acentos y espacios).
    No permite números ni caracteres especiales.
    """
    patron = r'^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+$'
    
    if re.match(patron, texto):
        return True
    else:
        print(" El texto solo puede contener letras y espacios. Vuelva a intentar.")
        return False

