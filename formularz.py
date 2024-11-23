from tkinter import *

def potwierdzenie(a, b) :
    print("Zapisane ", a, " ", b)
    exit()

okno = Tk()
okno.title("Formularz do zaliczenia")
etykieta1 = Label(okno, text="Etykieta")
etykieta1.grid(column=0, row = 0, sticky="n")
pole1 = Entry(okno)
pole1.grid(column = 1, row = 0, sticky="n")
etykieta2 = Label(okno, text="Dworska")
etykieta2.grid(column = 00, row = 1, sticky="n")
pole2 = Entry(okno)
pole2.grid(column = 1, row = 1, sticky="n")
zapis = Button(okno, text="Zapisz", command = lambda:potwierdzenie(pole1.get(), pole2.get()))
zapis.grid(sticky="s")
okno.mainloop()
