import tkinter as tk


root = tk.Tk()
root.title("Noter")
root.geometry("1024x720+0+0")
root.resizable(0, 0)

root.attributes('-transparent', 1)
root.config(bg='')

backg_img = tk.PhotoImage(file='images/images.001.png')
background = tk.Label(root, image=backg_img, width=1024, height=720)
background.place(relx=0, rely=0)


button1 = tk.Button(root)
button1.place(x=720, y=220, width=252, height=73)
button1.configure(relief="flat", overrelief="flat")
button1.configure(cursor="hand")
button1.configure(font="-family {Poppins SemiBold} -size 20")
button1.configure(borderwidth="0")
button1.configure(text="عملية جديدة")

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
