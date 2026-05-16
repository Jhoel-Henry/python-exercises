print("Base de datos de una tienda")

productos=[
  ('TR001', 'Gomlek', 140),
  ('TR002', 'eldivenler', 55),
  ('TR003', 'tisort' , 100),
  ('TR003', 'atki', 200)
]

print("Informacion de los productos: ")

for producto in productos:
  #Aplicando el concepto de PACKING
  id, descripcion, precio = producto
  print(f"PRODUCTO: id = {id} , descripcion = {descripcion} , precio = {precio}")