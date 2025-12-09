from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import font

from menu import Menu

def main_function():
    root = Tk()
    app = main_window(root)

class MainWindow:
    # constructor
    def __init__(self, master):
        # public data members
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("800x500+0+0")
        self.master.config(bg="powder blue")
        self.frame = Frame(self.master, bg="powder blue")
        self.frame.pack()

        self.username = StringVar()
        self.password = StringVar()

        self.lbl_title = Label(self.frame, text="HOSPITAL MANAGEMENT SYSTEM", font="Helvetica 20 bold", bg="powder blue", fg="black")
        self.lbl_title.grid(row=0, column=0, columnspan=2, pady=40)
        #======================
        self.login_frame1 = Frame(self.frame, width=400, height=80, relief="ridge", bg="cadet blue", bd=20)
        self.login_frame1.grid(row=1, column=0)
        self.login_frame2 = Frame(self.frame, width=400, height=80, relief="ridge", bg="cadet blue", bd=20)
        self.login_frame2.grid(row=2, column=0)
        #======LABEL AND ENTRY=========
        self.lbl_username = Label(self.login_frame1, text="Username", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lbl_username.grid(row=0, column=0)
        self.entry_username = Entry(self.login_frame1, font="Helvetica 14 bold", textvariable=self.username, bd=2)
        self.entry_username.grid(row=0, column=1)
        self.lbl_password = Label(self.login_frame1, text="Password ", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lbl_password.grid(row=1, column=0)
        self.entry_password = Entry(self.login_frame1, font="Helvetica 14 bold", show="*", textvariable=self.password, bd=2)
        self.entry_password.grid(row=1, column=1)
        #===========BUTTONS====
        self.btn_login = Button(self.login_frame2, text="Login", font="Helvetica 10 bold", width=10, bg="powder blue", command=self.login_system)
        self.btn_login.grid(row=3, column=0)
        self.btn_exit = Button(self.login_frame2, text="Exit", font="Helvetica 10 bold", width=10, bg="powder blue", command=self.exit_function)
        self.btn_exit.grid(row=3, column=1)

    # public member function  
    #Function for LOGIN
    def login_system(self):
        ADMIN_USERNAME = 'admin'
        ADMIN_PASSWORD = 'password123'
        ROOT_USERNAME = 'root'
        ROOT_PASSWORD = 'password123'
        S1 = (self.username.get())
        S2 = (self.password.get())
        if(S1 == ADMIN_USERNAME and S2 == ADMIN_PASSWORD):
            self.new_window = Toplevel(self.master)
            self.app = Menu(self.new_window)
        elif(S1 == ROOT_USERNAME and S2 == ROOT_PASSWORD):
            self.new_window = Toplevel(self.master)
            self.app = Menu(self.new_window)
        else:
            tkinter.messagebox.askretrycancel("HOSPITAL MANAGEMENT SYSTEM", "PLEASE ENTER VALID USERNAME AND PASSWORD")

    #Function for Exit
    def exit_function(self):
        self.master.destroy()

def main_window(root):
    return MainWindow(root)

if __name__ == "__main__":
    main_function()