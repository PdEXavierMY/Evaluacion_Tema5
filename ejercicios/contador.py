from io import open
import sys

def crear_contadortxt():
    contadortxt = open("contador.txt", "a+") 
    contadortxt.seek(0)
    contenido = contadortxt.readline()
    if len(contenido) == 0:
        contenido = "0"
        contadortxt.write(contenido)
    contadortxt.close()
    