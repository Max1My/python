class Car:
    speed = 60
    color = "Color"
    name = 'Brand'
    is_police = True or False
    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')
    def show_speed(self):
        self.speed

class TownCar(Car):
    is_police = False
    def __init__(self,color,name,speed):
        self.color = color
        self.name = name
        self.speed = speed

    def go(self):
        print(f'{self.name} Начала движение')
    def show_speed(self):
        speed_limit = 60
        if self.speed > speed_limit:
            print(f'{self.name} превысил скорость на {self.speed - speed_limit} км\ч')
        print(f'Текущая скорость {self.speed} км\ч')
    def color_car(self):
        print(f'Цвет автомобиля: {self.color}')
    def name_car(self):
        print(f'Марка машины: {self.name}')
    def turn_left(self):
        print(f'{self.name} повернула налево')
    def turn_right(self):
        print(f'{self.name} повернула направо')
    def stop(self):
        print(f'{self.name} остановилась')
class SportCar(Car):
    is_police = False
    speed = 120
    def __init__(self,color,name,speed):
        self.name = name
        self.color = color
        self.speed = speed
    def name_car(self):
        print(f'Марка машины: {self.name}')
    def color_car(self):
        print(f'Цвет машины: {self.color}')
    def show_speed(self):
        print(f'Текущая скорость {self.name}: {self.speed} км\ч')
    def go(self):
        print('Машина поехала')
    def turn_left(self):
        print(f'{self.name} повернула налево')
    def turn_right(self):
        print(f'{self.name} повернула направо')
    def stop(self):
        print('Машина остановилась')

class WorkCar(Car):
    is_police = False
    def __init__(self,color,name,speed):
        self.speed = speed
        self.color = color
        self.name = name
    def show_speed(self):
        speed_limit = 40
        if self.speed > speed_limit:
            print(f'{self.name} превысил скорость на {self.speed - speed_limit} км\ч')
        print(f'Текущая скорость {self.speed} км\ч')
    def color_car(self):
        print(f'Цвет автомобиля: {self.color}')
    def name_car(self):
        print(f'Марка машины: {self.name}')
    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')
    def turn_left(self):
        print(f'{self.name} повернула налево')
    def turn_right(self):
        print(f'{self.name} повернула направо')
class PoliceCar(Car):
    is_police = True
    speed = 60
    def __init__(self,color,name,speed):
        self.name = name
        self.color = color
        self.speed = speed
    def name_car(self):
        print(f'Марка машины: {self.name}')
    def color_car(self):
        print(f'Цвет машины: {self.color}')
    def show_speed(self):
        print(f'Текущая скорость {self.name}: {self.speed} км\ч')
    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')
    def turn_left(self):
        print(f'{self.name} повернула налево')
    def turn_right(self):
        print(f'{self.name} повернула направо')
t = TownCar('White','Prius',72)
t.go()
t.name_car()
t.color_car()
t.show_speed()
t.turn_left()
t.turn_right()
t.stop()
print(t.is_police)
# w = WorkCar('Yellow','Solaris',54)
# w.go()
# w.name_car()
# w.color_car()
# w.show_speed()
# w.turn_right()
# w.turn_left()
# w.stop()
# s = SportCar('Black','Supra',140)
# s.go()
# s.name_car()
# s.color_car()
# s.show_speed()
# s.turn_right()
# s.turn_left()
# s.stop()
# p = PoliceCar('Blue','LADA',70)
# p.go()
# p.name_car()
# p.color_car()
# p.show_speed()
# p.turn_right()
# p.turn_left()
# p.stop()