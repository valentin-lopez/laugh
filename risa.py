import random

def risa():
  largo = int(input("Largo de la risa:"))
  for i in range(largo):
    if i % 2 == 0:
      n = random.random()
      if (n <= 0.6):
        print("J",end = '')
      elif (n > 0.6 and n <= 0.8):
        print("K", end = '')
      elif (n > 0.8):
        print("JJ", end = '')
  else:
        print("A", end = '')

risa()
