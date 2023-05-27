"""
* Write a python program that asks the user a minimum of 3 riddles.

* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got
  correct
"""

from tkinter import simpledialog, messagebox, Tk

window = Tk()
window.withdraw()

riddle1 = "What has a head, a tail, is brown, and has no legs"
riddle2 = "Can you name three consecutive days without using the words Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?"
riddle3 = "The more you take, the more you leave behind. 'What am I?'"
count = 0

ans1 = simpledialog.askstring(title="Riddler", prompt=riddle1)


if ans1 == "a penny":
    count+=1
    messagebox.showinfo(title="Riddler", message="You got it!")
else:
    messagebox.showinfo(title="Riddler", message="Not quite. The answer is a penny")
ans2 = simpledialog.askstring(title="Riddler", prompt=riddle2)
if ans2 == "yesterday, today, tomorrow":
    count+=1
    messagebox.showinfo(title="Riddler", message="You got it!")
else:
    messagebox.showinfo(title="Riddler", message="Not quite. The answer is a yesterday, today, tomorrow")
ans3 = simpledialog.askstring(title="Riddler", prompt=riddle3)

if ans3 == "steps":
    count+=1
    messagebox.showinfo(title="Riddler", message="You got it!")
else:
    messagebox.showinfo(title="Riddler", message="Not quite. The answer is steps")
messagebox.showinfo(title="Riddler", message="Your score is " + str(count) + ".")
