import mysql.connector
import queue
class search_in_db():
    def one(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="item02"
        )
        sql = "SELECT * FROM item2 WHERE 1 ORDER BY year"
        
        c = conn.cursor()
        c.execute(sql)
        records = c.fetchall()
        conn.commit()
        conn.close()
        return records
    def two(self,status,year,type):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="item02"
        )
        if status == "สถานะทั้งหมด" and year!="ปีทั้งหมด" and type!="ประเภททั้งหมด" :
            sql = "select * from item2 where year='"+ year +"'and type='"+type+"' ORDER BY year"
        elif type=="ประเภททั้งหมด" and status != "สถานะทั้งหมด" and year!="ปีทั้งหมด":
            sql = "select * from item2 where status='"+ status +"'and year='"+year+"' ORDER BY year"
        elif year=="ปีทั้งหมด" and status != "สถานะทั้งหมด" and type!="ประเภททั้งหมด":
            sql = "select * from item2 where status='"+ status +"'and type='"+type+"' ORDER BY year"
        elif type=="ประเภททั้งหมด" and status == "สถานะทั้งหมด":
            sql = "select * from item2 where year='"+ year +"' ORDER BY year"
        elif year=="ปีทั้งหมด" and  status=="สถานะทั้งหมด":
            sql = "select * from item2 where type='"+ type +"' ORDER BY year"
        elif type=="ประเภททั้งหมด" and year=="ปีทั้งหมด":
            sql = "select * from item2 where status='"+ status +"' ORDER BY year"
        else:
            sql = "select * from item2 where status='"+ status +"'and type='"+type+"'and year='"+year+"' ORDER BY year"
        # if status == status_[0] and year!=year_[0] and type!=type_[0] :
        #     sql = "select * from item2 where year='"+ year +"'and type='"+type+"' ORDER BY year"
        # elif type==type_[0] and status != status_[0] and year!=year_[0]:
        #     sql = "select * from item2 where status='"+ status +"'and year='"+year+"' ORDER BY year"
        # elif year==year_[0] and status != status_[0] and type!=type_[0]:
        #     sql = "select * from item2 where status='"+ status +"'and type='"+type+"' ORDER BY year"
        # elif type==type_[0] and status == status_[0]:
        #     sql = "select * from item2 where year='"+ year +"' ORDER BY year"
        # elif year==year_[0] and  status==status_[0]:
        #     sql = "select * from item2 where type='"+ type +"' ORDER BY year"
        # elif type==type_[0] and year==year_[0]:
        #     sql = "select * from item2 where status='"+ status +"' ORDER BY year"
        # else:
        #     sql = "select * from item2 where status='"+ status +"'and type='"+type+"'and year='"+year+"' ORDER BY year"
        c = conn.cursor()
        c.execute(sql)
        records = c.fetchall()
        conn.commit()
        conn.close()
        return records
    def three(self,val):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="item02"
        )
        c = conn.cursor()
        sql='SELECT * FROM item2 WHERE id LIKE %s ORDER BY year'
        args=[val+'%']
        c.execute(sql,args)
        records = c.fetchall()
        conn.commit()
        conn.close()
        return records
    def get_db(self,id):
        if(id==""):#or type == ""or room == ""or date == ""or status == ""
            return
        else:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="item02"
            )
        mycursor = mydb.cursor()
        mycursor.execute("select * from item2 where id='"+ id +"'")
        rows = mycursor.fetchall()
        return rows
    def get_year_db(self):
        mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="item02"
            )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT DISTINCT year FROM item2 ORDER by year;")
        rows = mycursor.fetchall()
        return rows
    def get_type_db(self):
        mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="item02"
            )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT DISTINCT type FROM item2 ORDER by type;")
        rows = mycursor.fetchall()
        return rows