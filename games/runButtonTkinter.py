import tkinter as tk
import random

"""Бегающая кнопка"""

def move_button(event):
    width = root.winfo_width()
    height = root.winfo_height()

    x = random.randint(0, width - bt.winfo_width())
    y = random.randint(0, height - bt.winfo_height())

    bt.place(x=x, y=y)


root = tk.Tk()
root.title('Try to catch it')
root.geometry('400x400')
root.resizable(False, False)
root['background'] = '#AD66D5'

bt = tk.Button(root, text='Push me if you can)', bg='#48036F', fg='white')
bt.place(x=150, y=150)
bt.bind('<Enter>', move_button)


root.mainloop()
