class Stationery:
    title = 'Портрет'
    def draw(self):
        print(f'Запуск отрисовки {Stationery.title}а')
class Pen(Stationery):
    def draw(self):
        print(f'Зарисовка {Stationery.title}a')
class Pencil(Stationery):
    def draw(self):
        print(f'Создание подписи {Stationery.title}a')
class Handle(Stationery):
    def draw(self):
        print(f'Обведение {Stationery.title}a')

s = Stationery()
s.draw()
p = Pen()
p.draw()
Pl = Pencil()
Pl.draw()
h = Handle()
h.draw()