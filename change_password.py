#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.4
#  in conjunction with Tcl version 8.6
#    Aug 07, 2020 10:32:03 PM IST  platform: Windows NT

import sys
from tkinter import messagebox
from model import changePassword
import login
import main

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

import change_password_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    change_password_support.init(root, top)
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
    change_password_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def chPassword(self):
        old_pass = self.txtOld.get()
        new_pass = self.txtNew.get()

        rch = changePassword(old_pass, new_pass)

        if rch != False:
            msg = messagebox.showinfo("Attendance - Change Password", "Password Updated Successfully!", master=root)
            if msg:
                root.destroy()
        else:
            messagebox.showwarning("Attendance - Change Password", "Cannot Update - Invalid Password!", master=root)

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family {Segoe UI Emoji} -size 12 -weight bold"
        font11 = "-family {Yu Gothic UI Semibold} -size 12 -weight "  \
            "bold"
        font9 = "-family {Yu Gothic UI Semibold} -size 13 -weight bold"  \
            ""

        top.geometry("629x466+650+150")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1, 1)
        top.title("Attendance - Change Password")
        top.configure(background="#d9d9d9")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=1.011, relwidth=1.008)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#00ffff")

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.11, rely=0.191, height=48, width=159)
        self.Label1.configure(background="#00ffff")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Old Password''')

        self.txtOld = tk.Entry(self.Frame1)
        self.txtOld.place(relx=0.41, rely=0.191,height=44, relwidth=0.495)
        self.txtOld.configure(background="white")
        self.txtOld.configure(borderwidth="2")
        self.txtOld.configure(disabledforeground="#a3a3a3")
        self.txtOld.configure(font=font11)
        self.txtOld.configure(foreground="#000000")
        self.txtOld.configure(insertbackground="black")
        self.txtOld.configure(show="*")

        self.Label1_1 = tk.Label(self.Frame1)
        self.Label1_1.place(relx=0.11, rely=0.382, height=48, width=159)
        self.Label1_1.configure(activebackground="#f9f9f9")
        self.Label1_1.configure(activeforeground="black")
        self.Label1_1.configure(background="#00ffff")
        self.Label1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1.configure(font="-family {Yu Gothic UI Semibold} -size 13 -weight bold -slant roman -underline 0 -overstrike 0")
        self.Label1_1.configure(foreground="#000000")
        self.Label1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1.configure(highlightcolor="black")
        self.Label1_1.configure(text='''New Password''')

        self.txtNew = tk.Entry(self.Frame1)
        self.txtNew.place(relx=0.41, rely=0.382,height=44, relwidth=0.495)
        self.txtNew.configure(background="white")
        self.txtNew.configure(borderwidth="2")
        self.txtNew.configure(disabledforeground="#a3a3a3")
        self.txtNew.configure(font=font11)
        self.txtNew.configure(foreground="#000000")
        self.txtNew.configure(highlightbackground="#d9d9d9")
        self.txtNew.configure(highlightcolor="black")
        self.txtNew.configure(insertbackground="black")
        self.txtNew.configure(selectbackground="blue")
        self.txtNew.configure(selectforeground="white")
        self.txtNew.configure(show="*")

        self.btnChange = tk.Button(self.Frame1)
        self.btnChange.place(relx=0.41, rely=0.552, height=63, width=316)
        self.btnChange.configure(activebackground="#ececec")
        self.btnChange.configure(activeforeground="#000000")
        self.btnChange.configure(background="#eac515")
        self.btnChange.configure(borderwidth="3")
        self.btnChange.configure(disabledforeground="#a3a3a3")
        self.btnChange.configure(font=font10)
        self.btnChange.configure(foreground="#000000")
        self.btnChange.configure(highlightbackground="#d9d9d9")
        self.btnChange.configure(highlightcolor="black")
        self.btnChange.configure(pady="0")
        self.btnChange.configure(text='''Change''')
        self.btnChange.configure(command=self.chPassword)
if __name__ == '__main__':
    vp_start_gui()





