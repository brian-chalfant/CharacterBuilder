
def diceroll(number, sides):
    from random import randrange
    a = 0
    for i in range(number):
        a += randrange(1, (sides + 1))
    return a
