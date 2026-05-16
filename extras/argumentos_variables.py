def superheroe_superpoderes(superheroe, nombre, *args):
  print(f"Superheroe: {superheroe}-{nombre}-{args}")
  for superpoder in args:
    print(f"Superpoder: {superpoder}")

superheroe_superpoderes("Spiderman", "Tom Holland", "Telaraña", "Super Telaraña")
