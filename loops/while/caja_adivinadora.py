import random
print("Bienvenido a la caja adivinadora")
aleratorio= random.randrange(1,100)
vidas_jugador= 10
gano = False
while not gano and vidas_jugador > 0:
  
  numero_jugador = int(input("Ingrese su numero en el rango [1-100]"))
  if numero_jugador < aleratorio:
    print("Su número esta por debajo del número aleatorio\n Intentelo nuevamente\n")
    vidas_jugador-=1
    print(f"Vidas restantes: {vidas_jugador}\n")
  elif numero_jugador > aleratorio:
    print("Su número esta por encima del número aleatorio\n Intentelo nuevamente\n")
    vidas_jugador-=1
    print(f"Vidas restantes: {vidas_jugador}\n")
    
  elif numero_jugador==aleratorio:
    print("Felicidades usted a ganado el juego!!!")
    gano = True

  if vidas_jugador==0:
    print("PERDISTE :(")
    gano = True
  
    