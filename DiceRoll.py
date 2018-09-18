
def diceroll():
    from random import randrange

    a = []
    for i in range(4):
        a.append(randrange(1,7))
    a.sort()
    total = a[1] + a[2] + a[3]
    return total

