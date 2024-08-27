from tkinter import *
import tkinter as tk
# from MainMenu import MainMenu
from subprocess import call

root = tk.Tk()
root.geometry('887x586')
root.overrideredirect(False)
root.wm_attributes("-transparentcolor", "grey")


def move_app(e):
    root.geometry(f'+{e.x_root}+{e.y_root}')


def exit_click():
    root.quit()


def start_click():
    root.destroy()
    call(["python", "MainMenu.py"])


def about_click():
    call(["python", "About.py"])


frame_photo = PhotoImage(file='../FrameMain.png')
frame_label = Label(root, border=0, bg='grey', image=frame_photo)
frame_label.pack(fill=BOTH, expand=True)
frame_label.bind("<B1-Motion>", move_app)

exit_photo = PhotoImage(file='../UntitledExit.png')
exit_label = Label(root, image=exit_photo, border=0, bg='Gray85')
exit_label.place(x=810, y=13)
exit_label.bind("<Button>", lambda e: exit_click())

start_photo = PhotoImage(file='../Start.png')
start_label = Label(root, image=start_photo, border=0, bg='Gray85')
start_label.place(x=340, y=367, width=184, height=42)
start_label.bind("<Button>", lambda e: start_click())

about_photo = PhotoImage(file='../About.png')
about_label = Label(root, image=about_photo, border=0, highlightthickness=0)
about_label.place(x=340, y=442, width=184, height=42)
about_label.bind("<Button>", lambda e: about_click())

root.resizable(False, False)
root.title("Recipe Manager")

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
