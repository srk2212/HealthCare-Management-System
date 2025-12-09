from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import font
import sqlite3

# database connection
DB_NAME = "HOSPITAL_DB"

# establish a connection to the database
def get_db_connection():
    return sqlite3.connect(DB_NAME)

# create a cursor object
def get_cursor(conn):
    return conn.cursor()

# close the connection
def close_connection(conn):
    conn.close()

class EmployeeRegistrationForm:
    def __init__(self, master):
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master, bg="cadet blue")
        self.frame.pack()

        # =============ATTRIBUTES===========
        self.employee_id = StringVar()
        self.employee_name = StringVar()
        self.employee_sex = StringVar()
        self.employee_age = IntVar()
        self.employee_type = StringVar()
        self.employee_salary = IntVar()
        self.employee_experience = StringVar()
        self.employee_email = StringVar()
        self.employee_phone_number = IntVar()

        # ===============TITLE==========
        self.title_label = Label(self.frame, text="EMPLOYEE REGISTRATION FORM", font="Helvetica 20 bold", bg="cadet blue")
        self.title_label.grid(row=0, column=0, columnspan=4, pady=50)
        # ==============FRAME==========
        self.registration_frame = Frame(self.frame, width=800, height=200, relief="ridge", bg="cadet blue", bd=20)
        self.registration_frame.grid(row=1, column=0)

        self.button_frame = Frame(self.frame, width=400, height=80, relief="ridge", bg="cadet blue", bd=20)
        self.button_frame.grid(row=2, column=0)
        # ===========LABELS=============
        self.employee_id_label = Label(self.registration_frame, text="EMPLOYEE ID", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.employee_id_label.grid(row=0, column=0)
        self.employee_id_entry = Entry(self.registration_frame, font="Helvetica 14 bold", bd=2, textvariable=self.employee_id)
        self.employee_id_entry.grid(row=0, column=1)

        self.employee_name_label = Label(self.registration_frame, text="EMPLOYEE NAME", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.employee_name_label.grid(row=1, column=0)
        self.employee_name_entry = Entry(self.registration_frame, font="Helvetica 14 bold", bd=2, textvariable=self.employee_name)
        self.employee_name_entry.grid(row=1, column=1)

        self.sex_label = Label(self.registration_frame, text="SEX", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.sex_label.grid(row=2, column=0)
        self.sex_entry = Entry(self.registration_frame, font="Helvetica 14 bold", bd=2, textvariable=self.employee_sex)
        self.sex_entry.grid(row=2, column=1)

        self.age_label = Label(self.registration_frame, text="AGE", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.age_label.grid(row=3, column=0)
        self.age_entry = Entry(self.registration_frame, font="Helvetica 14 bold", bd=2, textvariable=self.employee_age)
        self.age_entry.grid(row=3, column=1)

        self.employee_type_label = Label(self.registration_frame, text="EMPLOYEE DESIGNATION", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.employee_type_label.grid(row=4, column=0)
        self.employee_type_entry = Entry(self.registration_frame, font="Helvetica 14 bold", bd=2, textvariable=self.employee_type)
        self.employee_type_entry.grid(row=4, column=1)

        self.salary_label = Label(self.registration_frame, text="SALARY", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.salary_label.grid(row=0, column=2)
        self.salary_entry = Entry(self.registration_frame, font="Helvetica 14 bold", bd=2, textvariable=self.employee_salary)
        self.salary_entry.grid(row=0, column=3)

        self.experience_label = Label(self.registration_frame, text="EXPERIENCE", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.experience_label.grid(row=1, column=2)
        self.experience_entry = Entry(self.registration_frame, font="Helvetica 14 bold", bd=2, textvariable=self.employee_experience)
        self.experience_entry.grid(row=1, column=3)

        self.phone_number_label = Label(self.registration_frame, text="CONTACT NUMBER", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.phone_number_label.grid(row=2, column=2)
        self.phone_number_entry = Entry(self.registration_frame, font="Helvetica 14 bold", bd=2, textvariable=self.employee_phone_number)
        self.phone_number_entry.grid(row=2, column=3)

        self.email_label = Label(self.registration_frame, text="EMAIL", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.email_label.grid(row=3, column=2)
        self.email_entry = Entry(self.registration_frame, font="Helvetica 14 bold", bd=2, textvariable=self.employee_email)
        self.email_entry.grid(row=3, column=3)

        self.save_button = Button(self.button_frame, text="SAVE", width=10, font="Helvetica 14 bold", bg="cadet blue",
                                  command=self.insert_employee_data)
        self.save_button.grid(row=0, column=1)

        self.delete_button = Button(self.button_frame, text="DELETE", width=10, font="Helvetica 14 bold", bg="cadet blue",
                                    command=self.delete_employee)
        self.delete_button.grid(row=0, column=2)

        self.exit_button = Button(self.button_frame, text="EXIT", width=10, font="Helvetica 14 bold", bg="cadet blue",
                                  command=self.exit_application)
        self.exit_button.grid(row=0, column=3)

    def insert_employee_data(self):
        conn = get_db_connection()
        cursor = get_cursor(conn)
        employee_id = self.employee_id.get()
        employee_name = self.employee_name.get()
        employee_sex = self.employee_sex.get()
        employee_age = self.employee_age.get()
        employee_type = self.employee_type.get()
        employee_salary = self.employee_salary.get()
        employee_experience = self.employee_experience.get()
        employee_email = self.employee_email.get()
        employee_phone_number = self.employee_phone_number.get()
        cursor.execute("SELECT * FROM employee WHERE EMP_ID = ?", (employee_id,))
        result = cursor.fetchall()
        if len(result) != 0:
            tkinter.messagebox.showerror("HOSPITAL DATABASE SYSTEM", "EMPLOYEE ID ALREADY EXISTS")
        else:
            cursor.execute("INSERT INTO employee VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (employee_id, employee_name, employee_sex, employee_age, employee_type, employee_salary, employee_experience, employee_email, employee_phone_number))
            tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "EMPLOYEE DATA ADDED")
        conn.commit()
        close_connection(conn)

    def delete_employee(self):
        self.new_window = Toplevel(self.master)
        self.app = DeleteEmployee(self.new_window)

    def exit_application(self):
        self.master.destroy()


class DeleteEmployee:
    def __init__(self, master):
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master, bg="cadet blue")
        self.frame.pack()
        self.employee_id_to_delete = StringVar()
        self.title_label = Label(self.frame, text="DELETE EMPLOYEE WINDOW", font="Helvetica 20 bold", bg="cadet blue")
        self.title_label.grid(row=0, column=0, columnspan=2, pady=50)
        # ==============FRAME==========
        self.delete_frame = Frame(self.frame, width=400, height=80, relief="ridge", bg="cadet blue", bd=20)
        self.delete_frame.grid(row=1, column=0)
        self.button_frame = Frame(self.frame, width=400, height=80, relief="ridge", bg="cadet blue", bd=20)
        self.button_frame.grid(row=2, column=0)
        # ===========LABELS=============
        self.employee_id_label = Label(self.delete_frame, text="ENTER EMPLOYEE ID TO DELETE", font="Helvetica 14 bold", bg="cadet blue",
                              bd=22)
        self.employee_id_label.grid(row=0, column=0)
        self.employee_id_entry = Entry(self.delete_frame, font="Helvetica 14 bold", bd=2, textvariable=self.employee_id_to_delete)
        self.employee_id_entry.grid(row=0, column=1)

        self.delete_button = Button(self.button_frame, text="DELETE", width=10, font="Helvetica 14 bold", bg="cadet blue",
                               command=self.delete_employee_from_database)
        self.delete_button.grid(row=0, column=1)

    def delete_employee_from_database(self):
        conn = get_db_connection()
        cursor = get_cursor(conn)
        employee_id = self.employee_id_to_delete.get()
        cursor.execute("SELECT * FROM employee WHERE EMP_ID = ?", (employee_id,))
        result = cursor.fetchall()
        if len(result) != 0:
            cursor.execute("DELETE FROM employee WHERE EMP_ID = ?", (employee_id,))
            tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "EMPLOYEE DATA DELETED")
        else:
            tkinter.messagebox.showerror("HOSPITAL DATABASE SYSTEM", "EMPLOYEE DATA DOESN'T EXIST")
        conn.commit()
        close_connection(conn)


root = Tk()
my_gui = EmployeeRegistrationForm(root)
root.mainloop()