import tkinter as tk
from tkinter import ttk
import aoc202301


root = tk.Tk()
root.title("Interface")
root.geometry("265x75+200+300")
root.resizable(False, False)

button_1 = tk.Button(root, text="AOC2023 01", command=aoc202301.problem.run)
button_1.place(x=5, y=5, height=30, width=90)

root.mainloop()
