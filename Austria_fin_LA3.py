import sqlite3
from tkinter import *
from tkinter import messagebox


# Function to create the database and table if they don't exist
def create_database_and_table(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                        ID INTEGER PRIMARY KEY,
                        Name TEXT,
                        Price REAL,
                        Quantity INTEGER
                      )''')
    conn.commit()


# Function to insert data into the database
def insert_data(conn, Name, Price, Quantity):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (Name, Price, Quantity) VALUES (?, ?, ?)", (Name, Price, Quantity))
    conn.commit()


# Function to retrieve and display all data from the database
def show_data(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    print(products)
    return products


# Function to update data in the database
def update_data(conn, ID, new_Name, new_Price, new_Quantity):
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET Name = ? WHERE ID = ? ", (new_Name, ID))
    cursor.execute("UPDATE products SET Price = ? WHERE ID = ? ", (new_Price, ID))
    cursor.execute("UPDATE products SET Quantity = ? WHERE ID = ?", (new_Quantity, ID))
    conn.commit()


# Function to add new data by taking input from GUI entries
def add_data():
    if name_entry.get() == "" or price_entry.get() == "" or quantity_entry.get() == "":
        messagebox.showinfo("Error", "Please enter all data.")
    elif price_entry.get().isalpha() or quantity_entry.get().isalpha():
        messagebox.showinfo("Error", "Please input an integer inside price and quantity.")
    else:
        Name = name_entry.get()
        Price = float(price_entry.get())
        Quantity = int(quantity_entry.get())

        if Name and Price and Quantity:
            insert_data(conn, Name, Price, Quantity)
            messagebox.showinfo("Success", "Product added successfully!")
            id_entry.delete(0, END)
            name_entry.delete(0, END)
            price_entry.delete(0, END)
            quantity_entry.delete(0, END)
            products = show_data(conn)
            if products:
                user_list.delete(0, END)
                for product in products:
                    user_list.insert(END, product)
        else:
            messagebox.showinfo("Error", "Please enter all data.")


# Function to update existing data based on ID
def update_datas():
    if name_entry.get() == "" or price_entry.get() == "" or quantity_entry.get() == "":
        messagebox.showinfo("Error", "Please enter all data.")
    elif price_entry.get().isalpha() or quantity_entry.get().isalpha():
        messagebox.showerror("Error", "Please input an integer inside price and quantity.")
    else:
        ID = int(id_entry.get())
        new_Name = name_entry.get()
        new_Price = float(price_entry.get())
        new_Quantity = int(quantity_entry.get())
        if ID and new_Name and new_Price and new_Quantity:
            update_data(conn, ID, new_Name, new_Price, new_Quantity)
            messagebox.showinfo("Success", "Data updated successfully!")
            id_entry.delete(0, END)
            name_entry.delete(0, END)
            price_entry.delete(0, END)
            quantity_entry.delete(0, END)
            products = show_data(conn)
            if products:
                user_list.delete(0, END)
                for product in products:
                    user_list.insert(END, product)
        else:
            messagebox.showinfo("Error", "Please enter all data.")


# Function to display all data in the GUI listbox
def show_datas():
    products = show_data(conn)
    if products:
        user_list.delete(0, END)
        for product in products:
            user_list.insert(END, product)
    else:
        user_list.delete(0, END)
        messagebox.showinfo("info", "No data found!")


# Function to delete data from the database
def delete_data(conn, ID):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE ID = ? ", (ID,))
    conn.commit()


# Function to delete data based on ID input from the GUI
def delete_datas():
    ID = id_entry.get()
    if ID:
        if ID.isalpha():
            messagebox.showinfo("Error", "Integer needed in ID.")
        else:
            response = messagebox.askyesno("Confirmation", "Are you sure you want to delete this product?")
            if response:
                delete_data(conn, ID)
                messagebox.showinfo("Success", "Product deleted successfully!")
                id_entry.delete(0, END)
                products = show_data(conn)
                if products:
                    user_list.delete(0, END)
                    for product in products:
                        user_list.insert(END, product)
                else:
                    user_list.delete(0, END)
            else:
                messagebox.showinfo("Success", "Product not deleted")
    else:
        messagebox.showinfo("Error", "Please enter all data.")


# Function to close the database connection and exit the application
def exit_app():
    conn.close()
    window.destroy()


# Connect to the SQLite database and create table if not exists
conn = sqlite3.connect("inventory.db")
create_database_and_table(conn)

# GUI setup
window = Tk()
window.title("Inventory")
window.geometry("300x450+500+200")
window.resizable(False, False)

ent_frm = Frame(window)
ent_frm.grid(row=1, column=0)
list_frm = Frame(window)
list_frm.grid(row=2, column=0)
btn_frm = Frame(window)
btn_frm.grid(row=3, column=0)

# Entry widgets
id_label = Label(ent_frm, text="ID:")
id_label.grid(row=0, column=0, pady=5)
id_entry = Entry(ent_frm)
id_entry.grid(row=0, column=1, pady=5)

name_label = Label(ent_frm, text="Name:")
name_label.grid(row=1, column=0, pady=5)
name_entry = Entry(ent_frm)
name_entry.grid(row=1, column=1, pady=5)

price_label = Label(ent_frm, text="Price:")
price_label.grid(row=2, column=0, pady=5)
price_entry = Entry(ent_frm)
price_entry.grid(row=2, column=1, pady=5)

quantity_label = Label(ent_frm, text="Quantity:")
quantity_label.grid(row=3, column=0, pady=5)
quantity_entry = Entry(ent_frm)
quantity_entry.grid(row=3, column=1, pady=5)

# Listbox widget
user_list = Listbox(list_frm, width=50)
user_list.grid(row=1, column=0)

# Buttons for various operations
add_button = Button(btn_frm, text="Add product", command=add_data, padx=10, pady=10, width=15)
add_button.grid(row=1, column=0, padx=5, pady=5)
update_button = Button(btn_frm, text="Update price/quantity", command=update_datas, padx=10, pady=10, width=15)
update_button.grid(row=2, column=0, padx=5, pady=5)
show_button = Button(btn_frm, text="Show products", command=show_datas, padx=10, pady=10, width=15)
show_button.grid(row=1, column=1, padx=5, pady=5)
delete_button = Button(btn_frm, text="Delete", command=delete_datas, padx=10, pady=10, width=15)
delete_button.grid(row=2, column=1, padx=5, pady=5)
exit_button = Button(btn_frm, text="Exit", command=exit_app, padx=10, pady=10, width=15)
exit_button.grid(row=3, column=0, padx=5, pady=5)

window.mainloop()
