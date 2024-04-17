import tkinter as tk

def button_click(symbol):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + symbol)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def clear():
    entry.delete(0, tk.END)

def convert():
    current = entry.get()
    try:
        number = float(current)
        entry.delete(0, tk.END)
        if number >= 0:
            entry.insert(tk.END, "-" + str(number))
        else:
            entry.insert(tk.END, str(abs(number)))
    except ValueError:
        pass

def delete_last():
    current = entry.get()
    if current:
        entry.delete(len(current) - 1)

def calculate_inverse():
    try:
        value = float(entry.get())
        if value != 0:
            inverse = 1 / value
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(inverse))
        else:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error: Division by zero")
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error: Invalid input")


def calculate_power():
    try:
        value = float(entry.get())
        power = 2
        result = value ** power
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error: Invalid input")

def calculate_square_root():
    try:
        value = float(entry.get())
        square_root = value ** 0.5
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(square_root))
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error: Invalid input")

def calculate_percentage():
    try:
        value = float(entry.get())
        percentage = value / 100
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(percentage))
    except ValueError:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error: Invalid input")

# Crearea ferestrei principale
root = tk.Tk()
root.title("Calculator")

root.geometry("300x400")  # Setează dimensiunile ferestrei la 400x300 pixeli
#root.minsize(300, 200)  # Stabilește dimensiunile minime ale ferestrei la 300x200 pixeli
#root.maxsize(400, 500)  # Stabilește dimensiunile maxime ale ferestrei la 800x600 pixeli

root.configure(bg="AntiqueWhite3")

# Crearea câmpului de intrare pentru afișarea și introducerea cifrelor și operatorilor
entry = tk.Entry(root, width=30, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


# Definirea butoanelor
buttons = [
    ("Mod", 1, 0), ("%", 1, 1), ("C", 1, 2), ("Del", 1, 3),
    ("1/x ", 2, 0), (" ^2", 2, 1), (" √ ", 2, 2), ("/", 2, 3),
    ("7", 3, 0), ("8", 3, 1), ("9", 3, 2), ("*", 3, 3),
    ("4", 4, 0), ("5", 4, 1), ("6", 4, 2), ("-", 4, 3),
    ("1", 5, 0), ("2", 5, 1), ("3", 5, 2), ("+", 5, 3),
    ("+/-", 6,0), ("0", 6, 1), (".", 6, 2), ("=", 6, 3)
]

# Adăugarea butoanelor în fereastră
for (text, row, column) in buttons:
    if text == "C":
        button = tk.Button(root, text=text, padx=20, pady=10, command=clear, bg="seashell2")
    elif text == "+/-":
        button = tk.Button(root, text=text, padx=20, pady=10, command=convert, bg="seashell2")
    elif text == "Del":
        button = tk.Button(root, text=text, padx=20, pady=10, command=delete_last, bg="seashell2")
    elif text == "1/x":
        button = tk.Button(root, text=text, padx=20, pady=10, command=calculate_inverse, bg="seashell2")
    elif text == "^2":
        button = tk.Button(root, text=text, padx=20, pady=10, command=calculate_power, bg="seashell2")
    elif text == "√":
        button = tk.Button(root, text=text, padx=20, pady=10, command=calculate_square_root, bg="seashell2")
    elif text == "=":
        button = tk.Button(root, text=text, padx=20, pady=10, command=calculate, bg="seashell2")
    elif text == "%":
        button = tk.Button(root, text=text, padx=20, pady=10, command=calculate_percentage, bg="seashell2")
   # elif text == "Mod":
    #    button = tk.Button(root, text=text, padx=20, pady=10, command=toggle_mode, bg="seashell2")
    else:
        button = tk.Button(root, text=text, padx=20, pady=10, command=lambda t=text: button_click(t), bg="seashell2")
    button.grid(row=row, column=column, padx=0, pady=0)


for (text, row, column) in buttons:
    if text == "C":
        button = tk.Button(root, text=text, padx=20, pady=10, command=clear, bg="seashell2")
    # Restul codului pentru celelalte butoane...
    
    # Adăugarea unui stil comun pentru toate butoanele
    button.grid(row=row, column=column, padx=0, pady=0, sticky="nsew")  # Folosește argumentul sticky pentru a fixa butoanele la marginile celulelor
    root.grid_rowconfigure(row, weight=1)  # Permite ca rândurile să se extindă uniform
    root.grid_columnconfigure(column, weight=1)  # Permite ca coloanele să se extindă uniform


root.mainloop()
