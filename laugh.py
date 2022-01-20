import random

'''Pasaje de parametro por referencia(direccion de memoria) vs valor(valor del parametro)
    cuando se pasa por valor no se modifica la variable del parametro
    los tipos compuestos (listas, arrays, etc) se pasan por referencia 
    los tipos primitivos (numeros, caracteres, etc) se pasan por valor'''
    
def end(n,tira):
  if (n <= 0.6):
   str = tira + "J"
   return str
  elif (n > 0.6 and n <= 0.8):
    str = tira + "K"
    return str
  elif (n > 0.9):
    str = tira + "S"
    return str
  else:
    str = tira + "A"
    return str

def laugh():
  res = ""
  length = random.randint(3,46)
  for i in range(length):
    if i % 2 == 0:
      n = random.random()
      res = end(n,res)
    else:
      res = end(2,res)
  return res

result = laugh()
print(result)