print('***Sistem de Administración de cuentas***')

salir=False
while not salir:
  print(f'''Menu de opciones:
  1. Crear cuenta
  2. Eliminar cuenta
  3. Salir''')
  opcion=int(input('Ingrese una opción: '))
  if opcion==1:
    print('Cuenta creada \n')
  elif opcion==2:
    print("Cuenta eliminada \n")
  elif opcion==3:
    print('Saliendo del sistema')
    salir=True