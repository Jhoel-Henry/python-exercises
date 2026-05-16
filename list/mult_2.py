#Dada una lista lo que se quiere realizar en multiplicar p*2 a cada elemento de lallista
def mult_2(lista):
  res = [n*2 for n in lista ]
  return res

list= [3, 7, 1, 9, 2, 8, 4, 6, 5]
prueba = mult_2(list)
print(prueba)