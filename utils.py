from tkinter import messagebox
# import _winapi as win
# from os import waitpid
# from sys import exc_info as ei
from PIL import ImageGrab


def exitt(parent):
    sure = messagebox.askyesno("الخروج", "هل أنت متأكد من أنك تريد إغلاق البرنامج", parent=parent)
    if sure:
        parent.destroy()


def fill(**kwargs):
    for elements in kwargs:
        elements[0].insert(0, elements[1])


# def print_doc(exe, wait=False):
#     try:
#         ph, th, pid, tid = win.CreateProcess(exe, None, None, None, 1, 0, None, None, None)
#         win.CloseHandle(th)
#     except:
#         print(ei()[1])
#         ph = 0
#         return (ph,'error')


def take_screenshot(width, height, pt1, pt2):
    image = ImageGrab.grab(bbox=(pt1, pt2, width, height))
    image.save('screenshot.png')
    image.show()


def capture(can):
    x0 = can.winfo_rootx()
    y0 = can.winfo_rooty()
    x1 = x0 + can.winfo_width()
    y1 = y0 + can.winfo_height()

    im = ImageGrab.grab((x0, y0, x1, y1))
    im.show()

