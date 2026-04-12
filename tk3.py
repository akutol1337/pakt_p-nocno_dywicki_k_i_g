import tkinter as tk
class Api:
    def __init__(self, root):
     
        self.tekst1 = tk.StringVar(root, "Imię")
        self.label1 = tk.Label(root, textvariable=self.tekst1, bg="#ff00ff", fg="#FFFFFF", font="none 16 bold")
        self.label1.grid(row=2, column=2)
        self.b1 = tk.Button(root, text="zmien", command=self.zmien_napis, bg="red")
        self.b1.grid(row=2, column=3)

        self.tekst2 = tk.StringVar(root, "Nazwisko")
        self.label2 = tk.Label(root, textvariable=self.tekst2, bg="Yellow", fg="black", font=("italic", 12),)
        self.label2.grid(row=4, column=4)
        self.b2 = tk.Button(root, text="zmien", command= self.zmien_napis_2, bg="blue")
        self.b2.grid(row=4, column=5)

    def zmien_napis(self):
        self.tekst1.set("Grzegorz")

    def zmien_napis_2(self):
        self.tekst2.set("Akutowicz")

    


root = tk.Tk()
root.title("Zseit")
root.geometry("200x200")
root.configure(bg="lightblue")

app = Api(root)

root.mainloop()
