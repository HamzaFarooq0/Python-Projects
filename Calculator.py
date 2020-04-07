val1 = int(input('Enter first value: '))
val2 = int(input('Enter second value: '))
opr = input('Enter Operator: ')

if opr == '+':
    val = val1 + val2
    print(val)
elif opr == '-':
    val = val1 - val2
    print(val)
elif opr == '/':
    val = val1 / val2
    print(val)
elif opr == '*':
    val = val1 * val2
    print(val)
else:
    print('Enter Valid operator!')