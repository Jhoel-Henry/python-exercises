correcto = False
while not correcto:
  print("Cree su contraseña: \nDebe tener al menos 8 caracteres, una mayúscula, una minúscula y un número")
  contrasena= input("Ingrese su contraseña: ")
  if len(contrasena) < 8:
    print("La contraseña debe tener al menos 8 caracteres")
  elif not any(c.isupper() for c in contrasena):
    print("La contraseña debe tener al menos una letra mayúscula")
  elif not any(c.islower() for c in contrasena):
    print("La contraseña debe tener al menos una letra minúscula")
  elif not any(c.isdigit() for c in contrasena):
    print("La contraseña debe tener al menos un número")
  else:
    correcto = True
    print("Contraseña creada exitosamente")