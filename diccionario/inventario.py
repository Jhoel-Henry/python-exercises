print("Sistema de inventarios: ")

inventario = []

numero_productos = int(input("Ingrese el numero de productos que desea añadir: "))

for indice in range (numero_productos):
  print(f"Proporcione los valores del producto {indice+1}")
  nombre = input("Ingrese el nombre del producto:")
  precio = float(input("Ingrese el precio del producto: "))
  cantidad= int(input("Ingrese la cantidad del producto: "))

  producto = {'id': indice, 'nombre': nombre, 'precio': precio, 'cantidad': cantidad}

  inventario.append(producto)

#Mostrar el inventario inicial

print(f'\nInventario inicial: {inventario}')