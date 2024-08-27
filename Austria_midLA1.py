from tkinter import *


def entry_activity():
    def display():
        label_text.config(text=f"{ent_text.get()}", bg="#4169E1", fg="#E1B941")

    window = Tk()
    window.geometry("250x150+800+400")
    window.title("J1T-midLA1")
    window.config(bg="#4169E1")

    lbl1_text = Label(window, text="Input Text Here", bg="#4169E1", fg="#E1B941")
    lbl1_text.place(x=10, y=40)

    ent_text = Entry(window, width=15)
    ent_text.place(x=10, y=65)

    lbl_text = Label(window, text="Arden Roland Nicholai M. Austria", bg="#4169E1", fg="#E1B941")
    lbl_text.place(x=30, y=10)

    lbl2_text = Label(window, text="Display", bg="#4169E1", fg="#E1B941")
    lbl2_text.place(x=150, y=40)

    label_text = Label(window, text="", bg="#4169E1", fg="#E1B941", wraplength=80)
    label_text.place(x=150, y=65)

    button = Button(text="Display Text", width=10, command=display)

    button.place(x=90, y=100)

    window.mainloop()


entry_activity()
