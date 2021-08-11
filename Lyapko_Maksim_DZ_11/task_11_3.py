class ClassIntList:
    def __init__(self, value):
        self.value = value
        if value is None:
            self.get_list()
        if not isinstance(value, (int)):
            raise IntValueError(value)
    def get_list(self):
        return self.empy_list

class IntValueError(Exception):
    def __init__(self,value):
        self.value = value

    def __str__(self):
        return '{} Неверный формат введенных данных. Вы можете вносить только целые числа.'.format(self.value)

empy_list = []
while True:
    command = input('Введите целые числа: ')
    if command == 'stop':
        for obj in empy_list:
            print(obj.value, sep = ' ')
        break
    else:
        command = int(command)
        empy_list.append(ClassIntList(command))
