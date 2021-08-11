class Clothes:
    pass
class Coat(Clothes):
    def __init__(self,size):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self,size):
        if size < 40:
            self.__size = 40
        elif size > 64:
            self.__size = 64
        else:
            self.__size = size
    def get_size(self):
        print(f"Размер: {self.size}")
        return self.size /6.5 + 0.5
class Suit(Clothes):
    def __init__(self,size):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self,size):
        if size < 154:
            self.__size = 154
        elif size > 197:
            self.__size = 197
        else:
            self.__size = size
    def get_size(self):
        print(f"Рост: {self.size}")
        return self.size * 2 + 0.3

c = Coat(30)
s = Suit(170)
print(c.get_size())
print(s.get_size())