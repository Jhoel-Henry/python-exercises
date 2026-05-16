metas_pasos_diarios=10000
calorias_por_paso=0.04

nombre_usuario= input("Ingrese su nombre: ")
pasos_dia= int(input("¿Cuantos pasos caminaste el día de hoy?: "))

meta_alcanzada= pasos_dia>= metas_pasos_diarios
meta= 'si' if meta_alcanzada else 'no'
calorias_quemadas= pasos_dia * calorias_por_paso

print(f"""\n Hola {nombre_usuario}
      Pasos caminados hoy: {pasos_dia}
      Calorias quemadas: {calorias_quemadas}
      Meta de pasos alcanzada {meta}
      Meta de pasos diarios es: {metas_pasos_diarios}""")