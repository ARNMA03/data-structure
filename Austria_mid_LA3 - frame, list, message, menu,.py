from tkinter import *
from tkinter import messagebox, filedialog, simpledialog

def open_file():
    ARNMA = filedialog.askopenfilename(title="Open text file")
    DMPS = open(ARNMA, "r").readlines()
    lb.delete(0, END)
    for item in DMPS:
        lb.insert(END, item.strip())
def save_file():
    ARNMA = filedialog.asksaveasfilename(defaultextension=".txt", title="Save as")
    DMPS = open(ARNMA, 'w')
    items = lb.get(0, END)
    DMPS.write('\n'.join(items))
def add_item():
    item = simpledialog.askstring("Add Item", "Enter new item:")
    if item:
        lb.insert(END, item)
def delete_item():
    selected_index = lb.curselection()
    lb.delete(selected_index)
def edit_item():
    selected_index = lb.curselection()
    if selected_index:
        item = simpledialog.askstring("Edit Item", "Enter new value:", initialvalue=lb.get(selected_index))
        if item:
            lb.delete(selected_index)
            lb.insert(selected_index, item)
def about():
    messagebox.showinfo("About", "List Manager Application\nVersion 1.0")


mainwindow = Tk()
mainwindow.title("MENU, LIST, FRAME")
mainwindow.geometry("500x500+800+200")
mainwindow.resizable(False, False)

frame = Frame(mainwindow)
frame.pack(fill=BOTH, expand=True)

lb = Listbox(frame)
lb.pack(fill=BOTH, expand=True)

menubar = Menu(mainwindow)

file = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=file)
file.add_command(label='Open', command=open_file)
file.add_command(label='Save', command=save_file)

edit = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=edit)
edit.add_command(label='Add', command=add_item)
edit.add_command(label='Delete', command=delete_item)
edit.add_command(label='Edit', command=edit_item)

Help = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Help", menu=Help)
Help.add_command(label='about', command=about)

mainwindow.config(menu=menubar)

mainwindow.mainloop()
