class Complex:

    def __init__(self,re = 0, im = 0):
        self.re = re
        self.im = im
    def __str__(self):
        return "{} {} {}i".format(self.re, '+' if self.im >= 0 else '-', abs(self.im))
    def __add__(self, other):
        return Complex(self.re + other.re, self.im + other.im)

    def __mul__(self, other):
        return Complex(self.re * other.re,self.im * other.im)

c1 = Complex(10,20)
c2 = Complex(5,3)
print(c1+c2)
print(c1*c2)