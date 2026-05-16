print("Agenda de Contactos: ")

agenda = {
  'Carlos': {
    'telefono': '71755551',
    'gmail': 'carlosestefano@gmail.com',
    'direccion': 'Vinto 35 Qllo'
  },
  'Marcos':{
    'telefono': '55647377',
    'gmail': 'marijimenez@gmail.com',
    'direccion': 'Suticollo'
  },
  'William':{
    'telefono': '55325522',
    'gmail': 'willamcussi@gmail.com',
    'direccion': 'Zona Licenciada'
  }
}

print(agenda)

#Acceder a la infroacion en especifico

print(f'''Informacion de contacto de Wlliam: 
      Telefono: {agenda['William']['telefono']}
      Gmail: {agenda.get('William').get('gmail')}''')

#Add a new component 
agenda['Jose']={
  'telefono': '98393384',
  'gmail': 'joseflores@gmail.com',
  'direccion': 'Calle Rosas entre Chaco y Puerto Suarez'
  ''

}

#Delete a component
agenda.pop('Marcos')
#del agenda('Marcos')
print(agenda)

#Contactos en la agenda
print("\nContactos de la agenda:")

for nombre, detalle in agenda.items():
  print(f"""
  Nombres: {nombre}
  Telefono: {detalle.get('telefono')}
  Gmail: {detalle.get('gmail')}
  Direccion: {detalle.get('direccion')}""")
