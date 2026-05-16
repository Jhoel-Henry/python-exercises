print("Suma de argumentos variables:")
def sumar (*args):
  total =0
  for numero in args:
    total += numero
  return total
resultado = sumar(10, 13, 34, 22, 2)

print(f"El resultado de la suma es: {resultado}")