
def initial_diceroll():
    from random import randrange

    a = []
    for i in range(4):
        a.append(randrange(1,7))
    a.sort()
    total = a[1] + a[2] + a[3]
    return total


def diceroll(number_of_dice, number_of_sides):
    from random import randrange
    a = 0
    for i in range(number_of_dice):
        a += randrange(1, (number_of_sides + 1))
    return a
