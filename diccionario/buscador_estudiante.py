#Basicamente buscar a un estudiante por su nombre , mostrarlo y si no hay mostrar en pantalla que no existe ese estudiante:

estudiantes = [
  {"nombre": "Marcos", "nota": 56},
  {"nombre": "Josias", "nota": 26},
  {"nombre": "Lorena", "nota": 94},
  {"nombre": "Jhoel", "nota": 94},
  {"nombre": "Josue", "nota": 96},
  {"nombre": "Jhon", "nota": 88},
  {"nombre": "Aida", "nota": 90},
  {"nombre": "Hamza", "nota": 59},
  {"nombre": "Steve", "nota": 46},
  {"nombre": "Herlam", "nota": 78},
  {"nombre": "Kadir", "nota": 34},
  {"nombre": "David", "nota": 89}

]

def buscar_estudiante(estudiantes):
  est= input("Ingrese el estudiante que quiere buscar: ")
  for estudiante in estudiantes:
    if estudiante["nombre"] == est:
      print (f"""Estudiante encontrado: 
            Nota : {estudiante["nota"]}""")
      break
  else:
    print("No encontrado")
    
  

buscar_estudiante(estudiantes)