from spells import get_invocations_name, get_invocation_description

x = get_invocations_name(2)
print(x)
print('\n')
for i in x:
    print('***' + i + '***')
    x = get_invocation_description(i)
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
    print(result + '\n')