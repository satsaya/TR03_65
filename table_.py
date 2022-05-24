import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="item02"
)
year_43 = ['43','44','45',
        '46','47','48',
        '49','50','51',
        '52','53','54']
year_T43 = ['หมายเลขอ้างอิง','43','43','44','44','45','45','46',
        '46','47','47','48','48','49',
        '49','50','50','51','51',
        '52','52','53','53']
year_54 = ['54',
        '55','56','57',
        '58','59','60',
        '61','62','63',
        '64']
year_T54 = ['หมายเลขอ้างอิง','54','54','55','55','56','56','57',
        '57','58','58','59','59','60',
        '60','61','61','62','62',
        '63','63','64','64']
typeall = ['AP','APO','Appliance','Cabinet','Camera',
        'Chair','General','Monitor',
        'Notebook','PC','Printer','Progarm','Projector'
        ,'Rack','Reader','Scanner','Server','Sound system','Storage'
        ,'Switch'
        ,'Table','Tablet','TV','UPS'
        ]
numtype = ['493,583','583','493,526,583','406','452,453,454,551','401','Gen','432,444,456,519,536,772',
           '444,493','493','493','494','516','446','545,584','525','493','404','458,459,462','493'
           ,'493,583','400','493','495',]


allcount43 = []
allcount54 = []
sum_allcount43 = []
sum_allcount54 = []
mycursor = mydb.cursor()
class table_:
    def data43(self):
        for i in typeall:
            x = []
            for j in year_43 :
                sql = "SELECT count(1) FROM  item2 WHERE year = '"+j+"' and type = '"+i+"'"
                sql2 = "SELECT count(1) FROM  item2 WHERE year = '"+j+"' and type = '"+i+"' and status = 'ปกติ'"
                mycursor.execute(sql)
                myresult = mycursor.fetchall()
                if myresult[0][0] == 0 :
                    x.append('-')
                else:
                    x.append(myresult[0][0])
                mycursor.execute(sql2)
                myresult = mycursor.fetchall()
                if myresult[0][0] == 0 :
                    x.append('-')
                else:
                    x.append(myresult[0][0])
            allcount43.append(x)
        return allcount43
    def data54(self):
        for i in typeall: 
            x = []
            for j in year_54 :
                sql = "SELECT count(1) FROM  item2 WHERE year = '"+j+"' and type = '"+i+"'"
                sql2 = "SELECT count(1) FROM  item2 WHERE year = '"+j+"' and type = '"+i+"' and status = 'ปกติ'"
                mycursor.execute(sql)
                myresult = mycursor.fetchall()
                if myresult[0][0] == 0 :
                    x.append('-')
                else:
                    x.append(myresult[0][0])
                mycursor.execute(sql2)
                myresult = mycursor.fetchall()
                if myresult[0][0] == 0 :
                    x.append('-')
                else:
                    x.append(myresult[0][0])
            allcount54.append(x)
        return allcount54
    def sum_43(self):
        for i in year_43:
            x = 0
            for j in typeall :
                sql = "SELECT count(1) FROM  item2 WHERE year = '"+i+"' and type = '"+j+"'"
                sql2 = "SELECT count(1) FROM  item2 WHERE year = '"+i+"' and type = '"+j+"' and status = 'ปกติ'"
                mycursor.execute(sql)
                myresult = mycursor.fetchall()
                if myresult[0][0] == 0 :
                   x = x+0

                else:
                    x=x + myresult[0][0]
                mycursor.execute(sql2)
                myresult = mycursor.fetchall()
                if myresult[0][0] == 0 :
                    x = x+0
                else:
                    x=x + myresult[0][0]
            sum_allcount43.append(x)
        return sum_allcount43
    def sum_54(self):
        for i in year_54:
            x = 0
            for j in typeall :
                sql = "SELECT count(1) FROM  item2 WHERE year = '"+i+"' and type = '"+j+"'"
                sql2 = "SELECT count(1) FROM  item2 WHERE year = '"+i+"' and type = '"+j+"' and status = 'ปกติ'"
                mycursor.execute(sql)
                myresult = mycursor.fetchall()
                if myresult[0][0] == 0 :
                   x = x+0

                else:
                    x=x + myresult[0][0]
                mycursor.execute(sql2)
                myresult = mycursor.fetchall()
                if myresult[0][0] == 0 :
                    x = x+0
                else:
                    x=x + myresult[0][0]
            sum_allcount43.append(x)
        return sum_allcount43
