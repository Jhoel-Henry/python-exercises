print("Sistema de inventario de una tienda boliviana")

# Base de datos de una tienda (ES UNA TUPLA DE DICCIONARIOS, DONDE CADA DICCIONARIO REPRESENTA UN PRODUCTO CON SUS ATRIBUTOS)
productos=[
  {'id':1, 'nombre': 'camisa', 'precio': 140, 'cantidad': 10},
  {'id':2, 'nombre': 'guantes', 'precio': 55, 'cantidad': 20},
  {'id':3, 'nombre': 'pantalon' , 'precio': 100, 'cantidad': 15},
  {'id':4, 'nombre': 'bufanda', 'precio': 200, 'cantidad': 5},
  {'id':5, 'nombre': 'zapatos', 'precio': 300, 'cantidad': 8},
  {'id':6, 'nombre': 'sombrero', 'precio': 80, 'cantidad': 12}
] 

def mostrar_inventario(productos):
  print("Inventario de la tienda:")
  for producto in productos:
    print(f"ID: {producto['id']} - Nombre: {producto['nombre']} - Precio: {producto['precio']} - Cantidad: {producto['cantidad']}")

def agregar_producto(productos, id, nombre, precio, cantidad):
  n_producto = {'id': id, 'nombre': nombre, 'precio': precio, 'cantidad': cantidad}
  productos.append(n_producto)
  print("Producto agregado exitosamente.")

def eliminar_producto_id(productos, id):
  for producto in productos:
    if producto['id'] == id:
      productos.remove(producto)
      print("Producto eliminado exitosamente.")
      break
  else:
    print("Producto no encontrado.")

def mostrar_producto_by_id(productos, id):
  for producto in productos:
    if producto["id"]==id:
      print (f"ID: {producto['id']}, Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
    else:
      print("Producto no encontrado.")
#Programa main

if __name__ == "__main__":
  print("Bienvenido al sistema de inventario de la tienda")
  print(""""Seleccione una opción:
        1. Mostrar inventario
        2. Agregar producto
        3. Eliminar producto por ID
        4. Mostrar producto por ID
        5. Salir""")
  while True:
    opcion = int(input("Ingrese la opcion que desea realizar: "))
    if opcion == 1:
      mostrar_inventario(productos)
    elif opcion ==2:
      id = int(input("Ingrese el ID del producto: "))
      nombre= input("Ingrese el nombre del producto: ")
      precio= float(input("Ingrese el precio del producto: "))
      cantidad= int(input("Ingrese la cantidad que existe del producto: "))
      agregar_producto(productos, id, nombre, precio, cantidad)
    elif opcion == 3:
      id= int(input("Ingrese el ID del producto que desee eliminar: "))
      eliminar_producto_id(productos, id)
    elif opcion == 4:
      id= int(input("Ingrese el ID del producto que desea mostrar: "))
      mostrar_producto_by_id(productos, id)
    elif opcion == 5:
      print("Gracias por usar el sistema de inventario de la tienda. ¡Hasta luego!")
      break
    