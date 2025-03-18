import math

class Calculator:
    def __init__(self, value):
        self.value = value
    
    def __add__(self, other):
        return Calculator(self.value + other.value)
    
    def __sub__(self, other):
        return Calculator(self.value - other.value)
    
    def __mul__(self, other):
        return Calculator(self.value * other.value)
    
    def __truediv__(self, other):
        return Calculator(self.value / other.value)
    
    def __pow__(self, other):
        return Calculator(self.value ** other.value)
    
    def log(self, base):
        return Calculator(math.log(self.value, base))
    
    def __repr__(self):
        return str(self.value)

a = Calculator(8)
b = Calculator(2)
print("Hasil Tambah:", a + b)         # 10
print("Hasil Pangkat:", a ** b)       # 64
print("Hasil Log Basis 2:", a.log(b)) # 3.0
