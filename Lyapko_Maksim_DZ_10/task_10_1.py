class Matrix:
    def __init__(self,param_1,param_2,param_3,param_4,param_5,param_6):
        self.param_1 = param_1
        self.param_2 = param_2
        self.param_3 = param_3
        self.param_4 = param_4
        self.param_5 = param_5
        self.param_6 = param_6
    def __str__(self):
        return f"{self.param_1},{self.param_2},{self.param_3},{self.param_4},{self.param_5},{self.param_6}"
    def __add__(self, other):
        return Matrix(self.param_1 + other.param_1, self.param_2 + other.param_2, self.param_3 + other.param_3, self.param_4 + other.param_4,self.param_5 + other.param_5,self.param_6 + other.param_6)



mx_1 = Matrix(31,22,37,43,51,86)
mx_2 = Matrix(3,5,32,2,4,6)
mx_3 = mx_1 + mx_2
print(mx_3)