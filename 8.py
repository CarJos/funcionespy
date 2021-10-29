'''8. Construir una función que reciba como parámetro un entero y retorne 1 si dicho entero
está entre los 30 primeros elementos de la serie de Fibonacci. Deberá retornar 0 si no es
así.
'''
def comprobar_fibonacci(entero):
    fibonacci = []
    vi = 0
    vf = 1
    cont = 0
    fibonacci.append(vi)
    fibonacci.append(vf)
    
    for i in range(28):
        val = vi + vf
        vi = vf
        vf = val
        fibonacci.append(val)
    
    for i in range(len(fibonacci)):
        if fibonacci[i] == entero:
            cont += 1
    
    if cont > 0:
        return 1
    else:
        return 0
def main():
    try:
        entero = int(input("Ingrese un numero entero: "))
        fibo = comprobar_fibonacci(entero)
        print (fibo)
    except ValueError:
        print("Error")

if __name__ == '__main__':
    main()