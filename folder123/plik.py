import tkinter as tk
from tkinter import ttk, messagebox
import re

root = tk.Tk()
def validate():
    kp = kod_pocztowy_entry.get()
    regex = r"^\d{2}-\d{3}$"
    valcmd = re.match(regex, kp)
    if(kod_pocztowy_entry.get() == ""):
        messagebox.showerror(root, 'Nie wypełniono formularza')
    elif not valcmd:
        messagebox.showerror(root, 'Niepoprawnie wypełniono kod pocztowy')
    else:
        messagebox.showinfo(root, 'Poprawnie wypełniono formularz')

kod_pocztowy = tk.Label(root, text="Podaj kod pocztwoy")
kod_pocztowy.pack()
kod_pocztowy_entry = tk.Entry(root)
kod_pocztowy_entry.pack()
checkbox_label = tk.Label(root, text="To jest checkbox")
checkbox_label.pack()
label_a = tk.Label(root, text='a')
label_a.pack()
checkbox_a = tk.Checkbutton(root)
checkbox_a.pack()
label_b = tk.Label(root, text='b')
label_b.pack()
checkbox_b = tk.Checkbutton(root)
checkbox_b.pack()
submit_label = tk.Label(root, text="To jest przycisk")
submit_label.pack()
submit_button = tk.Button(root, command=validate, text='wyślij')
submit_button.pack()

root.mainloop()