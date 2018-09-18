
def diceroll(number, sides):
    from random import randrange

    a = 0
    b = 0
    for i in range(3):
        a = 0
        for j in range(number):
            a += randrange(1, (sides + 1))
        if b == 0:
            b = a
        else:
            if a > b:
                b = a
    return b

