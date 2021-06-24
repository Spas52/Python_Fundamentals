class Circle:
    __pi = 3.14  # class attribute

    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = diameter/2

    def calculate_circumference(self):
        return Circle.__pi * self.diameter

    def calculate_area(self):
        return Circle.__pi * self.radius * self.radius

    def calculate_area_of_sector(self, angle):
        return (angle/360) * Circle.__pi * self.radius * self.radius


diameter_input = int(input())
circle = Circle(diameter_input)
angle = int(input())
print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(angle):.2f}")