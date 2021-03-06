import sqlite3
from sqlite3 import Error

def ConnectDB():
    way = 'task.db'
    con = None
    try:
        con=sqlite3.connect(way)
    except Error as ex:
        print(ex)
    return con

vcon = ConnectDB()

def insert(connection, sql):
    try:
        c = connection.cursor()
        c.execute(sql)
        connection.commit()
        print('Tarefa Criada')

    except Error as ex:
        print(ex)

def fill(connection, sql):
    try:
        c= connection.cursor()
        c.execute(sql)
        connection.commit()
        res=c.fetchall()
        vcon.close()
        print('Tarefas Atualizadas')
    except Error as ex:
        print(ex)
    return res

def read(connection, sql):
    try:
        c= connection.cursor()
        c.execute(sql)
        connection.commit()
        res=c.fetchall()
        vcon.close()
        print('Tarefa Encontrada')
    except Error as ex:
        print(ex)
    return res


def remove(connection, sql):
    try:
        c= connection.cursor()
        c.execute(sql)
        connection.commit()
        
        vcon.close()
        print('Tarefa Removida')
    except Error as ex:
        print(ex)

def intern(connection, sql):
    try:
        c= connection.cursor()
        c.execute(sql)
        connection.commit()
        res=c.fetchone()
        vcon.close()
        print('Itens selecionados')
    except Error as ex:
        print(ex)
    return res