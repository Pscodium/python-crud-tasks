import tkinter as tk
from tkinter import *
from turtle import update

white = '#ffffff'
black = '#000000'
entry = '#838383'
color = '#C1FCFF'
color1 = '#C9FFC2'
color2 = '#FFCFC2'
color3 = '#EDCFFF'




window = tk.Tk()
window.geometry('600x300')
window.title('Tarefas')
window.resizable(False, False)
window.configure(bg=white)


create = Button(window, text='Novo', activebackground=color1, command=create, bg=color1, fg=entry, cursor='hand2', border=0, highlightbackground=color1, activeforeground=black)
create.place(x=10, y=10)

update = Button(window, text='Atualizar', activebackground=color3, command='', bg=color3, fg=entry, cursor='hand2', border=0, highlightbackground=color3, activeforeground=black)
update.place(x=78, y=10)

delete = Button(window, text='Remover', activebackground=color2, command='', bg=color2, fg=entry, cursor='hand2', border=0, highlightbackground=color2, activeforeground=black)
delete.place(x=170, y=10)







window.mainloop()