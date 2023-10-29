class Vector:
    def __init__(self,*args):
        self.values=[]
        for n in args:
            if isinstance(n,int):
                self.values.append(n)

    def __str__(self):
        if self.values:
            return f'Вектор{tuple(sorted(self.values))}'
        else:
            return f'Пустой вектор'

v1=Vector(1,2,3)
print(v1) # печатает 'Вектор(1,2,3)'
v2=Vector()
print(v2) #Печатает 'Пустой вектор'