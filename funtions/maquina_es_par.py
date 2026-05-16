print("Verificación si un número es par o impar:")
def es_par(numero):
  if(numero %2 ==0):
    return True
  else:
    return False
#Llamanos a la función con diferentes números para verificar si son pares o impares
if __name__ =='__main__':
  numero = int(input("Ingrese un número: "))
  print(f'Numero par? {es_par(numero)}')