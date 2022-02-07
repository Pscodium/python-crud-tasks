import tkinter as tk
from tkinter import *
from tkinter import ttk


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

def create():

    days = []
    months = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
    year = []

    for i in range(1, 32):
        days.append(i)

    for i in range(1990, 2026):
        year.append(i)
    year.reverse()


    ## FRAME DE CRIAÇÃO DE TAREFA
    create_frame = Frame(window, width=300, height=220, bg=color1)
    create_frame.place(x=10, y=60)

    ## LABEL DE TAREFA COM ENTRY
    task_label = Label(create_frame, text='Tarefa', bg=color1, fg=black)
    task_label.place(x=10, y=10)

    task_entry = Entry(create_frame, text='Tarefa', bg=white, fg=black)
    task_entry.place(x=10, y=30)

    ## LABEL DE DATA COM COMBOBOX
    date_label = Label(create_frame, text='Data', bg=color1, fg=black)
    date_label.place(x=10, y=60)

    day_combo = ttk.Combobox(create_frame, values=days, width=3)
    day_combo.place(x=10, y=80)

    month_combo = ttk.Combobox(create_frame, values=months, width=5)
    month_combo.place(x=55, y=80)

    year_combo = ttk.Combobox(create_frame, values=year, width=5)
    year_combo.place(x=117, y=80)

    description_label = Label(create_frame, text='Descrição', bg=color1, fg=black)
    description_label.place(x=10, y=110)

    description = Text(create_frame, bg=white, fg=black, width=34, height=4)
    description.place(x=10, y=130)







create = Button(window, text='Novo', activebackground=color1, command=create, bg=color1, fg=entry, cursor='hand2', border=0, highlightbackground=color1, activeforeground=black)
create.place(x=10, y=10)

update = Button(window, text='Atualizar', activebackground=color3, command='', bg=color3, fg=entry, cursor='hand2', border=0, highlightbackground=color3, activeforeground=black)
update.place(x=78, y=10)

delete = Button(window, text='Remover', activebackground=color2, command='', bg=color2, fg=entry, cursor='hand2', border=0, highlightbackground=color2, activeforeground=black)
delete.place(x=170, y=10)







window.mainloop()