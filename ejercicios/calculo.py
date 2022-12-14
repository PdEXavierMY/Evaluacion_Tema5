from modulos.operaciones import * 

def ejercicio():
    a, b, c, d = (10, 5, 0, "Hola")
    print( f"{a} + {b} = {suma(a, b)}")
    print( f"{a} - {d} = {resta(b, d)}")
    print( f"{b} * {b} = {producto(b, b)}") 
    print( f"{a} / {c} = {division(a, c)}")