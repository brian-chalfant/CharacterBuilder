from modifiers import BColors, validate_choice, full_languages


def choose_language(known_languages):
    print(BColors.UNDERLINE + 'Choose an additional Language')
    print(BColors.ENDC)
    for key, value in full_languages().items():
        if value not in known_languages:
            print(key, value)
        else:
            continue
    x = validate_choice(full_languages().items())
    return full_languages().get(x)

