def pares(lista):
  res = []
  for n in lista:
    if n % 2 ==0:
      res.append(n)

  return res
  
#ejemplo usando una lista
lista = [2,3,3,12,5,6,7,50,4]
n_par = pares(lista)
print (n_par)