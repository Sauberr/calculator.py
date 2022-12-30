try:
    while True: print(eval(input('>>>:')))
except ZeroDivisionError:
    print('На 0 делить нельзя')
    while True: print(eval(input('>>>:')))
except (NameError,SyntaxError,TypeError)  :
    print('Введите число а не строку или переменною')
