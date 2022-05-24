import mysql.connector
from tkinter import *
class database_connector():
    def insert(self,id,type,room,status,year,noyear,notype,band,model,tel,owner):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="item02"
        )
        mycursor = mydb.cursor()
        mycursor.execute("Insert into item2 values('"+ id +"','"+ type +"','"+ room +"','"+ status +"','"+ year +"','"+ noyear +"','"+ notype +"','"+ band +"','"+ model +"','"+ tel +"','"+ owner +"')")
        mycursor.execute("commit")
        mydb.close()
        
    def delete(self,id):
        mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="item02"
                )
        mycursor = mydb.cursor()
        mycursor.execute("delete from item2 where id='"+ id +"'")
        mycursor.execute("commit")
        mydb.close()
        
        
    def update(self,id,type,room,status,year,noyear,notype,band,model,tel,owner):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="item02"
        )
        mycursor = mydb.cursor()
        sql = "UPDATE item2 SET type = %s,room = %s,status = %s,year = %s,noyear =%s ,notype =%s , band = %s ,model = %s,tel = %s , owner=%s WHERE  id= %s"
        val = (type,room,status,year,noyear,notype,band,model,tel,owner,id)
        mycursor.execute(sql, val)
        mycursor.execute("commit")
        mydb.close()

    allcount = []
    def InsertYearNO():
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="item02"
            )
        year = ['43','44','45',
                    '46','47','48',
                    '49','50','51',
                    '52','53','54',
                    '55','56','57',
                    '58','59','60',
                    '61','62','63',
                    '64']
        typeall = ['AP','APO','Appliance','Cabinet','Camera',
                    'Chair','General','Monitor',
                    'Notebook','PC','Printer','Progarm','Projector'
                    ,'Rack','Reader','Scanner','Sever','Sound system','Storage'
                    ,'Switch','Shelevs'
                    ,'Table','Tablet','TV','UPS'
                    ]
        mycursor = mydb.cursor()
        for i in year:
            for j in typeall:
                sql = "SELECT * FROM item2 WHERE year ='"+i+"' and type ='"+j+"'"
                mycursor.execute(sql)
                myresult = mycursor.fetchall()
                for x in myresult :
                    # sql = "UPDATE SET yearno = '"+str(years)+"'WHERE id = '"+x[0]+"'"
                    # years = years+1
                    pass
                
    def InserTypeNO():
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="item02"
            )
        year = ['43','44','45',
                    '46','47','48',
                    '49','50','51',
                    '52','53','54',
                    '55','56','57',
                    '58','59','60',
                    '61','62','63',
                    '64']
        typeall = ['AP','APO','Appliance','Cabinet','Camera',
                    'Chair','General','Monitor',
                    'Notebook','PC','Printer','Progarm','Projector'
                    ,'Rack','Reader','Scanner','Sever','Sound system','Storage'
                    ,'Switch','Shelevs'
                    ,'Table','Tablet','TV','UPS'
                    ]
        mycursor = mydb.cursor()
        tno = 1
        for i in typeall:
            sql = "SELECT * FROM item2 WHERE  type ='"+i+"'"
            mycursor.execute(sql)
            myresult = mycursor.fetchall()
            for x in myresult :
                sql = "UPDATE SET typeno = '"+str(tno)+"'WHERE id = '"+x[0]+"'"
                tno = tno+1

# insert_db_01.InsertYearNO()
# insert_db_01.InserTypeNO()