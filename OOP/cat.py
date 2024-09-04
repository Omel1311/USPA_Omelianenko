class Car:
    MINIMUM_SPEED = 1
    MAXIMUM_SPEED = 10
    @classmethod
    def validate_speed(cls, speed):
       return cls.MINIMUM_SPEED <= speed <= cls.MAXIMUM_SPEED

    def __init__(self, x=0, y=0):
        self.x = self.y = 0
        if self.validate_speed(x) and self.validate_speed(y):
            self.__x = x
            self.__y = y

    @staticmethod
    def speed(p, r):
        print(p * r)
    def __str__(self):
        print (f'({self.x}, {self.y}))')

mazda = Car(10, 9)
print(mazda.x, mazda.y)

Car.speed(3, 4)

