for a in range (1000):
    f = True
    for x in range (250):
        for y in range (250):
            if not ((x + 2 * y < a) or (y > x) or (x > 30)):
                f = False
    if f == True:
        print(a)
