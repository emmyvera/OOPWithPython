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

if __name__ == '__main__':
    point = Point(5, 8)
    lowerpoint = Point(3,7)
    upperpoint = Point(7,9)
    rectangle = Rectangle(lowerpoint, upperpoint)
    print(point.falls_in_rectangle(rectangle))

    
        