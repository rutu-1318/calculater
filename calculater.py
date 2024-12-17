import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen_var.set(result)
        except Exception as e:
            screen_var.set("Error")
    elif text == "C":
        screen_var.set("")
    else:
        screen_var.set(screen_var.get() + text)

root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")

screen_var = tk.StringVar()
screen_var.set("")

screen = tk.Entry(root, textvar=screen_var, font="lucida 20 bold", borderwidth=10, relief=tk.RIDGE)
screen.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    '7', '8', '9', '+',
    '4', '5', '6', '-',
    '1', '2', '3', '*',
    'C', '0', '=', '/',
]

button_colors = {
    '0': 'white', '1': 'white', '2': 'white', '3': 'white',
    '4': 'white', '5': 'white', '6': 'white', '7': 'white',
    '8': 'white', '9': 'white', '+': 'white', '-': 'white',
    '*': 'white', '/': 'white', '=': 'white', 'C': 'red'
}

button_shapes = {
    '0': "circle", '1': "circle", '2': "circle", '3': "circle",
    '4': "circle", '5': "circle", '6': "circle", '7': "circle",
    '8': "circle", '9': "circle", '+': "rect", '-': "rect",
    '*': "rect", '/': "rect", '=': "rect", 'C': "rect"
}

row, col = 0, 0
for button in buttons:
    color = button_colors[button]
    shape = button_shapes[button]
    if shape == "circle":
        btn = tk.Button(button_frame, text=button, font="lucida 15 bold", bg=color, width=6, height=3, relief=tk.GROOVE, borderwidth=5)
    else:
        btn = tk.Button(button_frame, text=button, font="lucida 15 bold", bg=color, width=6, height=3, relief=tk.RAISED, borderwidth=5)
    btn.grid(row=row, column=col, padx=10, pady=10)
    btn.bind("<Button-1>", click)
    col += 1
    if col == 4:
        col = 0
        row += 1

root.mainloop()