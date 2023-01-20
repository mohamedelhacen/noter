import tkinter as tk


root = tk.Tk()
root.title("Noter")
root.geometry("1024x720+0+0")
root.resizable(0, 0)

backg_img = tk.PhotoImage(file='images/images.001.png')
background = tk.Label(root, image=backg_img, width=1024, height=720)
background.place(relx=0, rely=0)

butt1 = tk.Button(root)
butt1.place(x=720, y=220, width=252, height=73)
butt1.configure(relief='flat', overrelief='flat', border='0', borderwidth='0', foreground='#ffffff',
                activebackground="#D2463E")
butt1.configure(text="""New one""")


root.mainloop()
