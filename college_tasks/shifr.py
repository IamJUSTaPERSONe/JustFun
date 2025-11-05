from tkinter import ttk as t
from tkinter import *
from tkinter import messagebox
import base64

"""Шифр цезаря с интерфейсом"""

out = t.Entry()
out.grid()
def ff():
    text = pole1.get()
    sift_text = base64.b64encode(text.encode('utf-8')).decode('utf-8')
    out.delete(0, END)
    out.insert(0,sift_text)
root = Tk()
root.geometry('500x400')

labl = t.Label(root, text = 'Зашифровать')
labl.pack()

pole1 = t.Entry(root)
pole1.pack()
pole2 = t.Entry(root)
pole2.pack()

but = t.Button(root, text = 'Зашифровать', command=ff)
but.pack()



root.mainloop()


# print('шифровка(S) или дешифровка(D)~ ')
# c =  input().upper()

# if c == 'S':
#     alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ'
#     mess = input('Введите сообщение~ ').upper()
#     step = int(input('введите шаг~ '))
#     itog = ''
#     for i in mess:
#         place = alfavit_RU.find(i)
#         new_place = place + step
#         if i in alfavit_RU:
#             itog +=alfavit_RU[new_place]
#         else:
#             itog+=1
#     print(itog.lower())

# else:
#     alfavit_RU1 = 'ЕЁЖЗИЙКЛМНОПРСТУФХЦЧЩШЪЬЫЭЮЯ'
#     mess1 = input('Введите сообщение~ ').upper()
#     step1 = int(input('введите шаг~ '))
#     itog1 = ''
#     for i in mess1:
#         place = alfavit_RU1.find(i)
#         new_place = place - step1
#         if i in alfavit_RU1:
#             itog1 +=alfavit_RU1[new_place]
#         else:
#             itog1+=1

#     print(itog1.lower())
