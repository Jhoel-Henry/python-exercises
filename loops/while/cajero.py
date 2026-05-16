print(f"""Bievenido a el cajero automatico, sleccione una opcion:
1. Retirar dinero
2. Depositar dinero
3. Consultar saldo
4. Salir""")
saldo=1000
salir=False
while not salir:
  opcion= int(input("Igrese una opción: "))
  if opcion==1:
    monto = int(input("Ingrese el monto que quiere retirar:"))
    if monto > saldo:
      print("No tiene suficiente saldo para retirar esa cantidad")
    else:
      saldo -= monto
      print("Retiro exitoso")
  elif opcion==2:
    monto = int(input("Ingrese el monto que desea depositar:"))
    saldo += monto
    print("Deposito exitoso")
  elif opcion==3:
    print(f"Su saldo actual es: {saldo}")

  elif opcion==4:
    print("Saliendo del cajero automatico")
    salir=True
