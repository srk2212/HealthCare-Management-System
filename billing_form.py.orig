from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import font
import sqlite3

class BillingClass:
    def __init__(self, master: Tk):
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master, bg="cadet blue")
        self.frame.pack()

        self.patient_id = IntVar()
        self.discharge_date = StringVar()
        self.treatment_1 = StringVar()
        self.treatment_2 = StringVar()
        self.treatment_cost = IntVar()
        self.medicine = StringVar()
        self.medicine_quantity = IntVar()
        self.medicine_price = IntVar()

        self.title_label = Label(self.frame, text="BILLING WINDOW", font="Helvetica 20 bold", bg="cadet blue")
        self.title_label.grid(row=0, column=0, columnspan=2, pady=25)

        self.login_frame = Frame(self.frame, width=400, height=80, relief="ridge", bg="cadet blue", bd=20)
        self.login_frame.grid(row=1, column=0)

        self.login_frame_2 = Frame(self.frame, width=400, height=80, relief="ridge", bg="cadet blue", bd=20)
        self.login_frame_2.grid(row=2, column=0)

        self.patient_id_label = Label(self.login_frame, text="PATIENT ID", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.patient_id_label.grid(row=0, column=0)
        self.patient_id_entry = Entry(self.login_frame, font="Helvetica 14 bold", bd=2, textvariable=self.patient_id)
        self.patient_id_entry.grid(row=0, column=1)

        self.discharge_date_label = Label(self.login_frame, text="DATE DISCHARGED(YYYY-MM-DD)", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.discharge_date_label.grid(row=1, column=0)
        self.discharge_date_entry = Entry(self.login_frame, font="Helvetica 14 bold", bd=2, textvariable=self.discharge_date)
        self.discharge_date_entry.grid(row=1, column=1)

        self.update_discharge_date_button = Button(self.login_frame, text="UPDATE DISCHARGE DATE", width=25, font="Helvetica 14 bold", bg="cadet blue", command=self.update_discharge_date)
        self.update_discharge_date_button.grid(row=1, column=3)

        self.treatment_label = Label(self.login_frame, text="TREATMENT", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.treatment_label.grid(row=2, column=0)
        self.treatment_entry = Entry(self.login_frame, font="Helvetica 14 bold", bd=2, textvariable=self.treatment_1)
        self.treatment_entry.grid(row=2, column=1)

        self.treatment_code_label = Label(self.login_frame, text="TREATMENT CODE", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.treatment_code_label.grid(row=3, column=0)
        self.treatment_code_entry = Entry(self.login_frame, font="Helvetica 14 bold", bd=2, textvariable=self.treatment_2)
        self.treatment_code_entry.grid(row=3, column=1)

        self.treatment_cost_label = Label(self.login_frame, text="TREATMENT COST ₹", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.treatment_cost_label.grid(row=4, column=0)
        self.treatment_cost_entry = Entry(self.login_frame, font="Helvetica 14 bold", bd=2, textvariable=self.treatment_cost)
        self.treatment_cost_entry.grid(row=4, column=1)

        self.medicine_label = Label(self.login_frame, text="MEDICINE", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.medicine_label.grid(row=2, column=2)
        self.medicine_entry = Entry(self.login_frame, font="Helvetica 14 bold", bd=2, textvariable=self.medicine)
        self.medicine_entry.grid(row=2, column=3)

        self.medicine_quantity_label = Label(self.login_frame, text="MEDICINE QUANTITY", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.medicine_quantity_label.grid(row=3, column=2)
        self.medicine_quantity_entry = Entry(self.login_frame, font="Helvetica 14 bold", bd=2, textvariable=self.medicine_quantity)
        self.medicine_quantity_entry.grid(row=3, column=3)

        self.medicine_price_label = Label(self.login_frame, text="MEDICINE PRICE ₹", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.medicine_price_label.grid(row=4, column=2)
        self.medicine_price_entry = Entry(self.login_frame, font="Helvetica 14 bold", bd=2, textvariable=self.medicine_price)
        self.medicine_price_entry.grid(row=4, column=3)

        self.update_data_button = Button(self.login_frame_2, text="UPDATE DATA", width=15, font="Helvetica 14 bold", bg="cadet blue", command=self.update_data)
        self.update_data_button.grid(row=3, column=2)

        self.generate_bill_button = Button(self.login_frame_2, text="GENERATE BILL", width=15, font="Helvetica 14 bold", bg="cadet blue", command=self.generate_bill)
        self.generate_bill_button.grid(row=3, column=3)

        self.exit_button = Button(self.login_frame_2, text="EXIT", width=10, font="Helvetica 14 bold", bg="cadet blue", command=self.exit_application)
        self.exit_button.grid(row=3, column=4)

    def update_discharge_date(self):
        try:
            with sqlite3.connect("HospitalDB.db") as conn:
                cursor = conn.cursor()
                patient_id = self.patient_id.get()
                discharge_date = self.discharge_date.get()
                cursor.execute("UPDATE ROOM SET DATE_DISCHARGED=? WHERE PATIENT_ID=?", (discharge_date, patient_id))
                conn.commit()
                tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "DISCHARGE DATE UPDATED")
        except sqlite3.Error as e:
            tkinter.messagebox.showerror("HOSPITAL DATABASE SYSTEM", str(e))

    def update_data(self):
        try:
            with sqlite3.connect("HospitalDB.db") as conn:
                cursor = conn.cursor()
                patient_id = self.patient_id.get()
                treatment = self.treatment_1.get()
                treatment_code = self.treatment_2.get()
                treatment_cost = self.treatment_cost.get()
                medicine = self.medicine.get()
                medicine_quantity = self.medicine_quantity.get()
                medicine_price = self.medicine_price.get()

                cursor.execute("SELECT * FROM TREATMENT WHERE PATIENT_ID=?", (patient_id,))
                if cursor.fetchone():
                    tkinter.messagebox.showerror("HOSPITAL DATABASE SYSTEM", "PATIENT ID IS ALREADY REGISTERED")
                else:
                    cursor.execute("INSERT INTO TREATMENT VALUES(?,?,?,?)", (patient_id, treatment, treatment_code, treatment_cost))
                    cursor.execute("INSERT INTO MEDICINE VALUES(?,?,?,?)", (patient_id, medicine, medicine_quantity, medicine_price))
                    conn.commit()
                    tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "BILLING DATA SAVED")
        except sqlite3.Error as e:
            tkinter.messagebox.showerror("HOSPITAL DATABASE SYSTEM", str(e))

    def generate_bill(self):
        try:
            with sqlite3.connect("HospitalDB.db") as conn:
                cursor = conn.cursor()
                patient_id = self.patient_id.get()
                cursor.execute("SELECT SUM(T_COST + (M_COST * M_QTY) + (DATE_DISCHARGED - DATE_ADMITTED) * RATE) FROM ROOM NATURAL JOIN TREATMENT NATURAL JOIN MEDICINE WHERE PATIENT_ID=?", (patient_id,))
                total_amount = cursor.fetchone()[0]
                if total_amount is None:
                    total_amount = 0
                self.total_amount_label = Label(self.login_frame, text="TOTAL AMOUNT OUTSTANDING", font="Helvetica 14 bold", bg="cadet blue", bd=22)
                self.total_amount_label.grid(row=5, column=0)
                self.total_amount_value = Label(self.login_frame, font="Helvetica 14 bold", bg="cadet blue", bd=22, text=total_amount)
                self.total_amount_value.grid(row=5, column=1)
        except sqlite3.Error as e:
            tkinter.messagebox.showerror("HOSPITAL DATABASE SYSTEM", str(e))

    def exit_application(self):
        self.master.destroy()

if __name__ == "__main__":
    root = Tk()
    app = BillingClass(root)
    root.mainloop()