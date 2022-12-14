def suma(a,b):
    try:
        r = a + b
    except TypeError:
        print("Tipo de dato no válido")
    else:
        return r


def resta(a,b):
    try:
        r = a - b
    except TypeError:
        print("Tipo de dato no válido")
    else:
        return r


def producto(a,b):
    try:
        r = a * b
    except TypeError:
        print("Tipo de dato no válido")
    else:
        return r


def division(a,b):
    try:
        r = a / b
    except TypeError:
        print("Tipo de dato no válido")
    except ZeroDivisionError:
        print("No se puede dividir entre cero")
    else:
        return r