import os
from introducir import solicitar_introducir_numero_extremo, solicitar_introducir_si_o_no
from ejercicios.calculo import ejercicio
from ejercicios.reloj import reloj_terminal
from ejercicios.contador import crear_contadortxt
from ejercicios.gestor import Gestor, Personaje
import time

def launcher():
    numero = solicitar_introducir_numero_extremo("Introduzca el ejercicio que desea ejecutar", 1, 4)
    if numero == 1:
        ejercicio()
    elif numero == 2:
        reloj_terminal()
    elif numero == 3:
        crear_contadortxt()
        modifica_contador = solicitar_introducir_si_o_no("¿Quieres incrementar o reducir el contador? (Sí/No)): ")
        if modifica_contador:
            numero = solicitar_introducir_numero_extremo("¿Quieres incrementarlo o reducirlo? (Incrementarlo=1, Reducirlo=2)", 1, 2)
            if numero == 1:
                os.system("python3 ejercicios/contador.py inc")
            elif numero == 2:
                os.system("python3 ejercicios/contador.py dec")
    elif numero == 4:
        ges = Gestor()
        print("Añadimos personajes:\n")
        print("Añadiendo caballero...")
        time.sleep(1)
        ges.agregar(Personaje("Caballero",4,2,4,2))
        print("Añadiendo guerrero...")
        time.sleep(1)
        ges.agregar(Personaje("Guerrero",2,4,2,4))
        print("Añadiendo arquero...")
        time.sleep(1)
        ges.agregar(Personaje("Arquero",2,4,1,8))
        ges.mostrar()
        print("Borramos arquero...")
        time.sleep(1)
        ges.borrar("Arquero")
        ges.mostrar()