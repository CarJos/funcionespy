'''15. Construir una función que reciba como parámetros dos números enteros y retorne 1 si
el primer número es múltiplo del segundo y 0 si no. 
'''
def multiplo_enteros(ent1,ent2):
    if ent1 % ent2 == 0:
        return 1
    else:
        return 0

def main():
    try:
        ent1 = int(input("Ingrese el primer numero entero: "))
        ent2 = int(input("Ingrese el segundo numero entero: "))
        mult = multiplo_enteros(ent1, ent2)
        print(mult)
        
    except ValueError:
        print("Error")
a
if __name__ == '__main__':
    main()