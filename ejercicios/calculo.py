from modulos.operaciones import * 

def ejercicio():
    a, b, c, d = (10, 5, 0, "Hola")
    print("Primera prueba:\n")
    print( f"{a} + {b} = {suma(a, b)}\n")
    print("Segunda prueba:\n")
    print( f"{a} - {d} = {resta(b, d)}\n")
    print("Tercera prueba:\n")
    print( f"{b} * {b} = {producto(b, b)}\n")
    print("Cuarta prueba:\n")
    print( f"{a} / {c} = {division(a, c)}\n")