import tkinter as tk
from tkinter import *
from tkinter import ttk
import datab
from datetime import datetime
from tkinter import messagebox


white = '#ffffff'
black = '#000000'
entry = '#838383'
color = '#C1FCFF'
color1 = '#C9FFC2'
color2 = '#FFCFC2'
color3 = '#EDCFFF'


class Inicial:
    def __init__(self):

        self.window = tk.Tk()
        self.window.geometry('600x300')
        self.window.title('Tarefas')
        self.window.resizable(False, False)
        self.window.configure(bg=white)

        def fill():
            self.app.delete(*self.app.get_children())
            vcon = datab.ConnectDB()
            query = "SELECT task FROM tasks ORDER BY id"
            lista = datab.fill(vcon, query)
            for i in lista:
                    self.app.insert("","end",values=i)


        def create():
            ## FUNÇÃO QUE INSERE ITEM CRIADO DENTRO DO BANCO DE DADOS
            def insert():
                if task_entry.get()=="" or day_combo.get()=="" or year_combo.get()=="" or month_combo.get()=="": 
                    messagebox.showinfo(title="ERRO", message="Digite todos os dados") 
                    return
                ## FUNÇÃO DE DATA DE CRIAÇÃO
                data_hora = datetime.now()
                data_hora_string = data_hora.strftime('%d/%m/%Y %H:%M')
                

                for i in range(12):
                    m = month_combo.get()
                    if self.months[i] == m:
                        self.mesnum = i+1
                        if self.mesnum<10:
                            self.mesnum = '0'+str(self.mesnum)

                tarefa = task_entry.get()
                dia = str(day_combo.get())
                ano = str(year_combo.get())
                mes = str(self.mesnum)
                data = dia+'/'+mes+'/'+ano
                descricao = description.get("1.0","end")
                vcon = datab.ConnectDB()
                query = "INSERT INTO tasks (task, date, description, created_at) VALUES ('"+tarefa+"','"+data+"','"+descricao+"', '"+data_hora_string+"')"
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
            self.months = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
            year = []

            for i in range(1, 32):
                if i<10:
                    days.append('0'+str(i))
                else:
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

            month_combo = ttk.Combobox(create_frame, values=self.months, width=5)
            month_combo.place(x=55, y=80)

            year_combo = ttk.Combobox(create_frame, values=year, width=5)
            year_combo.place(x=117, y=80)

            ## LABEL DE DESCRIÇÃO COM TEXT
            description_label = Label(create_frame, text='Descrição', bg=color1, fg=black)
            description_label.place(x=10, y=110)

            description = Text(create_frame, bg=white, fg=black, width=34, height=4, highlightbackground=white, highlightcolor=white, border=0)
            description.place(x=10, y=130)

            ## BOTÃO SE INSERÇÃO DE TAREFA
            insert_button = Button(create_frame, text='Enviar', command=insert, width=10, height=1, bg=color3, fg=black, highlightbackground=color3, highlightcolor=color3, border=0, activebackground=color3, cursor='hand2', activeforeground=white)
            insert_button.place(x=10, y=205)


        def update():
            ## FUNÇÃO QUE GERA UMA ALTERAÇÃO NO ITEM SELECIONADO DENTRO DO BANC0 DE DADOS
            def up_db():
                try:
                    ## FUNÇÃO DE DATA DE CRIAÇÃO
                    data_hora = datetime.now()
                    data_hora_string = data_hora.strftime('%d/%m/%Y %H:%M')

                    selection = self.app.selection()[0]
                    valores=self.app.item(selection, "values")
                    item = valores[0]


                    ## TRANSFORMANDO MESES EM NÚMEROS
                    for i in range(12):
                        m = month_combo.get()
                        if months[i] == m:
                            mesnum = i+1
                            if mesnum<10:
                                mesnum = '0'+str(mesnum)

                    tarefa = task_entry.get()
                    dia = str(day_combo.get())
                    ano = str(year_combo.get())
                    mes = str(mesnum)
                    data = dia+'/'+mes+'/'+ano
                    descricao = description.get("1.0","end")
                    
                    vcon = datab.ConnectDB()
                    query = "UPDATE tasks SET task='"+tarefa+"', date='"+data+"', description='"+descricao+"', created_at='"+data_hora_string+"' WHERE task='"+item+"'"
                    datab.insert(vcon, query)
                    task_entry.delete(0, END)
                    day_combo.delete(0, END)
                    month_combo.delete(0, END)
                    year_combo.delete(0, END)
                    description.delete("1.0", "end")
                    fill()
                except:
                    messagebox.showinfo(title="ERRO", message="Selecione uma tarefa")
        

            ## FRAME DE ATUALIZAÇÃO DE TAREFA
            create_frame = Frame(self.window, width=300, height=244, bg=color3)
            create_frame.place(x=10, y=40)

            days = []
            months = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
            year = []

            for i in range(1, 32):
                if i<10:
                    days.append('0'+str(i))
                else:
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

            description = Text(create_frame, bg=white, fg=black, width=34, height=4, highlightbackground=white, highlightcolor=white, border=0)
            description.place(x=10, y=130)     

            ## BOTÃO SE INSERÇÃO DE TAREFA
            insert_button = Button(create_frame, text='Enviar', command=up_db, width=10, height=1, bg=color1, fg=black, highlightbackground=color1, highlightcolor=color1, border=0, activebackground=color1, cursor='hand2', activeforeground=white)
            insert_button.place(x=10, y=205)

        ## FUNÇÃO PARA DELETAR UMA TAREFA SELECIONADA
        def delete():
            try:
                selection = self.app.selection()[0]
                valores=self.app.item(selection, "values")
                task = valores[0]
                vcon = datab.ConnectDB()
                query = "DELETE FROM tasks WHERE task='"+task+"'"
                datab.remove(vcon, query)
                fill()
            except:
                messagebox.showinfo(title="ERRO", message="Selecione uma tarefa")


        ## BOTÕES DE COMANDO
        create = Button(self.window, text='Novo', activebackground=color1, command=create, bg=color1, fg=entry, cursor='hand2', border=0, highlightbackground=color1, activeforeground=black)
        create.place(x=10, y=10)

        update = Button(self.window, text='Atualizar', activebackground=color3, command=update, bg=color3, fg=entry, cursor='hand2', border=0, highlightbackground=color3, activeforeground=black)
        update.place(x=78, y=10)

        delete = Button(self.window, text='Remover', activebackground=color2, command=delete, bg=color2, fg=entry, cursor='hand2', border=0, highlightbackground=color2, activeforeground=black)
        delete.place(x=170, y=10)

        ## TREEVIEW GLOBALIZADA PARA USO DA FUNÇÃO DOUBLE CLICK
        self.app = ttk.Treeview(self.window ,columns=('tarefas'), show='headings')
        self.app.column('tarefas', minwidth=0, width=250)
        self.app.heading('tarefas', text='TAREFAS')
        self.app.place(x=330, y=40)
        self.app.bind("<Double-1>", self.OnDoubleClick)


        fill()
        self.window.mainloop()

    ## FUNÇÃO CHAMADA AO UTILIZAR DUPLO CLIQUE, ABRE O FRAME DE DESCRIÇÃO DE TAREFA
    def OnDoubleClick(self,event):
        
        

        create_frame = Frame(self.window, width=300, height=244, bg=color)
        create_frame.place(x=10, y=40)

        task_label = Label(create_frame, text='Tarefa ', bg=white, fg=black, font=('Arial 10 bold'))
        task_label.place(x=10, y=10)

        label_task = Label(create_frame, text='', bg=color, fg=black)
        label_task.place(x=10, y=30)

        date_label = Label(create_frame, text="Data ", bg=white, fg=black, font=('Arial 10 bold'))
        date_label.place(x=10, y=60)

        label_date = Label(create_frame, text='', bg=color, fg=black)
        label_date.place(x=10, y=80)

        description_label = Label(create_frame, text="Descrição ", bg=white, fg=black, font=('Arial 10 bold'))
        description_label.place(x=10, y=110)

        label_description = Label(create_frame, text='', bg=color, fg=black)
        label_description.place(x=10, y=130)

        created_at_label = Label(create_frame, text="Criado em ", bg=white, fg=black, font=('Arial 10 bold'))
        created_at_label.place(x=10, y=160)

        label_created_at = Label(create_frame, text='', bg=color, fg=black)
        label_created_at.place(x=10, y=180)

        ## TREEVIEW CRIADA PARA LISTAGEM DOS ITENS SEM ELEMENTOS DA TUPLA
        app = ttk.Treeview(create_frame,columns=('tarefa','data','descrição','criado'), show='headings')
        app.column('tarefa', minwidth=0, width=70)
        app.column('data', minwidth=0, width=90)
        app.column('descrição', minwidth=0, width=90)
        app.column('criado', minwidth=0, width=90)
        app.heading('tarefa', text='TAREFA')
        app.heading('data', text='DATA')
        app.heading('descrição', text='DESCRIÇÃO')
        app.heading('criado', text='CRIADO')
        
        ## PEGA ITEM SELECIONADO DA TREEVIEW PRINCIPAL ORIENTADA À OBJETO E PESQUISA NA DATABASE ALGUMAS INFORMAÇÕES
        item = self.app.selection()[0]
        valores=self.app.item(item, "values")
        task = valores[0]
        vcon = datab.ConnectDB()
        query = "SELECT task, date, description, created_at FROM tasks WHERE task='"+task+"'"
        lista = datab.read(vcon, query)
        ## ADICIONA ITENS CONSULTADOS NA DB DENTRO DA TREEVIEW CRIADA PARA USO ÚNICO
        for i in lista:
            app.insert("","end", values=i)

        ## SELECIONA PRIMEIRO ITEM DESSA TREEVIEW 
        child_id = app.get_children()[-1] 
        app.focus(child_id)
        app.selection_set(child_id)

        ## A PARTIR DESSE ITEM SELECIONADO TRANSFORMAMOS EM UMA LISTA COM OS VALORES DENTRO DELA
        selected = app.selection()[0]
        valores=app.item(selected, "values")

        ## CADA LABEL VAZIA GANHA UM ITEM DE CADA POSIÇÃO DA LISTA VALORES
        label_task['text'] = valores[0]
        label_date['text'] = valores[1]
        label_description['text'] = valores[2]
        label_created_at['text']= valores[3]


construct = Inicial()
