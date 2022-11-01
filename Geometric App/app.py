class Point:
    def __init__(self, x, y):
        self.x_coordinate = x
        self.y_coordinate = y
    
    def falls_in_rectangle(self, rectangle):
        if rectangle.lowerpoint.x_coordinate < self.x_coordinate < rectangle.upperpoint.x_coordinate \
            and rectangle.lowerpoint.y_coordinate < self.y_coordinate < rectangle.upperpoint.y_coordinate:
            return True
        else:
            return False

class Rectangle:
    def __init__(self, P1, P2):
        self.lowerpoint = P1
        self.upperpoint = P2

    def area(self):
        return(self.upperpoint.x_coordinate - self.lowerpoint.x_coordinate) * \
                (self.upperpoint.y_coordinate - self.lowerpoint.y_coordinate)

class GUIPoint(Point):

    def draw_point(self, canvas, size=10, color='blue'):

        canvas.penup()
        canvas.goto(self.x_coordinate, self.y_coordinate) # To to a particular coordinate
        canvas.pendown()

        canvas.dot(size, color)

class GUIRectangle(Rectangle):

    def draw_rectangle(self, canvas):
        canvas.penup()
        canvas.goto(self.lowerpoint.x_coordinate, self.lowerpoint.y_coordinate) # To to a particular coordinate
        canvas.pendown()

        canvas.forward(self.upperpoint.x_coordinate - self.lowerpoint.x_coordinate) # move 100px forward
        canvas.left(90) # Turn 90 degrees
        canvas.forward(self.upperpoint.y_coordinate - self.lowerpoint.y_coordinate)
        canvas.left(90)
        canvas.forward(self.upperpoint.x_coordinate - self.lowerpoint.x_coordinate)
        canvas.left(90)
        canvas.forward(self.upperpoint.y_coordinate - self.lowerpoint.y_coordinate)

