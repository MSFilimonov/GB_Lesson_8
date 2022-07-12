class OfficeEquipmentWarehouse:
    print('Склад')


class OfficeEquipment:
    def __init__(self, producer, color):
        self.producer = producer
        self.color = color


class Printer(OfficeEquipment):
    amount_pr = 0

    def __init__(self, producer, color, pr_type):
        super().__init__(producer, color)
        self.pr_type = pr_type
        Printer.amount_pr += 1

    @staticmethod
    def name():
        return ' Принтер '

    def type_printer(self):
        return self.pr_type

    def __str__(self):
        return 'производитель: {}\n цвет: {}\n   тип принтера: {}\n'.format(self.producer, self.color, self.pr_type)


class Scanner(OfficeEquipment):

    amount_sc = 0

    def __init__(self, producer, color, sc_sensor):
        super().__init__(producer, color)
        self.sc_sensor = sc_sensor
        Scanner.amount_sc += 1

    @staticmethod
    def name():
        return'Сканер'

    def type_sensor(self):
        return self.sc_sensor

    def __str__(self):
        return 'производитель: {}\n цвет: {}\n тип сенсора: {}\n'.format(self.producer, self.color, self.sc_sensor)


class Xerox(OfficeEquipment):

    amount_x = 0

    def __init__(self, producer, color, xer_mfu):
        super().__init__(producer, color)
        self.xer_mfu = xer_mfu
        Xerox.amount_x += 1

    @staticmethod
    def name():
        return 'Ксерокс'

    def mfu_module(self):
        return self.xer_mfu

    def __str__(self):
        return 'производитель: {}\n цвет: {}\n МФУ: {}\n'.format(self.producer, self.color, self.xer_mfu)


p = Printer('Epson', 'серый', 'струйный')
p2 = Printer('HP', 'белый', 'лазерный')
print(p.name(), p.amount_pr, "шт")
print(p.__str__())
print(p2.__str__())

s = Scanner('Epson', 'серый', 'CIS')
s2 = Scanner('Canon', 'черный', 'CCD')
print(s.name(), s.amount_sc, "шт")
print(s.__str__())
print(s2.__str__())

x = Xerox('HP', 'белый', 'есть')
x2 = Xerox('Canon', 'черный', 'нет')
print(x.name(), x.amount_x, "шт")
print(x.__str__())
print(x2.__str__())
