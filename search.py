import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import os

dir = os.path.abspath(os.path.dirname(__file__))
values=['رقم البيعة', 'الرقم الوطني ', 'رقم الوحدة السكنية', 'رقم لوحة السيارة']

conn = sqlite3.connect(os.path.join(dir, 'database.db'))
cur = conn.cursor()


class Search:
    def __init__(self):
        self.root = tk.Toplevel()
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
        self.img1 = tk.PhotoImage(file=os.path.join(dir, 'design/search.001.png'))

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

                        self.root.geometry("700x500+50+50")
                        self.root.title("نتيجة البحث")

                        # operation
                        label1 = tk.Label(self.root, image=self.img1)
                        label1.place(relx=0, rely=0)
                        # label1.configure(image=img)

                        label11 = tk.Label(self.root, font=('Helvetica, 12'))
                        label11.place(x=500, y=70, width=100, height=30)
                        label11.configure(text=self.rows[3])

                        label12 = tk.Label(self.root, font=('Helvetica, 12'))
                        label12.place(x=320, y=70, width=100, height=30)
                        label12.configure(text=self.rows[1])

                        label13 = tk.Label(self.root, font=('Helvetica, 12'))
                        label13.place(x=180, y=70, width=80, height=30)
                        label13.configure(text=self.rows[2])

                        label14 = tk.Label(self.root, font=('Helvetica, 12'))
                        label14.place(x=80, y=70, width=80, height=30)
                        label14.configure(text=self.rows[3])

                        # seller
                        label21 = tk.Label(self.root, font=('Helvetica, 12'))
                        label21.place(x=500, y=170, width=150, height=30)
                        label21.configure(text=self.seller[1])

                        label22 = tk.Label(self.root, font=('Helvetica, 12'))
                        label22.place(x=320, y=170, width=100, height=30)
                        label22.configure(text=self.seller[2])

                        label23 = tk.Label(self.root, font=('Helvetica, 12'))
                        label23.place(x=200, y=170, width=80, height=30)
                        label23.configure(text=self.seller[3])

                        label24 = tk.Label(self.root, font=('Helvetica, 12'))
                        label24.place(x=100, y=170, width=80, height=30)
                        label24.configure(text=self.seller[4])

                        # buyer
                        label31 = tk.Label(self.root)
                        label31.place(x=500, y=270, width=150, height=30)
                        label31.configure(text=self.buyer[1])

                        label32 = tk.Label(self.root)
                        label32.place(x=320, y=270, width=100, height=30)
                        label32.configure(text=self.buyer[2])

                        label33 = tk.Label(self.root)
                        label33.place(x=200, y=270, width=80, height=30)
                        label33.configure(text=self.buyer[3])

                        label34 = tk.Label(self.root)
                        label34.place(x=100, y=270, width=80, height=30)
                        label34.configure(text=self.buyer[4])

                        # real estate
                        label41 = tk.Label(self.root)
                        label41.place(x=550, y=370, width=100, height=30)
                        label41.configure(text=self.real_estate[1])

                        label42 = tk.Label(self.root)
                        label42.place(x=400, y=370, width=80, height=30)
                        label42.configure(text=self.real_estate[2])

                        label43 = tk.Label(self.root)
                        label43.place(x=300, y=370, width=80, height=30)
                        label43.configure(text=self.real_estate[3])

                        label44 = tk.Label(self.root)
                        label44.place(x=200, y=370, width=80, height=30)
                        label44.configure(text=self.real_estate[4])

                        label45 = tk.Label(self.root)
                        label45.place(x=100, y=370, width=50, height=30)
                        label45.configure(text=self.real_estate[5])

                        label46 = tk.Label(self.root)
                        label46.place(x=30, y=370, width=50, height=30)
                        label46.configure(text=self.real_estate[5])

                        # buttons
                        but1 = tk.Button(self.root, text="إغلاق")
                        but1.place(x=500, y=450, width=80, height=30)
                        but1.configure(command=self.root.destroy)

                        but2 = tk.Button(self.root, text="بحث جديد")
                        but2.place(x=300, y=450, width=80, height=30)
                        but2.configure(command= lambda: self.back())

                        but2 = tk.Button(self.root, text="طباعة وثيقة")
                        but2.place(x=100, y=450, width=80, height=30)
                        but2.configure(command=Search)

                    else:
                        messagebox.showinfo('خطأ', "عذرا لا توحد بيعة بهذا الرقم!\nيرجى التأكد من نوع الرقم ومن الرقم نفسه")

                elif self.combobox.get() == values[1]:
                    messagebox.showinfo(values[1], values[1])
                elif self.combobox.get() == values[2]:
                    messagebox.showinfo(values[2], values[2])
                elif self.combobox.get() == values[3]:
                    messagebox.showinfo(values[3], values[3])

    def back(self):
        self.root.destroy()
        Search()
