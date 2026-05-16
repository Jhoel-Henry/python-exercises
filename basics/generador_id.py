from random import randint
print("--- Generador de IDs Únicos ---")
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
year_of_birth = input("Ingrese su año de nacimiento (YYYY): ")
nombre= nombre.strip().upper()[0:2]
apellido= apellido.strip().upper()[-2:]
year_of_birth= year_of_birth.strip()[2:4]

aleatorio= randint(1000,9999)

id_unico= f"{nombre}{apellido}{year_of_birth}{aleatorio}"

print(f"""\nHola {nombre}, 
      su ID único es: {id_unico}
      FELICIDADES!
""")