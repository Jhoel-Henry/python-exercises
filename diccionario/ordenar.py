#Se va a ordenar este diccionario de estudiantes de mayor a menor sin usar "sort"
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

def bubble_sort(estudiantes):
  for i in range (len(estudiantes)):
    for j in range(len(estudiantes)-1):
      if(estudiantes[j]["nota"]< estudiantes[j+1]["nota"]):
        tmp = estudiantes[j]
        estudiantes[j]= estudiantes[j+1]
        estudiantes[j+1]= tmp
  
  return estudiantes

print(bubble_sort(estudiantes))