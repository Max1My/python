class WareHouse:
    address = 'Moscow'
    tel = '8(495)603-20-12'
class Characteristic:
    capacity = 6000
    num_of_empoyees = 100
class Office_equipment:
    inventory = {
        'Canon':100,
        'Xerox':20,
        'Kyocera':200
    }
    def __init__(self,brand,amount):
        self.brand = brand
        self.amount = amount
    def add_equipment(brand,amount):
        if not isinstance(amount, (int)):
            print(f'Принимаются только целые числа!')
        if brand in Office_equipment.inventory:
            Office_equipment.inventory[brand] = amount
        else:
            print(f'{brand} не числится на складу')
class Printer(Office_equipment):
    brand = 'Kyocera'
    inv_number = '10.22.3.000'
class Scanner(Office_equipment):
    brand = 'Canon'
    inv_number = '10.22.5.000'
class Xerox(Office_equipment):
    brand = 'Xerox'
    inv_number = '10.22.6.000'

O = Office_equipment.add_equipment('Canon',50)
print(Office_equipment.inventory)