from app import GUIPoint, Point
from app import GUIRectangle
from random import randint
import turtle

mycanvas = turtle.Turtle()

rectangle = GUIRectangle(Point(randint(1,100), randint(1,100)),
                        Point(randint(100,400), randint(100,400)))
print(f'''
Rectangle Coordinate : ({rectangle.lowerpoint.x_coordinate}, {rectangle.lowerpoint.y_coordinate}) 
and ({rectangle.upperpoint.x_coordinate}, {rectangle.upperpoint.y_coordinate})
''')

print('Guess your point that falls between the reactangle')

point = GUIPoint(x=float(input('X Coordinate ')), y=float(input('Y Coordinate ')))
print(point.falls_in_rectangle(rectangle))

area = float(input('Guess the area '))
print(f'''You were off by {rectangle.area() - area} ''')

rectangle.draw_rectangle(mycanvas)
point.draw_point(mycanvas)

turtle.done()