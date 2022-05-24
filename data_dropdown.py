from openpyxl import load_workbook
from search_in_db import  *

myFileName=r"D:/Py/project02/data.xlsx"

type_ = ['ประเภททั้งหมด']
year_ = ['ปีทั้งหมด']
def all_year():
        tem = search_in_db()
        rows = tem.get_year_db()
        # df = pd.read_excel(myFileName, sheet_name=0)
        # x = df['ปีทั้งหมด'].tolist()
        for i in rows:
                year_.append(i)
all_year()

def all_type():
        tem = search_in_db()
        rows = tem.get_type_db()
        # df = pd.read_excel(myFileName, sheet_name=1)
        # y = df['ประเภททั้งหมด'].tolist()
        for i in rows:
                type_.append(i)

all_type()
# type_= ['ประเภททั้งหมด','AP','APO','Appliance','Cabinet','Camera',
#         'Chair','General','Monitor',
#         'Notebook','PC','Printer','Progarm','Projector'
#         ,'Rack','Reader','Scanner','Server','Sound system','Storage'
#         ,'Switch'
#         ,'Table','Tablet','TV','UPS'
#         ]
# year_ = ["ปีทั้งหมด",'43','44','45',
#         '46','47','48',
#         '49','50','51',
#         '52','53','54',
#         '55','56','57',
#         '58','59','60',
#         '61','62','63',
#         '64']
# year_for_col = ['43','43','44','44','45','45','46',
#         '46','47','47','48','48','49',
#         '49','50','50','51','51',
#         '52','52','53','53','54','54','55','55','56','56','57',
#         '57','58','58','59','59','60',
#         '60','61','61','62','62',
#         '63','63','64','64'
# ]
status_ = ["สถานะทั้งหมด",'ปกติ','ชำรุด/ซ่อมได้','ชำรุด/ซ่อมไม่ได้','ยุบสภาพ']
status_text = ["ปกติ","ชำรุด/ซ่อมได้","ชำรุด/ซ่อมไม่ได้","ยุบสภาพ"]