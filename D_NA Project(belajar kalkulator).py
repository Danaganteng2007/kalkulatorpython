from tkinter import*
import tkinter.font as font
import math

root = Tk()
root.title("belajar frame")
root["bg"] = "#d1d1d1"
root.geometry("310x400")

myfont  = font.Font(size=15)

e = Entry (root,width=25,borderwidth=0)
e ["font"] = myfont
e ["bg"] = "#d1d1d1" 
e.grid (row=0,column=0,columnspan=4,padx=20,pady=20,)

#fungsi angka 
def angka(nilai):
    sebelum = e.get()
    e.delete(0,END)
    e.insert(0,str(sebelum)+str(nilai))
    

#fungsi tambah kali bagi kurang samadengan dan hapus 
def tambah():
    nomber_awal = e.get()
    global n_awal
    global mtk
    mtk = "penjumlahan"
    n_awal = int(nomber_awal)
    e.delete(0,END)

def kurang():
    nomber_awal = e.get()
    global n_awal
    global mtk
    mtk = "pengurangan"
    n_awal = int(nomber_awal)
    e.delete(0,END)

def bagi():
    nomber_awal = e.get()
    global n_awal
    global mtk
    mtk = "pembagian"
    n_awal = int(nomber_awal)
    e.delete(0,END)

def kali():
    nomber_awal = e.get()
    global n_awal
    global mtk
    mtk = "perkalian"
    n_awal = int(nomber_awal)
    e.delete(0,END)

def akar():
    nomber_awal = e.get()
    global n_awal
    n_awal = int(nomber_awal)
    e.delete(0,END)
    e.insert(0,math.sqrt(n_awal))

def pangkat():
    nomber_awal = e.get()
    global n_awal
    n_awal = int(nomber_awal)
    e.delete(0,END)
    e.insert(0,n_awal **2)

def sisabagi():
    nomber_awal = e.get()
    global n_awal
    global mtk
    mtk = "sisabagi"
    n_awal = int(nomber_awal)
    e.delete(0,END)

def hapus():
    e.delete(0,END)

def samadengan():
    nomber_akhir = e.get()
    e.delete(0,END)
    if mtk == "penjumlahan":
        e.insert(0,n_awal + int(nomber_akhir))
    elif mtk == "pengurangan":
        e.insert(0,n_awal - int(nomber_akhir))
    elif mtk == "perkalian":
        e.insert(0,n_awal * int(nomber_akhir))
    elif mtk == "pembagian":
        try :
            hitung = n_awal / int(nomber_akhir)
            e.insert(0,hitung)
        except ZeroDivisionError:
            e.insert(0,'laptop mu kentang')
    elif mtk == "sisabagi":
        e.insert(0,n_awal % int(nomber_akhir))

def dana():
    e.delete(0,END)
    e.insert(0,'D_NA PROJECT')



#ukuran tombol

btn1 = Button(root,text="1",padx=30,bg="#9BA4B5",pady=20,command=lambda:angka(1))
btn2 = Button(root,text="2",padx=30,bg="#9BA4B5",pady=20,command=lambda:angka(2))
btn3 = Button(root,text="3",padx=30,bg="#9BA4B5",pady=20,command=lambda:angka(3))
btn4 = Button(root,text="4",padx=30,bg="#9BA4B5",pady=20,command=lambda:angka(4))
btn5 = Button(root,text="5",padx=30,bg="#9BA4B5",pady=20,command=lambda:angka(5))
btn6 = Button(root,text="6",padx=30,bg="#9BA4B5",pady=20,command=lambda:angka(6))
btn7 = Button(root,text="7",padx=30,bg="#9BA4B5",pady=20,command=lambda:angka(7))
btn8 = Button(root,text="8",padx=30,bg="#9BA4B5",pady=20,command=lambda:angka(8))
btn9 = Button(root,text="9",padx=30,bg="#9BA4B5",pady=20,command=lambda:angka(9))
btn0 = Button(root,text="0",padx=30,bg="#9BA4B5",pady=20,command=lambda:angka(0))

#ukuran tombon selain angka 

tam = Button(root,text="+",padx=30,bg="#FEFBF6",pady=20,command=tambah)
kur = Button(root,text="-",padx=30,bg="#FEFBF6",pady=20,command=kurang)
bag = Button(root,text="÷",padx=30,bg="#FEFBF6",pady=20,command=bagi)
kal = Button(root,text="x",padx=30,bg="#FEFBF6",pady=20,command=kali)
akr = Button(root,text="√",padx=30,bg="#FEFBF6",pady=20,command=akar)
sis = Button(root,text="sb",padx=27,bg="#FEFBF6",pady=20,command=sisabagi)
pang = Button(root,text="x²",padx=30,bg="#FEFBF6",pady=20,command=pangkat)
hap = Button(root,text="C",padx=30,bg="#FEFBF6",pady=20,command=hapus)
sama = Button(root,text="=",padx=30,bg="#2F58CD",pady=20,command=samadengan)
dn = Button(root,text="D_NA",padx=19,bg="#2F58CD",pady=20,command=dana)


#tata letak tombol angka 

btn1.grid(row=3,column=0,pady=2)
btn2.grid(row=3,column=1,pady=2)
btn3.grid(row=3,column=2,pady=2)
btn4.grid(row=2,column=0,pady=2)
btn5.grid(row=2,column=1,pady=2)
btn6.grid(row=2,column=2,pady=2)
btn7.grid(row=1,column=0,pady=2)
btn8.grid(row=1,column=1,pady=2)
btn9.grid(row=1,column=2,pady=2)
btn0.grid(row=4,column=1,pady=2)

#tata letak tombol selain angka 

tam.grid(row=4,column=3,pady=2)
kur.grid(row=3,column=3,pady=2)
bag.grid(row=1,column=3,pady=2)
kal.grid(row=2,column=3,pady=2)
hap.grid(row=4,column=0,pady=2)
sama.grid(row=5,column=2,pady=2)
akr.grid(row=5,column=0,pady=2)
sis.grid(row=4,column=2,pady=2)
pang.grid(row=5,column=1,pady=2)
dn.grid(row=5,column=3,pady=2)






root.mainloop()









































































































































































