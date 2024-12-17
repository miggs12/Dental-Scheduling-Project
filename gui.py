import tkinter as tk
from tkinter import ttk
from database import init_database
import sqlite3

class DentalSchedulerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dental Appointment Scheduler")
        self.create_widgets()

    def create_widgets(self):
        #Patient name
        tk.Label(self.root, text = "Patient Name:").grid(row = 0, column = 0)
        self.name_entry = tk.Entry(self.root)
        self.name_entry.grid(row = 0, column = 1)

        #Phone number
        tk.Label(self.root, text = "Phone Number:").grid(row = 1, column = 0)
        self.phone_entry = tk.Entry(self.root)
        self.phone_entry.grid(row = 1, column = 1)

        #Procedure
        tk.Label(self.root, text = "Procedure:").grid(row = 2, column = 0)
        self.procedure_dropdown = tk.Entry(self.root)
        self.procedure_dropdown.grid(row = 2, column = 1)

        #Appointment time
        tk.Label(self.root, text = "Appointment time:").grid(row = 3, column = 0)
        self.time_entry = tk.Entry(self.root)
        self.time_entry.grid(row = 3, column = 1)

        #Buttons
        tk.Button(self.root, text = "Schedule Appointment", command = self.schedule_appointment).grid(row = 4, column = 0)
        tk.Button(self.root, text = "View Appointment", command = self.view_appointments).grid(row = 4, column = 1)

    def schedule_appointment(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        procedure = self.procedure_dropdown.get()
        time = self.time_entry.get()

        #Insert into database
        connection = sqlite3.connect("dental_scheduler.db")
        cursor = connection.cursor()
        cursor.execute("INSERT INTO patients (name, phone) VALUES (?, ?)", (name, phone))
        patient_id = cursor.lastrowid
        cursor.execute("INSERT INTO appointments (patient_id, procedure_id, appointment_time) VALUES (?, ?, ?)", (patient_id, 1, time))
        connection.commit()
        connection.close()
        print(f'Appointment scheduled for {name} at {time}.')

    def view_appointments(self):
        #Display appointments
        connection = sqlite3.connect("dental_scheduler.db")
        cursor = connection.cursor()
        cursor.execute("""
        SELECT patients.name, patients.phone, appointments.appointment_time
        FROM appointments
        JOIN patients ON appointments.patient_id = patient_id
        """)
        rows = cursor.fetchall()
        connection.close()

        for row in rows:
            print(row)

if __name__ == "__main__":
    init_database()
    root = tk.Tk()
    app = DentalSchedulerApp()
    root.mainloop()