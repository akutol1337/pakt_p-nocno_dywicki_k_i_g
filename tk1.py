import tkinter as tk
#import frameworku

root = tk.Tk()
#podanie nazwy okna
root.title("esza")
#zmienienie nazwy okna
root.geometry("300x400")
#skaloanie okna
root.resizable(False, False)
#wymyszenie nie skalowania na uzytk



tekst1 = tk.StringVar(root, "Elo")
#tekst potrzebny do pozniejszego edytowania

label1 = tk.Label(root, textvariable=tekst1, font="none 16 bold")
#wziecie tekstu1 i zmienienie jego trzcionki
label1.grid(row=0,column=0)
#ustawienie nowego tekstu
label2 = tk.Label(root, textvariable=tekst1, bg="black", fg="white")
label2.grid(row=3, column=2)

root.mainloop()
