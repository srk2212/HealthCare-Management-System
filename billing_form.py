from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import font
import sqlite3

class Billing:
    def __init__(self, master: Tk):
        """
        Initialize the Billing class.

        Args:
            master (Tk): The main application window.
        """
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master, bg="cadet blue")
        self.frame.pack()

        # =============ATTRIBUTES===========
        self.P_id = IntVar()
        self.dd = StringVar()
        self.treat_1 = StringVar()
        self.treat_2 = StringVar()
        self.cost_t = IntVar()
        self.med = StringVar()
        self.med_q = IntVar()
        self.price = IntVar()

        # ===============TITLE==========
        self.lblTitle = Label(self.frame, text="BILLING WINDOW", font="Helvetica 20 bold", bg="cadet blue")
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=25)

        # ===============FRAME==========
        self.LoginFrame = Frame(self.frame, width=400, height=80, relief="ridge", bg="cadet blue", bd=20)
        self.LoginFrame.grid(row=1, column=0)

        self.LoginFrame2 = Frame(self.frame, width=400, height=80, relief="ridge", bg="cadet blue", bd=20)
        self.LoginFrame2.grid(row=2, column=0)

        # ============LABELS=============
        self.lblpid = Label(self.LoginFrame, text="PATIENT ID", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblpid.grid(row=0, column=0)
        self.pid_entry = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.P_id)
        self.pid_entry.grid(row=0, column=1)

        self.lbldid = Label(self.LoginFrame, text="DATE DISCHARGED(YYYY-MM-DD)", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lbldid.grid(row=1, column=0)
        self.dd_entry = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.dd)
        self.dd_entry.grid(row=1, column=1)

        self.button2 = Button(self.LoginFrame, text="UPDATE DISCHARGE DATE", width=25, font="Helvetica 14 bold", bg="cadet blue", command=self.update_date)
        self.button2.grid(row=1, column=3)

        self.lbltreat = Label(self.LoginFrame, text="TREATMENT", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lbltreat.grid(row=2, column=0)
        self.treat_entry = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.treat_1)
        self.treat_entry.grid(row=2, column=1)

        self.lblcode_t1 = Label(self.LoginFrame, text="TREATMENT CODE", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblcode_t1.grid(row=3, column=0)
        self.treat_code_entry = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.treat_2)
        self.treat_code_entry.grid(row=3, column=1)

        self.lblap = Label(self.LoginFrame, text="TREATMENT COST ₹", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblap.grid(row=4, column=0)
        self.cost_entry = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.cost_t)
        self.cost_entry.grid(row=4, column=1)

        self.lblmed = Label(self.LoginFrame, text="MEDICINE", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblmed.grid(row=2, column=2)
        self.med_entry = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.med)
        self.med_entry.grid(row=2, column=3)

        self.med_t1 = Label(self.LoginFrame, text="MEDICINE QUANTITY", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.med_t1.grid(row=3, column=2)
        self.med_q_entry = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.med_q)
        self.med_q_entry.grid(row=3, column=3)

        self.lblapd = Label(self.LoginFrame, text="MEDICINE PRICE ₹", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblapd.grid(row=4, column=2)
        self.price_entry = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.price)
        self.price_entry.grid(row=4, column=3)

        # ============BUTTONS=============
        self.button3 = Button(self.LoginFrame2, text="UPDATE DATA", width=15, font="Helvetica 14 bold", bg="cadet blue", command=self.update_data)
        self.button3.grid(row=3, column=2)

        self.button4 = Button(self.LoginFrame2, text="GENERATE BILL", width=15, font="Helvetica 14 bold", bg="cadet blue", command=self.generate_bill)
        self.button4.grid(row=3, column=3)

        self.button6 = Button(self.LoginFrame2, text="EXIT", width=10, font="Helvetica 14 bold", bg="cadet blue", command=self.exit)
        self.button6.grid(row=3, column=4)

    def update_date(self):
        """
        Update the discharge date in the database.
        """
        try:
            with sqlite3.connect("HospitalDB.db") as conn:
                cursor = conn.cursor()
                patient_id = self.P_id.get()
                discharge_date = self.dd.get()
                cursor.execute("UPDATE ROOM SET DATE_DISCHARGED=? WHERE PATIENT_ID=?", (discharge_date, patient_id))
                conn.commit()
                tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "DISCHARGE DATE UPDATED")
        except sqlite3.Error as e:
            tkinter.messagebox.showerror("HOSPITAL DATABASE SYSTEM", str(e))

    def update_data(self):
        """
        Update the treatment and medicine data in the database.
        """
        try:
            with sqlite3.connect("HospitalDB.db") as conn:
                cursor = conn.cursor()
                patient_id = self.P_id.get()
                treatment = self.treat_1.get()
                treatment_code = self.treat_2.get()
                treatment_cost = self.cost_t.get()
                medicine = self.med.get()
                medicine_quantity = self.med_q.get()
                medicine_price = self.price.get()

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
        """
        Generate the bill for the patient.
        """
        try:
            with sqlite3.connect("HospitalDB.db") as conn:
                cursor = conn.cursor()
                patient_id = self.P_id.get()
                cursor.execute("SELECT SUM(T_COST + (M_COST * M_QTY) + (DATE_DISCHARGED - DATE_ADMITTED) * RATE) FROM ROOM NATURAL JOIN TREATMENT NATURAL JOIN MEDICINE WHERE PATIENT_ID=?", (patient_id,))
                total_amount = cursor.fetchone()[0]
                if total_amount is None:
                    total_amount = 0
                self.total_amount_label = Label(self.LoginFrame, text="TOTAL AMOUNT OUTSTANDING", font="Helvetica 14 bold", bg="cadet blue", bd=22)
                self.total_amount_label.grid(row=5, column=0)
                self.total_amount_value = Label(self.LoginFrame, font="Helvetica 14 bold", bg="cadet blue", bd=22, text=total_amount)
                self.total_amount_value.grid(row=5, column=1)
        except sqlite3.Error as e:
            tkinter.messagebox.showerror("HOSPITAL DATABASE SYSTEM", str(e))

    def exit(self):
        """
        Exit the application.
        """
        self.master.destroy()

if __name__ == "__main__":
    root = Tk()
    app = Billing(root)
    root.mainloop()