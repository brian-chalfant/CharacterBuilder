from spells import get_invocations_name, get_invocation_description


def num2word(number):
    import inflect
    x = inflect.engine()
    return x.number_to_words(number)


def warlock_slots(level):
    if level < 2:
        return 0
    if level < 5:
        return 2
    if level < 7:
        return 3
    if level < 9:
        return 4
    if level < 12:
        return 5
    if level < 15:
        return 6
    if level < 18:
        return 7
    else:
        return 8


def get_description(name):
    x = get_invocation_description(name)
    max_width = 60
    result = ""
    col = 0
    for word in x[0].split():
        end_col = col + len(word)
        if col != 0:
            end_col += 1
        if end_col > max_width:
            result += '\n'
            col = 0
        if col != 0:
            result += ' '
            col += 1
        result += word
        col += len(word)
    rtn = (result + '\n')
    return rtn


def invocation_cycling(slots):
    slot = 0
    invocations = []
    x = get_invocations_name(0)
    while slot < slots:
        count = 1
        print("ELDRITCH INVOCATIONS:  Please Select " + str(num2word(slots - slot).capitalize() +
                                                            "(" + str(slots - slot) + ")") + " Invocation Spells")
        for i in x:
            print(str(count) + ": " + i)
            count += 1
        selection = int(input("type the number to see spell description: "))
        print('\n')
        print(x[selection-1])
        print(get_description(x[selection-1]))
        process_item = input("Add to invocation list? (y/n):")
        if process_item.upper() == 'Y':
            invocations.append(x.pop(selection-1))
            slot += 1
        elif process_item.upper() == 'T':
            break
        else:
            continue

    return invocations
