import random

def end(n,res):
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
      res = end(n,res)
    else:
      res = end(2,res)
  return res

result = laugh()
print(result)