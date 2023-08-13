import tkinter as tk

def on_button_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(display_var.get())
            display_var.set(result)
        except Exception as e:
            display_var.set("Error")
    elif text == "C":
        display_var.set("")
    else:
        display_var.set(display_var.get() + text)

# Create the main application window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("500x600")
root.resizable(False, False)

# Create a variable to store the user input and result
display_var = tk.StringVar()

# Create the display widget to show user input and result
display = tk.Entry(root, textvariable=display_var, font=("Helvetica", 40), justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

# Define the buttons and their positions
button_texts = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0)
]

# Create buttons and add them to the grid
for btn_text, row, col in button_texts:
    btn = tk.Button(root, text=btn_text, font=("Helvetica", 20), height=2, width=7)
    btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    btn.bind("<Button-1>", on_button_click)

# Make the buttons expand to fill any extra space
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):
    root.grid_columnconfigure(i, weight=1)

root.mainloop()
