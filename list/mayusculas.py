def mayucula(lista):
  res = [n.upper() for n in lista]
  return res

list = ["juan, miguel, lorena, domingo, naomi, chrsitian, carlos, josue, sofia, jessica, santiago, ahmet"]
r = mayucula(list)
print(r)