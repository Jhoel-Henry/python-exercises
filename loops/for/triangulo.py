numero_filas= int(input("Ingrese el numero de filas que quiere que tenga el triángulo :"))
for fila in range(1, numero_filas+1):
  espacios = ' '*(numero_filas-fila)
  asteriscos= '*'*(2* fila -1)
  print(espacios + asteriscos+ "\n")