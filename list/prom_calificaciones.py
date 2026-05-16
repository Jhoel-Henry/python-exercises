nro_calificaciones= int(input("Proporciona el numero de calificaciones a evaluar:"))
calificaciones=[]
for indice in range (nro_calificaciones):
  calificacion= float(input(f"Ingrese el dato {indice +1}:  \n"))
  calificaciones.append(calificacion)

sum_califiaciones = sum(calificaciones)
promedio = sum_califiaciones  / nro_calificaciones
print(f"El promedio total de las calificaciones totales es: {promedio}")