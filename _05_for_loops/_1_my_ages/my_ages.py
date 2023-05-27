from tkinter import messagebox, simpledialog, Tk

window = Tk()
window.withdraw()

age = simpledialog.askinteger(title="My Ages", prompt="How old are you?")
for i in range(age):
    print(i+1)
