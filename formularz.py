from tkinter import *

def potwierdzenie() :
    print("Zapisane:")
    print(imie.get())
    print(nazwisko.get())
    print(email.get())
    print(adres.get())
    print(stan_cywilny.get())
    print(pole3.get())
    print(pole4.get())
    print(pole9.get())
    exit()

#Wstawiony komentarz 

okno = Tk()
okno.title("Formularz do zaliczenia")
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

etykieta3 = Label(okno, text="Telefon")
etykieta3.grid(column = 0, row = 2, sticky="n")
pole3 = Entry(okno)
pole3.grid(column = 1, row = 2, sticky="n")
etykieta4 = Label(okno, text="Email")
etykieta4.grid(column = 0, row = 3, sticky="n")
pole4 = Entry(okno)
pole4.grid(column = 1, row = 3, sticky="n")
etykieta5 = Label(okno, text="stan cywilny")
etykieta5.grid(column = 0, row = 4, sticky="n")
stan_cywilny = Entry(okno)
stan_cywilny.grid(column = 1, row = 4, sticky="n")
etykieta9 = Label(okno, text="Imię psa")
etykieta9.grid(column = 0, row = 6, sticky="n")
pole9 = Entry(okno)
pole9.grid(column = 1, row = 6, sticky="n")
zapis = Button(okno, text="Zapisz", command = potwierdzenie)
zapis.grid(sticky="s")
okno.mainloop()
