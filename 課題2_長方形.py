class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        area = self.height * self.width
        print(f'{area:2f}')

    def diagonal(self):
        line = pow(self.height, 2) + pow(self.width, 2)
        line = line ** (1 / 2)
        print(f'{line:.2f}')


rectangle1 = Rectangle(height=5, width=6)
rectangle1.area()  # 30.00
rectangle1.diagonal()  # 7.81

rectangle2 = Rectangle(height=3, width=3)
rectangle2.area()  # 9.00
rectangle2.diagonal()  # 4.24
