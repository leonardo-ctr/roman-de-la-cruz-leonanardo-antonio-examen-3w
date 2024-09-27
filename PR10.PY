n = int(input("Ingresa un numero entero: "))

if n < 0:
    print("El factorial no esta definido para numeros negativos.")
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print("El factorial de", n," es ",factorial,)