''' 7. Construir una función que reciba como parámetro un carácter y retorne el código ASCII
asociado a él. 
'''
#validar solo un caracter
def ascii_a_entero(caracter):
    entero = ord(caracter)
    return entero
def main():
    try:
        caracter = input("Ingrese un caracter: ")
        if len(caracter) == 1:
            ent_ascii = ascii_a_entero(caracter)
            print("El codigo ascii que pertenece a",caracter,"es: ",ent_ascii)
        else:
            print("Debe ingresar solo un caracter")
    except ValueError:
        print("Error")

if __name__ == '__main__':
    main()