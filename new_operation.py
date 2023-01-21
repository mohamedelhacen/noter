import tkinter as tk


class New:

    def __init__(self):
        self.new = tk.Toplevel()
        self.new.title("عملية جديدة")
        self.new.geometry("1024x720+0+0")

        self.background_img = tk.PhotoImage(file="images/images.002.png")
        self.label1 = tk.Label(self.new)
        self.label1.configure(image=self.background_img)
        self.label1.place(relx=0, rely=0)

        self.button1 = tk.Button(self.new)
        self.button1.place(x=718, y=210, width=252, height=72)
        self.button1.configure(text="بيع عقار")
        self.button1.configure(command=BuyRealEstate)

        self.button2 = tk.Button(self.new)
        self.button2.place(x=387, y=210, width=252, height=72)
        self.button2.configure(text="بيع سيارة")

        self.button3 = tk.Button(self.new)
        self.button3.place(x=22, y=210, width=252, height=72)
        self.button3.configure(text="بيع محل تجاري")

        self.button4 = tk.Button(self.new)
        self.button4.place(x=718, y=350, width=252, height=72)
        self.button4.configure(text="تنازل عن عقار")

        self.button5 = tk.Button(self.new)
        self.button5.place(x=387, y=350, width=252, height=72)
        self.button5.configure(text="تنازل عن سيارة")

        self.button6 = tk.Button(self.new)
        self.button6.place(x=22, y=350, width=252, height=72)
        self.button6.configure(text="تنازل عن محل تجاري")


        self.new.mainloop()


class BuyRealEstate:
    def __init__(self):
        self.top = tk.Toplevel()
        self.top.geometry("1024x720+0+0")
        self.top.title("بيع عقار")

        self.label1 = tk.Label(self.top)
        self.backg = tk.PhotoImage(file="design/design.003.png")
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
        self.entry1 = tk.Entry(self.top, justify='right')
        self.entry1.place(x=550, y=280, width=240, height=40)

        self.entry2 = tk.Entry(self.top, justify='center')
        self.entry2.place(x=380, y=280, width=120, height=40)

        self.entry3 = tk.Entry(self.top, justify='center')
        self.entry3.place(x=200, y=280, width=100, height=40)

        self.entry4 = tk.Entry(self.top, justify='right')
        self.entry4.place(x=40, y=280, width=100, height=40)

        # تفاصيل العقار
        self.entry1 = tk.Entry(self.top, justify='right')
        self.entry1.place(x=650, y=400, width=120, height=40)

        self.entry2 = tk.Entry(self.top, justify='center')
        self.entry2.place(x=480, y=400, width=120, height=40)

        self.entry3 = tk.Entry(self.top, justify='center')
        self.entry3.place(x=300, y=400, width=100, height=40)

        self.entry4 = tk.Entry(self.top, justify='right')
        self.entry4.place(x=40, y=400, width=100, height=40)

        self.top.mainloop()



