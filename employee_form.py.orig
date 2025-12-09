from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import font
import sqlite3

# Database connection
DB_NAME = "HospitalDB.db"

# Establish a connection to the database
def get_db_connection():
    return sqlite3.connect(DB_NAME)

# Create a cursor object
def get_cursor(conn):
    return conn.cursor()

# Close the connection
def close_connection(conn):
    conn.close()

class Employee:
    def __init__(self, master):
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master, bg="cadet blue")
        self.frame.pack()

        # =============ATTRIBUTES===========
        self.emp_ID = StringVar()
        self.emp_name = StringVar()
        self.emp_sex = StringVar()
        self.emp_age = IntVar()
        self.emp_type = StringVar()
        self.emp_salary = IntVar()
        self.emp_exp = StringVar()
        self.emp_email = StringVar()
        self.emp_phno = IntVar()

        # ===============TITLE==========
        self.lblTitle = Label(self.frame, text="EMPLOYEE REGISTRATION FORM", font="Helvetica 20 bold", bg="cadet blue")
        self.lblTitle.grid(row=0, column=0, columnspan=4, pady=50)
        # ==============FRAME==========
        self.LoginFrame = Frame(self.frame, width=800, height=200, relief="ridge", bg="cadet blue", bd=20)
        self.LoginFrame.grid(row=1, column=0)

        self.LoginFrame2 = Frame(self.frame, width=400, height=80, relief="ridge", bg="cadet blue", bd=20)
        self.LoginFrame2.grid(row=2, column=0)
        # ===========LABELS=============
        self.lblempid = Label(self.LoginFrame, text="EMPLOYEE ID", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblempid.grid(row=0, column=0)
        self.empid_entry = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.emp_ID)
        self.empid_entry.grid(row=0, column=1)

        self.lblempname = Label(self.LoginFrame, text="EMPLOYEE NAME", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblempname.grid(row=1, column=0)
        self.empname_entry = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.emp_name)
        self.empname_entry.grid(row=1, column=1)

        self.lblsex = Label(self.LoginFrame, text="SEX", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblsex.grid(row=2, column=0)
        self.sex_entry = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.emp_sex)
        self.sex_entry.grid(row=2, column=1)

        self.lblage = Label(self.LoginFrame, text="AGE", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblage.grid(row=3, column=0)
        self.age_entry = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.emp_age)
        self.age_entry.grid(row=3, column=1)

        self.etype1 = Label(self.LoginFrame, text="EMPLOYEE DESIGNATION", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.etype1.grid(row=4, column=0)
        self.type_entry = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.emp_type)
        self.type_entry.grid(row=4, column=1)

        self.lblCon = Label(self.LoginFrame, text="SALARY", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblCon.grid(row=0, column=2)
        self.salary_entry = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.emp_salary)
        self.salary_entry.grid(row=0, column=3)

        self.lblAlt = Label(self.LoginFrame, text="EXPERIENCE", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblAlt.grid(row=1, column=2)
        self.exp_entry = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.emp_exp)
        self.exp_entry.grid(row=1, column=3)

        self.lbleid = Label(self.LoginFrame, text="CONTACT NUMBER", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lbleid.grid(row=2, column=2)
        self.phno_entry = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.emp_phno)
        self.phno_entry.grid(row=2, column=3)

        self.lbleid = Label(self.LoginFrame, text="EMAIL", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lbleid.grid(row=3, column=2)
        self.email_entry = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.emp_email)
        self.email_entry.grid(row=3, column=3)

        self.button2 = Button(self.LoginFrame2, text="SAVE", width=10, font="Helvetica 14 bold", bg="cadet blue",
                              command=self.insert_employee)
        self.button2.grid(row=0, column=1)

        self.button3 = Button(self.LoginFrame2, text="DELETE", width=10, font="Helvetica 14 bold", bg="cadet blue",
                              command=self.delete_employee)
        self.button3.grid(row=0, column=2)

        self.button6 = Button(self.LoginFrame2, text="EXIT", width=10, font="Helvetica 14 bold", bg="cadet blue",
                              command=self.exit)
        self.button6.grid(row=0, column=3)

    def insert_employee(self):
        conn = get_db_connection()
        cursor = get_cursor(conn)
        e1 = self.emp_ID.get()
        e2 = self.emp_name.get()
        e3 = self.emp_sex.get()
        e4 = self.emp_age.get()
        e5 = self.emp_type.get()
        e6 = self.emp_salary.get()
        e7 = self.emp_exp.get()
        e8 = self.emp_email.get()
        e9 = self.emp_phno.get()
        cursor.execute("SELECT * FROM employee WHERE EMP_ID = ?", (e1,))
        p = cursor.fetchall()
        if len(p) != 0:
            tkinter.messagebox.showerror("HOSPITAL DATABASE SYSTEM", "EMPLOYEE ID ALREADY EXISTS")
        else:
            cursor.execute("INSERT INTO employee VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (e1, e2, e3, e4, e5, e6, e7, e8, e9))
            tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "EMPLOYEE DATA ADDED")
        conn.commit()
        close_connection(conn)

    def delete_employee(self):
        self.new_window = Toplevel(self.master)
        self.app = DeleteEmployee(self.new_window)

    def exit(self):
        self.master.destroy()


class DeleteEmployee:
    def __init__(self, master):
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master, bg="cadet blue")
        self.frame.pack()
        self.de1_emp = StringVar()
        self.lblTitle = Label(self.frame, text="DELETE EMPLOYEE WINDOW", font="Helvetica 20 bold", bg="cadet blue")
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=50)
        # ==============FRAME==========
        self.LoginFrame = Frame(self.frame, width=400, height=80, relief="ridge", bg="cadet blue", bd=20)
        self.LoginFrame.grid(row=1, column=0)
        self.LoginFrame2 = Frame(self.frame, width=400, height=80, relief="ridge", bg="cadet blue", bd=20)
        self.LoginFrame2.grid(row=2, column=0)
        # ===========LABELS=============
        self.lblpatid = Label(self.LoginFrame, text="ENTER EMPLOYEE ID TO DELETE", font="Helvetica 14 bold", bg="cadet blue",
                              bd=22)
        self.lblpatid.grid(row=0, column=0)
        self.empid_entry = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.de1_emp)
        self.empid_entry.grid(row=0, column=1)

        self.DeleteB = Button(self.LoginFrame2, text="DELETE", width=10, font="Helvetica 14 bold", bg="cadet blue",
                               command=self.delete_employee)
        self.DeleteB.grid(row=0, column=1)

    def delete_employee(self):
        conn = get_db_connection()
        cursor = get_cursor(conn)
        de = self.de1_emp.get()
        cursor.execute("SELECT * FROM employee WHERE EMP_ID = ?", (de,))
        p = cursor.fetchall()
        if len(p) != 0:
            cursor.execute("DELETE FROM employee WHERE EMP_ID = ?", (de,))
            tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "EMPLOYEE DATA DELETED")
        else:
            tkinter.messagebox.showerror("HOSPITAL DATABASE SYSTEM", "EMPLOYEE DATA DOESN'T EXIST")
        conn.commit()
        close_connection(conn)


root = Tk()
my_gui = Employee(root)
root.mainloop()