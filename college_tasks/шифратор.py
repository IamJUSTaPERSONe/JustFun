import tkinter as tk
from tkinter import *

root = Tk()

def caesar_cipher():
  if message.get() == '' or step.get() == '':
    # messagebox.showwarning(title='error', message='Enter dates')
    info['text'] = 'Enter dates'
  else:
    mess = message.get()
    stp = step.get()

    ciphertext = ""
    for char in mess.upper():
      if char.isalpha():
        ciphertext += chr((ord(char) + int(stp) - 65) % 26 + 65)
    else:
      ciphertext += char
    print(ciphertext)
    info['text'] = ciphertext


root['bg'] = '#008080'
root.geometry('700x400')
root.resizable(width=False, height=False)
root.title('EaD')

fr = Frame(root, bg='#20B2AA')
fr.place(relx=0.05, rely=0.08, relwidth=0.90, relheight=0.85)

title = Label(fr, text="Let's encoding", bg='#20B2AA', font=('Courier', 15))
title.place(x=30)


message = Entry(fr, bg='white', font=('Courier', 10))
message.place(x=25,y=30)
step = Entry(fr, bg='white', font=('Courier', 10))
step.place(x=25,y=60)

btn = Button(fr, text='encoding', bg = '#008080', command=caesar_cipher)
btn.place(x=75, y=90)
info = Label(fr, text='///', bg = '#66CDAA', font=('Courier', 13))
info.place(x=84, y=130)



root.mainloop()
