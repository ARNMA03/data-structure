from tkinter import *
from tkinter import messagebox

def calculate():
    car_cost = float(selected_car.get())
    interior_cost = float(sum(float(interior_option_variables[i].get()) for i in range(len(interior_option_variables))))
    exterior_option_cost = float(sum(float(exterior_option_variables[i].get()) for i in range(len(exterior_option_variables))))

    total = car_cost + interior_cost + exterior_option_cost

    lbl_ttl.config(text=f"Total Cost: ₱{total:.2f}")

    car_message = f"Car selected:\n-{list(car.keys())[list(car.values()).index(selected_car.get())]} (₱{float(selected_car.get())})\n"

    interior_option_message = f"Interior Option: \n"
    new_interior_option_variables = [interior_option_variables[i].get() for i in range(len(interior_option_variables))]
    if new_interior_option_variables.count(0) == 2:
        interior_option_message += f" N/A \n"
    else:
        for item in new_interior_option_variables:
            if item != "0":
                interior_option_message += f"-{list(Interior_option.keys())[list(Interior_option.values()).index(item)]} (₱{item})\n"

    exterior_finish_cost = f"Exterior Finish: \n-{selected_exterior_finish.get()}\n"

    exterior_option_message = f"Exterior Option: \n"
    new_exterior_option_variables = [exterior_option_variables[i].get() for i in range(len(exterior_option_variables))]
    if new_interior_option_variables.count(0) == 2:
        exterior_option_message += f" N/A \n"
    else:
        for item in new_exterior_option_variables:
            if item != "0":
                exterior_option_message += f"-{list(Exterior_option.keys())[list(Exterior_option.values()).index(item)]}(₱{item})\n"

    totality = f"Total: ₱{total}"
    final_message = car_message + interior_option_message + exterior_finish_cost + exterior_option_message + totality
    messagebox.showinfo(title="Receipt", message=final_message)

window = Tk()
window.geometry("300x475+150+150")
window.resizable(False, False)
window.title("Austria_mid_LA2 check, radio")

selected_car = StringVar()
selected_car.set(None or 0)
car = {"BMW": "5000.00",
       "Subaru": "2500.00",
       "Chevrolet": "4100.00"}

selected_interior = StringVar()
selected_interior.set(0)
Interior_option = {"Leather": "550.00",
                   "GPS": "1000.00"}
interior_option_variables = ["invar1", "invar2"]

selected_exterior_finish = StringVar()
selected_exterior_finish.set(None or 0)
Exterior_finish = ["Hard top", "Convertible"]

selected_exterior_option = StringVar()
selected_exterior_option.set(0)
Exterior_option = {"Wheel Upgrade": "1000.00",
                   "Performance Package": "2000.00"}
exterior_option_variables = ["exvar1", "exvar2"]

lbl_car = Label(window, text="Select Car:").pack()
for cars in car:
    c = Radiobutton(window,
                    text=cars,
                    value=car[cars],
                    variable=selected_car).pack(fill='x', padx=5, pady=5)

lbl_si = Label(window, text="Select Interior Option:").pack()
for index, si in enumerate(Interior_option):
    interior_option_variables[index] = StringVar()
    interior_option_variables[index].set(None or 0)
    s = Checkbutton(window,
                    text=si,
                    onvalue=Interior_option[si],
                    offvalue=0,
                    variable=interior_option_variables[index]).pack(fill='x', padx=5, pady=5)

lbl_sef = Label(window, text="Select Exterior Finish:").pack()
for sef in Exterior_finish:
    h = Radiobutton(window,
                    text=sef,
                    value=sef,
                    variable=selected_exterior_finish).pack(fill='x', padx=5, pady=5)

lbl_seo = Label(window, text="Select Exterior Option:").pack()
for index, seo in enumerate(Exterior_option):
    exterior_option_variables[index] = StringVar()
    exterior_option_variables[index].set(None or 0)
    g = Checkbutton(window,
                    text=seo,
                    onvalue=Exterior_option[seo],
                    offvalue=0,
                    variable=exterior_option_variables[index]).pack(fill='x', padx=5, pady=5)

lbl_ttl = Label(window, text="")
lbl_ttl.pack()
btn_calc = Button(window, text="Calculate", command=calculate).pack()

window.mainloop()