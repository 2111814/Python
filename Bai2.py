class PhanSo:
    def __init__(self, tu_, mau_so):
        self.tu_so = tu_so
        self.mau_so = mau_so 
        
    def __str__(self):
        return f"{self.tu_so}/{self.mau_so}"
    
    def rutGon(self):

        pass

    def __add__(self, other):
        pass
    
    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __truediv__(self, other):
        pass

a = PhanSo()
a.tu= 2
a.mau= 3
b = PhanSo(3,5)
print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")
print(f"{a} / {b} = {a/b}")