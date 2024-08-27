from dictionary import *
import tkinter as tk
from tkinter.scrolledtext import ScrolledText


# Create a custom dialog box with scrolling
def show_custom_message(message):
    root = tk.Tk()
    root.title("Formulas")

    # Create a scrolled text widget
    text = ScrolledText(root, wrap=tk.WORD)
    text.pack(expand=True, fill=tk.BOTH)

    # Insert the message into the scrolled text widget
    text.insert(tk.END, message)

    # Disable text editing
    text.configure(state=tk.DISABLED)

    # Run the Tkinter event loop
    root.mainloop()


# Initialize the message string
message = "Conversion Formulas:\n\n"

# Iterate through the volume conversions dictionary and add each formula pair to the message
for from_unit, conversions in volume_conversions.items():
    for to_unit, formula_func in conversions.items():
        # Convert the lambda function to a string
        formula_str = str(formula_func(1))
        operation = "/"

        # Add the formula pair to the message with appropriate wrapping
        message += f"{from_unit} to {to_unit}: * {formula_str}\n"

# Show the custom dialog box with all the formulas
show_custom_message(message)

# messagebox.showinfo("Formula",
#                             "Cubic inches --- Cubic feet: Cubic inches / 1728"
#                             "\nCubic feet --- Cubic inches: Cubic feet * 1728"
#                             "\nCubic inches --- Liters: Cubic inches / 61.0237"
#                             "\nLiters --- Cubic inches: Liters * 61.0237"
#                             "\nMillimeters --- Inches: Millimeters / 25.4"
#                             "\nInches --- Millimeters: Inches * 25.4"
#                             "\nImperial gallons --- Liters: Imperial gallons * 4.54609"
#                             "\nLiters --- Imperial gallons: liters / 4.54609"
#                             "\nImperial tablespoons --- Milliliters: imperial tablespoons * 14.20653125"
#                             "\nMilliliters --- Imperial tablespoons: milliliters / 14.20653125"
#                             "\nImperial fluid ounces --- Milliliters: imperial fluid ounces * 28.4130625"
#                             "\nMilliliters --- Imperial fluid ounces: milliliters / 28.4130625"
#                             "\nImperial teaspoons --- Milliliters: imperial teaspoons * 4.92892159375"
#                             "\nMilliliters --- Imperial teaspoons: milliliters / 4.92892159375")