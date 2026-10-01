#Un programa que tiene los siguientes objetivos:
#1. promedio / 2. nota más alta / 3. estudiante con la nota mas baja / 4. aprobacion >= 60 / 5. Mostrar nombres de los aprobados

estudiantes = [
  {"nombre": "Jose", "nota": 56},
  {"nombre": "Juan", "nota": 46},
  {"nombre": "Lorena", "nota": 92},
  {"nombre": "Jhoel", "nota": 95},
  {"nombre": "Josue", "nota": 99},
  {"nombre": "Jhon", "nota": 87},
  {"nombre": "Aida", "nota": 90},
  {"nombre": "Santiago", "nota": 59},
  {"nombre": "Steven", "nota": 46},
  {"nombre": "Matias", "nota": 78},
  {"nombre": "Kadir", "nota": 34},
  {"nombre": "Mehmet", "nota": 89}

]

def promedio (estudiantes):
  prom = 0;
  c=0
  for estudiante in estudiantes:
    prom = prom + estudiante["nota"]
    c+=1
  
  prom = prom /c
  print(f"Promedio : {prom}")


def max_nota(estudiantes):
  max =-1
  mjr_est = " "
  for estudiante in estudiantes:
    if estudiante["nota"]>= max:
      max = estudiante["nota"]
      mjr_est = estudiante["nombre"]

  print (f"Mejor estudiante : {mjr_est}")

def min_nota(estudiantes):
  max =100
  peor_est = " "
  for estudiante in estudiantes:
    if estudiante["nota"]<= max:
      max = estudiante["nota"]
      mjr_est = estudiante["nombre"]

  print (f"Peor estudiante : {peor_est}")

#numero de aprobados
def aprobados(estudiantes):
  aprobados=0
  for estudiante in estudiantes:
    if estudiante["nota"]>=60:
      aprobados+=1

  print (f"Número de aprobados: {aprobados}")

#mostrar a los aprobados :
def mostrar_aprobados(estudiantes): 
  for estudiante in estudiantes:
    if estudiante["nota"]>=60:
      print(estudiante)

promedio(estudiantes)
max_nota(estudiantes)
min_nota(estudiantes)
aprobados(estudiantes)
mostrar_aprobados(estudiantes)