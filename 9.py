'''9. Construir una función que reciba un entero y le calcule su factorial sabiendo que el
factorial de un número es el resultado de multiplicar sucesivamente todos los enteros
comprendidos entre 1 y el número dado. El factorial de 0 es 1. No están definidos los
factoriales de números negativos.
'''
def factorial(entero):
    if entero == 0:
        return 1
    elif entero > 0:
        fact = 1
        for i in  range(1,entero + 1):
            fact = fact * i
        return fact

def main():
    try:
        entero = int(input("Ingrese un numero entero: "))
        if entero < 0:
            print("El factorial de un negativo no esta definido")
        else:
            f = factorial(entero)
            print ("El factorial del numero es :",f)
    except ValueError:
        print("Error")

if __name__ == '__main__':
    main()