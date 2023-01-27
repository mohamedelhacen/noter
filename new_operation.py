import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import os
import sqlite3

from utils import exitt, fill

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

        button4 = tk.Button(self.new)
        button4.place(x=358, y=527, width=252, height=73)
        button4.configure(relief="flat", overrelief="flat")
        button4.configure(cursor="hand")
        button4.configure(font="-family {Poppins SemiBold} -size 20")
        button4.configure(borderwidth=0)
        button4.configure(border=0)
        button4.configure(background='orange')
        button4.configure(text="خروج")
        button4.configure(command=lambda: exitt(top))

        self.new.mainloop()


def save_to_db(s_name, s_ni, s_birthd, s_birthp, b_name, b_ni, b_birthd, b_birthp, nbr_rec, city, block,
               re_data, re_number, amount, date, code):

    cursor.execute("""INSERT OR IGNORE INTO people(name, ni, birth_date, birth_place) VALUES (?, ?, ?, ?)""",
                   [s_name, s_ni, s_birthd, s_birthp])

    cursor.execute("""INSERT OR IGNORE INTO people(name, ni, birth_date, birth_place) VALUES (?, ?, ?, ?)""",
                   [b_name, b_ni, b_birthd, b_birthp])

    cursor.execute(f"""INSERT OR IGNORE INTO real_estate(nbr_rec, city, block, date, number) VALUES (?, ?, ?, ?, ?)""",
                   [nbr_rec, city, block, re_data, re_number])

    s_id = cursor.execute("SELECT id FROM people WHERE ni = ?", [s_ni]).fetchone()[0]
    b_id = cursor.execute("SELECT id FROM people WHERE ni = ?", [b_ni]).fetchone()[0]
    re_id = cursor.execute("SELECT id FROM real_estate WHERE nbr_rec = ?", [re_number]).fetchone()[0]

    cursor.execute("""INSERT INTO real_estate_sales(amount, date, code, seller_Id, buyer_Id, real_estate_Id) 
    VALUES (?, ?, ?, ?, ?, ?)""", [amount, date, code, s_id, b_id, re_id])

    db.commit()


def create_real_estate_facture(s_name, s_ni, s_birthd, s_birthp, b_name, b_ni, b_birthd, b_birthp, nbr_rec, city, block,
                               re_data, re_number, amount, date, code):
    facture = tk.Toplevel()
    facture.geometry("500x800+100+0")
    facture.title("الوثيقة")

    fac_img = tk.PhotoImage(file=os.path.join(dir, 'design/fac.001.png'))
    backg = tk.Label(facture, image=fac_img)
    backg.place(x=0, y=0, width=500, height=700)

    content = f""" أشهدني واستكتبني السيد(ة){s_name} المولود بتاريخ {s_birthd} في {s_birthp} رقم البطاقة الوطنية {s_ni} أنه تنازل عن قطعة أرضية في {city} القطاع {block} رقمها {re_number} عندها إفادة (batch) صادرة بتاريخ {re_data} من وكالة التنيمة الحضرية للسيد(ة) {b_name} المولود بتاريخ {b_birthd} في {b_birthp} رقم البطاقة الوطنية {b_ni} مقابل مبلغ قدره {amount} استلم البائع المبلغ ولم تبقى بينهم أي مطالبة
     """
    # canvas = tk.Frame(facture, border=1)
    # canvas.place(x=0, y=180, width=500, height=600, bordermode='outside')

    dt = tk.Label(facture, text=code, font=('Helvetica', 16), justify='center')
    dt.place(x=180, y=100, width=120, height=25)
    cd = tk.Label(facture, text=date, font=('Helvetica', 16), justify='right')
    cd.place(x=180, y=130, width=120, height=25)

    # doc = tk.Label(canvas, text=text, font=('Helvetica', 18), wraplength=480, justify='right')
    # doc.place(x=0, y=120, width=500, height=400)

    text = tk.Text(facture, font=('Helvetica', 18), spacing1=5, spacing2=20, spacing3=5, borderwidth='0')
    text.tag_configure("right", justify='right')
    text.insert('end', content)
    text.tag_add('right', 1.0, 'end')
    text.configure(state='disabled', wrap='word', blockcursor=False)
    text.place(x=0, y=200, width=500, height=300)

    butt1 = tk.Button(facture, text="طباعة و حفظ")
    butt1.place(x=300, y=750, width=100, height=25)
    butt1.configure(command=lambda: save_and_print(s_name, s_ni, s_birthd, s_birthp, b_name, b_ni, b_birthd, b_birthp,
                                                   nbr_rec, city, block, re_data, re_number, amount, date, code))

    butt2 = tk.Button(facture, text="تعديل أو إلغاء")
    butt2.place(x=100, y=750, width=100, height=25)

    facture.mainloop()


def print_document():
    print('printed')


def save_and_print(s_name, s_ni, s_birthd, s_birthp, b_name, b_ni, b_birthd, b_birthp, nbr_rec, city, block,
                   re_data, re_number, amount, date, code):
    save_to_db(s_name, s_ni, s_birthd, s_birthp, b_name, b_ni, b_birthd, b_birthp, nbr_rec, city, block,
               re_data, re_number, amount, date, code)
    print_document()


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

        self.entry2 = tk.Entry(self.top, justify='center')
        self.entry2.place(x=380, y=160, width=120, height=40)

        self.entry3 = tk.Entry(self.top, justify='center')
        self.entry3.place(x=200, y=160, width=100, height=40)

        self.entry4 = tk.Entry(self.top, justify='right')
        self.entry4.place(x=40, y=160, width=100, height=40)

        # المشتري
        self.entry5 = tk.Entry(self.top, justify='right')
        self.entry5.place(x=550, y=282, width=240, height=40)

        self.entry6 = tk.Entry(self.top, justify='center')
        self.entry6.place(x=380, y=282, width=120, height=40)

        self.entry7 = tk.Entry(self.top, justify='center')
        self.entry7.place(x=200, y=282, width=100, height=40)

        self.entry8 = tk.Entry(self.top, justify='right')
        self.entry8.place(x=40, y=282, width=100, height=40)

        # تفاصيل العقار
        self.entry9 = tk.Entry(self.top, justify='right')
        self.entry9.place(x=680, y=415, width=120, height=40)

        self.entry10 = tk.Entry(self.top, justify='right')
        self.entry10.place(x=680, y=415, width=120, height=40)

        self.entry11 = tk.Entry(self.top, justify='center')
        self.entry11.place(x=480, y=415, width=120, height=40)

        self.entry12 = tk.Entry(self.top, justify='center')
        self.entry12.place(x=280, y=415, width=120, height=40)

        self.entry13 = tk.Entry(self.top, justify='right')
        self.entry13.place(x=80, y=415, width=120, height=40)
        # self.entry13.insert(0, '750')

        # تفاصيل العملية
        self.entry14 = tk.Entry(self.top, justify='center')
        self.entry14.place(x=680, y=550, width=120, height=40)
        # self.entry14.insert(0, '40000')

        self.entry15 = tk.Entry(self.top, justify='center')
        self.entry15.place(x=480, y=550, width=120, height=40)
        self.entry15.insert('0', self.date)
        self.entry15.configure(state='disabled')

        self.entry16 = tk.Entry(self.top, justify='center')
        self.entry16.place(x=280, y=550, width=120, height=40)
        self.entry16.insert('0', self.code)
        self.entry16.configure(state='disabled')

        # buttons
        self.button1 = tk.Button(self.top, text="إلغاء")
        self.button1.place(x=727, y=645, width=180, height=65)

        self.button2 = tk.Button(self.top, text="حفظ")
        self.button2.place(x=396, y=645, width=180, height=65)
        self.button2.configure(command=lambda: self.save())

        self.button3 = tk.Button(self.top, text="العودة")
        self.button3.place(x=80, y=645, width=180, height=65)
        self.button3.configure(command=lambda: self.fill())

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
                                                            if self.entry14.get():
                                                                amount = self.entry14.get()
                                                                if self.entry15.get() and self.entry16.get():
                                                                    date = self.entry15.get()
                                                                    code = self.entry16.get()

                                                                    create_real_estate_facture(seller_name, seller_ni, seller_birthdate, seller_birthplace,
                                                                                               buyer_name, buyer_ni, buyer_birthdate, buyer_birthplace,
                                                                                               nbr_rec, city, block, re_data, re_number, amount, date, code)

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

    def back(self):
        pass




