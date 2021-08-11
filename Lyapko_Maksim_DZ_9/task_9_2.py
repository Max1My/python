class Road:
    _length = 20
    _width = 5000
    def __init__(self):
        thickness = 5
        weigth = 25
        self.result = self._length * self._width * thickness * weigth
        self.result = self.result // 100

a = Road()
print(a.result)