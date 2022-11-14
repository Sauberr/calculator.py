try:
    while True: print(eval(input('>>>:')))
except ZeroDivisionError:
    print('На 0 делить нельзя')
    while True: print(eval(input('>>>:')))
except NameError:
    print('Введите число а не строку или переменною')
    while True: print(eval(input('>>>:')))
except SyntaxError:
    print('Введите заново число')
    while True: print(eval(input('>>>:')))
except TypeError:
    print('Введите число а не что то другое ')
    while True: print(eval(input('>>>:')))
