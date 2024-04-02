from tkinter import *
from tkinter import messagebox

def login():
    username = entry1.get()
    password = entry2.get()

    if username == "" or password == "":
        messagebox.showinfo("", "Blanks not allowed")
    elif username == "shanika1" and password == "dilki@123":
        messagebox.showinfo("", "Login success")
    else:
        messagebox.showinfo("", "Incorrect username or password")

root = Tk()
root.title("Login")
root.geometry("600x300")
root.configure(bg="pink")

entry1 = Entry(root, bd=1)
entry1.place(x=40, y=90)

entry2 = Entry(root, bd=1, show='*')  # Show asterisks instead of actual characters
entry2.place(x=40, y=150)

Label(root, text="Login here", fg="black", font=("Arial", 16), bg="pink").place(x=180, y=10)
Label(root, text="Username", bg="pink", fg="black", font=("Arial", 16)).place(x=40, y=50)
Label(root, text="Password", bg="pink", fg="black", font=("Arial", 16)).place(x=40, y=120)

Button(root, text="Login", command=login, height=1, width=10, bd=6, bg="purple",fg="white", font=("Arial", 12), border=2).place(x=50, y=190)

root.mainloop()
