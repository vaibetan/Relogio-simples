#relogio

import time
import tkinter
import locale

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

root = tkinter.Tk()
root.geometry('500x300')
root.config(background='black')
def relogio():
    data = time.strftime('%H:%M:%S')
    tempo.config(text=data, font=('circular', 56), bg='black', fg='purple')
    tempo.after(1, relogio )

def data():
    dia = time.strftime('%A, %B, %Y')
    Day.config(text=dia,font=('circular', 16), bg='black', fg='purple')

Day = tkinter.Label(root)
Day.pack(pady=0)    
tempo = tkinter.Label(root)
tempo.pack(pady= 100)


data()
relogio()
root.mainloop()