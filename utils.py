from tkinter import messagebox


def exitt(parent):
    sure = messagebox.askyesno("Exit", "Are you sure you want to exit?", parent=parent)
    if sure:
        parent.destroy()
