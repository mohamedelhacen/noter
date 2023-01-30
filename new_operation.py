import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

from datetime import datetime
import os
import sqlite3
from utils import exitt, capture

dir = os.path.abspath(os.path.dirname(__file__))
db = sqlite3.connect(os.path.join(dir, 'database.db'))
cursor = db.cursor()


class New:
    def __init__(self, top=None):
        self.new = tk.Toplevel(top)
        self.new.title("عملية جديدة")
        self.new.geometry("1024x720+0+0")
        self.new.protocol("WM_DELETE_WINDOW", lambda: exitt(self.new))

        self.background_img = tk.PhotoImage(file=os.path.join(dir, 'design/design.002.png'))
        self.label1 = tk.Label(self.new)
        self.label1.configure(image=self.background_img)
        self.label1.place(relx=0, rely=0)

        self.button1 = tk.Button(self.new, font=("Helvetica, 30"))
        self.button1.place(x=700, y=150, width=200, height=80)
        self.button1.configure(relief="flat", overrelief="flat")
        self.button1.configure(borderwidth=0)
        self.button1.configure(border=0)
        self.button1.configure(background='orange')
        self.button1.configure(text="عقار")
        self.button1.configure(command=RealEstate)

        self.button2 = tk.Button(self.new, font=("Helvetica, 30"))
        self.button2.place(x=400, y=150, width=200, height=80)
        self.button2.configure(relief="flat", overrelief="flat")
        self.button2.configure(borderwidth=0)
        self.button2.configure(border=0)
        self.button2.configure(background='orange')
        self.button2.configure(text="سيارة")
        self.button2.configure(command=Car)

        self.button3 = tk.Button(self.new, font=("Helvetica, 30"))
        self.button3.place(x=100, y=150, width=200, height=80)
        self.button3.configure(relief="flat", overrelief="flat")
        self.button3.configure(borderwidth=0)
        self.button3.configure(border=0)
        self.button3.configure(background='orange')
        self.button3.configure(text="محل تجاري")
        self.button3.configure(command=lambda: capture(self.new))

        button4 = tk.Button(self.new)
        button4.place(x=150, y=450, width=250, height=60)
        button4.configure(relief="flat", overrelief="flat")
        button4.configure(font=("Helvetica, 20"))
        button4.configure(borderwidth=0)
        button4.configure(border=0)
        button4.configure(background='orange')
        button4.configure(text="إغلاق البرنامج")
        button4.configure(command=lambda: exitt(top))

        button4 = tk.Button(self.new)
        button4.place(x=600, y=450, width=250, height=60)
        button4.configure(relief="flat", overrelief="flat")
        button4.configure(font=("Helvetica, 20"))
        button4.configure(borderwidth=0)
        button4.configure(border=0)
        button4.configure(background='orange')
        button4.configure(text="العودة للصفحة السابقة")
        button4.configure(command=self.new.destroy)

        self.new.mainloop()


def save_to_db(s_name, s_ni, s_birthd, s_birthp, b_name, b_ni, b_birthd, b_birthp, nbr_rec, city, block,
               re_data, re_number, statement, amount, date, code, sale_type):

    cursor.execute("""INSERT OR IGNORE INTO people(name, ni, birth_date, birth_place) VALUES (?, ?, ?, ?)""",
                   [s_name, s_ni, s_birthd, s_birthp])

    cursor.execute("""INSERT OR IGNORE INTO people(name, ni, birth_date, birth_place) VALUES (?, ?, ?, ?)""",
                   [b_name, b_ni, b_birthd, b_birthp])

    cursor.execute(f"""INSERT OR IGNORE INTO real_estate(nbr_rec, city, block, date, number, statement) VALUES (?, ?, ?, ?, ?, ?)""",
                   [nbr_rec, city, block, re_data, re_number, statement])

    s_id = cursor.execute("SELECT id FROM people WHERE ni = ?", [s_ni]).fetchone()[0]
    b_id = cursor.execute("SELECT id FROM people WHERE ni = ?", [b_ni]).fetchone()[0]
    re_id = cursor.execute("SELECT id FROM real_estate WHERE nbr_rec = ?", [nbr_rec]).fetchone()[0]

    cursor.execute("""INSERT INTO real_estate_sales(amount, date, code, sale_type, seller_Id, buyer_Id, real_estate_Id) 
    VALUES (?, ?, ?, ?, ?, ?, ?)""", [amount, date, code, sale_type, s_id, b_id, re_id])

    db.commit()


def save_and_print(s_name, s_ni, s_birthd, s_birthp, b_name, b_ni, b_birthd, b_birthp, nbr_rec, city, block,
                   re_data, re_number, statement, amount, date, code, sale_type, window):
    print(window.winfo_y(), window.winfo_rooty(), window.winfo_height())
    print(window.winfo_x(), window.winfo_rootx(), window.winfo_width())
    capture(window)
    save_to_db(s_name, s_ni, s_birthd, s_birthp, b_name, b_ni, b_birthd, b_birthp, nbr_rec, city, block,
               re_data, re_number, statement, amount, date, code, sale_type)


def create_real_estate_facture(s_name, s_ni, s_birthd, s_birthp, b_name, b_ni, b_birthd, b_birthp, nbr_rec, city, block,
                               re_data, re_number, statement, amount, date, code, sale_type):
    facture = tk.Toplevel()
    facture.geometry("500x800+100+0")
    facture.title("الوثيقة")

    canvas = tk.Canvas(facture)
    canvas.place(x=0, y=0, width=500, height=700)

    fac_img = tk.PhotoImage(file=os.path.join(dir, 'design/fac.001.png'))
    backg = tk.Label(canvas, image=fac_img)
    backg.place(x=0, y=0, width=500, height=700)

    content = f""" أشهدني واستكتبني السيد(ة){s_name} المولود بتاريخ {s_birthd} في {s_birthp} رقم البطاقة الوطنية {s_ni} أنه {sale_type} قطعة أرضية في {city} القطاع {block} رقمها {re_number} عندها إفادة {statement} صادرة بتاريخ {re_data} من وكالة التنيمة الحضرية للسيد(ة) {b_name} المولود بتاريخ {b_birthd} في {b_birthp} رقم البطاقة الوطنية {b_ni} مقابل مبلغ قدره {amount} استلم البائع المبلغ ولم تبقى بينهم أي مطالبة
     """

    dt = tk.Text(canvas, font=('Helvetica', 16), bd=0, bg='white')
    dt.insert('end', code)
    dt.tag_configure("center", justify='center')
    dt.tag_add('center', 1.0, 'end')
    dt.place(x=180, y=100, width=150, height=25)
    dt.config(highlightthickness=0, borderwidth=0)

    cd = tk.Text(canvas, font=('Helvetica', 16))
    cd.insert('end', date)
    cd.tag_configure("center", justify='center')
    cd.tag_add('center', 1.0, 'end')
    cd.place(x=180, y=132, width=150, height=25)
    cd.config(highlightthickness=0, borderwidth=0)

    text = tk.Text(canvas, font=('Helvetica', 18), spacing1=5, spacing2=20, spacing3=5, borderwidth='0')
    text.tag_configure("right", justify='right')
    text.insert('end', content)
    text.tag_add('right', 1.0, 'end')
    text.configure(state='disabled', wrap='word', blockcursor=True)
    text.place(x=0, y=200, width=500, height=300)
    text.config(highlightthickness=0, borderwidth=0)

    butt1 = tk.Button(facture, text="طباعة و حفظ")
    butt1.place(x=300, y=750, width=150, height=60)
    butt1.configure(command=lambda: save_and_print(s_name, s_ni, s_birthd, s_birthp, b_name, b_ni, b_birthd, b_birthp,
                                                   nbr_rec, city, block, re_data, re_number, statement, amount, date,
                                                   code, sale_type, canvas))

    butt2 = tk.Button(facture, text="تعديل أو إلغاء")
    butt2.place(x=100, y=750, width=150, height=60)
    butt2.config(command=facture.destroy)

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
        self.entry1.place(x=380, y=130, width=280, height=30)

        self.entry2 = tk.Entry(self.top, justify='center')
        self.entry2.place(x=740, y=130, width=120, height=30)

        self.entry3 = tk.Entry(self.top, justify='center')
        self.entry3.place(x=200, y=130, width=110, height=30)

        self.entry4 = tk.Entry(self.top, justify='right')
        self.entry4.place(x=50, y=130, width=110, height=30)

        # المشتري
        self.entry5 = tk.Entry(self.top, justify='right')
        self.entry5.place(x=380, y=230, width=280, height=30)

        self.entry6 = tk.Entry(self.top, justify='center')
        self.entry6.place(x=740, y=230, width=120, height=30)

        self.entry7 = tk.Entry(self.top, justify='center')
        self.entry7.place(x=200, y=230, width=110, height=30)

        self.entry8 = tk.Entry(self.top, justify='right')
        self.entry8.place(x=50, y=230, width=110, height=30)

        # تفاصيل العقار
        self.entry9 = tk.Entry(self.top, justify='right')
        self.entry9.place(x=740, y=360, width=120, height=30)
        self.entry9.insert(0, 'tns-1900')

        self.entry10 = tk.Entry(self.top, justify='right')
        self.entry10.place(x=600, y=360, width=100, height=30)

        self.entry11 = tk.Entry(self.top, justify='center')
        self.entry11.place(x=450, y=360, width=100, height=30)

        self.entry12 = tk.Entry(self.top, justify='center')
        self.entry12.place(x=300, y=360, width=100, height=30)

        self.entry13 = tk.Entry(self.top, justify='right')
        self.entry13.place(x=150, y=360, width=100, height=30)

        self.combobox = ttk.Combobox(self.top, values=['badch', 'nobadch'])
        self.combobox.place(x=20, y=360, width=100, height=30)

        # تفاصيل العملية
        self.entry14 = tk.Entry(self.top, justify='center')
        self.entry14.place(x=740, y=500, width=120, height=30)

        self.entry15 = tk.Entry(self.top, justify='center')
        self.entry15.place(x=540, y=500, width=120, height=30)
        self.entry15.insert('0', self.date)
        # self.entry15.configure(state='disabled')

        self.entry16 = tk.Entry(self.top, justify='center')
        self.entry16.place(x=365, y=500, width=120, height=30)
        self.entry16.insert('0', self.code)
        # self.entry16.configure(state='disabled')

        self.var1 = tk.IntVar()
        self.checkb1 = tk.Checkbutton(self.top, text='بيع', variable=self.var1)
        self.checkb1.place(x=200, y=500, width=80, height=30)

        self.var2 = tk.IntVar()
        self.checkb2 = tk.Checkbutton(self.top, text='تنازل', variable=self.var2)
        self.checkb2.place(x=200, y=530, width=80, height=30)

        # buttons
        self.button1 = tk.Button(self.top, text="إلغاء")
        self.button1.place(x=200, y=600, width=150, height=60)
        self.button1.configure(command=self.top.destroy)

        self.button2 = tk.Button(self.top, text="حفظ")
        self.button2.place(x=600, y=600, width=150, height=60)
        self.button2.configure(command=lambda: self.save())

        self.conn = sqlite3.connect(os.path.join(dir, 'database.db'))
        self.cur = self.conn.cursor()

        # self.entry2.bind('<KeyRelease>', lambda: self.fill())

        self.top.mainloop()

    def cancel(self):
        pass

    def fill(self):

        if self.entry2.get():
            self.s_rows = self.cur.execute("SELECT * FROM people WHERE ni = ?", [self.entry2.get()])
            print(self.s_rows.fetchall())
            if len(self.s_rows.fetchall()) > 0:
                self.s_rows_fetched = self.s_rows.fetchall()[0]

                self.entry1.insert(0, self.s_rows_fetched[1])
                self.entry3.insert(0, self.s_rows_fetched[3])
                self.entry4.insert(0, self.s_rows_fetched[4])

        if self.entry6.get():
            self.b_rows = self.cur.execute("SELECT * FROM people WHERE ni = ?", [self.entry6.get()]).fetchall()[0]
            self.entry5.insert(0, self.b_rows[1])
            self.entry7.insert(0, self.b_rows[3])
            self.entry8.insert(0, self.b_rows[4])

        if self.entry9.get():
            self.b_rows = self.cur.execute("SELECT * FROM real_estate WHERE nbr_rec = ?", [self.entry9.get()]).fetchall()[0]
            self.entry10.insert(0, self.b_rows[1])
            self.entry11.insert(0, self.b_rows[3])
            self.entry12.insert(0, self.b_rows[4])
            self.entry13.insert(0, self.b_rows[5])

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
                                            nbr_rec = self.entry9.get()
                                            if self.entry10.get():
                                                city = self.entry10.get()
                                                if self.entry11.get():
                                                    block = self.entry11.get()
                                                    if self.entry12.get():
                                                        re_data = self.entry12.get()
                                                        if self.entry13.get():
                                                            re_number = self.entry13.get()
                                                            if self.combobox.get():
                                                                statement = self.combobox.get()
                                                                if self.entry14.get():
                                                                    amount = self.entry14.get()
                                                                    if self.entry15.get() and self.entry16.get():
                                                                        date = self.entry15.get()
                                                                        code = self.entry16.get()
                                                                        if (self.var1.get() == self.var2.get()):
                                                                            messagebox.showerror('خطأ', "قم بتحديد 'بيع' أو 'تبادل'")
                                                                        else:
                                                                            if self.var1.get():
                                                                                sale_type = 'باع'
                                                                            else:
                                                                                sale_type = 'تنازل عن'
                                                                            create_real_estate_facture(seller_name, seller_ni, seller_birthdate, seller_birthplace,
                                                                                                   buyer_name, buyer_ni, buyer_birthdate, buyer_birthplace,
                                                                                                   nbr_rec, city, block, re_data, re_number, statement, amount, date, code, sale_type)

                                                                    else:
                                                                        messagebox.showerror('خطأ', "يوجد خطأ في المدخلات")
                                                                else:
                                                                    messagebox.showerror('خطأ', "يجب إدخال المبلغ")
                                                            else:
                                                                messagebox.showerror('خطأ', "يجب إدخال نوع الإفادة")
                                                        else:
                                                            messagebox.showerror('خطأ', "يجب إدخال رقم العقار")
                                                    else:
                                                        messagebox.showerror('خطأ', "يجب إدخال تاريخ الإصدار")
                                                else:
                                                    messagebox.showerror('خطأ', "يجب إدخال القطاع")
                                            else:
                                                messagebox.showerror('خطأ', "يجب إدخال المقاطعة")
                                        else:
                                            messagebox.showerror('خطأ', "يجب إدخال رقم الوحدة السكنية")
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


class Car:
    def __init__(self):
        self.car = tk.Toplevel()
        self.car.geometry("1024x720+0+0")
        self.car.title("سيارة")
        self.car.protocol("WM_DELETE_WINDOW", lambda: exitt(self.car))

        self.now = datetime.now()
        self.date = self.now.strftime("%Y-%m-%d")
        self.code = self.now.strftime("%Y%m%d%H%M%S")

        self.label1 = tk.Label(self.car)
        self.backg = tk.PhotoImage(file=os.path.join(dir, 'design/design.003.png'))
        self.label1.configure(image=self.backg)
        self.label1.place(relx=0, rely=0)

        # اليائع
        self.entry1 = tk.Entry(self.car, justify='right')
        self.entry1.place(x=380, y=130, width=280, height=30)

        self.entry2 = tk.Entry(self.car, justify='center')
        self.entry2.place(x=740, y=130, width=120, height=30)

        self.entry3 = tk.Entry(self.car, justify='center')
        self.entry3.place(x=200, y=130, width=110, height=30)

        self.entry4 = tk.Entry(self.car, justify='right')
        self.entry4.place(x=50, y=130, width=110, height=30)

        # المشتري
        self.entry5 = tk.Entry(self.car, justify='right')
        self.entry5.place(x=380, y=230, width=280, height=30)

        self.entry6 = tk.Entry(self.car, justify='center')
        self.entry6.place(x=740, y=230, width=120, height=30)

        self.entry7 = tk.Entry(self.car, justify='center')
        self.entry7.place(x=200, y=230, width=110, height=30)

        self.entry8 = tk.Entry(self.car, justify='right')
        self.entry8.place(x=50, y=230, width=110, height=30)

        # تفاصيل السيارة
        self.entry9 = tk.Entry(self.car, justify='right')
        self.entry9.place(x=740, y=360, width=120, height=30)
        self.entry9.insert(0, '5432AK00')

        # تفاصيل العملية
        self.entry14 = tk.Entry(self.car, justify='center')
        self.entry14.place(x=740, y=500, width=120, height=30)

        self.entry15 = tk.Entry(self.car, justify='center')
        self.entry15.place(x=540, y=500, width=120, height=30)
        self.entry15.insert('0', self.date)
        # self.entry15.configure(state='disabled')

        self.entry16 = tk.Entry(self.car, justify='center')
        self.entry16.place(x=365, y=500, width=120, height=30)
        self.entry16.insert('0', self.code)
        # self.entry16.configure(state='disabled')

        # buttons
        self.button1 = tk.Button(self.car, text="إلغاء")
        self.button1.place(x=200, y=600, width=150, height=60)
        self.button1.configure(command=self.car.destroy)

        self.button2 = tk.Button(self.car, text="حفظ")
        self.button2.place(x=600, y=600, width=150, height=60)
        self.button2.configure(command=lambda: self.save())

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
                                            nbr_rec = self.entry9.get()
                                            if self.entry9.get():
                                                city = self.entry9.get()
                                                if self.entry9.get():
                                                    block = self.entry9.get()
                                                    if self.entry9.get():
                                                        re_data = self.entry9.get()
                                                        if self.entry9.get():
                                                            re_number = self.entry9.get()

                                                            if self.entry14.get():
                                                                amount = self.entry14.get()
                                                                if self.entry15.get() and self.entry16.get():
                                                                    date = self.entry15.get()
                                                                    code = self.entry16.get()

                                                                    create_real_estate_facture(seller_name, seller_ni, seller_birthdate, seller_birthplace,
                                                                                                   buyer_name, buyer_ni, buyer_birthdate, buyer_birthplace,
                                                                                                   nbr_rec, city, block, re_data, re_number, re_number, amount, date, code, code)
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
                                            messagebox.showerror('خطأ', "يجب إدخال رقم الوحدة السكنية")
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
