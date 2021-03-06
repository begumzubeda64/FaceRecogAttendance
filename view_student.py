#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.4
#  in conjunction with Tcl version 8.6
#    Mar 24, 2021 06:36:53 PM IST  platform: Windows NT

import sys
import model
from tkinter import messagebox
import edit_student

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

import view_student_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    view_student_support.init(root, top)
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
    view_student_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def delStudent(self):
        cls = self.scrollClass.curselection()
        roll = self.scrollStudent.curselection()

        if cls != () and roll != ():
            selectedCls = self.scrollClass.get(cls)
            selectedRoll = self.scrollStudent.get(roll).split(" ")[0]
            if selectedCls != "Select Class" and selectedRoll != "RollNo":
                result = model.deleteStudent(selectedRoll, selectedCls)
                if result == True:
                    messagebox.showinfo("Attendance - Students", "Successfully Deleted a student.", master=root)
                    self.scrollStudent.delete(roll)
                    self.value_list.pop(roll[0])
                else:
                    messagebox.showwarning("Attendance - Students", "Error Deleting Student!.", master=root)
            else:
                messagebox.showwarning("Attendance - Students", "Please select a class and a student!", master=root)
        else:
            messagebox.showwarning("Attendance - Students", "Please select a class and a student!", master=root)

    def editStudent(self):
        cls = self.scrollClass.curselection()
        st = self.scrollStudent.curselection()

        if cls != () and st != ():
            selectedCls = self.scrollClass.get(cls)
            selectedRoll = self.scrollStudent.get(st).split(" ")[0]
            if selectedCls != "Select Class" and selectedRoll != "RollNo":
                selectedName = self.scrollStudent.get(st).split("{:<30s}".format(selectedRoll))[1]
                view_student_support.set_Tk_var()
                view_student_support.cval.set(selectedCls)
                view_student_support.rval.set(selectedRoll)
                view_student_support.nval.set(selectedName.strip())
                edit_student.vp_start_gui()
            else:
                messagebox.showwarning("Attendance - Students", "Please select a class and a student!", master=root)
        else:
            messagebox.showwarning("Attendance - Students", "Please select a class and a student!", master=root)

    def onselect(self, evt):
        self.scrollStudent.delete(1, len(self.value_list))
        del self.value_list[1:]
        selected = self.scrollClass.curselection()
        selectClass = self.scrollClass.get(selected)
        self.vl = model.readAllStudent(selectClass, self.value_list)
        for i in range(1, len(self.vl)):
            row = self.vl[i]
            r = row['roll']
            n = row['name']
            st = "{:<30s}{:>6s}".format(str(r), n)
            self.scrollStudent.insert(i, st)

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family {Segoe UI Black} -size 13 -weight bold"
        font9 = "-family {Yu Gothic UI Semibold} -size 12 -weight bold"  \
            ""
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("692x508+650+150")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1, 1)
        top.title("Attendance - Students")
        top.configure(background="#d9d9d9")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.0, rely=0.0, relheight=1.014, relwidth=1.004)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#00ffff")

        self.scrollClass = ScrolledListBox(self.Frame1)
        self.scrollClass.configure(exportselection=False)
        self.scrollClass.place(relx=0.043, rely=0.078, relheight=0.596
                , relwidth=0.223)
        self.scrollClass.configure(background="white")
        self.scrollClass.configure(cursor="xterm")
        self.scrollClass.configure(disabledforeground="#a3a3a3")
        self.scrollClass.configure(font=font9)
        self.scrollClass.configure(foreground="black")
        self.scrollClass.configure(highlightbackground="#d9d9d9")
        self.scrollClass.configure(highlightcolor="#d9d9d9")
        self.scrollClass.configure(selectbackground="blue")
        self.scrollClass.configure(selectforeground="white")
        self.value_list = ["Select Class"]
        self.vl = model.readAllClass(self.value_list)
        for i in range(len(self.vl)):
            self.scrollClass.insert(i, self.vl[i])
        self.scrollClass.bind('<<ListboxSelect>>', self.onselect)

        self.scrollStudent = ScrolledListBox(self.Frame1)
        self.scrollStudent.configure(exportselection=False)
        self.scrollStudent.place(relx=0.302, rely=0.078, relheight=0.596
                , relwidth=0.655)
        self.scrollStudent.configure(background="white")
        self.scrollStudent.configure(cursor="xterm")
        self.scrollStudent.configure(disabledforeground="#a3a3a3")
        self.scrollStudent.configure(font=font9)
        self.scrollStudent.configure(foreground="black")
        self.scrollStudent.configure(highlightbackground="#d9d9d9")
        self.scrollStudent.configure(highlightcolor="#d9d9d9")
        self.scrollStudent.configure(selectbackground="blue")
        self.scrollStudent.configure(selectforeground="white")
        self.header = "{:<25s}{:>6s}".format("RollNo", "Name")
        self.value_list = [self.header]
        self.scrollStudent.insert(0, self.value_list[0])

        self.btnEdit = tk.Button(self.Frame1)
        self.btnEdit.place(relx=0.158, rely=0.738, height=53, width=208)
        self.btnEdit.configure(activebackground="#ececec")
        self.btnEdit.configure(activeforeground="#000000")
        self.btnEdit.configure(background="#eac515")
        self.btnEdit.configure(borderwidth="3")
        self.btnEdit.configure(disabledforeground="#a3a3a3")
        self.btnEdit.configure(font=font10)
        self.btnEdit.configure(foreground="#000000")
        self.btnEdit.configure(highlightbackground="#d9d9d9")
        self.btnEdit.configure(highlightcolor="black")
        self.btnEdit.configure(pady="0")
        self.btnEdit.configure(text='''Edit''')
        self.btnEdit.configure(command=self.editStudent)

        self.btnDelete = tk.Button(self.Frame1)
        self.btnDelete.place(relx=0.547, rely=0.738, height=53, width=208)
        self.btnDelete.configure(activebackground="#ececec")
        self.btnDelete.configure(activeforeground="#000000")
        self.btnDelete.configure(background="#eac515")
        self.btnDelete.configure(borderwidth="3")
        self.btnDelete.configure(disabledforeground="#a3a3a3")
        self.btnDelete.configure(font=font10)
        self.btnDelete.configure(foreground="#000000")
        self.btnDelete.configure(highlightbackground="#d9d9d9")
        self.btnDelete.configure(highlightcolor="black")
        self.btnDelete.configure(pady="0")
        self.btnDelete.configure(text='''Delete''')
        self.btnDelete.configure(command=self.delStudent)

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





