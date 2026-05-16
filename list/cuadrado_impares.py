#Dada una lista , lo que se requiere es elevar al cuadrado cada numero impar de la lista
def cuadrado_impares(lista):
  res = [n**2 for n in lista if n%2 != 0 ]
  return res

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res= cuadrado_impares(numeros)
print (res)