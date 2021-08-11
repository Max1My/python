import re
class Data:
    def __init__(self,data):
        self.data = data
    @classmethod
    def get_data(cls,data):
        re_data = re.match(r'(\d{2})[-](\d{2})[-](\d{4})',data)
        data = []
        data.append(int(re_data.group(1)))
        data.append(int(re_data.group(2)))
        data.append(int(re_data.group(3)))
        return data
    @staticmethod
    def validation_data(day,month,year):
        if day > 31:
            raise ValueError(f'День не прошел валидацию. Введите заново от 0 - 31!')
        if day < 0:
            raise ValueError(f'День не прошел валидацию. Вы ввели отрицательное число! Принимается только от 0 - 31')
        if month > 12:
            raise ValueError(f'Месяц не прошел валидацию. Введите заново от 1 - 12')
        if month < 1:
            raise ValueError(f'Месяц не прошел валидацию. Вы ввели число меньше 1. Введите заново от 1 - 12')
        if year < 0:
            raise ValueError(f'Год не прошел валидацию. Отрацительные числа не принимаются!')
        print(f'{day} {month} {year}')
d = Data.get_data('31-12-1995')
v = Data.validation_data(d[0],d[1],d[2])

