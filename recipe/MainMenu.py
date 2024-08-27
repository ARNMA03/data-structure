import tkinter as tk
# import tkinter.ttk
from tkinter import ttk, messagebox, simpledialog, filedialog
# from PIL import Image, ImageTk
import os
# import shutil
import tkinter.font as tkFont
import sqlite3
from subprocess import call
# from tkinter import *
# from tkinter.ttk import *
# import PIL.Image
# import PIL.ImageTk



class MainMenu:
    def __init__(self, root):
        self.root = root

    def show(self):
        # Create an instance of RecipeManager and call its show method
        recipe_manager = RecipeManager(self.root)
        recipe_manager.create_widgets()

class RecipeManager:
    def __init__(self, root):
        self.root = root
        self.image_frame = tk.Frame(self.root)  # Create a frame to hold the recipe image label
        self.image_frame.place(x=700, y=165)  # Adjust the x position to move it slightly to the right
        self.root.wm_attributes("-transparentcolor", "grey")
        self.root.overrideredirect(False)

        self.recipe_image_label = None  # Initialize recipe image label
        # Connect to SQLite database
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
                                           rating INTEGER
                                           cooking_time TEXT)''')  # Add a column for storing the rating
        self.conn.commit()

        # Create directory to store images if it doesn't exist
        self.IMAGE_DIR = "recipe_images"
        if not os.path.exists(self.IMAGE_DIR):
            os.makedirs(self.IMAGE_DIR)

        self.categories = ["Breakfast", "Lunch", "Dinner", "Snacks"]
        self.category_var = tk.StringVar()
        self.create_widgets()
        self.ingredient_checkbuttons = []
        self.root = root

    def create_widgets(self):
        def move_app(e):
            self.root.geometry(f'+{e.x_root}+{e.y_root}')

        # Load image and set it as background
        frame_photo = tk.PhotoImage(file='../Main Menuframe (1).png')
        frame_label = tk.Label(self.root, border=0, bg='grey', image=frame_photo)
        frame_label.image = frame_photo  # Keep a reference to the image
        frame_label.pack(fill=tk.BOTH, expand=True)
        frame_label.bind("<B1-Motion>", move_app)

        def exit_click():
            self.root.quit()

        exit_photo1 = tk.PhotoImage(file='../Exit 1.png')
        exit_label1 = tk.Label(frame_label, border=0, bg='Gray85', image=exit_photo1)
        exit_label1.image = exit_photo1
        exit_label1.place(x=820, y=9, width=48, height=53)
        exit_label1.bind("<Button>", lambda e: exit_click())

        # Shopping list button
        shop_photo = tk.PhotoImage(file='../shoplist.png')
        shop_label = tk.Label(frame_label, border=0, bg='#B0A9A8', image=shop_photo)
        shop_label.image = shop_photo
        shop_label.place(x=140, y=525, width=133.66, height=36)
        shop_label.bind("<Button>", lambda e: self.open_shopping_list_window())


        # Buttons for each category
        breakfastbtn = tk.PhotoImage(file='../breakfast btn.png')
        breakfastlbl = tk.Label(frame_label, border=0, bg='Gray85', image=breakfastbtn)
        breakfastlbl.image = breakfastbtn
        breakfastlbl.place(x=68, y=87.5, width=167.48, height=49.95)
        breakfastlbl.bind("<Button>", lambda e: self.load_recipes("Breakfast"))

        lunchbtn = tk.PhotoImage(file='../lunch btn.png')
        lunchlbl = tk.Label(frame_label, border=0, bg='Gray85', image=lunchbtn)
        lunchlbl.image = lunchbtn
        lunchlbl.place(x=262.51, y=87, width=167.48, height=49.95)
        lunchlbl.bind("<Button>", lambda e: self.load_recipes("Lunch"))

        dinnerbtn = tk.PhotoImage(file='../dinner btn.png')
        dinnerlbl = tk.Label(frame_label, border=0, bg='Gray85', image=dinnerbtn)
        dinnerlbl.image = dinnerbtn
        dinnerlbl.place(x=456.01, y=88.17, width=167.48, height=49.95)
        dinnerlbl.bind("<Button>", lambda e: self.load_recipes("Dinner"))

        snacksbtn = tk.PhotoImage(file='../snacks btn.png')
        snackslbl = tk.Label(frame_label, border=0, bg='Gray85', image=snacksbtn)
        snackslbl.image = snacksbtn
        snackslbl.place(x=649.52, y=88, width=167.48, height=49.95)
        snackslbl.bind("<Button>", lambda e: self.load_recipes("Snack"))

        # Recipe button
        addbtn = tk.PhotoImage(file='../Add button.png')
        addlbl = tk.Label(frame_label, border=0, bg='#B0A9A8', image=addbtn)
        addlbl.image = addbtn
        addlbl.place(x=35, y=525, width=69, height=36)
        addlbl.bind("<Button>", lambda e: self.add_recipe_popup())

        # Recipe listbox
        self.recipe_listbox = tk.Listbox(frame_label)
        self.recipe_listbox.place(x=283, y=165, width=317, height=274)
        # self.recipe_listbox.bind("<Motion>", self.show_recipe_image)  # Bind the <Motion> event
        # self.recipe_listbox.bind("<Leave>", self.hide_recipe_image)  # Bind the <Leave> event
        self.recipe_listbox.bind("<<ListboxSelect>>", self.on_recipe_select)  # Bind the event here

        # Search bar
        self.search_entry = ttk.Entry(frame_label, width=32)
        self.search_entry.place(x=347, y=533)
        self.search_entry.insert(0, "Search Recipes")
        self.search_entry.bind("<KeyRelease>", self.search_recipes)

        # Dropdown button for sorting by rating
        self.sort_by_rating_var = tk.StringVar()
        self.sort_by_rating_var.set("Sort by Rating")
        self.sort_by_rating_dropdown = ttk.Combobox(frame_label, textvariable=self.sort_by_rating_var,
                                                    values=["Sort by Rating", "Highest to Lowest Rating",
                                                            "Lowest to Highest Rating", "Rice Meals",
                                                            "Pork Meals", "Chicken Meals", "Beef Meals",
                                                            "Fish Meals"])
        self.sort_by_rating_dropdown.place(x=337, y=505, width=222)
        self.sort_by_rating_dropdown.bind("<<ComboboxSelected>>", self.sort_recipes)


    def add_recipe_popup(self):
        call(['python', 'AddRecipe.py'])
    # def show_recipe_image(self, event):
    #     x = event.x
    #     y = event.y
    #     index = self.recipe_listbox.index("@%d,%d" % (x, y))  # Get the index of the item under the cursor
    #     if index:
    #         selected_recipe = self.recipe_listbox.get(index)
    #         self.cur.execute("SELECT image FROM recipes WHERE name=?", (selected_recipe,))
    #         result = self.cur.fetchone()
    #         if result:
    #             image_path = result[0]
    #             if image_path:
    #                 try:
    #                     # Hide the previous image if exists
    #                     for widget in self.image_frame.winfo_children():
    #                         widget.destroy()
    #
    #                     # Lift the image frame to the top
    #                     self.image_frame.lift()
    #
    #                     image = Image.open(image_path)
    #                     image = image.resize((100, 100), Image.LANCZOS)  # Resize the image if necessary
    #                     photo = ImageTk.PhotoImage(image)
    #                     self.recipe_image_label = tk.Label(self.image_frame, image=photo)
    #                     self.recipe_image_label.image = photo
    #                     self.recipe_image_label.pack()  # Use pack to add the image label to the frame
    #                 except Exception as e:
    #                     print("Error loading image:", e)  # Handle any errors during image loading
    #         else:
    #             print("No image found for the selected recipe.")
    #
    # def hide_recipe_image(self, event):
    #     if self.recipe_image_label:
    #         self.recipe_image_label.destroy()

    def open_shopping_list_window(self):
        self.shopping_list_window = tk.Toplevel(self.root)
        self.shopping_list_window.title("Shopping List")
        self.shopping_list_window.configure(bg="#D9D9D9")


        # Recipe selection dropdown
        selected_recipe = tk.StringVar()
        recipe_names = self.get_recipe_names()
        recipe_dropdown = ttk.Combobox(self.shopping_list_window, textvariable=selected_recipe, values=recipe_names,
                                       state="readonly")
        recipe_dropdown.pack(pady=10)

        def save_pdf_wrapper():
            recipe_name = selected_recipe.get()
            self.save_as_pdf(recipe_name)

        recipe_dropdown.bind("<<ComboboxSelected>>", self.populate_ingredients)  # Bind the method to the event

        # Group box for ingredients
        self.ingredients_group = ttk.LabelFrame(self.shopping_list_window, text="Ingredients")
        self.ingredients_group.pack(padx=10, pady=10, fill="both", expand=True)

        # Clear any existing checkboxes
        for widget in self.ingredients_group.winfo_children():
            widget.destroy()

        # Button to save as PDF
        save_pdf_button = tk.Button(self.shopping_list_window, text="Save as PDF", command=save_pdf_wrapper)
        save_pdf_button.pack(pady=10)

    def save_as_pdf(self, recipe_name):
        from reportlab.lib.pagesizes import letter  # Import letter size
        import reportlab.pdfgen.canvas  # Import canvas module

        # Get the content of the shopping list
        shopping_list_content = ""
        for widget in self.ingredients_group.winfo_children():
            if isinstance(widget, tk.Checkbutton) and widget.cget("text"):
                ingredient = widget.cget("text")
                if widget.var.get():  # Check if the checkbox is checked
                    shopping_list_content += f"[x] {ingredient}\n"
                else:
                    shopping_list_content += f"[ ] {ingredient}\n"

        # Ask user for file save location
        file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
        if file_path:
            # Generate the PDF file using ReportLab
            c = reportlab.pdfgen.canvas.Canvas(file_path, pagesize=reportlab.lib.pagesizes.letter)

            # Draw the recipe name
            c.drawString(100, 770, "Shopping List")
            c.drawString(100, 750, f"Recipe: {recipe_name}")
            c.drawString(100, 730, "=" * 20)

            y = 700
            for line in shopping_list_content.split("\n"):
                c.drawString(100, y, line)
                y -= 20
            c.save()
            messagebox.showinfo("Save Successful", "Shopping list saved as PDF successfully.")

    def populate_ingredients(self, event):
        selected_recipe_name = event.widget.get()
        if selected_recipe_name:
            # Clear previous checkboxes
            for widget in self.ingredients_group.winfo_children():
                widget.destroy()

            ingredients = self.get_recipe_ingredients(selected_recipe_name)
            for ingredient in ingredients:
                var = tk.BooleanVar(value=False)  # Initialize as unchecked
                chk = tk.Checkbutton(self.ingredients_group, text=ingredient, variable=var)
                chk.var = var  # Assign the BooleanVar to the Checkbutton
                chk.pack(anchor="w", padx=10)

    def get_recipe_names(self):
        self.cur.execute("SELECT name FROM recipes ORDER BY name ASC")
        return [row[0] for row in self.cur.fetchall()]

    def get_recipe_ingredients(self, recipe_name):
        self.cur.execute("SELECT ingredients FROM recipes WHERE name=?", (recipe_name,))
        result = self.cur.fetchone()
        if result:
            return result[0].split(", ")
        return []

    def sort_recipes(self, event=None):
        selected_option = self.sort_by_rating_var.get()

        if selected_option == "Highest to Lowest Rating":
            self.cur.execute("SELECT * FROM recipes ORDER BY rating DESC")
        elif selected_option == "Lowest to Highest Rating":
            self.cur.execute("SELECT * FROM recipes ORDER BY rating ASC")
        elif selected_option == "Rice Meals":
            self.cur.execute("SELECT * FROM recipes WHERE ingredients LIKE ? ORDER BY name", ('%rice%',))
        elif selected_option == "Pork Meals":
            self.cur.execute("SELECT * FROM recipes WHERE ingredients LIKE ? ORDER BY name", ('%pork%',))
        elif selected_option == "Chicken Meals":
            self.cur.execute("SELECT * FROM recipes WHERE ingredients LIKE ? ORDER BY name", ('%chicken%',))
        elif selected_option == "Beef Meals":
            self.cur.execute("SELECT * FROM recipes WHERE ingredients LIKE ? ORDER BY name", ('%beef%',))
        elif selected_option == "Fish Meals":
            self.cur.execute("SELECT * FROM recipes WHERE ingredients LIKE ? ORDER BY name", ('%fish%',))

        recipes = self.cur.fetchall()
        self.display_recipes(recipes)

    def load_recipes(self, category=None, sort_by=None):
        if category:
            if sort_by:
                self.cur.execute("SELECT * FROM recipes WHERE category=? ORDER BY rating " + sort_by, (category,))
            else:
                self.cur.execute("SELECT * FROM recipes WHERE category=?", (category,))
        else:
            if sort_by:
                self.cur.execute("SELECT * FROM recipes ORDER BY rating " + sort_by)
            else:
                self.cur.execute("SELECT * FROM recipes")
        recipes = self.cur.fetchall()
        self.display_recipes(recipes)

    def display_recipes(self, recipes):
        self.recipe_listbox.delete(0, tk.END)
        for recipe in recipes:
            self.recipe_listbox.insert(tk.END, recipe[1])  # Display recipe name

    def search_recipes(self, event=None):
        search_term = self.search_entry.get().lower()
        if not search_term:  # If search term is empty
            self.recipe_listbox.delete(0, tk.END)  # Clear the listbox
            return
        # Search by recipe names
        self.cur.execute("SELECT * FROM recipes WHERE name LIKE ?", ('%' + search_term + '%',))
        recipes_by_name = self.cur.fetchall()

        # Search by ingredients
        self.cur.execute("SELECT * FROM recipes WHERE ingredients LIKE ?", ('%' + search_term + '%',))
        recipes_by_ingredient = self.cur.fetchall()

        # Combine the results and remove duplicates
        combined_recipes = list(set(recipes_by_name + recipes_by_ingredient))

        self.display_recipes(combined_recipes)

    def on_recipe_select(self, event):
        from PIL import Image, ImageTk
        self.root = root
        self.root.wm_attributes("-transparentcolor", "grey")

        # Close any existing recipe window
        if hasattr(self, 'recipe_window'):
            self.recipe_window.destroy()

        selected_index = self.recipe_listbox.curselection()
        if selected_index:
            selected_recipe = self.recipe_listbox.get(selected_index)
            self.cur.execute("SELECT * FROM recipes WHERE name=?", (selected_recipe,))

            recipe = self.cur.fetchone()
            if recipe:
                # Create a popup window to display recipe information
                self.recipe_window_photo = tk.PhotoImage(file='../View Recipe.png')
                self.recipe_window = tk.Toplevel(self.root, bg="grey")
                self.recipe_window.title(recipe[1])
                self.recipe_window.resizable(False, False)  # Make the window not resizable

                # Set the title to the recipe name
                self.recipe_window.title(recipe[1])
                image_path = "../View Recipe.png"
                recipe_image = tk.PhotoImage(file=image_path)

                # Display the image using a Label widget
                image_label = tk.Label(self.recipe_window, image=recipe_image)
                image_label.image = recipe_image  # Keep a reference to prevent garbage collection
                image_label.pack()

                # Delete button
                delete_photo = tk.PhotoImage(file='../Delete btn.png')
                delete_label = tk.Label(self.recipe_window, image=delete_photo, border=0, bg='#D9D9D9')
                delete_label.image = delete_photo
                delete_label.place(x=233.64, y=825.47, width=88.50, height=36.01)
                delete_label.bind("<Button>", lambda e, recipe_id=recipe[0]: self.delete_recipe(recipe_id))

                # Image
                image_frame = tk.Label(self.recipe_window, text=recipe[1])  # Set text to recipe name
                custom_font = tkFont.Font(family="Archivo", size=12, weight="bold")
                image_frame.place(x=50.92, y=27.73, width=270.89, height=30.78)
                image_frame.config(font=custom_font, fg="#562525", bg='#D9D9D9')

                # Image
                image_frame = tk.Label(self.recipe_window)
                image_frame.place(x=1, y=55.69, width=350, height=300)
                if recipe[5]:  # If image file path exists
                    print('done')
                    try:
                        image = Image.open(recipe[5])
                        image = image.resize((350, 300), Image.LANCZOS)
                        photo = ImageTk.PhotoImage(image)
                        image_label = tk.Label(image_frame, image=photo)
                        image_label.image = photo
                        image_label.pack()
                    except Exception as e:
                        print("Error loading image:", e)  # Handle any errors during image loading
                        tk.Label(image_frame, text="Image loading failed").place(x=80, y=10)
                else:
                    tk.Label(image_frame, text="No image available").place(x=80, y=10)

                # Ingredients
                ingredients_frame = tk.LabelFrame(self.recipe_window)
                ingredients_frame.place(x=19.58, y=417.41, width=308.27, height=112.5)
                custom_font = tkFont.Font(family="Archivo", size=10, weight="bold")
                ingredients = recipe[2].split(", ")  # Split ingredients by comma
                ingredients_listbox = tk.Listbox(ingredients_frame, selectmode=tk.SINGLE, height=5, width=70,
                                                 font=custom_font, fg="#562525")
                ingredients_listbox.pack(fill=tk.BOTH, expand=True)
                for ingredient in ingredients:
                    ingredients_listbox.insert(tk.END, ingredient)

                # Procedure
                procedure_frame = tk.LabelFrame(self.recipe_window)
                procedure_frame.place(x=19.58, y=567.53, width=308.27, height=112.5)
                custom_font = tkFont.Font(family="Archivo", size=10, weight="bold")
                procedure = recipe[3].split("\n")  # Split procedure by new line
                procedure_text = tk.Text(procedure_frame, wrap=tk.WORD, font=custom_font, fg="#562525", height=10)
                procedure_text.pack(fill=tk.BOTH, expand=True)
                for step in procedure:
                    procedure_text.insert(tk.END, step + '\n')

                # Cooking Time
                cooking_time_label = tk.Label(self.recipe_window, text=recipe[7], font=custom_font, fg="#562525", bg='#D9D9D9')
                cooking_time_label.place(x=176.06, y=368.92)

                # Rating
                rating_frame = tk.LabelFrame(self.recipe_window, bd=0, bg='Gray85')
                rating_frame.place(x=33.72, y=761.39)
                rating_frame1 = tk.LabelFrame(self.recipe_window, bd=0, bg='Gray85')
                rating_frame1.place(x=174.28, y=739.04, width=94.71, height=20)

                def rate_recipe(rating):
                    self.rate_recipe(recipe[0], rating)  # Save the rating to the database
                    messagebox.showinfo("Rating", f"You rated this recipe {rating} stars!")
                    # Update the rating display
                    self.current_rating_label.config(text=f"{rating} stars")
                    # Give focus back to the main window
                    self.root.focus_set()

                star_font = tkFont.Font(family="Arial", size=20, weight="bold")
                rate_font = tkFont.Font(family="Archivo", size=12, weight="bold")
                for i in range(1, 6):
                    rating_button = tk.Button(rating_frame, text="\u2605", font=star_font, fg="#FFFF00",
                                              bg='Gray85', bd=0, highlightthickness=0,
                                              command=lambda rating=i: rate_recipe(rating))
                    rating_button.grid(row=0, column=i - 1,
                                       padx=5)  # Use grid instead of place for better alignment

                # Display the recipe's current rating
                self.current_rating_label = tk.Label(rating_frame1, text=f" {recipe[6]} stars", font=rate_font,
                                                     bg='Gray85', fg='#562525')
                self.current_rating_label.place(x=3, y=-6)

                # Exit button
                exit_photo = tk.PhotoImage(file='../Back.png')
                exit_label = tk.Label(self.recipe_window, image=exit_photo, border=0, bg='Gray85')
                exit_label.image = exit_photo
                exit_label.place(x=26.64, y=825.47)
                exit_label.bind("<Button>", lambda e: self.recipe_window.destroy())

    def delete_recipe(self, recipe_id):
        confirm = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this recipe?")
        if confirm:
            self.cur.execute("DELETE FROM recipes WHERE id=?", (recipe_id,))
            self.conn.commit()
            messagebox.showinfo("Recipe Deleted", "Recipe deleted successfully!")
            # Refresh the listbox
            self.load_recipes()  # Assuming this method loads recipes into the listbox
            # Check if recipe_window exists and destroy it
            if hasattr(self, 'recipe_window'):
                self.recipe_window.destroy()

    def rate_recipe(self, recipe_id, rating):
        self.cur.execute("UPDATE recipes SET rating=? WHERE id=?", (rating, recipe_id))
        self.conn.commit()

if __name__ == "__main__":
    root = tk.Tk()
    app = RecipeManager(root)
    root.resizable(False, False)
    root.title("Recipe Manager")

    # Calculate the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate the position to center the window
    window_width = 890  # Set your window width
    window_height = 590  # Set your window height
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    # Set window position
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    root.mainloop()