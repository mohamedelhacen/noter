import sqlite3
import tkinter as tk
from tkinter import font, ttk
import os

from new_operation import New
from utils import exitt
from search import Search

dir = os.path.abspath(os.path.dirname(__file__))

conn = sqlite3.connect(os.path.join(dir, 'database.db'))
cur = conn.cursor()

# real_estate_sales
cur.execute("""CREATE TABLE IF NOT EXISTS real_estate_sales (
            id INTEGER PRIMARY KEY,
            amount REAL NOT NULL,
            date DATE NOT NULL,
            code INTEGER NOT NULL,
            sale_type VARCHAR(50) NOT NULL,
            seller_Id INTEGER NOT NULL,
            buyer_Id INTEGER NOT NULL,
            real_estate_Id INTEGER NOT NULL,
            FOREIGN KEY (seller_Id) REFERENCES people (id),
            FOREIGN KEY (buyer_Id) REFERENCES people (id),
            FOREIGN KEY (real_estate_Id) REFERENCES real_estate(id)
            )
""")
# cur.execute("""ALTER TABLE real_estate_sales ADD COLUMN sale_type VARCHAR(50)""")
# cur.execute("""UPDATE real_estate_sales SET sale_type='بيع'""")

# real_estate
cur.execute("""CREATE TABLE IF NOT EXISTS real_estate (
            id INTEGER PRIMARY KEY,
            nbr_rec VARCHAR(50) NOT NULL UNIQUE,
            city VARCHAR(50) NOT NULL,
            block VARCHAR(50) NOT NULL,
            date DATE NOT NULL,
            number VARCHAR(50) NOT NULL,
            statement VARCHAR(50) NOT NULL
            )
""")
# cur.execute("""ALTER TABLE real_estate ADD COLUMN statement VARCHAR(50) NOT NULL DEFAULT 'badch'""")
# cur.execute("""UPDATE real_estate SET statement='badch'""")

# people
cur.execute("""CREATE TABLE IF NOT EXISTS people (
            id INTEGER PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            ni INTEGER NOT NULL UNIQUE,
            birth_date DATE NOT NULL,
            birth_place VARCHAR(50) NOT NULL
            )
""")

conn.commit()


root = tk.Tk()
root.title("Noter")
root.geometry("1024x720+0+0")
root.resizable(0, 0)
root.protocol("WM_DELETE_WINDOW", lambda: exitt(root))

# defaultFont = font.nametofont("TkDefaultFont")
# defaultFont.configure(family="Segoe Script",
#                       size=19,
#                       weight=font.BOLD)
#
# style = ttk.Style()
# style.configure('root.Button', font=('TkFixedFont', 16))
#
# print(font.nametofont("TkFixedFont").actual())
# print(font.nametofont('TkDefaultFont').actual())

# root.option_add("*Button.Font", "Tahoma 9 normal roman underline")

backg_img = tk.PhotoImage(file=os.path.join(dir, 'design/design.001.png'))
background = tk.Label(root, image=backg_img, width=1024, height=720)
background.place(relx=0, rely=0)

button1 = tk.Button(root)
button1.place(x=600, y=150, width=200, height=80)
button1.configure(relief="flat", overrelief="flat")
button1.configure(font=("Helvetica, 30"))
button1.configure(background='orange')
button1.configure(text="عملية جديدة")
button1.configure(command=lambda: New(root))
button1.config(highlightthickness=0, borderwidth=0)

# button2 = tk.Button(root)
# button2.place(x=400, y=150, width=200, height=80)
# button2.configure(relief="flat", overrelief="flat")
# button2.configure(font=("Helvetica, 30"))
# button2.configure(borderwidth=0)
# button2.configure(border=0)
# button2.configure(background='orange')
# button2.configure(text="السجل")

button3 = tk.Button(root)
button3.place(x=300, y=150, width=200, height=80)
button3.configure(relief="flat", overrelief="flat")
button3.configure(font=("Helvetica, 30"))
button3.configure(borderwidth=0)
button3.configure(border=0)
button3.configure(background='orange')
button3.configure(text="بحث")
button3.configure(command=Search)
button3.config(highlightthickness=0, borderwidth=0)

button4 = tk.Button(root)
button4.place(x=450, y=450, width=200, height=60)
button4.configure(relief="flat", overrelief="flat")
button4.configure(font=("Helvetica, 30"))
button4.configure(borderwidth=0)
button4.configure(border=0)
button4.configure(background='orange')
button4.configure(text="إغلاق البرنامج")
button4.configure(command=lambda: exitt(root))
button4.config(highlightthickness=0, borderwidth=0)



root.mainloop()

