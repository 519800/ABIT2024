from tkinter import *

def potwierdzenie() :
    print("Zapisane:")
    print(pole1.get())
    print(pole2.get())
    print(imie.get())
    print(nazwisko.get())
    print(email.get))
    print(adres.get))
    exit()

#Wstawiony komentarz 

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

etykietaImie = Label(okno, text="Imie")
etykietaImie .grid(column = 00, row = 2, sticky="n")
imie = Entry(okno)
imie.grid(column = 1, row = 3, sticky="n")

etykietaNazwisko = Label(okno, text="Nazwisko")
etykietaNazwisko .grid(column = 00, row = 4, sticky="n")
nazwisko = Entry(okno)
nazwisko.grid(column = 1, row = 5, sticky="n")

etykietaEmail = Label(okno, text="Email")
etykietaEmail .grid(column = 00, row = 6, sticky="n")
email = Entry(okno)
email.grid(column = 1, row = 7, sticky="n")

etykietaAdres = Label(okno, text="Adres")
etykietaAdres .grid(column = 00, row = 8, sticky="n")
adres = Entry(okno)
adres.grid(column = 1, row = 9, sticky="n")


zapis = Button(okno, text="Zapisz", command = potwierdzenie)
zapis.grid(sticky="s")
okno.mainloop()
