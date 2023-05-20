
from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    ans = simpledialog.askstring(title='UNbirthday', prompt="When is your birthday? (mm/dd)")
    if ans == "05/19":
        messagebox.showinfo(title="Birthday", message="Happy Birthday!")
    else:
        messagebox.showinfo(title="UNbirthday", message="Happy UN-Birthday!")

