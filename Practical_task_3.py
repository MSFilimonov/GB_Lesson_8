class Error(Exception):
    def __init__(self):
        pass


class TypeCheck:
    def __init__(self):
        self.my_list = []

    def check_value(self):
        global user_values
        while True:
            try:
                try:
                    user_values = int(input('Введите числа: '))
                    val = input(f'Введено число "{user_values}" . Для прекращения введите stop : ').lower()
                    self.my_list.append(user_values)
                    if val == 'stop':
                        print(self.my_list)
                        break
                except ValueError:
                    raise Error
            except Error:
                val = input(f"Введено не число! Для прекращения введите stop : ").lower()
                if val == 'stop':
                    print(self.my_list)
                    break
                else:
                    self.check_value()


a = TypeCheck()
a.check_value()
