def laugh():
    import random
    length = int(input("Length:"))
    for i in range(length):
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

laugh()