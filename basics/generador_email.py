nombre=input("Ingrese su nombre: ")
apellido=input("Ingrese su apellido: ")
empresa=input("Ingrese el nombre de la empresa: ")
entension_dominio=input("Ingrese la extensión de dominio (com, org, net): ")

nombre = nombre.lower().replace(" ",".")
apellido = apellido.lower().replace(" ",".")
empresa = empresa.lower().replace(" ","")
email = f"{nombre}.{apellido}@{empresa}.{entension_dominio}"

print(f"Su correo electrónico generado es: {email}")