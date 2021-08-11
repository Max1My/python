import time

class TrafficLight:
    _color_1 = "Red"
    _color_2 = "Yellow"
    _color_3 = "Green"
    status = 0
    def running(self):
        self.status += 1
        if self.status == 1:
            print("Запуск светофора")
        if self.status == 2:
            print(TrafficLight._color_1)
        if self.status == 3:
            print(TrafficLight._color_2)
        if self.status == 4:
            print(TrafficLight._color_3)

a = TrafficLight()
a.running()
time.sleep(1)
a.running()
time.sleep(7)
a.running()
time.sleep(2)
a.running()
time.sleep(6)
