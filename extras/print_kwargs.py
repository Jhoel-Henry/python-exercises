print("Imprimir detalles de una persona")
def imprimir_d_persona(**kwargs):
  #EL **kwargs permite recibir un número variable de argumentos con nombre, y los almacena en un diccionario llamado kwargs. Cada clave del diccionario representa el nombre del argumento, y su valor correspondiente es el valor pasado al llamar a la función.
  print("Detalles de la persona:")
  for clave, valor in kwargs.items():
    print(f"{clave}: {valor}")
  #son argumentos variables con nombre, lo que significa que puedes pasar cualquier cantidad de argumentos con nombre a la función, y se almacenarán en el diccionario kwargs. Luego, puedes acceder a estos argumentos utilizando sus claves dentro de la función.
imprimir_d_persona(nombre="Juan", edad=30, ciudad="Madrid", profesion="Ingeniero")