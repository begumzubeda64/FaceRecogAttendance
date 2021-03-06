#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.4
#  in conjunction with Tcl version 8.6
#    Mar 30, 2021 01:24:29 PM IST  platform: Windows NT

import sys
from tkinter import messagebox
import model

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import edit_class_support
import view_class_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    edit_class_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    edit_class_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def editClass(self):
        name = self.txtClass.get().upper()
        pname = view_class_support.val.get()
        if name != "":
            iclass = model.updateClass(pname, name)
            if iclass:
                messagebox.showinfo("Attendance - Edit Class", "Class updated succesfully!", master=root)
                root.destroy()
            else:
                messagebox.showwarning("Attendance - Edit Class", "Failed to add class or class already exists!", master=root)
        else:
            messagebox.showwarning("Attendance - Edit Class", "Class Name field is required!", master=root)

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family {Yu Gothic UI Semibold} -size 12 -weight "  \
            "bold"
        font11 = "-family {Segoe UI Emoji} -size 12 -weight bold"
        font9 = "-family {Yu Gothic UI Semibold} -size 13 -weight bold"  \
            ""

        top.geometry("650x450+650+150")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1, 1)
        top.title("Attendance - Edit Class")
        top.configure(background="#d9d9d9")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=1.011, relwidth=1.008)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#00ffff")

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.082, rely=0.264, height=46, width=152)
        self.Label1.configure(background="#00ffff")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Class Name''')

        self.txtClass = tk.Entry(self.Frame1)
        self.txtClass.place(relx=0.38, rely=0.264,height=44, relwidth=0.502)
        self.txtClass.configure(background="white")
        self.txtClass.configure(borderwidth="2")
        self.txtClass.configure(disabledforeground="#a3a3a3")
        self.txtClass.configure(font=font10)
        self.txtClass.configure(foreground="#000000")
        self.txtClass.configure(insertbackground="black")
        self.txtClass.insert(0, view_class_support.val.get())

        self.btnEditClass = tk.Button(self.Frame1)
        self.btnEditClass.place(relx=0.38, rely=0.505, height=53, width=306)
        self.btnEditClass.configure(activebackground="#ececec")
        self.btnEditClass.configure(activeforeground="#000000")
        self.btnEditClass.configure(background="#eac515")
        self.btnEditClass.configure(borderwidth="3")
        self.btnEditClass.configure(disabledforeground="#a3a3a3")
        self.btnEditClass.configure(font=font11)
        self.btnEditClass.configure(foreground="#000000")
        self.btnEditClass.configure(highlightbackground="#d9d9d9")
        self.btnEditClass.configure(highlightcolor="black")
        self.btnEditClass.configure(pady="0")
        self.btnEditClass.configure(text='''Save''')
        self.btnEditClass.configure(command=self.editClass)

if __name__ == '__main__':
    vp_start_gui()





