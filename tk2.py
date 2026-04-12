import tkinter as tk
root = tk.Tk()

root.geometry("300x400")
root.configure(bg="lightblue")
root.title("3Tpgr1")

icon = tk.PhotoImage(file="BAN.png")
root.iconphoto(True, icon)

tekst1 = tk.StringVar(root, "Imie")
tekst2 = tk.StringVar(root, "Nazwisko")

label1 = tk.Label(root, textvariable=tekst1 , bg="black",fg="white", font="none 16 bold",)
label1.grid(row=1, column=0)
label2 = tk.Label(root, textvariable=tekst2, bg="#00FFFF",fg="yellow", font=("Times New Roman", 16, "italic"))
label2.grid(row=2, column=1)


root.mainloop()
