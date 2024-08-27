from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText

from dictionary import *


# Function to convert data speed units
def convert_data_speed(iral, from_unit, to_unit):
    if from_unit in data_speed_conversions and to_unit in data_speed_conversions[from_unit]:
        converted_value = data_speed_conversions[from_unit][to_unit](iral)
        return converted_value
    else:
        return None


# Function to convert computer storage units
def convert_computer_storage(iral, from_unit, to_unit):
    if from_unit in storage_conversions and to_unit in storage_conversions[from_unit]:
        conversion_factor = storage_conversions[from_unit][to_unit]
        result = iral * conversion_factor
        return result
    else:
        return None


# Function to convert length units
def convert_length(iral, from_unit, to_unit):
    if from_unit in length_conversions and to_unit in length_conversions[from_unit]:
        conversion_factor = length_conversions[from_unit][to_unit]
        result = iral * conversion_factor
        return result
    else:
        return None


# Function to convert mass units
def convert_mass(iral, from_unit, to_unit):
    if from_unit in mass_conversions and to_unit in mass_conversions[from_unit]:
        conversion_factor = mass_conversions[from_unit][to_unit]
        result = iral * conversion_factor
        return result
    else:
        return None


# Function to convert speed units
def convert_speed(iral, from_unit, to_unit):
    if from_unit in speed_conversions and to_unit in speed_conversions[from_unit]:
        conversion_factor = speed_conversions[from_unit][to_unit]
        result = iral * conversion_factor
        return result
    else:
        return None


# Function to convert temperature units
def convert_temperature(iral, from_unit, to_unit):
    if from_unit in temperature_conversions and to_unit in temperature_conversions[from_unit]:
        converted_value = temperature_conversions[from_unit][to_unit](iral)
        return converted_value
    else:
        return None


# Function to convert time units
def convert_time(iral, from_unit, to_unit):
    if from_unit in time_conversions and to_unit in time_conversions[from_unit]:
        converted_value = time_conversions[from_unit][to_unit](iral)
        return converted_value
    else:
        return None


# Function to convert volume units
def convert_volume(iral, from_unit, to_unit):
    if from_unit in volume_conversions and to_unit in volume_conversions[from_unit]:
        converted_value = volume_conversions[from_unit][to_unit](iral)
        return converted_value
    else:
        return None


# Function to handle conversion process
def convert():
    # Check the selected category and show messagebox for errors
    if measure.get() == "" or measure.get() == "Categories of Units" or measure.get() == "Select an option":
        messagebox.showerror("Error", "Please select a category")
    elif ent_numR.get("1.0", "end-1c").isalpha() or ent_numL.get("1.0", "end-1c").isalpha():
        messagebox.showerror("Error", "Please input an integer")
    else:
        corales = ent_numL.get("1.0", "end-1c").strip()
        if corales == "" or corales == " ":
            messagebox.showerror("Error", "Please input a number")
        else:
            iral = float(ent_numL.get("1.0", "end-1c"))
            from_unit = unitL.get()
            to_unit = unitR.get()
            if from_unit == "Units" or to_unit == "Units":
                messagebox.showerror("Error", "Please select a unit")
            else:
                # Check the selected category and perform conversion accordingly
                if measure.get() == "Computer storage":
                    result = convert_computer_storage(iral, from_unit, to_unit)
                    if result is not None:
                        ent_numR.config(state=NORMAL)
                        ent_numR.delete('1.0', 'end')
                        ent_numR.insert('1.0', str(result))
                        ent_numR.config(state=DISABLED)
                elif measure.get() == "Data speed":
                    result = convert_data_speed(iral, from_unit, to_unit)
                    if result is not None:
                        ent_numR.config(state=NORMAL)
                        ent_numR.delete('1.0', 'end')
                        ent_numR.insert('1.0', str(result))
                        ent_numR.config(state=DISABLED)
                elif measure.get() == "Length":
                    result = convert_length(iral, from_unit, to_unit)
                    if result is not None:
                        ent_numR.config(state=NORMAL)
                        ent_numR.delete('1.0', 'end')
                        ent_numR.insert('1.0', str(result))
                        ent_numR.config(state=DISABLED)
                elif measure.get() == "Mass":
                    result = convert_mass(iral, from_unit, to_unit)
                    if result is not None:
                        ent_numR.config(state=NORMAL)
                        ent_numR.delete('1.0', 'end')
                        ent_numR.insert('1.0', str(result))
                        ent_numR.config(state=DISABLED)
                elif measure.get() == "Speed":
                    result = convert_speed(iral, from_unit, to_unit)
                    if result is not None:
                        ent_numR.config(state=NORMAL)
                        ent_numR.delete('1.0', 'end')
                        ent_numR.insert('1.0', str(result))
                        ent_numR.config(state=DISABLED)
                elif measure.get() == "Temperature":
                    result = convert_temperature(iral, from_unit, to_unit)
                    if result is not None:
                        ent_numR.config(state=NORMAL)
                        ent_numR.delete('1.0', 'end')
                        ent_numR.insert('1.0', str(result))
                        ent_numR.config(state=DISABLED)
                elif measure.get() == "Time":
                    result = convert_time(iral, from_unit, to_unit)
                    if result is not None:
                        ent_numR.config(state=NORMAL)
                        ent_numR.delete('1.0', 'end')
                        ent_numR.insert('1.0', str(result))
                        ent_numR.config(state=DISABLED)
                elif measure.get() == "Volume/Liquid":
                    result = convert_volume(iral, from_unit, to_unit)
                    if result is not None:
                        ent_numR.config(state=NORMAL)
                        ent_numR.delete('1.0', 'end')
                        ent_numR.insert('1.0', str(result))
                        ent_numR.config(state=DISABLED)


# Function to handle the event when the measure dropdown is clicked
def on_click(event):
    if measure.get() == "Categories of Units":
        measure.set("Select an option")
        measure.config(foreground="black")
    # Update options and GUI elements based on the selected measure
    elif measure.get() == "Computer storage":
        # Update units and GUI colors for Computer storage category
        unitL.set("Units")
        unitR.set("Units")
        frm.config(bg="#A0DEFF")
        lbl_enter.config(bg="#A0DEFF", fg="blue")
        lbl_measure.config(bg="#A0DEFF", fg="blue")
        ent_numL.config(fg="blue")
        unitL.config(values=["Bytes", "Kilobytes", "Megabytes", "Gigabytes", "Terabytes", "Petabytes"])
        unitR.config(values=["Bytes", "Kilobytes", "Megabytes", "Gigabytes", "Terabytes", "Petabytes"])
        ent_numR.config(fg="green")
    # Update options and GUI elements for other categories
    elif measure.get() == "Data speed":
        # Update units and GUI colors for Data speed category
        unitL.set("Units")
        unitR.set("Units")
        frm.config(bg="#7ABA78")
        lbl_enter.config(bg="#7ABA78", fg="#1A4D2E")
        lbl_measure.config(bg="#7ABA78", fg="#1A4D2E")
        ent_numL.config(fg="#1A4D2E")
        unitL.config(values=["Kilobits", "Megabits", "Gigabits"])
        unitR.config(values=["Kilobits", "Megabits", "Gigabits"])
        ent_numR.config(fg="green")
    # Update options and GUI elements for other categories
    elif measure.get() == "Length":
        # Update units and GUI colors for Length category
        unitL.set("Units")
        unitR.set("Units")
        frm.config(bg="#FDDE55")
        lbl_enter.config(bg="#FDDE55", fg="red")
        lbl_measure.config(bg="#FDDE55", fg="red")
        ent_numL.config(fg="red")
        unitL.config(values=["Kilometre", "Metre", "Centimetre", "Millimetre", "Micrometre", "Mile", "Yard", "Foot",
                             "Inch"])
        unitR.config(values=["Kilometre", "Metre", "Centimetre", "Millimetre", "Micrometre", "Mile", "Yard", "Foot",
                             "Inch"])
        ent_numR.config(fg="green")
    # Update options and GUI elements for other categories
    elif measure.get() == "Mass":
        # Update units and GUI colors for Mass category
        unitL.set("Units")
        unitR.set("Units")
        frm.config(bg="#B2B2B2")
        lbl_enter.config(bg="#B2B2B2", fg="black")
        lbl_measure.config(bg="#B2B2B2", fg="black")
        ent_numL.config(fg="black")
        unitL.config(values=["Kilogram", "Gram", "Milligram", "Imperial ton", "Pound", "Ounce"])
        unitR.config(values=["Kilogram", "Gram", "Milligram", "Imperial ton", "Pound", "Ounce"])
        ent_numR.config(fg="green")
    # Update options and GUI elements for other categories
    elif measure.get() == "Speed":
        # Update units and GUI colors for Speed category
        unitL.set("Units")
        unitR.set("Units")
        frm.config(bg="#FF204E")
        lbl_enter.config(bg="#FF204E", fg="yellow")
        lbl_measure.config(bg="#FF204E", fg="yellow")
        ent_numL.config(fg="#FF204E")
        unitL.config(values=["Mile/hour", "Kilometer/hour", "Meter/second", "Knot", "Mach", "Mile/hour", "Meter/second",
                             "Kilometer/hour", "Knot", "Mile/hour"])
        unitR.config(values=["Mile/hour", "Kilometer/hour", "Meter/second", "Knot", "Mach", "Mile/hour", "Meter/second",
                             "Kilometer/hour", "Knot", "Mile/hour"])
        ent_numR.config(fg="green")
    # Update options and GUI elements for other categories
    elif measure.get() == "Temperature":
        # Update units and GUI colors for Temperature category
        unitL.set("Units")
        unitR.set("Units")
        frm.config(bg="#FC4100")
        lbl_enter.config(bg="#FC4100", fg="yellow")
        lbl_measure.config(bg="#FC4100", fg="yellow")
        ent_numL.config(fg="#FC4100")
        unitL.config(values=["Celsius", "Fahrenheit", "Kelvin", "Celsius", "Fahrenheit", "Rankine"])
        unitR.config(values=["Celsius", "Fahrenheit", "Kelvin", "Celsius", "Fahrenheit", "Rankine"])
        ent_numR.config(fg="green")
    # Update options and GUI elements for other categories
    elif measure.get() == "Time":
        # Update units and GUI colors for Time category
        unitL.set("Units")
        unitR.set("Units")
        frm.config(bg="#DDDDDD")
        lbl_enter.config(bg="#DDDDDD", fg="black")
        lbl_measure.config(bg="#DDDDDD", fg="black")
        ent_numL.config(fg="black")
        unitL.config(values=["Millennium", "Century", "Decade", "Year", "Month", "Week", "Day", "Hour", "Minute",
                             "Second"])
        unitR.config(values=["Millennium", "Century", "Decade", "Year", "Month", "Week", "Day", "Hour", "Minute",
                             "Second"])
        ent_numR.config(fg="green")
    # Update options and GUI elements for other categories
    elif measure.get() == "Volume/Liquid":
        # Update units and GUI colors for Volume/Liquid category
        unitL.set("Units")
        unitR.set("Units")
        frm.config(bg="#0E21A0")
        lbl_enter.config(bg="#0E21A0", fg="#A0DEFF")
        lbl_measure.config(bg="#0E21A0", fg="#A0DEFF")
        ent_numL.config(fg="#0E21A0")
        unitL.config(values=["Cubic meter", "Liter", "Milliliter", "Imperial Gallon", "Imperial Cup",
                             "Imperial fluid ounce", "Imperial tablespoon", "Imperial teaspoon", "Cubic foot",
                             "Cubic Inch"])
        unitR.config(values=["Cubic meter", "Liter", "Milliliter", "Imperial Gallon", "Imperial Cup",
                             "Imperial fluid ounce", "Imperial tablespoon", "Imperial teaspoon", "Cubic foot",
                             "Cubic Inch"])
        ent_numR.config(fg="green")


def show_custom_message(message):
    root = Tk()
    root.title("Formulas")
    root.geometry("700x350+450+200")

    # Create a scrolled text widget
    text = ScrolledText(root, wrap=WORD)
    text.pack(expand=True, fill=BOTH)

    # Insert the message into the scrolled text widget
    text.insert(END, message)

    # Disable text editing
    text.configure(state=DISABLED)

    # Run the Tkinter event loop
    root.mainloop()


def show_formula():
    # Show formula based on the selected measure category
    if measure.get() == "Computer storage":
        message = "Speed Conversion Formulas:\n\n"
        # Iterate through the conversions dictionary and add each formula pair to the message
        for from_unit, conversions in storage_conversions.items():
            for to_unit, conversion_factor in conversions.items():
                # Add the formula pair to the message with appropriate wrapping
                message += f"{from_unit} to {to_unit}: {from_unit} * {conversion_factor}\n"
        # Show the custom dialog box with all the formulas
        show_custom_message(message)
    elif measure.get() == "Data speed":
        message = "Conversion Formulas:\n\n"
        # Iterate through the conversions dictionary and add each formula pair to the message
        for from_unit, conversions in data_speed_conversions.items():
            for to_unit, formula_func in conversions.items():
                # Convert the lambda function to a string
                formula_str = str(formula_func(1))
                # Add the formula pair to the message with appropriate wrapping
                message += f"{from_unit} to {to_unit}: {from_unit} * {formula_str}\n"
        # Show the custom dialog box with all the formulas
        show_custom_message(message)
    elif measure.get() == "Length":
        message = "Speed Conversion Formulas:\n\n"
        for from_unit, conversions in length_conversions.items():
            for to_unit, conversion_factor in conversions.items():
                message += f"{from_unit} to {to_unit}: {from_unit} * {conversion_factor}\n"
        show_custom_message(message)
    elif measure.get() == "Mass":
        message = "Speed Conversion Formulas:\n\n"
        for from_unit, conversions in mass_conversions.items():
            for to_unit, conversion_factor in conversions.items():
                message += f"{from_unit} to {to_unit}: {from_unit} * {conversion_factor}\n"
        show_custom_message(message)
    elif measure.get() == "Speed":
        message = "Speed Conversion Formulas:\n\n"
        for from_unit, conversions in speed_conversions.items():
            for to_unit, conversion_factor in conversions.items():
                message += f"{from_unit} to {to_unit}: {from_unit} * {conversion_factor}\n"
        show_custom_message(message)
    elif measure.get() == "Temperature":
        message = ("Conversion Formulas:\n\n"
                   "Celsius to Celsius: Celsius * 1\n"
                   "Celsius to Fahrenheit: (Celsius * 9 / 5) + 32\n"
                   "Celsius to Kelvin: Celsius + 273.15\n"
                   "Celsius to Rankine: Celsius * 9 / 5\n"
                   "Fahrenheit to Celsius: (Fahrenheit - 32) * 5 / 9\n"
                   "Fahrenheit to Fahrenheit: Fahrenheit * 1\n"
                   "Fahrenheit to Kelvin: (Fahrenheit + 459.67) * 5 / 9\n"
                   "Fahrenheit to Rankine: Fahrenheit * 1\n"
                   "Kelvin to Celsius: Kelvin - 273.15\n"
                   "Kelvin to Fahrenheit: (Kelvin * 9 / 5) - 459.67\n"
                   "Kelvin to Kelvin: Kelvin * 1\n"
                   "Kelvin to Rankine: Kelvin * 5 / 9\n"
                   "Rankine to Celsius: Rankine * 5 / 9 - 273.15\n"
                   "Rankine to Fahrenheit: Rankine - 459.67\n"
                   "Rankine to Kelvin: Rankine * 5 / 9\n"
                   "Rankine to Rankine: Rankine * 1")
        show_custom_message(message)
    elif measure.get() == "Time":
        message = "Conversion Formulas:\n\n"
        for from_unit, conversions in time_conversions.items():
            for to_unit, formula_func in conversions.items():
                formula_str = str(formula_func(1))
                message += f"{from_unit} to {to_unit}: {from_unit} * {formula_str}\n"
        show_custom_message(message)
    elif measure.get() == "Volume/Liquid":
        message = "Conversion Formulas:\n\n"
        for from_unit, conversions in volume_conversions.items():
            for to_unit, formula_func in conversions.items():
                formula_str = str(formula_func(1))
                message += f"{from_unit} to {to_unit}: {from_unit} * {formula_str}\n"
        show_custom_message(message)


# Create the main application window
main = Tk()
main.title("PyScalePro")
main.resizable(False, False)
main.geometry("700x350+450+200")

# Create a frame within the main window to hold all the GUI elements
frm = Frame(main, height=350, width=700, bg="khaki")

# Create input and output text widgets for entering and displaying numerical values
ent_numL = Text(frm, width=12, font=("Arial", 15), height=1, padx=10, pady=30)
ent_numR = Text(frm, width=12, font=("Arial", 15), height=1, padx=10, pady=30, state=DISABLED)

# Create labels for displaying instructions and information
lbl_enter = Label(frm, text="Enter Value \n of Measurement:", bg="khaki", font=("Serif", 9, "bold"))
lbl_measure = Label(frm, text="Select category to see units", bg="khaki", font=("Serif", 9, "bold"))

# Create combo boxes for selecting different units and measurement categories
unitL = ttk.Combobox(frm, values=[], width=22, font=("Serif", 8))
unitL.set("Units")
unitR = ttk.Combobox(frm, values=[], width=22, foreground="green", font=("Serif", 8))
unitR.set("Units")
measure = ttk.Combobox(frm, values=["Computer storage", "Data speed", "Length", "Mass", "Speed", "Temperature", "Time",
                                    "Volume/Liquid"], width=22, font=("Serif", 8))
measure.set("Categories of Units")

# Create buttons for performing conversion and displaying formulas
btn_convert = Button(frm, text="Convert", fg="red", width=21, height=1, command=convert, font=("Serif", 9, "bold"))
btn_show = Button(text="Formula", command=show_formula, fg="red", width=21, height=1, font=("Serif", 9, "bold"))

# Position the GUI elements within the frame
ent_numL.place(x=160, y=80)
unitL.place(x=160, y=165)
measure.place(x=160, y=230)
ent_numR.place(x=380, y=80)
unitR.place(x=380, y=165)
btn_convert.place(x=380, y=230)
lbl_enter.place(x=50, y=110)
lbl_measure.place(x=155, y=255)
btn_show.place(x=380, y=260)

# Position the frame within the main window
frm.place(x=0, y=0)

# Bind the "FocusIn" event to the "on_click" function
measure.bind("<FocusIn>", on_click)

# Start the GUI event loop
main.mainloop()
