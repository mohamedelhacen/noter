import sqlite3
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import os
import sqlite3

from utils import exitt

dir = os.path.abspath(os.path.dirname(__file__))
db = sqlite3.connect(os.path.join(dir, 'database.db'))
cursor = db.cursor()

class New:
    def __init__(self):
        self.new = tk.Toplevel()
        self.new.title("عملية جديدة")
        self.new.geometry("1024x720+0+0")
        self.new.protocol("WM_DELETE_WINDOW", lambda: exitt(self.new))

        self.background_img = tk.PhotoImage(file=os.path.join(dir, 'design/design.002.png'))
        self.label1 = tk.Label(self.new)
        self.label1.configure(image=self.background_img)
        self.label1.place(relx=0, rely=0)

        self.button1 = tk.Button(self.new)
        self.button1.place(x=718, y=210, width=252, height=72)
        self.button1.configure(text="بيع عقار")
        self.button1.configure(command=RealEstate)

        self.button2 = tk.Button(self.new)
        self.button2.place(x=387, y=210, width=252, height=72)
        self.button2.configure(text="سيارة")

        self.button3 = tk.Button(self.new)
        self.button3.place(x=22, y=210, width=252, height=72)
        self.button3.configure(text="محل تجاري")

        self.new.mainloop()


def create_real_estate_facture(s_name, s_ni, s_birthd, s_birthp, b_name, b_ni, b_birthd, b_birthp, city, block,
                               re_data, re_number, amount, date, code):

    cursor.execute("""INSERT INTO people(name, ni, birth_date, birth_place) VALUES (?, ?, ?, ?) WHERE NOT EXISTS (
                    SELECT ni FROM people WHERE ni = ?)
    """, [s_name, s_ni, s_birthd, s_birthp, s_ni])
    cursor.execute(f"""INSERT INTO people(name, ni, birth_date, birth_place), 
                    [{b_name}, {b_ni}, {b_birthd}, {b_birthp}] WHERE NOT EXISTS (
                    SELECT ni FROM people WHERE ni = ?)
    """, [b_ni])

    cursor.execute(f"""INSERT INTO real_estate(city, block, date, number), 
                    [{city}, {block}, {re_data}, {re_number}] WHERE NOT EXISTS (
                    SELECT * FROM real_estate WHERE city = ? and block = ? and date = ? and number = ?)
    """, [city, block, re_data, re_number])

    s_id = cursor.execute("SELECT ni FROM people WHERE ni = ?", [s_ni])
    b_id = cursor.execute("SELECT ni FROM people WHERE ni = ?", [s_ni])
    re_id = cursor.execute("SELECT id FROM real_estate WHERE city = ? and block = ? and date = ? and number = ?",
                           [city, block, re_data, re_number])

    cursor.execute(f"""INSERT INTO real_estate_sales(amount, date, code, seller_Id, buyer_Id, real_estate_Id),
                [{amount}, {date}, {code}, {s_id}, {b_id}, {re_id}]
    """)


    facture = tk.Toplevel()
    facture.geometry("400x720")
    facture.title("الوثيقة")

    text = tk.Text(facture, font=('calibri', 16))
    text.insert('end', f"""
            No:                                                    {code}    :الرقم 
            Date:                                                {date}         :التاريخ
    """)
    text.insert('end', f"""
    أشهدني واستكتبني السيد(ة) {s_name} المولود بتاريخ {s_birthd} في {s_birthp} رقم البطاقة الوطنية {s_ni}\
     أنه تنازل عن قطعة أرضية في {city} القطاع {block} رقمها {re_number} عندها إفادة (batch) صادرة بتاريخ {re_data}\
      من وكالة التنيمة الحضرية للسيد(ة) {b_name} المولود بتاريخ {b_bithd} في {b_birthp} رقم البطاقة الوطنية {b_ni}\
       مقابل مبلغ قدره {amount} استلم البائع المبلغ ولم تبقى بينهم أي مطالبة
    """)
    text.configure(state='disabled')
    text.pack()


    facture.mainloop()


class RealEstate:
    def __init__(self):
        self.top = tk.Toplevel()
        self.top.geometry("1024x720+0+0")
        self.top.title("عقار")
        self.top.protocol("WM_DELETE_WINDOW", lambda: exitt(self.top))

        self.now = datetime.now()
        self.date = self.now.strftime("%Y-%m-%d")
        self.code = self.now.strftime("%Y%m%d%H%M%S")

        self.label1 = tk.Label(self.top)
        self.backg = tk.PhotoImage(file=os.path.join(dir, 'design/design.003.png'))
        self.label1.configure(image=self.backg)
        self.label1.place(relx=0, rely=0)

        # اليائع
        self.entry1 = tk.Entry(self.top, justify='right')
        self.entry1.place(x=550, y=160, width=240, height=40)
        self.entry1.insert(0, 'محمد الحسن حبيب')

        self.entry2 = tk.Entry(self.top, justify='center')
        self.entry2.place(x=380, y=160, width=120, height=40)
        self.entry2.insert(0, '222222222')

        self.entry3 = tk.Entry(self.top, justify='center')
        self.entry3.place(x=200, y=160, width=100, height=40)
        self.entry3.insert(0, '12/12/1995')

        self.entry4 = tk.Entry(self.top, justify='right')
        self.entry4.place(x=40, y=160, width=100, height=40)
        self.entry4.insert(0, 'بوكي')

        # المشتري
        self.entry5 = tk.Entry(self.top, justify='right')
        self.entry5.place(x=550, y=282, width=240, height=40)
        self.entry5.insert(0, 'محمد محمود')

        self.entry6 = tk.Entry(self.top, justify='center')
        self.entry6.place(x=380, y=282, width=120, height=40)
        self.entry6.insert(0, '33333333')

        self.entry7 = tk.Entry(self.top, justify='center')
        self.entry7.place(x=200, y=282, width=100, height=40)
        self.entry7.insert(0, '10/10/1989')

        self.entry8 = tk.Entry(self.top, justify='right')
        self.entry8.place(x=40, y=282, width=100, height=40)
        self.entry8.insert(0, 'روصو')

        # تفاصيل العقار
        self.entry9 = tk.Entry(self.top, justify='right')
        self.entry9.place(x=680, y=415, width=120, height=40)
        self.entry9.insert(0, 'دار النعيم')

        self.entry10 = tk.Entry(self.top, justify='center')
        self.entry10.place(x=480, y=415, width=120, height=40)
        self.entry10.insert(0, 'TNS1')

        self.entry11 = tk.Entry(self.top, justify='center')
        self.entry11.place(x=280, y=415, width=120, height=40)
        self.entry11.insert(0, '2013')

        self.entry12 = tk.Entry(self.top, justify='right')
        self.entry12.place(x=80, y=415, width=120, height=40)
        self.entry12.insert(0, '750')


        # تفاصيل العملية
        self.entry13 = tk.Entry(self.top, justify='center')
        self.entry13.place(x=680, y=550, width=120, height=40)
        self.entry13.insert(0, '40000')

        self.entry14 = tk.Entry(self.top, justify='center')
        self.entry14.place(x=480, y=550, width=120, height=40)
        self.entry14.insert('0', self.date)
        self.entry14.configure(state='disabled')
        # self.entry14.configure(textvariable=date)

        self.entry15 = tk.Entry(self.top, justify='center')
        self.entry15.place(x=280, y=550, width=120, height=40)
        self.entry15.insert('0', self.code)
        self.entry15.configure(state='disabled')
        # self.entry15.configure(textvariable=code)

        # buttons
        self.button1 = tk.Button(self.top, text="إلغاء")
        self.button1.place(x=727, y=645, width=180, height=65)

        self.button2 = tk.Button(self.top, text="حفظ")
        self.button2.place(x=396, y=645, width=180, height=65)
        self.button2.configure(command=lambda: self.save())

        self.button3 = tk.Button(self.top, text="العودة")
        self.button3.place(x=80, y=645, width=180, height=65)

        self.top.mainloop()

    def cancel(self):
        pass

    def save(self):
        if self.entry1.get():
            seller_name = self.entry1.get()
            if self.entry2.get():
                seller_ni = self.entry2.get()
                if self.entry3.get():
                    seller_birthdate = self.entry3.get()
                    if self.entry4.get():
                        seller_birthplace = self.entry4.get()
                        if self.entry5.get():
                            buyer_name = self.entry5.get()
                            if self.entry6.get():
                                buyer_ni = self.entry6.get()
                                if self.entry7.get():
                                    buyer_birthdate = self.entry7.get()
                                    if self.entry8.get():
                                        buyer_birthplace = self.entry8.get()
                                        if self.entry9.get():
                                            city = self.entry9.get()
                                            if self.entry10.get():
                                                block = self.entry10.get()
                                                if self.entry11.get():
                                                    re_data = self.entry11.get()
                                                    if self.entry12.get():
                                                        re_number = self.entry12.get()
                                                        if self.entry13.get():
                                                            amount = self.entry13.get()
                                                            if self.entry14.get() and self.entry15.get():
                                                                date = self.entry14.get()
                                                                code = self.entry15.get()

                                                                create_real_estate_facture(seller_name, seller_ni, seller_birthdate, seller_birthplace,
                                                                                           buyer_name, buyer_ni, buyer_birthdate, buyer_birthplace,
                                                                                           city, block, re_data, re_number, amount, date, code)

                                                            else:
                                                                messagebox.showerror('خطأ', "يوجد خطأ في المدخلات")
                                                        else:
                                                            messagebox.showerror('خطأ', "يجب إدخال المبلغ")
                                                    else:
                                                        messagebox.showerror('خطأ', "يجب إدخال رقم العقار")
                                                else:
                                                    messagebox.showerror('خطأ', "يجب إدخال تاريخ الإصدار")
                                            else:
                                                messagebox.showerror('خطأ', "يجب إدخال القطاع")
                                        else:
                                            messagebox.showerror('خطأ', "يجب إدخال المقاطعة")
                                    else:
                                        messagebox.showerror('خطأ', "يجب إدخال محل ميلاد المشتري")
                                else:
                                    messagebox.showerror('خطأ', "يجب إدخال تاريخ ميلاد المشتري")
                            else:
                                messagebox.showerror('خطأ', "يجب إدخال الرقم الوطني للمشتري")
                        else:
                            messagebox.showerror('خطأ', "يجب إدخال اسم المشتري")
                    else:
                        messagebox.showerror('خطأ', "يجب إدخال محل ميلاد البائع")
                else:
                    messagebox.showerror('خطأ', "يجب إدخال تاريخ ميلاد البائع")
            else:
                messagebox.showerror('خطأ', "يجب إدخال الرقم الوطني للبائع")
        else:
            messagebox.showerror('خطأ', "يجب إدخال اسم البائع")

    def back(self):
        pass




