print("Welcome to our first version of our CALCULATOR:")
salir = False
while not salir:
  print(f"""Menu de opciones:
  1. Suma
  2. Resta
  3. Multiplicación
  4. División
  5. Limpiar valores
  6. Salir""")
  opcion = int(input("Ingrese una opción: "))
  if opcion ==1:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = num1+num2
    print(f"El resultado de la suma es: {resultado}")
  elif opcion == 2:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = num1-num2
    print(f"El resultado de la resta es: {resultado}")
  elif opcion == 3:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    resultado = num1*num2
    print(f"El resultado de la multiplicación es: {resultado}")
  elif opcion == 4:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    if num2 == 0:
      print("No se puede dividir por cero")
    else:
      resultado = num1/num2
      print(f"El resultado de la división es: {resultado}")
  elif opcion == 5:
    print("Limpiando valores...")
  elif opcion == 6:
    print("Saliendo de la calculadora")
    salir = True

