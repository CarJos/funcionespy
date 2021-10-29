''' 14. Construir una función que reciba como parámetros dos números enteros y retorne el
valor del mayor. 
'''
def comparacion_dos(ent1,ent2):
    if ent1 > ent2:
        return ent1
    elif ent2 > ent1:
        return ent2
    else:
        return "Ambos numeros son iguales"

def main():
    try:
        ent1 = int(input("Ingrese el primer numero entero: "))
        ent2 = int(input("Ingrese el segundo numero entero: "))
        comp = comparacion_dos(ent1,ent2)
        print(comp)
    except ValueError:
        print("Error")

if __name__ == '__main__':
    main()