from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    ans = simpledialog.askstring(title='Remarkable', prompt="What is your name?")
    if ans == "Suryani":
        messagebox.showinfo(title='Remarkable', message="You like boba")
    if ans == "Aryahi":
        messagebox.showinfo(title="Remarkable", message="You are a junior in high school")
    
