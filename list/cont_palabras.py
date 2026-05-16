#Basicamente es una lista de palabras, pero el objetivo principal es mostrrar en el res las palabras cuya longitud en mayor a 4 
"""""
def palabra(lista):
  res = []
  for n in lista:
    if len(n)> 4:
      res.append(n)
  return res
"""


#Esta es usando los  List Comprehension
def palabra(lista):
  res = [n for n in lista if len(n) > 4]
  return res

list= ["gato", "perro", "elefante", "oso", "mariposa"]
r= palabra(list)
print(r)