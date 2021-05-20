from tkinter import *
from math import hypot

janela = Tk()

janela.title('NoThing')
janela.geometry('300x250+430+150')
janela['bg'] = 'Red'

lb1 = Label(janela,text = 'Welcome',bg = 'Red',fg = 'White')
lb1.pack(side = TOP)
lb2 = Label(janela,text = 'Cateto Oposto -> ',bg = 'Red',fg = 'White')
lb2.place(x = 30 , y = 60)
lb3 = Label(janela,text = 'Cateto Adjacente -> ',bg = 'Red',fg = 'White')
lb3.place(x = 30 , y = 90)

camp1 = Entry(janela,text='',bg = 'White',fg = 'Black',width = 20)
camp1.place(x = 150 , y = 60)
camp2 = Entry(janela,text='',bg = 'White',fg = 'Black',width = 20)
camp2.place(x = 150 , y = 90)

def bt_fun ():
    a = float(camp1.get())
    b = float(camp2.get())
    c = hypot(a,b)
    lb4 = Label(janela,text =  "A Hipotenusa é : {:.3f}".format(c),bg = 'White',fg = 'Black')
    lb4.place(x = 110 , y = 170)

btn = Button(janela,text = '_-Verificar-_',bg = 'Black',fg = 'Red',width = '32',command = bt_fun)
btn.place(x = 30 , y = 130)

brd1 = Label(janela,text = '',bg = 'Black',height = 1)
brd1.pack(side = BOTTOM, fill = X)
brd2 = Label(janela,text = '',bg = 'Black',height = 5)
brd1.pack(side = TOP, fill = X)
brd3 = Label(janela,text = '   ',bg = 'Black')
brd3.pack(side = RIGHT, fill = Y)
brd4 = Label(janela,text = '   ',bg = 'Black')
brd4.pack(side = LEFT, fill = Y)


janela.mainloop()