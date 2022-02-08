import tkinter as tk
from tkinter import *
from tkinter import ttk
import datab


white = '#ffffff'
black = '#000000'
entry = '#838383'
color = '#C1FCFF'
color1 = '#C9FFC2'
color2 = '#FFCFC2'
color3 = '#EDCFFF'


class App:
    def __init__(self):

        self.window = tk.Tk()
        self.window.geometry('600x300')
        self.window.title('Tarefas')
        self.window.resizable(False, False)
        self.window.configure(bg=white)

        def fill():
            app.delete(*app.get_children())
            vcon = datab.ConnectDB()
            query = "SELECT task FROM tasks ORDER BY id"
            lista = datab.fill(vcon, query)
            for i in lista:
                    app.insert("","end",values=i)


        def create():
            def insert():
                tarefa = task_entry.get()
                data = day_combo.get()+'-'+month_combo.get()+'-'+year_combo.get()
                descricao = description.get("1.0","end")
                vcon = datab.ConnectDB()
                query = "INSERT INTO tasks (task, date, description) VALUES ('"+tarefa+"','"+data+"','"+descricao+"')"
                datab.insert(vcon, query)
                task_entry.delete(0, END)
                day_combo.delete(0, END)
                month_combo.delete(0, END)
                year_combo.delete(0, END)
                description.delete("1.0", "end")
                fill()

            ## FRAME DE CRIAÇÃO DE TAREFA
            create_frame = Frame(self.window, width=300, height=244, bg=color1)
            create_frame.place(x=10, y=40)

            days = []
            months = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
            year = []

            for i in range(1, 32):
                days.append(i)

            for i in range(1990, 2026):
                year.append(i)
            year.reverse()


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

            ## LABEL DE DESCRIÇÃO COM TEXT
            description_label = Label(create_frame, text='Descrição', bg=color1, fg=black)
            description_label.place(x=10, y=110)

            description = Text(create_frame, bg=white, fg=black, width=34, height=4)
            description.place(x=10, y=130)

            ## BOTÃO SE INSERÇÃO DE TAREFA
            insert_button = Button(create_frame, text='Enviar', command=insert, width=10, height=1, bg=color3, fg=black, highlightbackground=color3, highlightcolor=color3, border=0, activebackground=color3, cursor='hand2', activeforeground=white)
            insert_button.place(x=10, y=200)


        def update():

            def up_db():
                selection = app.selection()[0]
                valores=app.item(selection, "values")
                item = valores[0]

                tarefa = task_entry.get()
                data = day_combo.get()+'-'+month_combo.get()+'-'+year_combo.get()
                descricao = description.get("1.0","end")
                
                vcon = datab.ConnectDB()
                query = "UPDATE tasks SET task='"+tarefa+"', date='"+data+"', description='"+descricao+"' WHERE task='"+item+"'"
                datab.insert(vcon, query)
                task_entry.delete(0, END)
                day_combo.delete(0, END)
                month_combo.delete(0, END)
                year_combo.delete(0, END)
                description.delete("1.0", "end")
                fill()
                

            ## FRAME DE ATUALIZAÇÃO DE TAREFA
            create_frame = Frame(self.window, width=300, height=244, bg=color3)
            create_frame.place(x=10, y=40)

            days = []
            months = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
            year = []

            for i in range(1, 32):
                days.append(i)

            for i in range(1990, 2026):
                year.append(i)
            year.reverse()

            ## LABEL DE TAREFA COM ENTRY
            task_label = Label(create_frame, text='Tarefa', bg=color3, fg=black)
            task_label.place(x=10, y=10)

            task_entry = Entry(create_frame, text='Tarefa', bg=white, fg=black)
            task_entry.place(x=10, y=30)

            ## LABEL DE DATA COM COMBOBOX
            date_label = Label(create_frame, text='Data', bg=color3, fg=black)
            date_label.place(x=10, y=60)

            day_combo = ttk.Combobox(create_frame, values=days, width=3)
            day_combo.place(x=10, y=80)

            month_combo = ttk.Combobox(create_frame, values=months, width=5)
            month_combo.place(x=55, y=80)

            year_combo = ttk.Combobox(create_frame, values=year, width=5)
            year_combo.place(x=117, y=80)

            ## LABEL DE DESCRIÇÃO COM TEXT
            description_label = Label(create_frame, text='Descrição', bg=color3, fg=black)
            description_label.place(x=10, y=110)

            description = Text(create_frame, bg=white, fg=black, width=34, height=4)
            description.place(x=10, y=130)     

            ## BOTÃO SE INSERÇÃO DE TAREFA
            insert_button = Button(create_frame, text='Enviar', command=up_db, width=10, height=1, bg=color1, fg=black, highlightbackground=color1, highlightcolor=color1, border=0, activebackground=color1, cursor='hand2', activeforeground=white)
            insert_button.place(x=10, y=200)

        def delete():
            selection = app.selection()[0]
            valores=app.item(selection, "values")
            task = valores[0]
            vcon = datab.ConnectDB()
            query = "DELETE FROM tasks WHERE task='"+task+"'"
            datab.remove(vcon, query)
            fill()



        create = Button(self.window, text='Novo', activebackground=color1, command=create, bg=color1, fg=entry, cursor='hand2', border=0, highlightbackground=color1, activeforeground=black)
        create.place(x=10, y=10)

        update = Button(self.window, text='Atualizar', activebackground=color3, command=update, bg=color3, fg=entry, cursor='hand2', border=0, highlightbackground=color3, activeforeground=black)
        update.place(x=78, y=10)

        delete = Button(self.window, text='Remover', activebackground=color2, command=delete, bg=color2, fg=entry, cursor='hand2', border=0, highlightbackground=color2, activeforeground=black)
        delete.place(x=170, y=10)



        app = ttk.Treeview(self.window ,columns=('tarefas'), show='headings')
        app.column('tarefas', minwidth=0, width=250)
        app.heading('tarefas', text='TAREFAS')
        app.place(x=330, y=40)



        fill()
        self.window.mainloop()
app = App()
