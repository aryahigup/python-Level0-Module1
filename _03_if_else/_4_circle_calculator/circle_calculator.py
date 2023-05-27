# Write a Python program that asks the user for the radius of a circle.
# Next, ask the user if they would like to calculate the area or circumference of a circle.
# If they choose area, display the area of the circle using the radius.
# Otherwise, display the circumference of the circle using the radius.

#Area = πr^2
#Circumference = 2πr

from tkinter import simpledialog, messagebox, Tk
import math

window = Tk()
window.withdraw();
radius = simpledialog.askinteger(title='Circle Calculator', prompt="What is the radius of the circle you would like to calculate?")
ans = simpledialog.askstring(title="Circle Calculator", prompt="Would like to calculate the area or the circumference?")

if ans == "circumference":
    messagebox.showinfo(title='Circle Calculator', message="The circumference is 2π(" + str(radius) + ") or " + str(radius*2* math.pi))
if ans == "area":
    messagebox.showinfo(title='Circle Calculator', message="The area is π(" + str(radius)  + ")^2 or " + str(radius*radius* math.pi))

