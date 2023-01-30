import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3

import selenium.webdriver.common.bidi.console

values=['رقم البيعة', 'الرقم الوطني ', 'رقم الوحدة السكنية', 'رقم لوحة السيارة']

conn = sqlite3.connect('database.db')
cur = conn.cursor()

class Search:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("400x500+50+50")
        self.root.title("بحث")

        self.combobox = ttk.Combobox(self.root, values=values, justify='center')
        self.combobox.place(x=100, y=40, width=200, height=30)

        self.entry1 = tk.Entry(self.root, justify='center')
        self.entry1.place(x=125, y=100, width=150, height=30)

        self.butt1 = tk.Button(self.root, text='بحث', justify='center')
        self.butt1.place(x=150, y=160, width=100, height=30)
        self.butt1.configure(command=lambda: self.search())

        self.rows = None

    def search(self):
        if not self.combobox.get():
            messagebox.showerror("خطأ", "الرجاء اختيار نوع الرقم")
        else:
            if not self.entry1.get():
                messagebox.showinfo('ok', "الرجاء إدخال الرقم")
            else:
                if self.combobox.get() == values[0]:
                    self.rows = cur.execute("SELECT * from real_estate_sales WHERE code=?",
                                            [self.entry1.get()]).fetchall()
                    if len(self.rows) > 0:
                        self.rows = self.rows[0]
                        self.seller = cur.execute("SELECT * from people WHERE id=?", [self.rows[4]]).fetchall()[0]
                        self.buyer = cur.execute("SELECT * from people WHERE id=?", [self.rows[5]]).fetchall()[0]
                        self.real_estate = cur.execute("SELECT * from real_estate WHERE id=?", [self.rows[6]]).fetchall()[0]

                        label1 = tk.Label(self.root)
                        label1.place(x=200, y=200)
                        label1.configure(text=self.seller[1])

                        label1 = tk.Label(self.root)
                        label1.place(x=200, y=300)
                        label1.configure(text=self.buyer[1])

                        label1 = tk.Label(self.root)
                        label1.place(x=200, y=400)
                        label1.configure(text=self.real_estate[3])

                elif self.combobox.get() == values[1]:
                    messagebox.showinfo(values[1], values[1])
                elif self.combobox.get() == values[2]:
                    messagebox.showinfo(values[2], values[2])
                elif self.combobox.get() == values[3]:
                    messagebox.showinfo(values[3], values[3])
