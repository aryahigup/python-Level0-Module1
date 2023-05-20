import turtle
from tkinter import messagebox, simpledialog, Tk
import math

# Goal: Write a Python program that asks the user for the radius 
#       of a circle and displays the area of that circle.
#       The formula for the area of a circle is πr^2.
#       See example image in package to check your output.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Ask the user for the radius in pixels and store it in a variable
    r = simpledialog.askinteger(title='Radius', prompt="Enter the radius of the circle")
    
    # Make a new turtle
    t = turtle.Turtle()
    # Have your turtle draw a circle with the correct radius
    t.circle(r)

    # Call the turtle .penup() method
    t.penup()
    # Move your turtle to a new x,y position using .goto()
    t.goto(100, 100)
    # Calculate the area of your circle and store it in a variable
    # Hint, you can use math.pi
    area = r*r*math.pi
    # Write the area of your circle using the turtle .write() method
    t.write(arg="area = " + str(area), move=True, align='left', font=('Arial',8,'normal'))

    # Hide your turtle
    t.hideturtle()
    # Call turtle.done()
    turtle.done()
