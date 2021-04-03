#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.4
#  in conjunction with Tcl version 8.6
#    Mar 28, 2021 05:38:26 PM IST  platform: Windows NT

import sys
import sys
import view_class
import view_subject
import add_student
import view_student
import add_subject
import login
import add_class
import change_password
import model
import AttendancePro
from tkinter import messagebox
import re

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

import main_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    main_support.set_Tk_var()
    top = mainTop (root)
    main_support.init(root, top)
    root.mainloop()

w = None
def create_mainTop(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_mainTop(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    main_support.set_Tk_var()
    top = mainTop (w)
    main_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_mainTop():
    global w
    w.destroy()
    w = None

class mainTop:
    def navStudent(self):
        add_student.vp_start_gui()

    def navViewStudent(self):
        view_student.vp_start_gui()

    def navSubject(self):
        add_subject.vp_start_gui()

    def navViewSubject(self):
        view_subject.vp_start_gui()

    def navClass(self):
        add_class.vp_start_gui()

    def navViewClass(self):
        view_class.vp_start_gui()

    def navChPass(self):
        change_password.vp_start_gui()

    def logoutUser(self):
        root.destroy()
        login.vp_start_gui()

    def onRefresh(self):
        self.scrollClass.delete(0, self.scrollClass.size_())
        v = ["Select Class"]
        self.vl = model.readAllClass(v)
        for i in range(0, len(self.vl)):
            self.scrollClass.insert(i, self.vl[i])

    def onselect(self, evt):
        self.scrollSubject.delete(1, self.scrollSubject.size_())
        del self.value_list[1:]
        selected = self.scrollClass.curselection()
        selectClass = self.scrollClass.get(selected)
        self.vl = model.readSubject(selectClass, self.value_list)
        for i in range(1, len(self.vl)):
            self.scrollSubject.insert(i, self.vl[i])

    def markAttend(self):
        c = self.scrollClass.curselection()
        s = self.scrollSubject.curselection()
        teacher = self.txtTeacher.get()
        lec = self.txtLec.get()
        t = self.comboLecType.get()
        p = re.compile('[0-2][0-9][:][0-5][0-9]-[0-2][0-9][:][0-5][0-9]$')  # checks for pattern eg 12:00-13:00

        if lec != "" and p.match(lec):  # if you enter more than 23:59 time like 24:00 or 29:00 the 24 or 29 will be automatically be replaced by 00
            s1 = lec.split("-")[0]
            sh1 = s1.split(":")[0]
            sm1 = s1.split(":")[1]

            s2 = lec.split("-")[1]
            sh2 = s2.split(":")[0]
            sm2 = s2.split(":")[1]

            if s1.startswith('2') and int(s1[1]) > 3:
                x = s1.replace(sh1, "00")
                xm = x.replace(sm1, "00")
                lec = xm + "-" + s2
            if s2.startswith('2') and int(s2[1]) > 3:
                x = s2.replace(sh2, "00")
                xm = x.replace(sm2, "00")
                lec = s1 + "-" + xm
            if s1.startswith('2') and int(s1[1]) > 3 and s2.startswith('2') and int(s2[1]) > 3:
                x = s1.replace(sh1, "00")
                xm = x.replace(sm1, "00")
                y = s2.replace(sh2, "00")
                ym = y.replace(sm2, "00")
                lec = xm + "-" + ym

            if c != () and s != ():
                selectClass = self.scrollClass.get(c)
                selectSubject = self.scrollSubject.get(s)
                if selectClass != "Select Class" and selectSubject != "Select Subject" and teacher != "" and lec != "" and t != "Select Type":
                    rl = model.readlframes(selectClass)
                    b = False

                    s1 = lec.split("-")[0]
                    h1 = s1.split(":")[0]
                    m1 = s1.split(":")[1]

                    ss = lec.split("-")[1]
                    hs = ss.split(":")[0]
                    ms = ss.split(":")[1]

                    if rl != [] and int(h1) < int(hs) or (int(h1) == int(hs) and int(m1) < int(ms)):
                        for row in rl:
                            s2s = row.split("-")[0]
                            h2s = s2s.split(":")[0]
                            m2s = s2s.split(":")[1]

                            s2 = row.split("-")[1]
                            h2 = s2.split(":")[0]
                            m2 = s2.split(":")[1]

                            if int(h1) < int(h2) and int(h1) >= int(h2s):
                                print("First if")
                                b = True
                                break
                            elif int(h1) == int(h2) and int(m1) < int(m2):
                                print("Second If")
                                b = True
                                break
                            elif int(h1) == int(hs) and int(m1) == int(ms):
                                print("Third If")
                                b = True
                                break
                            elif int(h1) < int(h2) and int(hs) >= int(h2s):
                                print("Fourth if")
                                b = True
                                break

                    if b == False and int(h1) < int(hs) or (int(h1) == int(hs) and int(m1) < int(ms)):
                        a = AttendancePro.Attend(selectClass, selectSubject, teacher, lec, t)
                        if a == False:
                            messagebox.showinfo("Attendance", "No students in this class! Please add some students.", master=root)
                    else:
                        messagebox.showwarning("Attendance", "Lecture Frame should match pattern like 08:00-13:00, 24 hour format, it should not exist in other time frame, start time and end time should not be same, and also start time should be less than end time", master=root)
                else:
                    messagebox.showwarning("Attendance", "Class, Subject, teacher name, lecture frame and lecture type feilds are required! Note: If subject(s) are not available for the selected class please do add subjects.", master=root)
            else:
                messagebox.showwarning("Attendance", "Class field and Subject field is required! Note: If subject(s) are not available for the selected class please do add subjects.", master=root)
        else:
            messagebox.showwarning("Attendance", "Lecture Frame should match pattern like 08:00-13:00, 24 hour format, it should not exist in other time frame, start time and end time should not be same, and also start time should be less than end time", master=root)

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font9 = "-family {Segoe UI Black} -size 9 -weight bold"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("765x512+650+150")
        top.minsize(148, 1)
        top.maxsize(1924, 1030)
        top.resizable(1, 1)
        top.title("Attendance")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=1.006, relwidth=1.0)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#00ffff")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.scrollClass = ScrolledListBox(self.Frame1)
        self.scrollClass.configure(exportselection=False)
        self.scrollClass.place(relx=0.026, rely=0.068, relheight=0.408
                , relwidth=0.319)
        self.scrollClass.configure(background="white")
        self.scrollClass.configure(cursor="xterm")
        self.scrollClass.configure(disabledforeground="#a3a3a3")
        self.scrollClass.configure(font="-family {Yu Gothic UI Semibold} -size 12 -weight bold")
        self.scrollClass.configure(foreground="black")
        self.scrollClass.configure(highlightbackground="#d9d9d9")
        self.scrollClass.configure(highlightcolor="#d9d9d9")
        self.scrollClass.configure(selectbackground="blue")
        self.scrollClass.configure(selectforeground="white")
        self.vlist = ["Select Class"]
        self.vl = model.readAllClass(self.vlist)
        for i in range(len(self.vl)):
            self.scrollClass.insert(i, self.vl[i])
        self.scrollClass.bind('<<ListboxSelect>>', self.onselect)

        self.scrollSubject = ScrolledListBox(self.Frame1)
        self.scrollSubject.configure(exportselection=False)
        self.scrollSubject.place(relx=0.026, rely=0.509, relheight=0.406
                , relwidth=0.319)
        self.scrollSubject.configure(background="white")
        self.scrollSubject.configure(cursor="xterm")
        self.scrollSubject.configure(disabledforeground="#a3a3a3")
        self.scrollSubject.configure(font="-family {Yu Gothic UI Semibold} -size 12 -weight bold")
        self.scrollSubject.configure(foreground="black")
        self.scrollSubject.configure(highlightbackground="#d9d9d9")
        self.scrollSubject.configure(highlightcolor="#d9d9d9")
        self.scrollSubject.configure(selectbackground="blue")
        self.scrollSubject.configure(selectforeground="white")
        self.value_list = ["Select Subject"]
        self.scrollSubject.insert(0, self.value_list[0])

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.405, rely=0.167, height=31, width=152)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#00ffff")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Yu Gothic UI Semibold} -size 13 -weight bold -slant roman -underline 0 -overstrike 0")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Lecture Frame''')

        self.txtLec = tk.Entry(self.Frame1)
        self.txtLec.place(relx=0.641, rely=0.167,height=34, relwidth=0.319)
        self.txtLec.configure(background="white")
        self.txtLec.configure(borderwidth="2")
        self.txtLec.configure(disabledforeground="#a3a3a3")
        self.txtLec.configure(font="-family {Yu Gothic UI Semibold} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
        self.txtLec.configure(foreground="#000000")
        self.txtLec.configure(highlightbackground="#d9d9d9")
        self.txtLec.configure(highlightcolor="black")
        self.txtLec.configure(insertbackground="black")
        self.txtLec.configure(selectbackground="blue")
        self.txtLec.configure(selectforeground="white")

        self.Label1_3 = tk.Label(self.Frame1)
        self.Label1_3.place(relx=0.405, rely=0.315, height=32, width=152)
        self.Label1_3.configure(activebackground="#f9f9f9")
        self.Label1_3.configure(activeforeground="black")
        self.Label1_3.configure(background="#00ffff")
        self.Label1_3.configure(disabledforeground="#a3a3a3")
        self.Label1_3.configure(font="-family {Yu Gothic UI Semibold} -size 13 -weight bold -slant roman -underline 0 -overstrike 0")
        self.Label1_3.configure(foreground="#000000")
        self.Label1_3.configure(highlightbackground="#d9d9d9")
        self.Label1_3.configure(highlightcolor="black")
        self.Label1_3.configure(text='''Teacher Name''')

        self.txtTeacher = tk.Entry(self.Frame1)
        self.txtTeacher.place(relx=0.641, rely=0.315,height=34, relwidth=0.319)
        self.txtTeacher.configure(background="white")
        self.txtTeacher.configure(borderwidth="2")
        self.txtTeacher.configure(disabledforeground="#a3a3a3")
        self.txtTeacher.configure(font="-family {Yu Gothic UI Semibold} -size 11 -weight bold -slant roman -underline 0 -overstrike 0")
        self.txtTeacher.configure(foreground="#000000")
        self.txtTeacher.configure(highlightbackground="#d9d9d9")
        self.txtTeacher.configure(highlightcolor="black")
        self.txtTeacher.configure(insertbackground="black")
        self.txtTeacher.configure(selectbackground="blue")
        self.txtTeacher.configure(selectforeground="white")

        self.btnAttend = tk.Button(self.Frame1)
        self.btnAttend.place(relx=0.523, rely=0.592, height=123, width=236)
        self.btnAttend.configure(activebackground="#ececec")
        self.btnAttend.configure(activeforeground="#000000")
        self.btnAttend.configure(background="#eac515")
        self.btnAttend.configure(borderwidth="3")
        self.btnAttend.configure(disabledforeground="#a3a3a3")
        self.btnAttend.configure(font="-family {Segoe UI Black} -size 13 -weight bold -slant roman -underline 0 -overstrike 0")
        self.btnAttend.configure(foreground="#000000")
        self.btnAttend.configure(highlightbackground="#d9d9d9")
        self.btnAttend.configure(highlightcolor="black")
        self.btnAttend.configure(pady="0")
        self.btnAttend.configure(text='''Mark Attendance''')
        self.btnAttend.configure(command=self.markAttend)

        self.Label1_4 = tk.Label(self.Frame1)
        self.Label1_4.place(relx=0.405, rely=0.462, height=32, width=153)
        self.Label1_4.configure(activebackground="#f9f9f9")
        self.Label1_4.configure(activeforeground="black")
        self.Label1_4.configure(background="#00ffff")
        self.Label1_4.configure(disabledforeground="#a3a3a3")
        self.Label1_4.configure(font="-family {Yu Gothic UI Semibold} -size 13 -weight bold -slant roman -underline 0 -overstrike 0")
        self.Label1_4.configure(foreground="#000000")
        self.Label1_4.configure(highlightbackground="#d9d9d9")
        self.Label1_4.configure(highlightcolor="black")
        self.Label1_4.configure(text='''Lecture Type''')

        self.comboLecType = ttk.Combobox(self.Frame1)
        self.comboLecType.place(relx=0.641, rely=0.462, relheight=0.068
                , relwidth=0.323)
        self.value_list = ['Select Type','Lecture','Practical','Workshop/Seminar',]
        self.comboLecType.configure(values=self.value_list)
        self.comboLecType.configure(state='readonly')
        self.comboLecType.configure(font="-family {Yu Gothic UI Semibold} -size 12 -weight bold -slant roman -underline 0 -overstrike 0")
        self.comboLecType.configure(textvariable=main_support.combobox)
        self.comboLecType.configure(takefocus="")
        self.comboLecType.current(0)

        self.btnRefresh = tk.Button(self.Frame1)
        self.btnRefresh.place(relx=0.261, rely=0.019, height=23, width=66)
        self.btnRefresh.configure(activebackground="#ececec")
        self.btnRefresh.configure(activeforeground="#000000")
        self.btnRefresh.configure(background="#eac515")
        self.btnRefresh.configure(borderwidth="3")
        self.btnRefresh.configure(disabledforeground="#a3a3a3")
        self.btnRefresh.configure(font=font9)
        self.btnRefresh.configure(foreground="#000000")
        self.btnRefresh.configure(highlightbackground="#d9d9d9")
        self.btnRefresh.configure(highlightcolor="black")
        self.btnRefresh.configure(pady="0")
        self.btnRefresh.configure(text='''Refresh''')
        self.btnRefresh.configure(command=self.onRefresh)

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.sub_menu = tk.Menu(top,
                activebackground="#ececec",
                activeborderwidth=1,
                activeforeground="#000000",
                background="#d9d9d9",
                borderwidth=1,
                disabledforeground="#a3a3a3",
                foreground="#000000",
                tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu,
                                 label="View")
        self.sub_menu.add_command(
            label="Student", command=self.navViewStudent)
        self.sub_menu.add_command(
            label="Subject", command=self.navViewSubject)
        self.sub_menu.add_command(
            label="Class", command=self.navViewClass)
        self.sub_menu1 = tk.Menu(top,
                activebackground="#ececec",
                activeborderwidth=1,
                activeforeground="#000000",
                background="#d9d9d9",
                borderwidth=1,
                disabledforeground="#a3a3a3",
                foreground="#000000",
                tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu1,
                label="Add")
        self.sub_menu1.add_command(
            label="Student", command=self.navStudent)
        self.sub_menu1.add_command(
            label="Subject", command=self.navSubject)
        self.sub_menu1.add_command(
            label="Class", command=self.navClass)
        self.menubar.add_command(
            label="Reports")
        self.menubar.add_command(
            label="Change Password", command=self.navChPass)
        self.menubar.add_command(
            label="Logout", command=self.logoutUser)

# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''
    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                  + tk.Place.__dict__.keys()
        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledListBox(AutoScroll, tk.Listbox):
    '''A standard Tkinter Listbox widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        tk.Listbox.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)
    def size_(self):
        sz = tk.Listbox.size(self)
        return sz

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')

if __name__ == '__main__':
    vp_start_gui()





