from tkinter import *

def potwierdzenie() :
    print("Zapisane:")
    print(pole3.get())
    print(pole4.get())
    exit()

okno = Tk()
okno.title("Formularz do zaliczenia")
etykieta3 = Label(okno, text="Telefon")
etykieta3.grid(column = 0, row = 2, sticky="n")
pole3 = Entry(okno)
pole3.grid(column = 1, row = 2, sticky="n")
etykieta4 = Label(okno, text="Email")
etykieta4.grid(column = 0, row = 3, sticky="n")
pole4 = Entry(okno)
pole4.grid(column = 1, row = 3, sticky="n")

zapis = Button(okno, text="Zapisz", command = potwierdzenie)
zapis.grid(sticky="s")
okno.mainloop()
