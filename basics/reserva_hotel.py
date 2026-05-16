print("Bienvenido! Sistema de Reserva de Hoteles: ")
nombre_cliente= input("Ingrese su nombre: ")
dias_estancia= int(input("Ingrese sus días de estadía: "))
cuarto_vista_mar=input("¿Quiere su habitación vista al mar?: ").strip().lower()
cuarto_vista_mar= "si"

print("DATOS: \n----------------------------\n")
print(f"""
Cliente: {nombre_cliente}
Días de estancia: {dias_estancia}
Precio $50.0
Habitacion con vista al mar: {cuarto_vista_mar}""")
