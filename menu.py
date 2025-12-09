from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import font
import sqlite3
from patient_form import Patient
from room_form import Room
from employee_form import Employee
from appointment_form import Appointment
from billing_form import Billing

class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None

    def connect(self):
        try:
            self.conn = sqlite3.connect(self.db_name)
            print("DATABASE CONNECTION SUCCESSFUL")
        except sqlite3.Error as e:
            print(f"Failed to connect to database: {e}")

    def close(self):
        if self.conn:
            self.conn.close()
            print("DATABASE CONNECTION CLOSED")

class Menu:
    def __init__(self, master):
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("800x600+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master, bg="cadet blue")
        self.frame.pack()

        self.lblTitle = Label(self.frame, text="MAIN MENU", font="Helvetica 20 bold", bg="cadet blue")
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=50)

        self.LoginFrame = Frame(self.frame, width=400, height=400, relief="ridge", bg="cadet blue", bd=20)
        self.LoginFrame.grid(row=1, column=0)
        
        self.button1 = Button(self.LoginFrame, text="1.PATIENT REGISTRATION", width=30, font="Helvetica 14 bold", bg="cadet blue", command=self.Patient_Reg)
        self.button1.grid(row=1, column=0, pady=10)

        self.button2 = Button(self.LoginFrame, text="2.ROOM ALLOCATION", width=30, font="Helvetica 14 bold", bg="cadet blue", command=self.Room_Allocation)
        self.button2.grid(row=2, column=0, pady=10)

        self.button3 = Button(self.LoginFrame, text="3.EMPLOYEE REGISTRATION", width=30, font="Helvetica 14 bold", bg="cadet blue", command=self.Employee_Reg)
        self.button3.grid(row=3, column=0, pady=10)

        self.button4 = Button(self.LoginFrame, text="4.BOOK APPOINTMENT", width=30, font="Helvetica 14 bold", bg="cadet blue", command=self.Appointment_Form)
        self.button4.grid(row=4, column=0, pady=10)

        self.button5 = Button(self.LoginFrame, text="5.PATIENT BILL", width=30, font="Helvetica 14 bold", bg="cadet blue", command=self.Billing_Form)
        self.button5.grid(row=5, column=0, pady=10)

        self.button6 = Button(self.LoginFrame, text="6.EXIT", width=30, font="Helvetica 14 bold", bg="cadet blue", command=self.Exit)
        self.button6.grid(row=6, column=0, pady=10)

        self.db_connection = DatabaseConnection("HospitalDB.db")
        self.db_connection.connect()

    def Exit(self):
        self.db_connection.close()
        self.master.destroy()

    def Patient_Reg(self):
        try:
            self.newWindow = Toplevel(self.master)
            self.app = Patient(self.newWindow)
        except Exception as e:
            tkinter.messagebox.showerror("Error", f"Failed to open patient registration window: {e}")

    def Room_Allocation(self):
        try:
            self.newWindow = Toplevel(self.master)
            self.app = Room(self.newWindow)
        except Exception as e:
            tkinter.messagebox.showerror("Error", f"Failed to open room allocation window: {e}")

    def Employee_Reg(self):
        try:
            self.newWindow = Toplevel(self.master)
            self.app = Employee(self.newWindow)
        except Exception as e:
            tkinter.messagebox.showerror("Error", f"Failed to open employee registration window: {e}")

    def Appointment_Form(self):
        try:
            self.newWindow = Toplevel(self.master)
            self.app = Appointment(self.newWindow)
        except Exception as e:
            tkinter.messagebox.showerror("Error", f"Failed to open appointment window: {e}")

    def Billing_Form(self):
        try:
            self.newWindow = Toplevel(self.master)
            self.app = Billing(self.newWindow)
        except Exception as e:
            tkinter.messagebox.showerror("Error", f"Failed to open billing window: {e}")

def main():
    root = Tk()
    app = Menu(root)
    root.mainloop()

if __name__ == "__main__":
    main()