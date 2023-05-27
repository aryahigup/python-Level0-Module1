"""
* Write a Python program that asks the user for two numbers.

* Display the sum of the two numbers to the user
"""

from tkinter import simpledialog, messagebox, Tk

window = Tk()
window.withdraw()

num1 = simpledialog.askfloat(title="Simple Adder", prompt="What is the first number?")
num2 = simpledialog.askfloat(title="Simple Adder", prompt="What is the second number?")
messagebox.showinfo(title="Simple Adder", message="The answer is " + str(num1+num2))
