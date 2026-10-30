import turtle
import time
import square.Square # get the Square class from Square.py

################################################################################################################

#SETUP TURTLE ENVIRONMENT (Screen, Turtles, Costumes)-------------

square = Square() #Just like a Turtle() but has a position number.  The default is 0.
square.onclick(square.playSquare)
screen = turtle.Screen()
screen.setup(400,400)

empty_image = "Empty.gif"
X_image = "X.gif"
O_image = "O.gif"
x_turn = True #Keeps track of whose turn it is True for X and False for O

screen.addshape(empty_image)
screen.addshape(X_image)
screen.addshape(O_image)

#FUNCTION DEFINITIONS-----------------------------------------------
def drawBoard(square):
    #at first the square, and all of its clones, should be empty
    square.shape(empty_image)
    square.penup()
    square.onclick(square.playSquare)
    position_number = 1
    #create 9 clones, each with its own position number
    #1) outer loop to create 3 rows

        #2) inner loop to create 3 columns in each row

          #3) clone the square with line below
            #square.clone(position_number)  #clone the square

            #4)add one to position number variable  that way, the next sqauare
            #  will get the next position number.

            #5)move the square forward
        #6)use square.sety(), putting a number/variable/expression in the parenthesis, to
        #  change the y value, to go down a row

        #7) use square.setx(), putting a number/variable/expression in the parenthesis,
        #   to go back to the left column position

        
    #8)  hide the original turtle using square.hideturtle()   


#Given the square that was clicked on, if the square is blank, change the shape/costue
#to an X or an O depending on whose turn it is.
def playSquare(squareClicked):
  #the next 5 lines are just sample code that can be deleted.
  squareClicked.write(squareClicked.position_number)
  squareClicked.hideturtle()
  time.sleep(.5)
  squareClicked.showturtle()
  print(squareClicked.position_number)
  

square.click_function = playSquare   # tell the square which function to call when clicked
drawBoard(square)

turtle.mainloop()