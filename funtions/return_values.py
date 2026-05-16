print("Regresar tuplas desde una funcion")

def persona_mayusculas(nombre, apellido, edad):
  print(f"Esta funcion regresa varios valores (tupla)")
  return nombre.upper(), apellido.upper(), edad

nombre, apellido, edad= persona_mayusculas("Jose", "Hernandes", 23)
print(f"Resulado Persona : nombre {nombre}, apellido: {apellido}, edad:{edad}")