from tkinter import * 
from tkinter.ttk import *
from tkinter import ttk
from multiprocessing import Process
import os
from database_connector import *
from table_ import  *
import tkinter.messagebox as MessageBox
from search_in_db import  *
from data_dropdown import *
from asyncio.windows_events import NULL
from PIL import Image
from PIL import ImageTk
import threading
root = Tk()
w = 1366
h = 768
bg_frame = '#ebfcfc'
root.geometry(f"{w}x{h}+100+100")
photo_ = PhotoImage("D:\Py\project02\_C.ico")
img  = Image.open("D:\Py\project02\photo_top_frame-removebg.png")  
img = img.resize((100, 100))
photo_01=ImageTk.PhotoImage(img)
root.iconbitmap(photo_)
root.configure(bg = bg_frame)
root.title("ครุภัณฑ์เทศบาลนครแหลมฉบัง")

id= StringVar()          
type = StringVar()
room = StringVar()
year = StringVar()
status = StringVar()
year = StringVar()
noyear = StringVar()
notype = StringVar()
band = StringVar()
model = StringVar()
tel = StringVar()
owner = StringVar()
s_entry = StringVar()

def bttn(x,y,text,cmd):
    global mybutton
    mybutton = ttk.Button(root,text=text,style='font.TButton',command=cmd)#style='font.TButton'
    mybutton.place(relwidth = 0.15, relheight = 0.07, relx = x, rely = y)

font_in =  ttk.Style()
font_in.configure('font_in.TButton',font=("TH Sarabun New",18,'bold'))
s =  ttk.Style()
s.configure('top.TFrame',background = 'lightblue',)
dropbox = ttk.Style()
dropbox.configure('top.TButton',font=("TH Sarabun New",18,'bold'),background = 'green',relief="flat", borderwidth = '4')#borderwidth = '4'
font01 =  ttk.Style()
font01.configure('font.TButton',font=("TH Sarabun New",18,'bold'),relief="flat",padding=6,fg= 'black', bg= 'RoyalBlue3', activebackground=
'gray71', activeforeground='gray71')#relief="flat" background="#ccc"
style =  ttk.Style()
style.theme_use()
style.configure("mystyle.Treeview",font=("TH Sarabun New",18),
	background="#D3D3D3",
	foreground="black",
	rowheight=25,
	fieldbackground="#D3D3D3")
style.configure("mystyle.Treeview.Heading", font=("TH Sarabun New",18,'bold'))
# Change Selected Color
style.map('mystyle.Treeview',
	background=[('selected', "#347083")])#347083

def get_detail_more():
    id.set("")
    type.set("")
    room.set("")
    status.set("")
    year.set("")
    noyear.set("")
    notype.set("")
    band.set("")
    model.set("")
    tel.set("")
    owner.set("")
    top = Toplevel()
    top.geometry("1050x550+500+300")
    top.iconbitmap(photo_)
    top.title("รายละเอียดรหัสครุภัณฑ์")
    x_en = 0.25
    def label(top,x,y,text):
        label = ttk.Label(top,text = text,font=("TH Sarabun New",18,'bold'))
        label.place(relwidth = 0.1, relheight = 0.05, relx = x, rely = y)
    label(top,0.1,0.1,"รหัสครุภัณฑ์ :")
    entry_id = ttk.Entry(top,textvariable=id).place(relwidth = 0.1, relheight = 0.05, relx = x_en, rely = 0.1)
    label(top,0.55,0.1,"ประเภท :")
    entry_type = ttk.Entry(top,textvariable=type).place(relwidth = 0.1, relheight = 0.05, relx = x_en+0.4, rely = 0.1)
    label(top,0.1,0.2,"ห้อง :")
    entry_room = ttk.Entry(top,textvariable=room).place(relwidth = 0.1, relheight = 0.05, relx = x_en, rely = 0.2)
    label(top,0.45,0.2,"สถานะ :")
    entry_status = ttk.Entry(top,textvariable=status).place(relwidth = 0.1, relheight = 0.05, relx = x_en+0.3, rely = 0.2)
    label(top,0.1,0.3,"ปี:")
    entry_year = ttk.Entry(top,textvariable=year).place(relwidth = 0.1, relheight = 0.05, relx = x_en, rely = 0.3)
    label(top,0.45,0.3,"ลำดับในปี :")
    entry_noyear = ttk.Entry(top,textvariable=noyear).place(relwidth = 0.1, relheight = 0.05, relx = x_en+0.3, rely = 0.3)
    label(top,0.1,0.4,"ลำดับในประเภท :")
    entry_notype = ttk.Entry(top,textvariable=notype).place(relwidth = 0.1, relheight = 0.05, relx = x_en, rely = 0.4)
    label(top,0.45,0.4,"Band :")
    entry_band = ttk.Entry(top,textvariable=band).place(relwidth = 0.1, relheight = 0.05, relx = x_en+0.3, rely = 0.4)
    label(top,0.1,0.5,"Model :")
    entry_model = ttk.Entry(top,textvariable=model).place(relwidth = 0.1, relheight = 0.05, relx = x_en, rely = 0.5)
    label(top,0.45,0.5,"Tel :")
    entry_tel = ttk.Entry(top,textvariable=tel).place(relwidth = 0.1, relheight = 0.05, relx = x_en+0.3, rely = 0.5)
    label(top,0.1,0.6,"Owner :")
    entry_owner = ttk.Entry(top,textvariable=owner).place(relwidth = 0.1, relheight = 0.05, relx = x_en, rely = 0.6)
    def search_id_up():
        temp = search_in_db()
        id_value = id.get()
        if(id_value ==""):
            MessageBox.showinfo("อัพเดตสถานะรหัสครุภัณฑ์","กรุณาใส่ข้อมูล",parent = top)
            return
        try:
            rows = temp.get_db(id_value)
            if rows[0]!= NULL:
                for i in rows:
                    type.set(i[1])
                    room.set(i[2])
                    status.set(i[3])
                    year.set(i[4])
                    noyear.set(i[5])
                    notype.set(i[6])
                    band.set(i[7])
                    model.set(i[8])
                    tel.set(i[9])
                    owner.set(i[10])
        except IndexError:
            MessageBox.showinfo("อัพเดตสถานะรหัสครุภัณฑ์","ไม่พบครุภัณฑ์ : " + id_value,parent = top)
    search_ = ttk.Button(top,text="ค้นหา",style='font_in.TButton',command= lambda:search_id_up()).place( relx = x_en+0.12, rely = 0.08)
def get_detail():
    id.set("")
    type.set("")
    room.set("")
    status.set("")
    year.set("")
    noyear.set("")
    notype.set("")
    top = Toplevel()
    top.geometry("640x480+500+300")
    top.iconbitmap(photo_)
    top.title("อัพเดตสถานะรหัสครุภัณฑ์")
    x_en = 0.35
    def label(top,x,y,text):
        label = ttk.Label(top,text = text,font=("TH Sarabun New",18,'bold'))
        label.place(relwidth = 0.2, relheight = 0.07, relx = x, rely = y)
    label(top,0.1,0.1,"รหัสครุภัณฑ์ :")
    entry_id = ttk.Entry(top,textvariable=id).place(relwidth = 0.2, relheight = 0.05, relx = x_en, rely = 0.1)
    label(top,0.1,0.17,"ประเภท:")
    entry_type = ttk.Entry(top,textvariable=type).place(relwidth = 0.2, relheight = 0.05, relx = x_en, rely = 0.17)
    label(top,0.1,0.24,"ห้อง:")
    entry_room = ttk.Entry(top,textvariable=room).place(relwidth = 0.2, relheight = 0.05, relx = x_en, rely = 0.24)
    label(top,0.1,0.31,"สถานะ:")
    entry_status = ttk.Entry(top,textvariable=status).place(relwidth = 0.2, relheight = 0.05, relx = x_en, rely = 0.31)
    clicked = StringVar()
    status_com = ttk.Combobox(top,justify='center',textvariable=clicked,font=("TH Sarabun New",18), values = status_text )
    status_com.place(relwidth = 0.2, relheight = 0.05, relx = x_en+0.25, rely = 0.31)
    label(top,0.1,0.38,"ปีงบประมาณ:")
    entry_year = ttk.Entry(top,textvariable=year).place(relwidth = 0.2, relheight = 0.05, relx = x_en, rely = 0.38)
    label(top,0.1,0.45,"ลำดับในปี:")
    entry_noyear = ttk.Entry(top,textvariable=noyear).place(relwidth = 0.2, relheight = 0.05, relx = x_en, rely = 0.45)
    label(top,0.1,0.52,"ลำดับในประเภท:")
    entry_notype = ttk.Entry(top,textvariable=notype).place(relwidth = 0.2, relheight = 0.05, relx = x_en, rely = 0.52)
    label(top,0.1,0.59,"Band:")
    entry_band = ttk.Entry(top,textvariable=band).place(relwidth = 0.2, relheight = 0.05, relx = x_en, rely = 0.59)
    label(top,0.1,0.66,"Model:")
    entry_model = ttk.Entry(top,textvariable=model).place(relwidth = 0.2, relheight = 0.05, relx = x_en, rely = 0.66)
    label(top,0.1,0.73,"Tel:")
    entry_tel = ttk.Entry(top,textvariable=tel).place(relwidth = 0.2, relheight = 0.05, relx = x_en, rely = 0.73)
    label(top,0.1,0.8,"Owner:")
    entry_owner = ttk.Entry(top,textvariable=owner).place(relwidth = 0.2, relheight = 0.05, relx = x_en, rely = 0.8)
    
    def search_id_up():
        temp = search_in_db()
        id_value = id.get()
        if(id_value ==""):
            MessageBox.showinfo("อัพเดตสถานะรหัสครุภัณฑ์","กรุณาใส่ข้อมูล",parent = top)
            return
        try:
            rows = temp.get_db(id_value)
            if rows[0]!= NULL:
                for i in rows:
                    type.set(i[1])
                    room.set(i[2])
                    status.set(i[3])
                    year.set(i[4])
                    noyear.set(i[5])
                    notype.set(i[6])
                    band.set(i[7])
                    model.set(i[8])
                    tel.set(i[9])
                    owner.set(i[10])
        except IndexError:
            MessageBox.showinfo("อัพเดตสถานะรหัสครุภัณฑ์","ไม่พบครุภัณฑ์ : " + id_value,parent = top)
    
    def update_database():
        temp = database_connector()
        id_value = id.get()
        type_value = type.get()
        room_value = room.get()
        year_value = year.get()
        status_value = clicked.get()
        notype_value = notype.get()
        noyear_value = noyear.get()
        band_value = band.get()
        model_value = model.get()
        tel_value = tel.get()
        owner_value = owner.get()
        if(id_value ==""):
            MessageBox.showinfo("อัพเดตสถานะรหัสครุภัณฑ์","กรุณาใส่ข้อมูล",parent = top)
            return
        try:
            temp.update(id_value,type_value,room_value,status_value,year_value,noyear_value,notype_value,band_value,model_value,tel_value,owner_value)
            id.set("")
            type.set("")
            room.set("")
            status.set("")
            year.set("")
            noyear.set("")
            notype.set("")
            band.set("")
            model.set("")
            tel.set("")
            owner.set("")
            MessageBox.showinfo("อัพเดตสถานะรหัสครุภัณฑ์","Successfully",parent = top,)
            threading.Thread(target=search(1)).start()
            all_year()
        except IndexError:
            MessageBox.showinfo("อัพเดตสถานะรหัสครุภัณฑ์","????? : " + id_value,parent = top)
            id.set("")
            type.set("")
            room.set("")
            status.set("")
            year.set("")
            noyear.set("")
            notype.set("")
            band.set("")
            model.set("")
            tel.set("")
            owner.set("")
    search_ = ttk.Button(top,text="ค้นหา",style='font_in.TButton',command= lambda:search_id_up()).place( relx = x_en+0.25, rely = 0.085)
    insert = ttk.Button(top,text="อัพเดต",style='font_in.TButton',command=lambda:update_database()).place( relx = x_en+.35, rely = 0.85)

def delete_database():
    id.set("")
    top = Toplevel()
    top.geometry("500x240+500+300")
    top.iconbitmap(photo_)
    top.title("ลบรหัสครุภัณฑ์")
    temp = database_connector()
    x_en = 0.35
    def label(top,x,y,text):
        label = ttk.Label(top,text = text,font=("TH Sarabun New",18,'bold'))
        label.place(relwidth = 0.22, relheight = 0.15, relx = x, rely = y)
    label(top,0.1,0.1,"รหัสครุภัณฑ์ :")
    def ask():
        return MessageBox.askyesno("ลบข้อมูล", "ต้องการลบครุภัณฑ์ : "+id.get()+" ?",parent = top)
    def delete_():
        id_value = id.get()
        if(id_value ==""):
            MessageBox.showinfo("ลบข้อมูล","กรุณาใส่ข้อมูล",parent = top)
            return
        if ask():
            try :
                temp.delete(id_value)
                MessageBox.showinfo("ลบข้อมูล","ลบข้อมูลแล้ว "+id_value,parent = top)
                id.set("")
                threading.Thread(target=search(1)).start()
                all_year()
            except:
                id.set("")
                MessageBox.showinfo("ลบข้อมูล","ไม่พบข้อมูลที่จะลบ",icon ='error',parent = top)
        else :
            return
    entry_id = ttk.Entry(top,textvariable=id).place(relwidth = 0.3, relheight = 0.1, relx = x_en, rely = 0.115)
    b = ttk.Button(top,text="ลบข้อมูล",style='font_in.TButton',command=lambda:delete_()).place(relwidth = 0.15, relheight = 0.15, relx = 0.71, rely = 0.75)

def insert_database():
    id.set("")
    type.set("")
    room.set("")
    status.set("")
    year.set("")
    noyear.set("")
    notype.set("")
    top = Toplevel()
    top.geometry("640x480+500+300")
    top.iconbitmap(photo_)
    top.title("เพิ่มรหัสครุภัณฑ์")
    x_en = 0.35
    def label(top,x,y,text):
        label = ttk.Label(top,text = text,font=("TH Sarabun New",18,'bold'))
        label.place(relwidth = 0.2, relheight = 0.07, relx = x, rely = y)
    label(top,0.1,0.1,"รหัสครุภัณฑ์ :")
    entry_id = ttk.Entry(top,textvariable=id).place(relwidth = 0.2, relheight = 0.05, relx = x_en, rely = 0.1)
    label(top,0.1,0.17,"ประเภท:")
    entry_type = ttk.Entry(top,textvariable=type).place(relwidth = 0.2, relheight = 0.05, relx = x_en, rely = 0.17)
    label(top,0.1,0.24,"ห้อง:")
    entry_room = ttk.Entry(top,textvariable=room).place(relwidth = 0.2, relheight = 0.05, relx = x_en, rely = 0.24)
    label(top,0.1,0.31,"สถานะ:")
    entry_status = ttk.Entry(top,textvariable=status).place(relwidth = 0.2, relheight = 0.05, relx = x_en, rely = 0.31)
    label(top,0.1,0.38,"ปีงบประมาณ:")
    entry_year = ttk.Entry(top,textvariable=year).place(relwidth = 0.2, relheight = 0.05, relx = x_en, rely = 0.38)
    label(top,0.1,0.45,"ลำดับในปี:")
    entry_noyear = ttk.Entry(top,textvariable=noyear).place(relwidth = 0.2, relheight = 0.05, relx = x_en, rely = 0.45)
    label(top,0.1,0.52,"ลำดับในประเภท:")
    entry_notype = ttk.Entry(top,textvariable=notype).place(relwidth = 0.2, relheight = 0.05, relx = x_en, rely = 0.52)
    label(top,0.1,0.59,"Band:")
    entry_band = ttk.Entry(top,textvariable=band).place(relwidth = 0.2, relheight = 0.05, relx = x_en, rely = 0.59)
    label(top,0.1,0.66,"Model:")
    entry_model = ttk.Entry(top,textvariable=model).place(relwidth = 0.2, relheight = 0.05, relx = x_en, rely = 0.66)
    label(top,0.1,0.73,"Tel:")
    entry_tel = ttk.Entry(top,textvariable=tel).place(relwidth = 0.2, relheight = 0.05, relx = x_en, rely = 0.73)
    label(top,0.1,0.8,"Owner:")
    entry_owner = ttk.Entry(top,textvariable=owner).place(relwidth = 0.2, relheight = 0.05, relx = x_en, rely = 0.8)
    b = ttk.Button(top,text="เพิ่มข้อมูล",style='font_in.TButton',command=lambda:test01()).place(relwidth = 0.15, relheight = 0.075, relx = x_en+0.35, rely = 0.87)
    call_in_db_ = database_connector()
    def test01():
        id_value = id.get()
        type_value = type.get()
        room_value = room.get()
        year_value = year.get()
        status_value = status.get()
        notype_value = notype.get()
        noyear_value = noyear.get()
        band_value = band.get()
        model_value = model.get()
        tel_value = tel.get()
        owner_value = owner.get()
        if(id_value==""):
            MessageBox.showinfo("Insert Status","กรุณาใส่ข้อมูล",parent = top)
            return
        try :
            call_in_db_.insert(id_value,type_value,room_value,status_value,year_value,noyear_value,notype_value,band_value,model_value,tel_value,owner_value)
            id.set("")
            type.set("")
            room.set("")
            status.set("")
            year.set("")
            noyear.set("")
            notype.set("")
            band.set("")
            model.set("")
            tel.set("")
            owner.set("")
            MessageBox.showinfo("Insert Status","Successfully",parent = top)
            threading.Thread(target=search(1)).start()
            all_year()
        except:
            id.set("")
            type.set("")
            room.set("")
            status.set("")
            year.set("")
            noyear.set("")
            notype.set("")
            band.set("")
            model.set("")
            tel.set("")
            owner.set("")
            MessageBox.showinfo("Insert Status","มีข้อมูลนี้อยู่แล้ว",parent = top)

    call_in_db_.InsertYearNO
    call_in_db_.InserTypeNO

def table_43():
    allcount = table_()
    list_ = allcount.data43()
    total_rows = len(list_)
    total_columns = len(list_[0])
    all = []
    def sum_all():
        for i in range(total_columns):
            x=0
            for j in range(total_rows):
                if j>=0 and i>=0:
                    if list_[j][i]=='-':
                        x = x + 0
                    else :
                        x = x + list_[j][i]
            all.append(x)
    t1 = threading.Thread(target=sum_all)
    t1.start()
    top = Toplevel()
    top.iconbitmap(photo_)
    top.title("ป๊ 43 - 53")
    for i in range(total_rows+1):#row
        for j in range(total_columns):#col
                    if j ==0 and i ==0:
                        e = Entry(top, width=15,
                        font=('TH Sarabun New',14,'bold'),justify='center')
                        e.grid(row=0, column=0)
                        e.insert(END, 'ประเภท')
                    elif j >=1 and i ==0:
                        if i ==0 and j ==1:
                            e = Entry(top, width=25, fg='Black',
                            font=('TH Sarabun New',14,'bold'),justify='center')
                            e.grid(row=0, column=j)
                            e.insert(END, year_T43[j-1])
                        else:
                            e = Entry(top, width=5, fg='Black',
                            font=('TH Sarabun New',14,'bold'),justify='center')
                            e.grid(row=0, column=j)
                            e.insert(END, year_T43[j-1])
                    elif j ==0 and i >=1:
                        e = Entry(top, width=15, fg='Black',
                        font=('TH Sarabun New',14,'bold',),justify='center')
                        e.grid(row=i, column=0)
                        e.insert(0, typeall[i-1])
                    elif j== 1 and i>=1:
                        e = Entry(top, width=25, fg='white',
                        font=('TH Sarabun New',14,'bold'),justify='center')
                        e.grid(row=i, column=1)
                        e.insert(END, numtype[i-1])
                        e.configure({"background": "#6560FA"})
                    else :
                        e = Entry(top, width=5, fg='Black',
                        font=('TH Sarabun New',14,'bold'),justify='center')
                        e.grid(row=i, column=j)
                        if j%2 ==0:
                            e.insert(END, list_[i-1][j-2])            
                        else :
                            e.insert(END, list_[i-1][j-2])
                            e.configure({"background": "#D6B2FF"})
                    if j>=2 and i==total_rows:
                        e = Entry(top, width=5,
                        font=('TH Sarabun New',14,'bold'),justify='center')
                        e.grid(row=total_rows+2, column=j)
                        e.insert(END, all[j-2])
                    elif j==0 and i==total_rows:
                        e = Entry(top, width=15,
                        font=('TH Sarabun New',14,'bold'),justify='center')
                        e.grid(row=total_rows+2, column=j)
                        e.insert(END, "")
                    elif j==1 and i==total_rows:
                        e = Entry(top, width=25,
                        font=('TH Sarabun New',14,'bold'),justify='center')
                        e.grid(row=total_rows+2, column=j)
                        e.insert(END, "รวม")
    b = ttk.Button(top,text = "54-64",width=5,command=table_54)
    b.grid(row=total_rows+3, column=total_columns-1) 
    list_.clear() 

def table_54():
    allcount = table_()
    list_ = allcount.data54()
    total_rows = len(list_)
    total_columns = len(list_[0])
    all = []
    def sum_all():
        for i in range(total_columns):
            x=0
            for j in range(total_rows):
                if j>=0 and i>=0:
                    if list_[j][i]=='-':
                        x = x + 0
                    else :
                        x = x + list_[j][i]
            all.append(x)
    t1 = threading.Thread(target=sum_all)
    t1.start()
    top = Toplevel()
    top.iconbitmap(photo_)
    top.title("ปี 54 - 64")
    for i in range(total_rows+1):#row
        for j in range(total_columns+2):#col
                    if j ==0 and i ==0:
                        e = Entry(top, width=15,
                        font=('TH Sarabun New',14,'bold'),justify='center')
                        e.grid(row=0, column=0)
                        e.insert(END, 'ประเภท')
                    elif j >=1 and i ==0:
                        if i ==0 and j ==1:
                            e = Entry(top, width=25, fg='Black',
                            font=('TH Sarabun New',14,'bold'),justify='center')
                            e.grid(row=0, column=j,ipady=0)
                            e.insert(END, year_T54[j-1])
                        else:
                            e = Entry(top, width=5, fg='Black',
                            font=('TH Sarabun New',14,'bold'),justify='center')
                            e.grid(row=0, column=j)
                            e.insert(END, year_T54[j-1])
                    elif j ==0 and i >=1:
                        e = Entry(top, width=15, fg='Black',
                        font=('TH Sarabun New',14,'bold'),justify='center')
                        e.grid(row=i, column=0)
                        e.insert(END, typeall[i-1])
                    elif j==1 and i>=1:
                        e = Entry(top, width=25, fg='white',
                        font=('TH Sarabun New',14,'bold'),justify='center')
                        e.grid(row=i, column=1)
                        e.insert(END, numtype[i-1])
                        e.configure({"background": "#6560FA"})
                    else:
                        e = Entry(top, width=5, fg='Black',
                        font=('TH Sarabun New',14,'bold'),justify='center')
                        e.grid(row=i, column=j)
                        if j%2 ==0:
                            e.insert(END, list_[i-1][j-2])
                        else :
                            e.insert(END, list_[i-1][j-2])
                            e.configure({"background": "#D6B2FF"})
                    if j>=2 and i==total_rows:
                        e = Entry(top, width=5,
                        font=('TH Sarabun New',14,'bold'),justify='center')
                        e.grid(row=total_rows+2, column=j)
                        e.insert(END, all[j-2])
                    elif j==0 and i==total_rows:
                        e = Entry(top, width=15,
                        font=('TH Sarabun New',14,'bold'),justify='center')
                        e.grid(row=total_rows+2, column=j)
                        e.insert(END, "")
                    elif j==1 and i==total_rows:
                        e = Entry(top, width=25,
                        font=('TH Sarabun New',14,'bold'),justify='center')
                        e.grid(row=total_rows+2, column=j)
                        e.insert(END, "รวม")
    list_.clear()
    b = ttk.Button(top,text = "43-53",width=5,command= table_43)
    b.grid(row=total_rows+3, column=total_columns+1)

bttn(0.07,0.3,"เพิ่มรหัสครุภัณฑ์",insert_database)
bttn(0.07,0.4,"อัพเดตสถานะครุภัณฑ์",get_detail)
bttn(0.07,0.5,"ลบข้อมูลครุภัณฑ์",delete_database)
bttn(0.07,0.6,"ปีงบประมาณ 43-53",table_43)
bttn(0.07,0.7,"ปีงบประมาณ 54-64",table_54)
bttn(0.07,0.8,"รายละเอียดรหัสครุภัณฑ์",get_detail_more)
img = Image.open(r"D:\Py\project02\search_icon.png")
img = img.resize((13,13))
photoImg =  ImageTk.PhotoImage(img)
def search_box():
    search_entry = ttk.Entry(root,textvariable = s_entry).place(relwidth = 0.1, relheight = 0.027, relx = 0.8, rely = 0.181)
    search_button = ttk.Button(root,image=photoImg,command=search_box_in_db).place(relwidth = 0.015, relheight = 0.026, relx = 0.901, rely = 0.181)
    # add_button = ttk.Button(root,text= "เพิ่ม",command=search_box_in_db).place(relwidth = 0.025, relheight = 0.025, relx = 0.7, rely = 0.181)
def search_box_in_db():
    clear_all()
    year_com.set("ปีทั้งหมด")
    type_com.set("ประเภททั้งหมด")
    status_com.set("สถานะทั้งหมด")
    record = []
    temp = search_in_db()
    records = temp.three(s_entry.get())
    count = 0
    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags=('evenrow',))
        else :
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags=('oddrow',))
        count += 1

def search(e):
    clear_all()
    record = []
    global count
    status = clicked_status.get()
    type = clicked_type.get()
    year = clicked_year.get()
    s_entry.set("")
    if(type==type_[0] and status==status_[0] and year==year_[0]):
        temp = search_in_db()
        records = temp.one()
    else:
        temp = search_in_db()
        records = temp.two(status,year,type)
    
    count = 0
    for record in records:
        if count % 2 == 0:
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags=('evenrow',))
        else :
            my_tree.insert(parent='', index='end', iid=count, text='', values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6]), tags=('oddrow',))
        count += 1

t = Label(root,text='เทศบาลนครแหลมฉบัง',font=("TH Sarabun New italic",60,'bold'))
t.config(bg=bg_frame)
t.place(relx = 0.09, rely = 0.001)
# lab=Label(image=photo_01).place(x=50,y=50)
t1 = Label(root,image=photo_01)
t1.config(bg=bg_frame)
t1.place(relx = 0.01, rely = 0)
frame01 = ttk.Frame(root, width=1255, height=60, style='top.TFrame').place(relwidth = 0.98, relheight = 0.09, relx = 0.01, rely = 0.15)
# Create a Treeview Frame
tree_frame = ttk.Frame(root)
tree_frame.pack(pady=10,fill=BOTH,expand=TRUE)
tree_frame.place(relwidth = 0.67, relheight = 0.55, relx = 0.25, rely = 0.3)
# Create a Treeview Scrollbar
tree_scroll = ttk.Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)
# Create The Treeview
my_tree = ttk.Treeview(tree_frame, style="mystyle.Treeview",height=20,yscrollcommand=tree_scroll.set, selectmode="extended",)
my_tree.pack(fill=BOTH,expand=TRUE)
# Configure the Scrollbar
tree_scroll.config(command=my_tree.yview)
# Define Our Columns
my_tree['columns'] = ("id", "type", "room", "status", "year", "noyear","notype")
# Format Our Columns
my_tree.column("#0", width=0, stretch=NO)
my_tree.column("id", anchor=W, width=130)
my_tree.column("type", anchor=W, width=110)
my_tree.column("room", anchor=CENTER, width=100)
my_tree.column("status", anchor=CENTER, width=100)
my_tree.column("year", anchor=CENTER, width=100)
my_tree.column("noyear", anchor=CENTER, width=100)
my_tree.column("notype", anchor=CENTER, width=130)
# Create Headings
my_tree.heading("#0", text="", anchor=W)
my_tree.heading("id", text="ID", anchor=W)
my_tree.heading("type", text="ประเภท", anchor=W)
my_tree.heading("room", text="ห้อง", anchor=CENTER)
my_tree.heading("status", text="สถานะ", anchor=CENTER)
my_tree.heading("year", text="ปี", anchor=CENTER)
my_tree.heading("noyear", text="ลำดับในปี", anchor=CENTER)
my_tree.heading("notype",text = "ลำดับในประเภท",anchor=CENTER)

# Create Striped Row Tags
my_tree.tag_configure('oddrow', background="white")
my_tree.tag_configure('evenrow', background="lightblue")

def clear_all():
	for item in my_tree.get_children():
    			my_tree.delete(item)

clicked_year = StringVar()
year_com = ttk.Combobox(frame01,justify='center',textvariable=clicked_year,font=("TH Sarabun New",18,'bold'),values = year_, )

year_com.config(style='top.TButton')
year_com.set("ปีทั้งหมด")
year_com.place(relwidth = 0.1, relheight = 0.03, relx = 0.05, rely = 0.181)
year_com.bind("<<ComboboxSelected>>", search)

clicked_type = StringVar()
type_com = ttk.Combobox(frame01,justify='center',textvariable=clicked_type,font=("TH Sarabun New",18,'bold'),values = type_,)
type_com.config(style='top.TButton')
type_com.set("ประเภททั้งหมด")
type_com.place(relwidth = 0.1, relheight = 0.03, relx = 0.17, rely = 0.181)
type_com.bind("<<ComboboxSelected>>", search)

clicked_status = StringVar()
status_com = ttk.Combobox(frame01,justify='center',textvariable=clicked_status,font=("TH Sarabun New",18,'bold'),values = status_,)
status_com.config(style='top.TButton')
status_com.set("สถานะทั้งหมด")
status_com.place(relwidth = 0.1, relheight = 0.03, relx = 0.29, rely = 0.181)
status_com.bind("<<ComboboxSelected>>", search)
my_tree.bind("<ButtonRelease-1>")
threading.Thread(target=search(1)).start()
search_box()
# a = search_in_db
# root.bind('<Configure>',resizer)
root.mainloop()