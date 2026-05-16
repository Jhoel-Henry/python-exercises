print("Calcular el factorial de un número n utilizando una función recursiva")

def factorial(n):
    if n == 0 or n == 1:
        return 1  # caso base
    else:
        return n * factorial(n - 1)  # llamada recursiva

# llamada a la función
resultado = factorial(5)

print(f"El factorial de 5 es {resultado}")