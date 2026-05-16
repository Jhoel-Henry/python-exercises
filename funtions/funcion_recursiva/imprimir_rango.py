#Una funcion recursiva, es aquella que se llama a mi misma dentro de su misma definicion.
#donde se tiene una condicion de parada, para evitar que se llame a si misma infinitamente.
def imprimir_rango(n):
  if n<=0:
    return #condicion de parada, para evitar que se llame a si misma infinitamente.
  print(n)
  imprimir_rango(n-1) #llamada recursiva, donde se llama a la misma funcion con un valor diferente, en este caso n-1.
imprimir_rango(10) #llamada a la funcion, donde se le pasa un valor inicial, en este caso 10.
