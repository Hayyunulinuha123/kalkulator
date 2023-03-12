from tkinter import *
import tkinter.font as font
import math

root = Tk()
root.title("CALCULATOR")
root.config(bg="darkgrey")
root.geometry("360x445")

myfont = font.Font(size=15)

e = Entry(root, width=30, borderwidth=2, fg="black", bg="black")
e["font"] = myfont
e["bg"] = "#d1d1d1"
e.grid(row=0, columnspan=5, padx=10, pady=10)


def cetak(nilai):
    nilai1 = e.get()
    e.delete(0, END)
    e.insert(0, str(nilai1) + str(nilai))


def tambah():
    nomor_awal = e.get()
    global n_awal
    global mtk
    mtk = "penjumlahan"
    n_awal = int(nomor_awal)
    e.delete(0, END)


def kurang():
    nomor_awal = e.get()
    global n_awal
    global mtk
    mtk = "pengurangan"
    n_awal = int(nomor_awal)
    e.delete(0, END)


def bagi():
    nomor_awal = e.get()
    global n_awal
    global mtk
    mtk = "pembagian"
    n_awal = int(nomor_awal)
    e.delete(0, END)


def kali():
    nomor_awal = e.get()
    global n_awal
    global mtk
    mtk = "perkalian"
    n_awal = int(nomor_awal)
    e.delete(0, END)


def sisabagi():
    nomor_awal = e.get()
    global n_awal
    global mtk
    mtk = "sisabagi"
    n_awal = int(nomor_awal)
    e.delete(0, END)


def pangkat():
    nomor_awal = e.get()
    global n_awal
    n_awal = int(nomor_awal)
    e.delete(0, END)
    e.insert(0, n_awal ** 2)


def akar():
    nomor_awal = e.get()
    global n_awal
    n_awal = int(nomor_awal)
    e.delete(0, END)
    e.insert(0, math.sqrt(n_awal))


def fact():
    nomor_awal = e.get()
    global n_awal
    n_awal = int(nomor_awal)
    e.delete(0, END)
    e.insert(0, math.factorial(n_awal))


def eks():
    nomor_awal = e.get()
    global n_awal
    n_awal = int(nomor_awal)
    e.delete(0, END)
    if n_awal == "":
        e.insert(0, math.e(n_awal))
    else:
        e.insert(0, math.e ** (n_awal))


def hapus():
    nomor_awal = e.get()
    length = len(nomor_awal) - 1
    e.delete(length, END)


def reset():
    e.delete(0, END)


def hasil():
    nomor_akhir = int(e.get())
    e.delete(0, END)
    if mtk == "penjumlahan":
        e.insert(0, n_awal + int(nomor_akhir))
    elif mtk == "pengurangan":
        e.insert(0, n_awal - int(nomor_akhir))
    elif mtk == "pembagian":
        try:
            hitung = n_awal / int(nomor_akhir)
            e.insert(0, hitung)
        except ZeroDivisionError:
            e.insert(0, "Math Error")

    elif mtk == "perkalian":
        e.insert(0, n_awal * int(nomor_akhir))
    elif mtk == "sisabagi":
        e.insert(0, n_awal % int(nomor_akhir))


angka0 = Button(root, text="0", padx=34, bg="#FFFFFF", fg="black", pady=20, command=lambda: cetak(0))
angka1 = Button(root, text="1", padx=34, bg="#FFFFFF", fg="black", pady=20, command=lambda: cetak(1))
angka2 = Button(root, text="2", padx=34, bg="#FFFFFF", fg="black", pady=20, command=lambda: cetak(2))
angka3 = Button(root, text="3", padx=34, bg="#FFFFFF", fg="black", pady=20, command=lambda: cetak(3))
angka4 = Button(root, text="4", padx=34, bg="#FFFFFF", fg="black", pady=20, command=lambda: cetak(4))
angka5 = Button(root, text="5", padx=34, bg="#FFFFFF", fg="black", pady=20, command=lambda: cetak(5))
angka6 = Button(root, text="6", padx=34, bg="#FFFFFF", fg="black", pady=20, command=lambda: cetak(6))
angka7 = Button(root, text="7", padx=34, bg="#FFFFFF", fg="black", pady=20, command=lambda: cetak(7))
angka8 = Button(root, text="8", padx=34, bg="#FFFFFF", fg="black", pady=20, command=lambda: cetak(8))
angka9 = Button(root, text="9", padx=34, bg="#FFFFFF", fg="black", pady=20, command=lambda: cetak(9))
tambah = Button(root, text="+", padx=31, bg="#878787", fg="white", pady=20, command=tambah)
kurang = Button(root, text="-", padx=33, bg="#878787", fg="white", pady=20, command=kurang)
bagi = Button(root, text="/", padx=32, bg="#878787", fg="white", pady=20, command=bagi)
kali = Button(root, text="x", padx=32, bg="#878787", fg="white", pady=20, command=kali)
pangkat = Button(root, text="^2", padx=30, bg="#878787", fg="white", pady=20, command=pangkat)
akar = Button(root, text="√", padx=34, bg="#878787", fg="white", pady=20, command=akar)
hapus = Button(root, text="DEL", padx=70, bg="#878787", fg="red", pady=20, command=hapus)
sisabagi = Button(root, text="%", padx=32, bg="#878787", fg="white", pady=20, command=sisabagi)
reset = Button(root, text="AC", padx=33, bg="#878787", fg="red", pady=20, command=reset)
hasil = Button(root, text="=", padx=75, bg="orange", fg="black", pady=20, command=hasil)
fact = Button(root, text="x!", padx=32, bg="#878787", fg="white", pady=20, command=fact)
eks = Button(root, text="e", padx=32, bg="#878787", fg="white", pady=20, command=eks)

angka0.grid(row=5, column=2)
angka1.grid(row=4, column=1)
angka2.grid(row=4, column=2)
angka3.grid(row=4, column=3)
angka4.grid(row=3, column=1)
angka5.grid(row=3, column=2)
angka6.grid(row=3, column=3)
angka7.grid(row=2, column=1)
angka8.grid(row=2, column=2)
angka9.grid(row=2, column=3)

bagi.grid(row=2, column=4)
kali.grid(row=3, column=4)
tambah.grid(row=4, column=4)
kurang.grid(row=5, column=4)
reset.grid(row=5, column=3)
hasil.grid(row=6, column=3, columnspan=2)
pangkat.grid(row=1, column=1)
akar.grid(row=1, column=2)
sisabagi.grid(row=5, column=1)
hapus.grid(row=6, column=1, columnspan=2)
fact.grid(row=1, column=3)
eks.grid(row=1, column=4)

root.mainloop()
