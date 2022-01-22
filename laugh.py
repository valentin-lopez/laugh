import random

def addLetter(n,res):
    '''Pasaje de parametro por referencia(direccion de memoria) vs valor(valor del parametro)
    cuando se pasa por valor no se modifica la variable del parametro
    los tipos compuestos (listas, arrays, etc) se pasan por referencia 
    los tipos primitivos (numeros, caracteres, etc) se pasan por valor'''

def addLetter(n,res):
  if (n <= 0.6):
   str = res + "J"
   return str
  elif (n > 0.6 and n <= 0.8):
    str = res + "K"
    return str
  elif (n > 0.9):
    str = res + "S"
    return str
  else:
    str = res + "A"
    return str

def laugh():
  res = ""
  length = random.randint(3,46)
  for i in range(length):
    if i % 2 == 0:
      n = random.random()
      res = addLetter(n,res)
    else:
      res = addLetter(2,res)
  return res
result = laugh()
print(result)