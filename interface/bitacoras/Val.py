def Int(msg):
    while True:
        aux = input(msg)

        if aux.isdigit():
            return int(aux)
        else:
            print("   Solo numeros enteros.")


def IntRange(msg, min, max):
    while True:
        aux = input(msg)

        if aux.isdigit():
            val = int(aux)

            if min <= val <= max:
                return val
            else:
                print(f"Valor fuera de rango. [{min} - {max}]")
        else:
            print("   Solo numeros enteros.")


def Menu(msg, min, max, menu):
    while True:
        menu()
        aux = input(msg)

        if aux.isdigit():
            val = int(aux)

            if min <= val <= max:
                return val
            else:
                print(f"Valor fuera de rango. [{min} - {max}]")
        else:
            print("   Solo numeros enteros.")


def Str(msg):
    while True:
        val = input(msg)
        aux = val.replace(" ", "")

        if not aux.isalpha():
            print("   Solo texto")
        elif len(aux) == 0:
            print("   Escribe algo")
        elif len(aux) < 3:
            print("   Minimo 2 caracteres")
        else:
            break

    return val


def Float(msg):
    while True:
        valor = input(msg)
        aux = valor.replace(".", "")

        if not aux.isdigit():
            print("   Solo numeros.")
        else:
            break

    return float(valor)


def KMEntrada(msg, kmSalida):
    while True:
        valor = input(msg)
        aux = valor.replace(".", "")

        if not aux.isdigit():
            print("   Solo numeros.")
        else:
            valor = float(valor)
            if (valor > kmSalida):
                break
            else:
                print(
                    f"Los km de entrada deben ser mayores a los de salida ({kmSalida})"
                )

    return valor


def GasEntrada(msg, gasEntrada):
    while True:
        valor = input(msg)
        aux = valor.replace(".", "")

        if not aux.isdigit():
            print("   Solo numeros.")
        else:
            valor = float(valor)
            if (valor < gasEntrada):
                break
            else:
                print(
                    f"La gasolina de entrada debe ser menor a la de salida ({gasEntrada})"
                )

    return valor


def Decision(msg):
    while True:
        val = input(msg)

        if val.isdigit():
            print("   Solo texto")
        else:
            if val.lower() == "si":
                return True
            elif val.lower() == "no":
                return False
            else:
                print("   Solo SI / NO")
