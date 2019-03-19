import time

time_in_seconds = time.time()
time_struct = time.localtime(time_in_seconds)
formatted = time.asctime(time_struct)
print(formatted)


class Coordinate:
    count = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        Coordinate.count += 1
        print("Coordinate Instance Nr", Coordinate.count, ". Current time is:", time.time())

    def dist(self, other):
        x_dist = (self.x - other.x)**2
        y_dist = (self.y - other.y)**2
        return (x_dist + y_dist)**0.5


c1 = Coordinate(1, 1)
c2 = Coordinate(2, 2)

print(Coordinate.dist(c1, c2))


# c1.name = "sven"
# print(c1.name)
#


class Hello:
    def greet(self):
        print("Hi")


obj = Hello()
temp = Hello.greet
temp(obj)
