from tkinter import *
from tkinter import messagebox
import mysql.connector
import xml.etree.ElementTree as ET
from mysql.connector import errorcode

from tkinter import filedialog


config = {
    'user': 'root',
    'password':'',
    'host':'localhost',
    'database':'database',
    'raise_on_warnings': True
    }


def load():
    try:
        conn = mysql.connector.connect(**config)  
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            messagebox.showerror('Ошибка', 'Неправильное имя или пароль!')
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            messagebox.showerror('Ошибка','Такой базы данных не существует!')
        else:
            messagebox.showerror('Ошибка','Неизвестная ошибка. Проверьте подключение')
    else:
        
        text_path = filedialog.askopenfilename(title='Выберите тест')

        
        tree = ET.parse(text_path)
        
        data = tree.findall("ВыборЗач") 


        for i, j in zip(data, range(1, 10001)): 

            name = i.get('НаимПлат') 
            oktmo_id = i.get('ОКТМО')
            date = i.get('ДатаЗач')
            inn = i.get('ИННАДБ')
            innul = i.get('ИННЮЛ')
            kbk = i.get('КБК')
            kpp = i.get('КПП')
            kppadb = i.get('КППАДБ')
            sum = i.get('СумЗач')

    
            
            data = """INSERT INTO main_nalogovaya(NAIMPLAT,oktmo_id,datetime,INNADB,INNUL,KBK,KPP,KPPADB,SUM) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"""

            c = conn.cursor() 
            c.execute(data,(name,oktmo_id,date,inn,innul,kbk,kpp,kppadb,sum))
            conn.commit()
        
        messagebox.showinfo('Загрузка', 'Успешно загружено в бд')


def clear():
    conn = mysql.connector.connect(**config)  
    c = conn.cursor()

    c.execute("TRUNCATE TABLE main_nalogovaya")

    c.close()


    