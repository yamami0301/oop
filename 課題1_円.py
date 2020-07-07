class Circle:
    def __init__(self, radius, area, perimeter):
        area = (radius ** 2 * 3.14)
        perimeter = (radius * 2 * 3.14)

        self.radius = radius
        self.area = area
        self.perimeter = perimeter

        self.radius(1)

circle1 = Circle(radius=1)
print(circle1.area())  # 3.14
print(circle1.perimeter())  # 6.28

# 半径3の円
circle3 = Circle(radius=3)
print(circle3.area())  # 28.27
print(circle3.perimeter())  # 1 8.85