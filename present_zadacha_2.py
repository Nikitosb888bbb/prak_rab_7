first_number=float(input('Введите первое число: '))
second_number=float(input('Введите второе число: '))
operation=str(input('Введите операцию (+-*/): '))

match operation:
    case '+':
        result=first_number+second_number
    case '-':
        result=first_number-second_number
    case '*':
        result=first_number*second_number
    case '/':
        result=first_number/second_number
    case _:
        print('Неизвестная операция!')
print('')
print(f'Результат операции: {operation}, с числами {first_number} и {second_number} равен = {result}')