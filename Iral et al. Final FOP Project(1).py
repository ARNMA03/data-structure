from tkinter import *
from tkinter import messagebox

def convert():
    gg = ent1.get().strip()
    if gg == "":
        messagebox.showerror("Error", "Please input a number!")
    elif gg.isalpha():
        messagebox.showerror("Error", "Please input a number!")
    else:
        gg = float(gg)
        if clicked.get() == "Length":
            lbl2.config(text=f"Conversion: "
                             f"\n{gg} Kilometre = {gg * 1000} Metre"
                             f"\n{gg} Metre = {gg * 100} Centimetre"
                             f"\n{gg} Centimetre = {gg * 10} Millimetre"
                             f"\n{gg} Millimetre = {gg * 1000} Micrometre"
                             f"\n{gg} Micrometre = {gg * 1000} Nanometre"
                             f"\n{gg} Mile = {gg * 1760} Yard"
                             f"\n{gg} Yard = {gg * 3} Foot"
                             f"\n{gg} Foot = {gg * 12} Inch"
                        )
        elif clicked.get() == "Mass":
            lbl2.config(text=f"Conversion: "
                             f"\n{gg} Kilogram = {gg * 1000} Gram"
                             f"\n{gg} Gram = {gg * 1000} Milligram"
                             f"\n{gg} Milligram = {gg * 1000} Microgram"
                             f"\n{gg} Imperial ton = {gg * 2240} Pound"
                             f"\n{gg} Pound = {gg * 16} Ounce"
                        )
        elif clicked.get() == "Volume":
            lbl2.config(text=f"Conversion: "
                             f"\n{gg} Cubic meter = {gg * 1000} Liter"
                             f"\n{gg} Liter = {gg * 1000} Milliliter"
                             f"\n{gg} Milliliter = {gg * 4546} Imperial gallon"
                             f"\n{gg} Imperial Gallon = {gg * 16} Imperial cup"
                             f"\n{gg} Imperial Cup= {gg * 10} imperial fluid ounce"
                             f"\n{gg} Imperial fluid ounce= {gg * 1.6} Imperial tablespoon"
                             f"\n{gg} Imperial tablespoon= {gg * 3} Imperial teaspoon"
                             f"\n{gg} Imperial teaspoon= {gg * 4784} Cubic foot"
                             f"\n{gg} Cubic foot= {gg * 2.768} Cubic Inch"
                        )
        elif clicked.get() == "Speed":
            lbl2.config(text=f"Conversion: "
                             f"\n{gg} Mile/hour = {round(gg * 1.609344, 3)} Kilometer/hour"
                             f"\n{gg} Kilometer/hour = {round(gg * 0.27777778, 3)} Meter/second"
                             f"\n{gg} Meter/second = {round(gg * 1.94384449, 3)} Knot"
                             f"\n{gg} Knot = {round(gg * 0.00149984, 3)} Mach"
                             f"\n{gg} Mach = {round(gg * 767.269148, 3)} Mile/hour"
                             f"\n{gg} Mile/hour = {round(gg * 0.44704, 3)} Meter/second"
                             f"\n{gg} Meter/second = {round(gg * 0.00291545, 3)} Mach"
                             f"\n{gg} Kilometer/hour = {round(gg * 0.5399568, 3)} Knot"
                             f"\n{gg} Knot = {round(gg * 1.15077945, 3)} Mile/hour"
                        )
        elif clicked.get() == "Time":
            lbl2.config(text=f"Conversion: "
                             f"\n{gg} Millennium = {round(gg * 10, 2)} Century"
                             f"\n{gg} Century = {round(gg * 10, 2)} Decade"
                             f"\n{gg} Decade = {round(gg * 10, 2)} Year"
                             f"\n{gg} Year = {round(gg * 12, 2)} Month"
                             f"\n{gg} Month = {round(gg * 4.3452381, 2)} Week"
                             f"\n{gg} Week = {round(gg * 7, 2)} Day"
                             f"\n{gg} Day = {round(gg * 24, 2)} Hour"
                             f"\n{gg} Hour = {round(gg * 60, 2)} Minute"
                             f"\n{gg} Minute = {round(gg * 60, 2)} Second"
                        )
        elif clicked.get() == "Temperature":
            lbl2.config(text=f"Conversion: "
                             f"\n{gg} Celsius = {round(gg * 33.8, 4)} Fahrenheit"
                             f"\n{gg} Fahrenheit = {round(gg * 255.927778, 4)} Kelvin"
                             f"\n{gg} Kelvin = {round(gg * 1.8, 4)} Rankine"
                             f"\n{gg} Rankine = {round(gg * -272.594444, 4)} Celsius"
                             f"\n{gg} Celsius = {round(gg * 274.15, 4)} Kelvin"
                             f"\n{gg} Fahrenheit = {round(gg * 460.67, 4)} Rankine"
                        )
        elif clicked.get() == "Choose":
            messagebox.showerror("Error", "Please select something from the option menu!")




main = Tk()
main.title("Unit Converter")
main.resizable(False, False)
main.geometry("700x350+450+200")

frm1 = Frame(main, height=200)
frm1.place(x=0, y=0)
frm2 = Frame(main, height=200)
frm2.place(x=300, y=0)

clicked = StringVar()
clicked.set("Choose")

drop = OptionMenu(frm1, clicked, "Length", "Mass", "Volume/Liquid", "Speed", "Time", "Temperature")
drop.grid(column=1, row=3)

lbl1 = Label(frm1, text="Amount input: ")
lbl1.grid(column=1, row=1)
ent1 = Entry(frm1)
ent1.grid(column=2, row=1)
btn = Button(frm1, text="Convert", command=convert)
btn.grid(column=3, row=1)
lbl2 = Label(frm2, text="Conversion: ")
lbl2.grid(column=1, row=1)



main.mainloop()