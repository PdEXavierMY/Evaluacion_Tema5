from introducir import solicitar_introducir_numero_extremo
from ejercicios.calculo import ejercicio
from ejercicios.reloj import reloj_terminal
from ejercicios.contador import crear_contadortxt
from ejercicios.gestor import Gestor, Personaje

def launcher():
    numero = solicitar_introducir_numero_extremo("Introduzca el ejercicio que desea ejecutar", 1, 4)
    if numero == 1:
        ejercicio()
    elif numero == 2:
        reloj_terminal()
    elif numero == 3:
        crear_contadortxt()
    elif numero == 4:
        G = Gestor()
        G.agregar(Personaje("Caballero",4,2,4,2))
        G.agregar(Personaje("Guerrero",2,4,2,4))
        G.agregar(Personaje("Arquero",2,4,1,8))
        G.mostrar()
        G.mostrar()
        G.borrar("Arquero")
        G.borrar("Caballera")
        G.mostrar()