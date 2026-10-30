#Here I create an extension of Turtle, called Square, that also has a position number, and can
#clone itself with the clone haveing a different position number.
#A Square is just like a Turtle except instead of creating it like the: myTurtle = Turtle()
# you create it like this: mySquare = Square()
# You can use Square objects the same as Turtle objects.  For example you can say mySquare.forward(10), mySquare.setx(100), mySquare.hide(), mySqaure.penup() etc.
#You can also set the Square's position number by saying mySquare.position_number = 5.  You can access the square's position number by saying mySquare.position_number.
#If a Square's position number is not set, its default position number is 0.
import turtle

class Square(turtle.Turtle):
    def __init__(self, click_function=None):
        super().__init__()
        self.position_number = 0
        self.click_function = click_function  # the function to call when clicked
        self.penup()

    # When clicked, call whatever function was handed to this Square,
    # passing along this square so its costume/position can be used.
    def playSquare(self, x, y):
        if self.click_function:
            self.click_function(self)

    def clone(self, positionNumber):
        newSquare = Square(self.click_function)
        newSquare.setposition(self.position())
        newSquare.setheading(self.heading())
        newSquare.position_number = positionNumber
        newSquare.shape(self.shape())
        newSquare.onclick(newSquare.playSquare)
        return newSquare
################################################################################################################