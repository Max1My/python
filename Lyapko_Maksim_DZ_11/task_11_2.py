class MyError(Exception):
    def __init__(self,text):
        self.text = text

try:
    a = int(input('Введите делимое: '))
    b = int(input('Введите делитель: '))
    if b < 1:
        raise MyError('На поль делить нельзя!')
except MyError as err:
    # b = int(input('Введите делитель: '))
    b += 1
    print(f'result: {a//b}')
else:
    print(f'{a//b}')