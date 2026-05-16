print("Calcular la potencia de un número n elevado a la n utilizando una función recursiva")
def potencia (base, exponente):
  if exponente ==0:
    return 1
  else:
    res = base * potencia(base, exponente-1)
    return res
  
resultado = potencia(10, 3)
print(f"La potencia de 10 elevado a la 3 es {resultado}")
