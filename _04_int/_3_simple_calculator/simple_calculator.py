"""
* Write a Python program that asks the user for two numbers.

* Then ask the user if the would like to add, subtract, multiply, or divide.

* Use if-else statements to provide the desired math operation on the numbers
  and display the result.
"""

from tkinter import simpledialog, messagebox, Tk

window = Tk()
window.withdraw()

process = simpledialog.askstring(title="Calculator", prompt="Would you like to add, subtract, multiply, or divide?")
num1 = simpledialog.askfloat(title="Calculator", prompt="What is the first number?")
num2 = simpledialog.askfloat(title="Calculator", prompt="What is the second number?")


if process == "add":
    messagebox.showinfo(message="The answer is " + str(num1+num2))
if process == "subtract":
    messagebox.showinfo(title="Calculator", message="The answer is " + str(num1-num2))
if process == "multiply":
    messagebox.showinfo(title="Calculator", message="The answer is " + str(num1*num2))
if process == "divide":
    messagebox.showinfo(title="Calculator", message="The answer is " + str(num1/num2))
