import sqlite3
import tkinter as tk
import os
from new_operation import New
from utils import exitt

dir = os.path.abspath(os.path.dirname(__file__))

conn = sqlite3.connect(os.path.join(dir, 'database.db'))
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS real_estate_sales (
            id INTEGER PRIMARY KEY,
            amount REAL NOT NULL,
            date DATE NOT NULL,
            code INTEGER NOT NULL,
            seller_Id INTEGER NOT NULL,
            buyer_Id INTEGER NOT NULL,
            real_estate_Id INTEGER NOT NULL,
            FOREIGN KEY (seller_Id) REFERENCES people (id),
            FOREIGN KEY (buyer_Id) REFERENCES people (id),
            FOREIGN KEY (real_estate_Id) REFERENCES real_estate(id)
            )
""")

cur.execute("""CREATE TABLE IF NOT EXISTS real_estate (
            id INTEGER PRIMARY KEY,
            city VARCHAR(50) NOT NULL,
            block VARCHAR(50) NOT NULL,
            date DATE NOT NULL,
            number VARCHAR(50) NOT NULL
            )
""")

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

backg_img = tk.PhotoImage(file=os.path.join(dir, 'design/design.001.png'))
background = tk.Label(root, image=backg_img, width=1024, height=720)
background.place(relx=0, rely=0)

button1 = tk.Button(root)
button1.place(x=720, y=220, width=252, height=73)
button1.configure(relief="flat", overrelief="flat")
button1.configure(cursor="hand")
button1.configure(font="-family {Poppins SemiBold} -size 20")
button1.configure(borderwidth="0")
button1.configure(text="عملية جديدة")
button1.configure(command=New)

button2 = tk.Button(root)
button2.place(x=389, y=220, width=252, height=73)
button2.configure(relief="flat", overrelief="flat")
button2.configure(cursor="hand")
button2.configure(font="-family {Poppins SemiBold} -size 20")
button2.configure(borderwidth="0")
button2.configure(text="السجل")

button3 = tk.Button(root)
button3.place(x=67, y=220, width=252, height=73)
button3.configure(relief="flat", overrelief="flat")
button3.configure(cursor="hand")
button3.configure(font="-family {Poppins SemiBold} -size 20")
button3.configure(borderwidth=0)
button3.configure(border=0)
button3.configure(background='orange')
button3.configure(text="بحث")

root.mainloop()

