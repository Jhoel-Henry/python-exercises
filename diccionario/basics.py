print("Diccionarios en Python")

persona ={
  'nombre': 'Jose',
  'edad': 19,
  
  'Pais': 'France'

}
print(f'Diccionario de persona: {persona}')
#Acceder internamente al diccionario

print(f'Nombre: {persona['nombre']}')
print(f'Edad: {persona.get('edad')}')

# Iterar elementos de un diccionario(llave, valor)
for llave, valor in persona.items():
  print(f'Llave: {llave}, valor : {valor}')

#Obtener los valores 
print("SOLO valores del diccionario: \n")
for valor in persona.values():
  print(f'-valor: {valor}')

#Obtener los elementos:
print("solos las LLAVES del diccionario")
for llave in persona.keys():
  print(f'-llave: {llave}')