class Error(Exception):
    pass


class MyZeroDivisionError(Error):
    pass


while True:
    try:
        number_1 = int(input('Введите делимое: '))
        number_2 = int(input('Введите делитель: '))
        if number_2 == 0:
            raise MyZeroDivisionError

        elif type(number_1) == int or type(number_2) == int:
            print(number_1 / number_2)
            break
    except MyZeroDivisionError:
        print('Деление на ноль недопустимо')
