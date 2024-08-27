from tkinter import *
import tkinter as tk

root = tk.Tk()
root.geometry('665x385')
root.overrideredirect(True)
root.wm_attributes("-transparentcolor", "grey")

def move_app(e):
    root.geometry(f'+{e.x_root}+{e.y_root}')

def exit_click():
    root.quit()

frame_photo = PhotoImage(file='../AboutFrm.png')
frame_label = Label(root, border=0, bg='grey', image=frame_photo)
frame_label.pack(fill=BOTH, expand=True)
frame_label.bind("<B1-Motion>", move_app)

exit_photo = PhotoImage(file='../UntitledExit.png')
exit_label = Label(root, image=exit_photo, border=0, highlightthickness=0, bg='Gray85')
exit_label.place(x=593.7, y=7)
exit_label.bind("<Button>", lambda e: exit_click())


root.resizable(False, False)


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate the position to center the window
window_width = 670  # Set your window width
window_height = 390  # Set your window height
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2

# Set window position
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

root.mainloop()