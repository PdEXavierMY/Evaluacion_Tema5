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
    try:
        contador = int(contenido)
        if len(sys.argv) == 2:
            if sys.argv[1] == "inc":
                contador += 1
            elif sys.argv[1] == "dec":
                contador -= 1
        print(contador)
        contadortxt = open("contador.txt", "w")
        contadortxt.write(str(contador))
        contadortxt.close()
    except:
        print("Error: Fichero corrupto.")

if __name__ == "__main__":
    crear_contadortxt()