from tkinter import *
import tkinter.messagebox
from tkinter import ttk
from tkinter import font
import sqlite3

class Appointment:
    def __init__(self, master: Tk):
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master, bg="cadet blue")
        self.frame.pack()

        # =============ATTRIBUTES===========
        self.pat_ID = IntVar()
        self.emp_ID = StringVar()
        self.ap_no = StringVar()
        self.ap_time = StringVar()
        self.ap_date = StringVar()
        self.des = StringVar()

        # ===============TITLE==========
        self.lblTitle = Label(self.frame, text="APPOINTMENT FORM", font="Helvetica 20 bold", bg="cadet blue")
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=50)
        # ===============FRAME==========
        self.LoginFrame = Frame(self.frame, width=800, height=200, relief="ridge", bg="cadet blue", bd=20)
        self.LoginFrame.grid(row=1, column=0)
        self.LoginFrame2 = Frame(self.frame, width=400, height=80, relief="ridge", bg="cadet blue", bd=20)
        self.LoginFrame2.grid(row=2, column=0)
        # ============LABELS=============
        self.lblpid = Label(self.LoginFrame, text="PATIENT ID", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblpid.grid(row=0, column=0)
        self.pid_entry = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.pat_ID)
        self.pid_entry.grid(row=0, column=1)

        self.lbldid = Label(self.LoginFrame, text="DOCTOR ID", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lbldid.grid(row=1, column=0)
        self.did_entry = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.emp_ID)
        self.did_entry.grid(row=1, column=1)

        self.lblap = Label(self.LoginFrame, text="APPOINTMENT NO", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblap.grid(row=2, column=0)
        self.ap_entry = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.ap_no)
        self.ap_entry.grid(row=2, column=1)

        self.lblapt = Label(self.LoginFrame, text="APPOINTMENT TIME(HH:MM:SS)", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblapt.grid(row=0, column=2)
        self.apt_entry = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.ap_time)
        self.apt_entry.grid(row=0, column=3)

        self.lblapd = Label(self.LoginFrame, text="APPOINTMENT DATE(YYYY-MM-DD)", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblapd.grid(row=1, column=2)
        self.apd_entry = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.ap_date)
        self.apd_entry.grid(row=1, column=3)

        self.lbldes = Label(self.LoginFrame, text="DESCRIPTION", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lbldes.grid(row=2, column=2)
        self.des_entry = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.des)
        self.des_entry.grid(row=2, column=3)

        # ============BUTTONS=============
        self.button2 = Button(self.LoginFrame2, text="SAVE", width=10, font="Helvetica 14 bold", bg="cadet blue",
                               command=self.insert_ap)
        self.button2.grid(row=0, column=1)

        self.button3 = Button(self.LoginFrame2, text="DELETE", width=10, font="Helvetica 14 bold", bg="cadet blue",
                             command=self.delete_ap_display)
        self.button3.grid(row=0, column=2)

        self.button4 = Button(self.LoginFrame2, text="SEARCH APPOINTMENTS", width=20, font="Helvetica 14 bold", bg="cadet blue",
                              command=self.search_ap_display)
        self.button4.grid(row=0, column=3)

        self.button6 = Button(self.LoginFrame2, text="EXIT", width=10, font="Helvetica 14 bold", bg="cadet blue",
                             command=self.exit)
        self.button6.grid(row=0, column=4)

    def exit(self):
        self.master.destroy()

    def insert_ap(self):
        try:
            conn = sqlite3.connect("HospitalDB.db")
            c = conn.cursor()
            e1 = self.pat_ID.get()
            e2 = self.emp_ID.get()
            e3 = self.ap_no.get()
            e4 = self.ap_time.get()
            e5 = self.ap_date.get()
            e6 = self.des.get()
            c.execute("SELECT * FROM appointment WHERE AP_NO = ?", (e3,))
            if c.fetchone():
                tkinter.messagebox.showerror("HOSPITAL DATABASE SYSTEM", "APPOINTMENT ALREADY EXISTS")
            else:
                c.execute("INSERT INTO appointment VALUES (?, ?, ?, ?, ?, ?)", (e1, e2, e3, e4, e5, e6))
                tkinter.messagebox.showinfo("Hospital DATABASE SYSTEM", "APPOINTMENT SET SUCCESSFULLY")
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            tkinter.messagebox.showerror("HOSPITAL DATABASE SYSTEM", str(e))

    def delete_ap_display(self):
        self.newWindow = Toplevel(self.master)
        self.app = DeleteAP(self.newWindow)

    def search_ap_display(self):
        self.newWindow = Toplevel(self.master)
        self.app = SearchAP(self.newWindow)


class DeleteAP:
    def __init__(self, master: Tk):
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master, bg="cadet blue")
        self.frame.pack()
        self.de1_ap = StringVar()

        self.lblTitle = Label(self.frame, text="DELETE APPOINTMENT WINDOW", font="Helvetica 20 bold", bg="cadet blue")
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=50)

        self.LoginFrame = Frame(self.frame, width=400, height=80, relief="ridge", bg="cadet blue", bd=20)
        self.LoginFrame.grid(row=1, column=0)

        self.LoginFrame2 = Frame(self.frame, width=400, height=80, relief="ridge", bg="cadet blue", bd=20)
        self.LoginFrame2.grid(row=2, column=0)

        self.lblpatid = Label(self.LoginFrame, text="ENTER APPOINTMENT NO TO DELETE", font="Helvetica 14 bold", bg="cadet blue",
                             bd=22)
        self.lblpatid.grid(row=0, column=0)
        self.patid_entry = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.de1_ap)
        self.patid_entry.grid(row=0, column=1)

        self.DeleteB = Button(self.LoginFrame2, text="DELETE", width=10, font="Helvetica 14 bold", bg="cadet blue",
                              command=self.delete_ap)
        self.DeleteB.grid(row=0, column=1)

    def delete_ap(self):
        try:
            conn = sqlite3.connect("HospitalDB.db")
            c = conn.cursor()
            inp_d = self.de1_ap.get()
            c.execute("SELECT * FROM appointment WHERE AP_NO = ?", (inp_d,))
            if not c.fetchone():
                tkinter.messagebox.showerror("HOSPITAL DATABASE SYSTEM", "PATIENT APPOINTMENT NOT FIXED")
            else:
                c.execute("DELETE FROM appointment WHERE AP_NO = ?", (inp_d,))
                tkinter.messagebox.showinfo("Hospital DATABASE SYSTEM", "PATIENT APPOINTMENT DELETED")
            conn.commit()
            conn.close()
        except sqlite3.Error as e:
            tkinter.messagebox.showerror("HOSPITAL DATABASE SYSTEM", str(e))


class SearchAP:
    def __init__(self, master: Tk):
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1500x700+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master, bg="cadet blue")
        self.frame.pack()
        self.entry = StringVar()

        self.lblTitle = Label(self.frame, text="SEARCH APPOINTMENT WINDOW", font="Helvetica 20 bold", bg="cadet blue")
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=25)

        self.LoginFrame = Frame(self.frame, width=400, height=200, relief="ridge", bg="cadet blue", bd=20)
        self.LoginFrame.grid(row=1, column=0)

        self.LoginFrame2 = Frame(self.frame, width=400, height=80, relief="ridge", bg="cadet blue", bd=20)
        self.LoginFrame2.grid(row=2, column=0)

        self.lblpatid = Label(self.LoginFrame, text="ENTER DATE TO VIEW APPOINTMENTS(YYYY-MM-DD)", font="Helvetica 14 bold",
                             bg="cadet blue", bd=22)
        self.lblpatid.grid(row=0, column=0)
        self.patid_entry = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.entry)
        self.patid_entry.grid(row=0, column=1)

        self.SearchB = Button(self.LoginFrame2, text="SEARCH", width=10, font="Helvetica 14 bold", bg="cadet blue",
                              command=self.search_ap)
        self.SearchB.grid(row=0, column=1)

    def search_ap(self):
        try:
            conn = sqlite3.connect("HospitalDB.db")
            c = conn.cursor()
            ap = self.entry.get()
            c.execute("SELECT * FROM appointment WHERE AP_DATE = ?", (ap,))
            if not c.fetchall():
                tkinter.messagebox.showerror("HOSPITAL DATABASE SYSTEM", "THERE'S NO APPOINTMENT BOOKED")
            else:
                c.execute("SELECT PATIENT_ID, EMP_ID, AP_NO, AP_DATE, AP_TIME, DES FROM appointment WHERE AP_DATE = ?",
                           (ap,))
                for i in c.fetchall():
                    self.l1 = Label(self.LoginFrame, text="PATIENT ID", font="Helvetica 14 bold", bg="cadet blue", bd=22)
                    self.l1.grid(row=1, column=0)
                    self.dis1 = Label(self.LoginFrame, font="Helvetica 14 bold", bd=2, bg="cadet blue", text=i[0])
                    self.dis1.grid(row=1, column=1)

                    self.l2 = Label(self.LoginFrame, text="DOCTOR ID", font="Helvetica 14 bold", bg="cadet blue", bd=22)
                    self.l2.grid(row=2, column=0)
                    self.dis2 = Label(self.LoginFrame, font="Helvetica 14 bold", bd=2, bg="cadet blue", text=i[1])
                    self.dis2.grid(row=2, column=1)

                    self.l3 = Label(self.LoginFrame, text="APPOINTMENT NO", font="Helvetica 14 bold", bg="cadet blue", bd=22)
                    self.l3.grid(row=3, column=0)
                    self.dis3 = Label(self.LoginFrame, font="Helvetica 14 bold", bd=2, bg="cadet blue", text=i[2])
                    self.dis3.grid(row=3, column=1)

                    self.l4 = Label(self.LoginFrame, text="APPOINTMENT DATE", font="Helvetica 14 bold", bg="cadet blue", bd=22)
                    self.l4.grid(row=4, column=0)
                    self.dis4 = Label(self.LoginFrame, font="Helvetica 14 bold", bd=2, bg="cadet blue", text=i[3])
                    self.dis4.grid(row=4, column=1)

                    self.l5 = Label(self.LoginFrame, text="APPOINTMENT TIME", font="Helvetica 14 bold", bg="cadet blue", bd=22)
                    self.l5.grid(row=5, column=0)
                    self.dis5 = Label(self.LoginFrame, font="Helvetica 14 bold", bd=2, bg="cadet blue", text=i[4])
                    self.dis5.grid(row=5, column=1)

                    self.l6 = Label(self.LoginFrame, text="DESCRIPTION", font="Helvetica 14 bold", bg="cadet blue", bd=22)
                    self.l6.grid(row=6, column=0)
                    self.dis6 = Label(self.LoginFrame, font="Helvetica 14 bold", bd=2, bg="cadet blue", text=i[5])
                    self.dis6.grid(row=6, column=1)
            conn.close()
        except sqlite3.Error as e:
            tkinter.messagebox.showerror("HOSPITAL DATABASE SYSTEM", str(e))


if __name__ == "__main__":
    root = Tk()
    app = Appointment(root)
    root.mainloop()