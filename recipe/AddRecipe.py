import tkinter as tk
from tkinter import ttk, simpledialog, filedialog, messagebox
from PIL import Image, ImageTk
import os
import shutil
import sqlite3
from PIL import ExifTags  # to rotate image


class AddRecipe:
    def __init__(self, root):
        self.root = root

    def show(self):
        # Create an instance of RecipeApp and call its show method
        recipe_app = RecipeApp(self.root)
        recipe_app.add_recipe_popup()


class RecipeApp:
    def __init__(self, root):
        self.root = root
        self.root.wm_attributes("-transparentcolor", "grey")
        self.root.overrideredirect(False)

        # Initialize categories
        self.categories = ["Breakfast", "Lunch", "Dinner", "Snack"]

        # Initialize database connection
        self.conn = sqlite3.connect("recipes.db")
        self.cur = self.conn.cursor()

        # Create table if not exists
        self.cur.execute('''CREATE TABLE IF NOT EXISTS recipes (
                                          id INTEGER PRIMARY KEY,
                                          name TEXT,
                                          ingredients TEXT,
                                          procedure TEXT,
                                          category TEXT,
                                          image TEXT,
                                          rating INTEGER,
                                          cooking_time TEXT)''')  # Add a column for storing the rating
        self.conn.commit()

        # Initialize image directory
        self.IMAGE_DIR = "recipe_images"
        # Create directory to store images if it doesn't exist
        if not os.path.exists(self.IMAGE_DIR):
            os.makedirs(self.IMAGE_DIR)

    def add_recipe_popup(self):
        def move_app(e):
            self.root.geometry(f'+{e.x_root}+{e.y_root}')

        frame_photo = tk.PhotoImage(file='../Add Recipe.png')
        frame_label = tk.Label(self.root, border=0, bg='grey', image=frame_photo)
        frame_label.image = frame_photo
        frame_label.pack(fill=tk.BOTH, expand=True)
        frame_label.bind("<B1-Motion>", move_app)

        def exit_click():
            self.root.quit()

        exit_photo1 = tk.PhotoImage(file='../Exit 2.png')
        exit_label1 = tk.Label(self.root, border=0, bg='Gray85', image=exit_photo1)
        exit_label1.image = exit_photo1
        exit_label1.place(x=415, y=19, width=47, height=51.18)
        exit_label1.bind("<Button>", lambda e: exit_click())

        # Add Image button
        add_photo1 = tk.PhotoImage(file='../Add Imagebtn.png')
        add_label1 = tk.Label(frame_label, border=0, bg='#8A7979', image=add_photo1)
        add_label1.image = add_photo1
        add_label1.place(x=81, y=200, width=76, height=36)
        add_label1.bind("<Button>", lambda e: self.add_image())

        # Placeholder for the image
        self.recipe_image_label = tk.Label(frame_label)
        self.recipe_image_label.place(x=182, y=113, width=200, height=200)

        self.recipe_name_entry = tk.Entry(frame_label)
        self.recipe_name_entry.place(x=169, y=350, width=229, height=26)

        # Cooking time entry
        self.cooking_time_entry = tk.Entry(frame_label)
        self.cooking_time_entry.place(x=168, y=561.5, width=229, height=23)

        self.ingredients_listbox = tk.Listbox(frame_label)
        self.ingredients_listbox.place(x=168, y=396, height=100.64, width=229)

        # Button to add ingredients
        add_photo2 = tk.PhotoImage(file='../Add Ingredient button.png')
        add_label2 = tk.Label(frame_label, border=0, bg='#8A7979', image=add_photo2)
        add_label2.image = add_photo2
        add_label2.place(x=167, y=508.44, width=106, height=36)
        add_label2.bind("<Button>", lambda e: self.add_ingredient_popup())

        delete_photo = tk.PhotoImage(file='../Delete btn.png')
        self.delete_label = tk.Label(frame_label, border=0, bg='#8A7979', image=delete_photo)
        self.delete_label.image = delete_photo
        self.delete_label.place(x=291, y=508.44, width=89, height=36)
        self.delete_label.bind("<Button>", lambda e: self.delete_ingredient())

        self.procedure_listbox = tk.Listbox(frame_label)
        self.procedure_listbox.place(x=170, y=600, height=151, width=228)

        # Button to add procedure
        add_photo3 = tk.PhotoImage(file='../Add Procedure btn.png')
        add_label3 = tk.Label(frame_label, border=0, bg='#8A7979', image=add_photo3)
        add_label3.image = add_photo3
        add_label3.place(x=235, y=759, width=106, height=36)
        add_label3.bind("<Button>", lambda e: self.add_procedure())

        # radio buttons
        self.selected_category = tk.StringVar(value="None")
        self.radio_buttons = []  # List to hold references to radio buttons
        for i, category in enumerate(self.categories):
            radio_button = tk.Radiobutton(frame_label, text='', variable=self.selected_category, value=category,
                                          highlightthickness=0, bd=0, bg='#B0A9A8', fg="#891616")
            radio_button.place(x=21 + i * 120, y=838)
            self.radio_buttons.append(radio_button)  # Add radio button reference to the list

        add_photo4 = tk.PhotoImage(file='../Add button1.png')
        add_label4 = tk.Label(frame_label, border=0, bg='#B0A9A8', image=add_photo4)
        add_label4.image = add_photo4
        add_label4.place(x=214, y=858, width=66.38, height=29.8)
        add_label4.bind("<Button>", lambda e: self.add_recipe())

        # Bind the listbox selection to enable/disable delete button
        self.ingredients_listbox.bind("<<ListboxSelect>>", self.enable_delete_button)

    def enable_delete_button(self, event):
        selected_index = self.ingredients_listbox.curselection()
        if selected_index:
            self.delete_label.config(state="normal")
        else:
            self.delete_label.config(state="disabled")

    def delete_ingredient(self):
        selected_index = self.ingredients_listbox.curselection()
        if selected_index:
            self.ingredients_listbox.delete(selected_index)

    def add_ingredient_popup(self):
        if getattr(self, 'ingredient_popup', None) is None or not self.ingredient_popup.winfo_exists():
            self.ingredient_popup = tk.Toplevel(self.root)
            self.ingredient_popup.title("Add Ingredient")
            self.ingredient_popup.geometry("290x120")
            self.ingredient_popup.configure(bg="#D9D9D9")

            tk.Label(self.ingredient_popup, text="Ingredient name:", bg="#D9D9D9").grid(row=0, column=0, padx=5, pady=5)
            self.ingredient_name_entry = tk.Entry(self.ingredient_popup)
            self.ingredient_name_entry.grid(row=0, column=1, padx=5, pady=5)

            tk.Label(self.ingredient_popup, text="Quantity:", bg="#D9D9D9").grid(row=1, column=0, padx=5, pady=5)
            self.quantity_var = tk.StringVar()
        quantities = [
            "1/4 cup",
            "1/3 cup",
            "1/2 cup",
            "2/3 cup",
            "3/4 cup",
            "1 cup",
            "1 1/4 cups",
            "1 1/3 cups",
            "1 1/2 cups",
            "1 2/3 cups",
            "1 3/4 cups",
            "2 cups",
            "3 cups",
            "4 cups",
            "1 tbsp",
            "2 tbsp",
            "3 tbsp",
            "4 tbsp",
            "1 1/4 tbsp",
            "1 1/3 tbsp",
            "1 1/2 tbsp",
            "1 2/3 tbsp",
            "1 3/4 tbsp",
            "1/8 cup",
            "1/4 cup",
            "1/3 cup",
            "1/2 cup",
            "2/3 cup",
            "3/4 cup",
            "1 1/4 tsp",
            "1 1/3 tsp",
            "1 1/2 tsp",
            "1 2/3 tsp",
            "1 3/4 tsp",
            "4 tsp",
            "3 tsp",
            "2 tsp",
            "1 tsp",
            "1/2 tsp",
            "1/4 tsp",
            "1/8 tsp",
            "1/16 tsp",
            "1/32 tsp",
            "100 grams",
            "200 grams",
            "250 grams",
            "300 grams",
            "350 grams",
            "400 grams",
            "450 grams",
            "500 grams",
            "550 grams",
            "600 grams",
            "650 grams",
            "700 grams",
            "750 grams",
            "800 grams",
            "850 grams",
            "900 grams",
            "950 grams",
            "1 kilogram",
            "1 1/4 kilograms",
            "1 1/2 kilograms",
            "1 3/4 kilograms",
            "2 kilograms",
            "2 1/4 kilograms",
            "2 1/2 kilograms",
            "2 3/4 kilograms",
            "3 kilograms",
            "3 1/4 kilograms",
            "3 1/2 kilograms",
            "3 3/4 kilograms",
            "4 kilograms",
            "4 1/4 kilograms",
            "4 1/2 kilograms",
            "4 3/4 kilograms",
            "5 kilograms",
            "6 kilograms",
            "7 kilograms",
            "8 kilograms",
            "9 kilograms",
            "10 kilograms",
            "1/2 piece",
            "1 piece",
            "2 pieces",
            "3 pieces",
            "4 pieces",
            "5 pieces",
            "6 pieces",
            "7 pieces",
            "8 pieces",
            "9 pieces",
            "10 pieces",
            "1 slice",
            "2 slices",
            "3 slices",
            "4 slices",
            "5 slices",
            "6 slices",
            "7 slices",
            "8 slices",
            "9 slices",
            "10 slices",
            "1 whole",
            "2 wholes",
            "3 wholes",
            "4 wholes",
            "5 wholes",
            "6 wholes",
            "7 wholes",
            "8 wholes",
            "9 wholes",
            "10 wholes"
        ]
        self.quantity_dropdown = ttk.Combobox(self.ingredient_popup, textvariable=self.quantity_var,
                                              values=quantities,
                                              state="editable")
        self.quantity_dropdown.grid(row=1, column=1, padx=5, pady=5)
        self.quantity_var.set("Choose or type")

        tk.Button(self.ingredient_popup, text="Add Ingredient", command=self.add_ingredient).grid(row=2, column=0,
                                                                                                  columnspan=4, padx=8,
                                                                                                  pady=8)
    def add_ingredient(self):
        ingredient_name = self.ingredient_name_entry.get()
        quantity = self.quantity_var.get()
        if ingredient_name and quantity:
            ingredient_with_quantity = f"{quantity} {ingredient_name}"
            self.ingredients_listbox.insert(tk.END, ingredient_with_quantity)
            self.ingredient_popup.destroy()  # Close the ingredient popup after adding the ingredient
        else:
            messagebox.showerror("Missing Information", "Please enter both ingredient name and quantity.")

    def add_procedure(self):
        self.procedure_popup = tk.Toplevel(self.root)
        self.procedure_popup.title("Add Procedure")
        self.procedure_popup.geometry("400x200")  # Adjust the width and height of the popup window
        self.procedure_popup.configure(bg="#D9D9D9")

        procedure_text = tk.Text(self.procedure_popup, wrap=tk.WORD, height=8)  # Adjust the height of the text area
        procedure_text.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Add scrollbar to the text area
        scrollbar = tk.Scrollbar(self.procedure_popup, command=procedure_text.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        procedure_text.config(yscrollcommand=scrollbar.set)

        tk.Button(self.procedure_popup, text="Add Procedure",
                  command=lambda: self.add_procedure_text(procedure_text)).grid(row=1, column=0, columnspan=2, padx=10,
                                                                                pady=10)

    def add_procedure_text(self, procedure_text):
        procedure = procedure_text.get("1.0", "end-1c").strip()  # Get the procedure text from the text area
        if procedure:
            procedure_number = self.procedure_listbox.size() + 1
            self.procedure_listbox.insert(tk.END, f"{procedure_number}. {procedure}")
            self.procedure_popup.destroy()  # Close the procedure popup window after adding the procedure
        else:
            messagebox.showerror("Missing Information", "Please enter the procedure text.")

    def add_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            # Generate a unique file name
            image_name = os.path.basename(file_path)
            image_name_base, image_ext = os.path.splitext(image_name)
            image_path = os.path.join(self.IMAGE_DIR, image_name)

            # Check if the file already exists, if so, append a unique identifier
            index = 1
            while os.path.exists(image_path):
                new_image_name = f"{image_name_base}_{index}{image_ext}"
                image_path = os.path.join(self.IMAGE_DIR, new_image_name)
                index += 1

            shutil.copyfile(file_path, image_path)
            # Display the selected image in the image box
            self.display_image(image_path)

            # Recreate the buttons after displaying the image
            self.add_buttons()
            self.add_radio_buttons()  # Add this line

    def add_buttons(self):
        def exit_click():
            self.root.quit()

        # Add Image button
        self.recipe_name_entry = tk.Entry(self.root)
        self.recipe_name_entry.place(x=169, y=350, width=229, height=26)

        # Cooking time entry
        self.cooking_time_entry = tk.Entry(self.root)
        self.cooking_time_entry.place(x=168, y=561.5, width=229, height=23)

        self.ingredients_listbox = tk.Listbox(self.root)
        self.ingredients_listbox.place(x=168, y=396, height=100.64, width=229)

        self.procedure_listbox = tk.Listbox(self.root)
        self.procedure_listbox.place(x=170, y=600, height=151, width=228)

        add_photo1 = tk.PhotoImage(file='../Add Imagebtn.png')
        add_label1 = tk.Label(self.root, border=0, bg='#8A7979', image=add_photo1)
        add_label1.image = add_photo1
        add_label1.place(x=81, y=200, width=76, height=36)
        add_label1.bind("<Button>", lambda e: self.add_image())

        # Button to add ingredients
        add_photo2 = tk.PhotoImage(file='../Add Ingredient button.png')
        add_label2 = tk.Label(self.root, border=0, bg='#8A7979', image=add_photo2)
        add_label2.image = add_photo2
        add_label2.place(x=167, y=508.44, width=106, height=36)
        add_label2.bind("<Button>", lambda e: self.add_ingredient_popup())

        delete_photo = tk.PhotoImage(file='../Delete btn.png')
        self.delete_label = tk.Label(self.root, border=0, bg='#8A7979', image=delete_photo)
        self.delete_label.image = delete_photo
        self.delete_label.place(x=291, y=508.44, width=89, height=36)
        self.delete_label.bind("<Button>", lambda e: self.delete_ingredient())

        # Button to add procedure
        add_photo3 = tk.PhotoImage(file='../Add Procedure btn.png')
        add_label3 = tk.Label(self.root, border=0, bg='#8A7979', image=add_photo3)
        add_label3.image = add_photo3
        add_label3.place(x=235, y=759, width=106, height=36)
        add_label3.bind("<Button>", lambda e: self.add_procedure())

        add_photo4 = tk.PhotoImage(file='../Add button1.png')
        add_label4 = tk.Label(self.root, border=0, bg='#B0A9A8', image=add_photo4)
        add_label4.image = add_photo4
        add_label4.place(x=214, y=858, width=66, height=30)
        add_label4.bind("<Button>", lambda e: self.add_recipe())

        exit_photo1 = tk.PhotoImage(file='../Exit 2.png')
        exit_label1 = tk.Label(self.root, border=0, bg='Gray85', image=exit_photo1)
        exit_label1.image = exit_photo1
        exit_label1.place(x=415, y=19, width=47, height=51.18)
        exit_label1.bind("<Button>", lambda e: exit_click())

        # radio buttons
        self.selected_category = tk.StringVar(value="None")
        self.radio_buttons = []  # List to hold references to radio buttons
        for i, category in enumerate(self.categories):
            radio_button = tk.Radiobutton(self.root, text='', variable=self.selected_category, value=category,
                                          highlightthickness=0, bd=0, bg='#B0A9A8', fg="#891616")
            radio_button.place(x=21 + i * 120, y=838)
            self.radio_buttons.append(radio_button)  # Add radio button reference to the list

    def add_radio_buttons(self):
        # Apply individual styling to each radio button
        for i, radio_button in enumerate(self.radio_buttons):
            if i % 2 == 0:
                radio_button.configure(bg='#B0A9A8', fg="#891616")  # Even index buttons
            else:
                radio_button.configure(bg="#B0A9A8", fg="#891616")  # Odd index buttons

    def display_image(self, file_path):
        image = Image.open(file_path)

        # Check if the image has an orientation tag
        if hasattr(image, '_getexif'):
            exif = image._getexif()
            if exif is not None:
                for tag, value in exif.items():
                    if tag in ExifTags.TAGS and ExifTags.TAGS[tag] == 'Orientation':
                        # Rotate the image according to its orientation
                        if value == 3:
                            image = image.rotate(180, expand=True)
                        elif value == 6:
                            image = image.rotate(270, expand=True)
                        elif value == 8:
                            image = image.rotate(90, expand=True)
                        break

        image = image.resize((200, 200), Image.LANCZOS)  # or Image.BICUBIC
        photo = ImageTk.PhotoImage(image)

        # Clear any existing image in the image box
        if hasattr(self, 'recipe_image_label'):
            self.recipe_image_label.destroy()

        # Create a new Label widget to display the image
        self.recipe_image_label = tk.Label(self.root, image=photo)
        self.recipe_image_label.image = photo  # Keep a reference to prevent garbage collection
        self.recipe_image_label.place(x=182, y=113, width=200, height=200)

        # Store the image file path in an attribute
        self.recipe_image_path = file_path

    def add_recipe(self):
        name = self.recipe_name_entry.get()
        ingredients = [self.ingredients_listbox.get(i) for i in range(self.ingredients_listbox.size())]
        procedure = [self.procedure_listbox.get(i) for i in range(self.procedure_listbox.size())]
        category = self.selected_category.get()  # Retrieve the string value of the StringVar
        cooking_time = self.cooking_time_entry.get()
        # Fetch the image file path
        image_path = self.recipe_image_path

        recipe_data = (
            name, ", ".join(ingredients), "\n".join(procedure), category, image_path, 0,
            cooking_time)  # Default rating is 0
        self.cur.execute(
            "INSERT INTO recipes (name, ingredients, procedure, category, image, rating, cooking_time) VALUES (?, ?, ?, ?, ?, ?, ?)",
            recipe_data)
        self.conn.commit()
        messagebox.showinfo("Recipe Added", "Recipe added successfully!")
        self.recipe_name_entry.delete(0, tk.END)
        self.ingredients_listbox.delete(0, tk.END)
        self.procedure_listbox.delete(0, tk.END)
        # Close the root window after adding the recipe
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    root.title ("Add Recipe")
    root.resizable(False, False)
    app = AddRecipe(root)
    app.show()
    root.mainloop()