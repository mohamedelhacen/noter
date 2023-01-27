from tkinter import messagebox


def exitt(parent):
    sure = messagebox.askyesno("Exit", "Are you sure you want to exit?", parent=parent)
    if sure:
        parent.destroy()


def fill(**kwargs):
    for elements in kwargs:
        elements[0].insert(0, elements[1])
