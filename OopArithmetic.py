class Arithmetic:
    MULTIPLIER = 2

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def divide(self):
        return self.x / self.y

    @classmethod
    def multiply(cls, x, y, multiplier=MULTIPLIER):
        a = x * y * multiplier
        return a

    @staticmethod
    def operation(operation_type, a, b):
        if operation_type == 'add':
            return a + b
        if operation_type == 'subtract':
            return b - a
        else:
            print('Please enter correct operation (add or subtract)!')

    @property
    def value(self):
        return (self.x, self.y)

    @value.setter
    def value(self, x, y):
        self.x = x
        self.y = y


a = Arithmetic(1, 2)
print(a.divide())
print(Arithmetic.multiply(2, 3))
print(a.operation('add', 3, 3))
print(a.operation('subtract', 5, 4))
print(a.value)

obj = Arithmetic(5, 5)
print(obj.value)

