import math

class MyMath:
    @staticmethod
    def circumference(radius):
        return 2 * math.pi * radius

    @staticmethod
    def circle_area(radius):
        return math.pi * radius ** 2

    @staticmethod
    def cube_volume(side):
        return side ** 3

    @staticmethod
    def sphere_surface_area(radius):
        return 4 * math.pi * radius ** 2


print("Длина окружности: ", MyMath.circumference(5))
print("Площадь окружности: ", MyMath.circle_area(5))
print("Объем куба: ", MyMath.cube_volume(3))
print("Площадь поверхности сферы: ", MyMath.sphere_surface_area(4))
