from app import Point
from app import Rectangle
from random import randint

rectangle = Rectangle(Point(randint(1,9), randint(1,9)),
                        Point(randint(10,19), randint(10,19)))
print(f'''
Rectangle Coordinate : ({rectangle.lowerpoint.x_coordinate}, {rectangle.lowerpoint.y_coordinate}) 
and ({rectangle.upperpoint.x_coordinate}, {rectangle.upperpoint.y_coordinate})
''')

print('Guess your point that falls between the reactangle')

point = Point(x=float(input('X Coordinate ')), y=float(input('Y Coordinate ')))
print(point.falls_in_rectangle(rectangle))

area = float(input('Guess the area '))
print(f'''You were off by {rectangle.area() - area} ''')