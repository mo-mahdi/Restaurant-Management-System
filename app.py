from tkinter import *
import random
import sys
import time
import datetime
from tkinter import messagebox, ttk
import win32api
import win32print
import tempfile
import pandas as pd
import numpy as np
import re
import xlsxwriter
import sqlite3
from tkinter.messagebox import showinfo
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
import pickle 
# =====================================================================================================
#sys.stdout = open ("file.txt", "w+")
root=Tk()
root.geometry("1600x700+0+0")
root.title("Restaurant Management System")
root.configure(background='blue')
# =====================================================================================================
#                                FRAMES
# =====================================================================================================
MainFrame = Frame(root, width=1600, height=600, bd=10, relief="raise")
MainFrame.pack(side=TOP)

f1 = Frame(MainFrame, width=400, height=600, bd=10, relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(MainFrame, width=400, height=600, bd=10, relief=SUNKEN)
f2.pack(side=LEFT)

f3 = Frame(MainFrame, width=400, height=600, bd=10, relief=SUNKEN)
f3.pack(side=LEFT)

f3Top = Frame(f3, width=400, height=300, bd=10, relief="raise")
f3Top.pack(side=TOP)
f3Bottom = Frame(f3, width=400, height=300,bd=10, relief="raise")
f3Bottom.pack(side=BOTTOM)

f4 = Frame(MainFrame, width=400, height=600, bd=10, relief=SUNKEN)
f4.pack(side=LEFT)
# ======================================================================================================
#                                VARIABLES
#=======================================================================================================   
var1 = IntVar()
var2 = IntVar(); var3 = IntVar(); var4 = IntVar(); var5 = IntVar(); var6 = IntVar(); var7 = IntVar();var8 = IntVar()
var9 = IntVar(); var10 = IntVar(); var11 = IntVar(); var12 = IntVar(); var13 = IntVar();var14 = IntVar(); 
var15 = IntVar(); var16 = IntVar(); var17 = IntVar(); var18 = IntVar(); var19 = IntVar(); var20 = IntVar()
var21 = IntVar(); var22 = IntVar(); var23 = IntVar(); var24 = IntVar(); var25 = IntVar(); var26 = IntVar() 
var27 = IntVar(); var28 = IntVar(); var29 = IntVar(); var30 = IntVar(); var31 = IntVar(); var32 = IntVar()
var33 = IntVar(); var34 = IntVar(); var35 = IntVar(); var36 = IntVar(); var37 = IntVar(); var38 = IntVar()
var39 = IntVar(); var40 = IntVar(); var41 = IntVar(); var42 = IntVar(); var43 = IntVar(); var44 = IntVar()
var45 = IntVar(); var46 = IntVar(); var47 = IntVar(); var48 = IntVar(); var49 = IntVar(); var50 = IntVar()
var51 = IntVar(); var52 = IntVar(); var53 = IntVar(); var54 = IntVar(); var55 = IntVar(); var56 = IntVar()
var57 = IntVar(); var58 = IntVar(); var59 = IntVar(); var60 = IntVar(); var61 = IntVar(); var62 = IntVar()
var63 = IntVar(); var64 = IntVar(); var65 = IntVar(); var66 = IntVar(); var67 = IntVar(); var68 = IntVar()
var100 = IntVar()

var_num_list = [var1,var2,var3,var4,var5,var6,var7,var8,var9,var10,var11,var12,var13,var14,var15,var16,var17,
var18,var19,var20,var21,var22, var23, var24, var25,var26, var27, var28, var29, var30,var31, var32,
var33,var34, var35, var36, var37, var38,var39, var40, var41,var42, var43, var44, var45, var46,var47,var48, var49,var50,
var51,var52, var53, var54, var55, var56, var57,var58, var59,var60, var61, var62, var63,var64, var65,var66, var67, var68]

for key in var_num_list:
    key.set(0)
#====================================BOTTOM FRAME : FRAME 1 VARIABLES====================================================================
varveeta=StringVar();varbaket_botatos=StringVar();varneston=StringVar();varcery = StringVar();varroomy_cheese = StringVar()
varroomy_lanchon=StringVar();varveeta_keshta=StringVar();varlanchon=StringVar();varbeef=StringVar();varsandwich_sohba=StringVar()
varmix_meats = StringVar();varomlet_neston = StringVar();varomlet_lanchon = StringVar();varroomy_cery_farm = StringVar()
varroomy_cery = StringVar();varlanchon_veta = StringVar();varveeta_eggs = StringVar();varrolls_mekseeky = StringVar()
#====================================BOTTOM FRAME : FRAME 2 TOP FRAME VARIABLES==========================================================

varhalawa_sada = StringVar();varhalawa_keshta = StringVar();varhalawa_cery = StringVar();varmeraba_sada = StringVar()
varmeraba_keshta = StringVar();varmeraba_cery = StringVar();varhunny_sada = StringVar();varhunny_keshta = StringVar()
varhunny_cery = StringVar();varkokteil_helw = StringVar()
#====================================BOTTOM FRAME : FRAME 2 BOTTOM FRAME VARIABLES======================================================
varTotal = StringVar()
varPM = StringVar()
#====================================BOTTOM FRAME : FRAME 3 VARIABLES===================================================================
varfoul = StringVar();varfoul_sogok = StringVar();varfoul_ta3 = StringVar();vareggs_rolls_big = StringVar();varfoul_zebda= StringVar()
varfoul_neston = StringVar();varfoul_eggs = StringVar();varfoul_keshta = StringVar();varta3 = StringVar();vareggs_rolls_small= StringVar()
varta3_chebs = StringVar();varbotatos_clo_slo = StringVar();varomlet_egg = StringVar();varneston_eggs = StringVar();varta3_eggs = StringVar()
varchebs = StringVar();varbotatos_farm = StringVar();varomlet_farm = StringVar();varboiled_eggs = StringVar()
#====================================BOTTOM FRAME : FRAME 4 VARIABLES==================================================
varborger_sada = StringVar();varborger_eggs = StringVar();varborger_eggs_roomy = StringVar();varkofta_sada = StringVar()
varkebda = StringVar();varchecken_baneh = StringVar();varroomy_baneh = StringVar();varcheese_borger_double = StringVar()
varfarm_nar = StringVar();varalagreek = StringVar();varta3_nar = StringVar();varroomy_cheese_nar = StringVar();varlanchon_nar = StringVar()
varroomy_cery_chebs_nar = StringVar();varroomy_lanchon_nar = StringVar();varkresby = StringVar();varcheese_kresby = StringVar()
varkebda_eskandarany = StringVar();varborger_double = StringVar();varcheese_makli = StringVar();varborger_farm = StringVar()

var_item_list = [
varveeta,varbaket_botatos,varneston,varcery,varroomy_cheese,varroomy_lanchon,varveeta_keshta,varlanchon,varbeef,varsandwich_sohba,varmix_meats,
varomlet_neston,varomlet_lanchon,varroomy_cery_farm,varroomy_cery,varlanchon_veta,varveeta_eggs,varrolls_mekseeky,varcheese_makli,
varfoul, varfoul_ta3, varfoul_sogok, vareggs_rolls_big, vareggs_rolls_small, varfoul_zebda, varfoul_neston, varfoul_eggs, varfoul_keshta,
varta3, varta3_chebs, varbotatos_clo_slo, varomlet_egg, varneston_eggs, varta3_eggs, varchebs, varbotatos_farm, varomlet_farm, varboiled_eggs, 
varhalawa_sada, varhalawa_keshta, varhalawa_cery, varmeraba_sada, varmeraba_keshta, varmeraba_cery, varhunny_sada, varhunny_keshta, 
varhunny_cery, varkokteil_helw, varborger_sada, varborger_eggs, varborger_eggs_roomy, varkofta_sada, varkebda, varchecken_baneh, varroomy_baneh,
varcheese_borger_double, varfarm_nar, varalagreek, varta3_nar, varroomy_cheese_nar, varlanchon_nar, varroomy_cery_chebs_nar,
varroomy_lanchon_nar, varkresby, varcheese_kresby, varkebda_eskandarany, varborger_double, varborger_farm, varTotal]

for key in var_item_list:
    key.set(0)
#================================================================================
#                       Database
# ================================================================================

connection = sqlite3.connect('items.db')
c = connection.cursor()

temp_1 = 1

def sohw_current_price(item_id_num):
    showinfo(title='Current Price', message='Current Price is {}: '.format(sql_fetch_item_price(item_id_num)))

def sohw_update_status(new_price):
    showinfo(title='Info', message='Price Updated to {}'.format(new_price))

def show_update_name_status(new_name):
    showinfo(title='Info', message='Name Updated to {}'.format(new_name))

def show_deletion_status(serial):
    showinfo(title='Info', message='Order {} has been deleted'.format(serial))

def set_temp_1(data):
    global temp_1
    temp_1 = data
    sohw_current_price(data)

def sql_update_price(new_price, temp_1):
    
    c.execute("""UPDATE items SET price = ? WHERE item_id_num = ?;""", (new_price,temp_1))
    connection.commit()
    sohw_update_status(new_price)

def sql_update_item_name(new_name, item_id_num):
    
    c.execute("""UPDATE items SET item_name = ? WHERE item_id_num = ?;""", (new_name,item_id_num))
    connection.commit()
    show_update_name_status(new_name)
    
def sql_replace_price_window():
    
    replace_root = Tk()
    replace_root.geometry("700x100+0+0")
    replace_root.title("Price Change")

    mainFrame = Frame(replace_root, width=300, height=300)
    mainFrame.pack(side=TOP)

    Label(mainFrame, text="Enter Item ID: ").pack(side=LEFT)
    ent_1 = Entry(mainFrame)
    ent_1.pack(side=LEFT)
    btn_1 = Button(mainFrame, text="Submit ID", command=(lambda: set_temp_1(ent_1.get())))
    btn_1.pack(side=LEFT)

    Label(mainFrame, text="Enter New Price: ").pack(side=LEFT)
    ent_2 = Entry(mainFrame)
    ent_2.pack(side=LEFT)
    btn_2 = Button(mainFrame, text="Submit Price", command = (lambda: sql_update_price(ent_2.get(),temp_1)))
    btn_2.pack(side=LEFT)

    replace_root.mainloop()

temp_2 = 1

def set_temp_2(data):
    global temp_2
    temp_2 = data
    
def sql_replace_item_name_window():
    
    replace_name_root = Tk()
    replace_name_root.geometry("700x100+0+0")
    replace_name_root.title("Name Change")

    mainFrame = Frame(replace_name_root, width=300, height=300)
    mainFrame.pack(side=TOP)

    Label(mainFrame, text="Enter Item ID: ").pack(side=LEFT)
    ent_1 = Entry(mainFrame)
    ent_1.pack(side=LEFT)
    btn_1 = Button(mainFrame, text="Submit ID", command=(lambda: set_temp_2(ent_1.get())))
    btn_1.pack(side=LEFT)

    Label(mainFrame, text="Enter New Name: ").pack(side=LEFT)
    ent_2 = Entry(mainFrame)
    ent_2.pack(side=LEFT)
    btn_2 = Button(mainFrame, text="Submit Name", command = (lambda: sql_update_item_name(ent_2.get(),temp_2)))
    btn_2.pack(side=LEFT)

    replace_name_root.mainloop()

def sql_fetch_item_name(item_id):

    sql = "SELECT item_name FROM items WHERE item_id = '{}' LIMIT 1".format(item_id)
    c.execute(sql)
    result = c.fetchone()
    if result != None:
        return result[0]
    else: return False

def sql_fetch_item_price(item_id_num):
    
    sql = "SELECT price FROM items WHERE item_id_num = '{}' LIMIT 1".format(item_id_num)
    c.execute(sql)
    result = c.fetchone()
    if result != None:
        return result[0]
    else: return False

def sql_fetch_item_serial_id(item_name):
    
    sql = "SELECT item_id FROM items WHERE item_name = '{}' LIMIT 1".format(item_name)
    c.execute(sql)
    result = c.fetchone()
    if result != None:
        return result[0]
    else: return False


def sql_fetch_item_id_num(item_name):
    
    sql = "SELECT item_id_num FROM items WHERE item_name = '{}' LIMIT 1".format(item_name)
    c.execute(sql)
    result = c.fetchone()
    if result != None:
        return result[0]
    else: return False

def add_delivery_cost_to_reciept(delivery_cost):
    
    Receipt(delivery_cost)

def add_delivery_cost():

    rooor = Tk()
    rooor.geometry("400x100+0+0")
    rooor.title("ADD DELIVERY COST")

    mainFrame = Frame(rooor, width=300, height=300)
    mainFrame.pack(side=TOP)

    Label(mainFrame, text="Enter Delivery Cost: ").pack(side=LEFT)
    ent_4 = Entry(mainFrame)
    ent_4.pack(side=LEFT)
    btn_4 = Button(mainFrame, text="Submit Cost", command=(lambda: add_delivery_cost_to_reciept(ent_4.get())))
    btn_4.pack(side=LEFT)

    rooor.mainloop()
#========================EXIT FUNCTION======================================
def iExit():
    qExit = messagebox.askyesno("Restraunt Management","Do you want to quit ?")
    if qExit > 0:
        root.destroy()
        return     
#========================RESET FUNCTION======================================
def Reset():
    for key in var_item_list:
        key.set(0)

    for key in var_num_list:
        key.set(0) 

    for key in txt_list:
        key.configure(state=DISABLED)    
# ===============================================================
#                       RECEIPT FUMCTION
# ================================================================
Receipt_Ref = StringVar()
DateofOrder = StringVar()
date_and_time = ""
def get_date_and_time():
    global date_and_time_list
    DateofOrder.set(datetime.datetime.now().strftime("%Y-%m-%d\t %H:%M:%S"))
    date_and_time = DateofOrder.get()
    return date_and_time
    
printers = win32print.EnumPrinters(2)

def installed_printer():
    for p in printers:
        return p

printerdef = ''

def locprinter():
    pt = Toplevel()
    pt.geometry("250x250")
    pt.title("choose printer")
    var1 = StringVar()
    LABEL = Label(pt, text="select Printer").pack()
    PRCOMBO = ttk.Combobox(pt, width = 35, textvariable = var1)
    print_list = []
    for i in printers:
        print_list.append(i[2])
    print (print_list)
    #put printers in combobox
    PRCOMBO['values'] = print_list
    PRCOMBO.pack()
    def select():
        global installed_printer
        printerdef = PRCOMBO.get()
        pt.destroy()
    BUTTON = ttk.Button(pt, text="Done", command=select).pack()

connection_2 = sqlite3.connect('sales.db')
con = connection_2.cursor()
def create_table():
    con.execute("CREATE TABLE IF NOT EXISTS sales(item_id TEXT,item_id_num INT, item_name TEXT, item_count INT, price INT, date TEXT,time TEXT, value INT, oreder_serial TEXT )")

create_table()

def sales_data_base_insert():
    global date_and_time_list
    for key in var_item_list[:-1]:
        if int(key.get()) != 0:
            item_name = item_list[var_item_list.index(key)].cget("text")
            item_count = key.get()
            item_id = sql_fetch_item_serial_id(item_name)
            item_id_num = sql_fetch_item_id_num(item_name)
            price = sql_fetch_item_price(item_id_num)
            date = get_date_and_time().split("\t")[0] 
            time = get_date_and_time().split("\t")[1] 
            value = float(item_count) * float(price) 
            oreder_serial = Receipt_Ref.get()
            sql = """INSERT INTO sales(item_id, item_id_num, item_name,item_count, price,date,time,value,oreder_serial) VALUES ("{}", "{}", "{}", "{}","{}", "{}", "{}", "{}", "{}");""".format(item_id, item_id_num, item_name,item_count, price,date,time,value,oreder_serial)
            con.execute(sql)
            connection_2.commit()
            print("insert is done")

def get_order_number():

        try:

            pk_file = open('order_number_pickle', 'rb')
            order_number_dict = pickle.load(pk_file)
            pk_file.close()

            if (order_number_dict["order_number"] <= 300):

                ord_num = order_number_dict["order_number"]
                order_number_dict["order_number"] = order_number_dict["order_number"] + 1
                pk_file = open('order_number_pickle', 'wb')
                pickle.dump(order_number_dict, pk_file)
                pk_file.close()
                return ord_num

            elif (order_number_dict["order_number"] > 300):

                order_number_dict["order_number"] = 1
                pk_file = open('order_number_pickle', 'wb')
                pickle.dump(order_number_dict, pk_file)
                pk_file.close()
                pk_file = open('order_number_pickle', 'rb')
                order_number_dict = pickle.load(pk_file)
                pk_file.close()
                ord_num = order_number_dict["order_number"]
                order_number_dict["order_number"] = order_number_dict["order_number"] + 1
                pk_file = open('order_number_pickle', 'wb')
                pickle.dump(order_number_dict, order_number_pickle)
                pk_file.close()
                return ord_num
        except:

            order_number_dict = {"order_number": 1}
            pk_file = open('order_number_pickle', 'wb')
            pickle.dump(order_number_dict, pk_file)
            pk_file.close()
            pk_file = open('order_number_pickle', 'rb')
            order_number_dict = pickle.load(pk_file)
            pk_file.close()
            ord_num = order_number_dict["order_number"]
            order_number_dict["order_number"] = order_number_dict["order_number"] + 1
            pk_file = open('order_number_pickle', 'wb')
            pickle.dump(order_number_dict, pk_file)
            pk_file.close()
            return ord_num

def Receipt(delivery_cost):
    
    global iTotal
    global date_and_time
    roor = Tk()
    roor.geometry("400x500+0+0")

    menubar = Menu(roor)
    roor.config(menu=menubar)

    file_menu = Menu(menubar)
    menubar.add_cascade(label="File", menu = file_menu)
    file_menu.add_command(label="printer", command=locprinter)

    f1 = Frame(roor, width = 100, height = 300, bd = 4, relief = "raise")
    f1.pack()
    lblReceipt = Label(f1, font=('arial', 9, 'bold'), text="Receipt", bd=2, anchor='w')
    lblReceipt.grid(row=0, column=0, sticky=W)
    txtReceipt = Text(f1, width=25, height=20, bg="white", bd=8, font=('arial', 12, 'bold'))
    txtReceipt.grid(row=1, column=0)
    txtReceipt.delete("1.0", END)
    x = random.randint(1000, 500890)
    randomRef = str(x)
    Receipt_Ref.set(randomRef)
    ord_num = str(get_order_number())
    txtReceipt.insert(END, 'Receipt Ref \t' + Receipt_Ref.get() + '\n' )
    txtReceipt.insert(END, 'Order Number \t' + ord_num + '\n' )
    txtReceipt.insert(END, get_date_and_time() + "\n\n" )
    txtReceipt.insert(END, 'الصنـــف \t' + "العــدد \n\n")
    
    for key in var_item_list[:-1]:
        if int(key.get()) != 0:
            txtReceipt.insert(END, '{}  \t'.format(item_list[var_item_list.index(key)].cget("text")) + key.get() + "\n")
    
    if (delivery_cost != False):
        txtReceipt.insert(END, '\nDelivery Cost \t' + delivery_cost + '\n' )
        iTotal += int(delivery_cost)
        striTotal = str(iTotal)
        varTotal.set(striTotal)

    else:
        pass

    txtReceipt.insert(END, '\nالاجمـــــالي \t' + varTotal.get())

    def INFO():

        printText = txtReceipt.get("1.0", END)
        workbook = xlsxwriter.Workbook("last_reciept.xlsx")
        worksheet1 = workbook.add_worksheet()
        worksheet1.set_column(0, 0, 30)
        worksheet1.set_margins(left=0.2,right=0.2,top=0.2,bottom=0.2)
        j = 0
        for i in printText.split("\n"):
            worksheet1.write(j,0,printText.split("\n")[j])
            j = j+1
        workbook.close()    
        win32api.ShellExecute(
        0,
        "print",
        "last_reciept.xlsx",
        '"%s"'%win32print.GetDefaultPrinter(),
        ".",
        0)

    def order_number_generation(): 
        
        workbook = xlsxwriter.Workbook("last_order_number.xlsx")
        worksheet1 = workbook.add_worksheet()
        worksheet1.set_margins(left=0.2,right=0.2,top=0.2,bottom=0.2)
        worksheet1.write(0,0,"ORD: {}".format(ord_num))
        workbook.close()
        win32api.ShellExecute(
        0,
        "print",
        "last_order_number.xlsx",
        '"%s"'%win32print.GetDefaultPrinter(),
        ".",
        0)

    Print_Button = Button(roor, text="Print Order", command = INFO).pack(side = BOTTOM) 
    Print_Button = Button(roor, text="Print Order Number", command = order_number_generation).pack(side = BOTTOM) 
    Save_Button = Button(roor, text="Save", command = sales_data_base_insert).pack(side = BOTTOM) 
    roor.mainloop()
#================================================PRICE LIST=======================================

def show_item_price(item_id_num):
    showinfo(title='Current Price', message='Current Price is {}: '.format(sql_fetch_item_price(item_id_num)))

def prompet_for_item_id():

    rooot = Tk()
    rooot.geometry("400x100+0+0")
    rooot.title("Price Info")

    mainFrame = Frame(rooot, width=300, height=300)
    mainFrame.pack(side=TOP)

    Label(mainFrame, text="Enter Item ID: ").pack(side=LEFT)
    ent_3 = Entry(mainFrame)
    ent_3.pack(side=LEFT)
    btn_3 = Button(mainFrame, text="Submit ID", command=(lambda: show_item_price(ent_3.get())))
    btn_3.pack(side=LEFT)

    rooot.mainloop()

def delete_order(serial):
    con.execute("""DELETE FROM sales WHERE oreder_serial = ?""", (serial,))
    connection_2.commit()
    show_deletion_status(serial)

def sql_delete_order_window():

    del_root = Tk()
    del_root.geometry("400x100+0+0")
    del_root.title("Delete Order")

    mainFrame = Frame(del_root, width=300, height=300)
    mainFrame.pack(side=TOP)

    Label(mainFrame, text="Enter Order Ref: ").pack(side=LEFT)
    ent_3 = Entry(mainFrame)
    ent_3.pack(side=LEFT)
    btn_3 = Button(mainFrame, text="Submit Ref", command=(lambda: delete_order(ent_3.get())))
    btn_3.pack(side=LEFT)

    del_root.mainloop()
    
# ===============================TOTAL FUNCTION===============================================
iTotal = 0
def TotalCost():

    global iTotal
    iTotal = 0
    for key in var_item_list:
        num = float(key.get())
        if num > 0:
            iTotal += num * sql_fetch_item_price((var_item_list.index(key) + 1))
        else:
            continue

    striTotal = str(iTotal)
    varTotal.set(striTotal)
#================================================================================
#                       CHECKBOX FUNCTION
# ================================================================================
def comand(var_num, txt_name, var_name):
    if var_num.get() == 1:
        txt_name.configure(state=NORMAL)
        var_name.set("")
    elif var_num.get() == 0:
        txt_name.configure(state=DISABLED)
        var_name.set("0")
#===================================Analysis=====================================
price_dict={}

for i in range(68):

    sql_fetch_name = "SELECT item_name FROM items WHERE item_id_num = '{}' LIMIT 1".format(str(i+1))
    c.execute(sql_fetch_name)
    name = c.fetchone()[0]
   
    '''sql_fetch_price = "SELECT price FROM items WHERE item_id_num = '{}' LIMIT 1".format(str(i+1))
    c.execute(sql_fetch_price)
    price = c.fetchone()[0]'''

    price = sql_fetch_item_price(str(i+1))
    
    price_dict[name] = price

def analysis():

    df = pd.read_sql_query("SELECT * FROM sales", connection_2)
    df["time"] = df["time"].str.replace(":[0-5][0-9]:[0-5][0-9]","")
    df = df[["item_name", "item_count", "price", "date", "time", "value"]]

    report_1 = df.groupby(["date",'time','item_name','item_count'])['value'].agg((np.sum, np.average))
    report_2 = df.groupby(["date",'item_name',"item_count"])['value'].agg((np.sum, np.average))
    report_3 = df.groupby(["date"])['value'].agg((np.sum, np.average))
    report_4 = df.groupby(["date",'time'])['value'].agg((np.sum, np.average))

    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template("report.html")
    
    report_1.rename(columns={"sum":"Total Value"},inplace=True)
    template_vars = {"title" : "Sales Report",
        "report_table": report_1.to_html()}
    html_out = template.render(template_vars)
    HTML(string=html_out).write_pdf("reportA.pdf",  stylesheets=["style.css"])

    report_2.rename(columns={"sum":"Total Value"},inplace=True)
    template_vars = {"title" : "Sales Report",
        "report_table": report_2.to_html()}
    html_out = template.render(template_vars)
    HTML(string=html_out).write_pdf("reportB.pdf",  stylesheets=["style.css"])

    report_3.rename(columns={"sum":"Total Value"},inplace=True)
    template_vars = {"title" : "Sales Report",
        "report_table": report_3.to_html()}
    html_out = template.render(template_vars)
    HTML(string=html_out).write_pdf("reportC.pdf",  stylesheets=["style.css"])

    report_4.rename(columns={"sum":"Total Value"},inplace=True)
    template_vars = {"title" : "Sales Report",
        "report_table": report_4.to_html()}
    html_out = template.render(template_vars)
    HTML(string=html_out).write_pdf("reportD.pdf",  stylesheets=["style.css"])

    #The following code is excuted if you want to print reports to excel sheets
    '''
    writer = pd.ExcelWriter('report_1.xlsx')
    report_1.to_excel(writer,'Sheet1')
    writer.save()
    writer = pd.ExcelWriter('report_2.xlsx')
    report_2.to_excel(writer,'Sheet1')
    writer.save()
    writer = pd.ExcelWriter('report_3.xlsx')
    report_3.to_excel(writer,'Sheet1')
    writer.save()
    writer = pd.ExcelWriter('report_4.xlsx')
    report_4.to_excel(writer,'Sheet1')
    writer.save()
    '''

menubar = Menu(root)
root.config(menu=menubar)

file_menu = Menu(menubar)
menubar.add_cascade(label="File", menu = file_menu)
file_menu.add_command(label="Update Reports", command=analysis)
file_menu.add_command(label="Change Item Price", command = sql_replace_price_window)
file_menu.add_command(label="Change Item Name", command = sql_replace_item_name_window)
file_menu.add_command(label="Delete Order from DataBase", command = sql_delete_order_window)
#================================================================================
#                       FRAME 1
# ===============================================================================
lblMeal = Label(f1,font=("arial",22,'bold'), text="الجبن")
lblMeal.grid(row=0, column=0)

veeta = Checkbutton(f1, text=sql_fetch_item_name("veeta"), variable=var1, onvalue=1, offvalue=0, font=("arial",9, 'bold'),
command=lambda: comand(var1,txtveeta,varveeta))
veeta.grid(row=1, column=0, sticky = W)
txtveeta = Entry(f1, font=("arial", 9, 'bold'), bd=8, textvariable = varveeta, width=3, justify="right",state=DISABLED)
txtveeta.grid(row=1, column=2)

baket_botatos = Checkbutton(f1, text=sql_fetch_item_name("baket_botatos"), variable=var2, onvalue=1, offvalue=0, font=("arial",9, 'bold'),
command=lambda: comand(var2,txtbaket_botatos,varbaket_botatos))
baket_botatos.grid(row=2, column=0, sticky = W)
txtbaket_botatos = Entry(f1, font=("arial", 9, 'bold'), bd=8, textvariable = varbaket_botatos, width=3, justify="right",state=DISABLED)
txtbaket_botatos.grid(row=2, column=2)

neston = Checkbutton(f1, text=sql_fetch_item_name("neston"), variable=var3, onvalue=1, offvalue=0, font=("arial",9, 'bold'),
command=lambda: comand(var3,txtneston,varneston))
neston.grid(row=3, column=0, sticky = W)
txtneston = Entry(f1, font=("arial", 9, 'bold'), bd=8, textvariable = varneston, width=3, justify="right",state=DISABLED)
txtneston.grid(row=3, column=2)

cery = Checkbutton(f1, text=sql_fetch_item_name("cery"), variable=var4, onvalue=1, offvalue=0, font=("arial",9, 'bold'),
command=lambda: comand(var4,txtcery,varcery))
cery.grid(row=4, column=0, sticky = W)
txtcery = Entry(f1, font=("arial", 9, 'bold'), bd=8, textvariable = varcery, width=3, justify="right",state=DISABLED)
txtcery.grid(row=4, column=2)

roomy_cheese = Checkbutton(f1, text=sql_fetch_item_name("roomy_cheese"), variable=var5, onvalue=1, offvalue=0, font=("arial",9, 'bold'),
command=lambda: comand(var5,txtroomy_cheese,varroomy_cheese))
roomy_cheese.grid(row=5, column=0, sticky = W)
txtroomy_cheese = Entry(f1, font=("arial", 9, 'bold'), bd=8, textvariable = varroomy_cheese, width=3, justify="right",state=DISABLED)
txtroomy_cheese.grid(row=5, column=2)

roomy_lanchon = Checkbutton(f1, text=sql_fetch_item_name("roomy_lanchon"), variable=var6, onvalue=1, offvalue=0, font=("arial",9, 'bold'),
command=lambda: comand(var6,txtroomy_lanchon,varroomy_lanchon))
roomy_lanchon.grid(row=6, column=0, sticky = W)
txtroomy_lanchon = Entry(f1, font=("arial", 9, 'bold'), bd=8, textvariable = varroomy_lanchon, width=3, justify="right",state=DISABLED)
txtroomy_lanchon.grid(row=6, column=2)

veeta_keshta = Checkbutton(f1, text=sql_fetch_item_name("veeta_keshta"), variable=var7, onvalue=1, offvalue=0, font=("arial",9, 'bold'),
command=lambda: comand(var7,txtveeta_keshta,varveeta_keshta))
veeta_keshta.grid(row=7, column=0, sticky = W)
txtveeta_keshta = Entry(f1, font=("arial", 9, 'bold'), bd=8, textvariable = varveeta_keshta, width=3, justify="right",state=DISABLED)
txtveeta_keshta.grid(row=7, column=2)

lanchon = Checkbutton(f1, text=sql_fetch_item_name("lanchon"), variable=var8, onvalue=1, offvalue=0, font=("arial",9, 'bold'),
command=lambda: comand(var8,txtlanchon,varlanchon))
lanchon.grid(row=8, column=0, sticky = W)
txtlanchon = Entry(f1, font=("arial", 9, 'bold'), bd=8, textvariable = varlanchon, width=3, justify="right",state=DISABLED)
txtlanchon.grid(row=8, column=2)

beef = Checkbutton(f1, text=sql_fetch_item_name("beef"), variable=var9, onvalue=1, offvalue=0, font=("arial",9, 'bold'),
command=lambda: comand(var9,txtbeef,varbeef))
beef.grid(row=9, column=0, sticky = W)
txtbeef = Entry(f1, font=("arial", 9, 'bold'), bd=8, textvariable = varbeef, width=3, justify="right",state=DISABLED)
txtbeef.grid(row=9, column=2)

sandwich_sohba = Checkbutton(f1, text=sql_fetch_item_name("sandwich_sohba"), variable=var10, onvalue=1, offvalue=0, font=("arial",9, 'bold'),
command=lambda: comand(var10,txtsandwich_sohba,varsandwich_sohba))
sandwich_sohba.grid(row=10, column=0, sticky = W)
txtsandwich_sohba = Entry(f1, font=("arial", 9, 'bold'), bd=8, textvariable = varsandwich_sohba, width=3, justify="right",state=DISABLED)
txtsandwich_sohba.grid(row=10, column=2)

mix_meats = Checkbutton(f1, text=sql_fetch_item_name("mix_meats"), variable=var11, onvalue=1, offvalue=0, font=("arial",9, 'bold'),
command=lambda: comand(var11,txtmix_meats,varmix_meats))
mix_meats.grid(row=11, column=0, sticky = W)
txtmix_meats = Entry(f1, font=("arial", 9, 'bold'), bd=8, textvariable = varmix_meats, width=3, justify="right",state=DISABLED)
txtmix_meats.grid(row=11, column=2)

omlet_neston = Checkbutton(f1, text=sql_fetch_item_name("omlet_neston"), variable=var12, onvalue=1, offvalue=0, font=("arial",9, 'bold'),
command=lambda: comand(var12,txtomlet_neston,varomlet_neston))
omlet_neston.grid(row=12, column=0, sticky = W)
txtomlet_neston = Entry(f1, font=("arial", 9, 'bold'), bd=8, textvariable = varomlet_neston, width=3, justify="right",state=DISABLED)
txtomlet_neston.grid(row=12, column=2)

omlet_lanchon = Checkbutton(f1, text=sql_fetch_item_name("omlet_lanchon"), variable=var13, onvalue=1, offvalue=0, font=("arial",9, 'bold'),
command=lambda: comand(var13,txtomlet_lanchon,varomlet_lanchon))
omlet_lanchon.grid(row=13, column=0, sticky = W)
txtomlet_lanchon = Entry(f1, font=("arial", 9, 'bold'), bd=8, textvariable = varomlet_lanchon, width=3, justify="right",state=DISABLED)
txtomlet_lanchon.grid(row=13, column=2)

roomy_cery_farm = Checkbutton(f1, text=sql_fetch_item_name("roomy_cery_farm"), variable=var14, onvalue=1, offvalue=0, font=("arial",9, 'bold'),
command=lambda: comand(var14,txtroomy_cery_farm,varroomy_cery_farm))
roomy_cery_farm.grid(row=14, column=0, sticky = W)
txtroomy_cery_farm = Entry(f1, font=("arial", 9, 'bold'), bd=8, textvariable = varroomy_cery_farm, width=3, justify="right",state=DISABLED)
txtroomy_cery_farm.grid(row=14, column=2)

roomy_cery = Checkbutton(f1, text=sql_fetch_item_name("roomy_cery"), variable=var15, onvalue=1, offvalue=0, font=("arial",9, 'bold'), 
command=lambda: comand(var15,txtroomy_cery,varroomy_cery))
roomy_cery.grid(row=15, column=0, sticky = W)
txtroomy_cery = Entry(f1, font=("arial", 9, 'bold'), bd=8, textvariable = varroomy_cery, width=3, justify="right",state=DISABLED)
txtroomy_cery.grid(row=15, column=2)

lanchon_veta = Checkbutton(f1, text=sql_fetch_item_name("lanchon_veta"), variable=var16, onvalue=1, offvalue=0, font=("arial",9, 'bold'), 
command=lambda: comand(var16,txtlanchon_veta,varlanchon_veta))
lanchon_veta.grid(row=16, column=0, sticky = W)
txtlanchon_veta = Entry(f1, font=("arial", 9, 'bold'), bd=8, textvariable = varlanchon_veta, width=3, justify="right",state=DISABLED)
txtlanchon_veta.grid(row=16, column=2)

veeta_eggs = Checkbutton(f1, text=sql_fetch_item_name("veeta_eggs"), variable=var17, onvalue=1, offvalue=0, font=("arial",9, 'bold'),
command=lambda: comand(var17,txtveeta_eggs,varveeta_eggs))
veeta_eggs.grid(row=17, column=0, sticky = W)
txtveeta_eggs = Entry(f1, font=("arial", 9, 'bold'), bd=8, textvariable = varveeta_eggs, width=3, justify="right",state=DISABLED)
txtveeta_eggs.grid(row=17, column=2)

rolls_mekseeky = Checkbutton(f1, text=sql_fetch_item_name("rolls_mekseeky"), variable=var18, onvalue=1, offvalue=0, font=("arial",9, 'bold'), 
command=lambda: comand(var18,txtrolls_mekseeky,varrolls_mekseeky))
rolls_mekseeky.grid(row=18, column=0, sticky = W)
txtrolls_mekseeky = Entry(f1, font=("arial", 9, 'bold'), bd=8, textvariable = varrolls_mekseeky, width=3, justify="right",state=DISABLED)
txtrolls_mekseeky.grid(row=18, column=2)

cheese_makli = Checkbutton(f1, text=sql_fetch_item_name("cheese_makli"), variable=var67, onvalue=1, offvalue=0, font=("arial",9, 'bold'), 
command=lambda: comand(var67,txtcheese_makli,varcheese_makli))
cheese_makli.grid(row=20, column=0, sticky = W)
txtcheese_makli = Entry(f1, font=("arial", 9, 'bold'), bd=8, textvariable = varcheese_makli, width=3, justify="right",state=DISABLED)
txtcheese_makli.grid(row=20, column=1)
#================================================================================
#                       FRAME 2
# ================================================================================
lblfouls = Label(f2,font=("arial",16,'bold'), text="فول وفلافل")
lblfouls.grid(row=0, column=0)

foul = Checkbutton(f2, text=sql_fetch_item_name("foul"), variable=var29, onvalue=1, offvalue=0, font=("arial",9, 'bold'), 
command=lambda: comand(var29,txtfoul,varfoul))
foul.grid(row=1, column=0, sticky = W)
txtfoul = Entry(f2, font=("arial", 9, 'bold'), bd=8, textvariable = varfoul, width=3, justify="right",state=DISABLED)
txtfoul.grid(row=1, column=2)

foul_ta3 = Checkbutton(f2, text=sql_fetch_item_name("foul_ta3"), variable=var30, onvalue=1, offvalue=0, font=("arial",9, 'bold'),
command=lambda: comand(var30,txtfoul_ta3,varfoul_ta3))
foul_ta3.grid(row=2, column=0, sticky = W)
txtfoul_ta3 = Entry(f2, font=("arial", 9, 'bold'), bd=8, textvariable = varfoul_ta3, width=3, justify="right",state=DISABLED)
txtfoul_ta3.grid(row=2, column=2)

foul_sogok = Checkbutton(f2, text=sql_fetch_item_name("foul_sogok"), variable=var31, onvalue=1, offvalue=0, font=("arial",9, 'bold'),
 command=lambda: comand(var31,txtfoul_sogok,varfoul_sogok))
foul_sogok.grid(row=3, column=0, sticky = W)
txtfoul_sogok = Entry(f2, font=("arial", 9, 'bold'), bd=8, textvariable = varfoul_sogok, width=3, justify="right",state=DISABLED)
txtfoul_sogok.grid(row=3, column=2)

eggs_rolls_big = Checkbutton(f2, text=sql_fetch_item_name("eggs_rolls_big"), variable=var32, onvalue=1, offvalue=0, font=("arial",9, 'bold'),
 command=lambda: comand(var32,txteggs_rolls_big,vareggs_rolls_big))
eggs_rolls_big.grid(row=4, column=0, sticky = W)
txteggs_rolls_big = Entry(f2, font=("arial", 9, 'bold'), bd=8, textvariable = vareggs_rolls_big, width=3, justify="right",state=DISABLED)
txteggs_rolls_big.grid(row=4, column=2)

eggs_rolls_small = Checkbutton(f2, text=sql_fetch_item_name("eggs_rolls_small"), variable=var38, onvalue=1, offvalue=0, font=("arial",9, 'bold'),
 command=lambda: comand(var38,txteggs_rolls_small,vareggs_rolls_small))
eggs_rolls_small.grid(row=5, column=0, sticky = W)
txteggs_rolls_small = Entry(f2, font=("arial", 9, 'bold'), bd=6, textvariable = vareggs_rolls_small, width=3, justify="right",state=DISABLED)
txteggs_rolls_small.grid(row=5, column=2)

foul_zebda = Checkbutton(f2, text=sql_fetch_item_name("foul_zebda"), variable=var33, onvalue=1, offvalue=0, font=("arial",9, 'bold'),
 command=lambda: comand(var33,txtfoul_zebda,varfoul_zebda))
foul_zebda.grid(row=6, column=0, sticky = W)
txtfoul_zebda = Entry(f2, font=("arial", 9, 'bold'), bd=8, textvariable = varfoul_zebda, width=3, justify="right",state=DISABLED)
txtfoul_zebda.grid(row=6, column=2)

foul_neston = Checkbutton(f2, text=sql_fetch_item_name("foul_neston"), variable=var34, onvalue=1, offvalue=0, font=("arial",9, 'bold'),
 command=lambda: comand(var34,txtfoul_neston,varfoul_neston))
foul_neston.grid(row=7, column=0, sticky = W)
txtfoul_neston = Entry(f2, font=("arial", 9, 'bold'), bd=8, textvariable = varfoul_neston, width=3, justify="right",state=DISABLED)
txtfoul_neston.grid(row=7, column=2)

foul_eggs = Checkbutton(f2, text=sql_fetch_item_name("foul_eggs"), variable=var35, onvalue=1, offvalue=0, font=("arial",9, 'bold'), 
 command=lambda: comand(var35,txtfoul_eggs,varfoul_eggs))
foul_eggs.grid(row=8, column=0, sticky = W)
txtfoul_eggs = Entry(f2, font=("arial", 9, 'bold'), bd=8, textvariable = varfoul_eggs, width=3, justify="right",state=DISABLED)
txtfoul_eggs.grid(row=8, column=2)

foul_keshta = Checkbutton(f2, text=sql_fetch_item_name("foul_keshta"), variable=var36, onvalue=1, offvalue=0, font=("arial",9, 'bold'),
 command=lambda: comand(var36,txtfoul_keshta,varfoul_keshta))
foul_keshta.grid(row=9, column=0, sticky = W)
txtfoul_keshta = Entry(f2, font=("arial", 9, 'bold'), bd=8, textvariable = varfoul_keshta, width=3, justify="right",state=DISABLED)
txtfoul_keshta.grid(row=9, column=2)

ta3 = Checkbutton(f2, text=sql_fetch_item_name("ta3"), variable=var37, onvalue=1, offvalue=0, font=("arial",9, 'bold'), 
command=lambda: comand(var37,txtta3,varta3))
ta3.grid(row=10, column=0, sticky = W)
txtta3 = Entry(f2, font=("arial", 9, 'bold'), bd=8, textvariable = varta3, width=3, justify="right",state=DISABLED)
txtta3.grid(row=10, column=2)

ta3_chebs = Checkbutton(f2, text=sql_fetch_item_name("ta3_chebs"), variable=var39, onvalue=1, offvalue=0, font=("arial",9, 'bold'),
 command=lambda: comand(var39,txtta3_chebs,varta3_chebs))
ta3_chebs.grid(row=11, column=0, sticky = W)
txtta3_chebs = Entry(f2, font=("arial", 9, 'bold'), bd=8, textvariable = varta3_chebs, width=3, justify="right",state=DISABLED)
txtta3_chebs.grid(row=11, column=2)

botatos_clo_slo = Checkbutton(f2, text=sql_fetch_item_name("botatos_clo_slo"), variable=var40, onvalue=1, offvalue=0, font=("arial",9, 'bold'),
 command=lambda: comand(var40,txtbotatos_clo_slo,varbotatos_clo_slo))
botatos_clo_slo.grid(row=12, column=0, sticky = W)
txtbotatos_clo_slo = Entry(f2, font=("arial", 9, 'bold'), bd=8, textvariable = varbotatos_clo_slo, width=3, justify="right",state=DISABLED)
txtbotatos_clo_slo.grid(row=12, column=2)

omlet_egg = Checkbutton(f2, text=sql_fetch_item_name("omlet_egg"), variable=var41, onvalue=1, offvalue=0, font=("arial",9, 'bold'),
 command=lambda: comand(var41,txtomlet_egg,varomlet_egg))
omlet_egg.grid(row=13, column=0, sticky = W)
txtomlet_egg = Entry(f2, font=("arial", 9, 'bold'), bd=8, textvariable = varomlet_egg, width=3, justify="right",state=DISABLED)
txtomlet_egg.grid(row=13, column=2)

neston_eggs = Checkbutton(f2, text=sql_fetch_item_name("neston_eggs"), variable=var42, onvalue=1, offvalue=0, font=("arial",9, 'bold'),
 command=lambda: comand(var42,txtneston_eggs,varneston_eggs))
neston_eggs.grid(row=14, column=0, sticky = W)
txtneston_eggs = Entry(f2, font=("arial", 9, 'bold'), bd=8, textvariable = varneston_eggs, width=3, justify="right",state=DISABLED)
txtneston_eggs.grid(row=14, column=2)

ta3_eggs = Checkbutton(f2, text=sql_fetch_item_name("ta3_eggs"), variable=var43, onvalue=1, offvalue=0, font=("arial",9, 'bold'),
 command=lambda: comand(var43,txtta3_eggs,varta3_eggs))
ta3_eggs.grid(row=15, column=0, sticky = W)
txtta3_eggs = Entry(f2, font=("arial", 9, 'bold'), bd=8, textvariable = varta3_eggs, width=3, justify="right",state=DISABLED)
txtta3_eggs.grid(row=15, column=2)

chebs = Checkbutton(f2, text=sql_fetch_item_name("chebs"), variable=var44, onvalue=1, offvalue=0, font=("arial",9, 'bold'),
 command=lambda: comand(var44,txtchebs,varchebs))
chebs.grid(row=16, column=0, sticky = W)
txtchebs = Entry(f2, font=("arial", 9, 'bold'), bd=8, textvariable = varchebs, width=3, justify="right",state=DISABLED)
txtchebs.grid(row=16, column=2)

botatos_farm = Checkbutton(f2, text=sql_fetch_item_name("botatos_farm "), variable=var45, onvalue=1, offvalue=0, font=("arial",9, 'bold'),
 command=lambda: comand(var45,txtbotatos_farm,varbotatos_farm))
botatos_farm.grid(row=17, column=0, sticky = W)
txtbotatos_farm = Entry(f2, font=("arial", 9, 'bold'), bd=8, textvariable = varbotatos_farm, width=3, justify="right",state=DISABLED)
txtbotatos_farm.grid(row=17, column=2)

omlet_farm = Checkbutton(f2, text=sql_fetch_item_name("omlet_farm"), variable=var46, onvalue=1, offvalue=0, font=("arial",9, 'bold'), 
command=lambda: comand(var46,txtomlet_farm,varomlet_farm))
omlet_farm.grid(row=18, column=0, sticky = W)
txtomlet_farm = Entry(f2, font=("arial", 9, 'bold'), bd=8, textvariable = varomlet_farm, width=3, justify="right",state=DISABLED)
txtomlet_farm.grid(row=18, column=2)

boiled_eggs= Checkbutton(f2, text=sql_fetch_item_name("boiled_eggs"), variable=var47, onvalue=1, offvalue=0, font=("arial",9, 'bold'),
 command=lambda: comand(var47,txtboiled_eggs,varboiled_eggs))
boiled_eggs.grid(row=19, column=0, sticky = W)
txtboiled_eggs = Entry(f2, font=("arial", 9, 'bold'), bd=8, textvariable = varboiled_eggs, width=3, justify="right",state=DISABLED)
txtboiled_eggs.grid(row=19, column=1)

#================================================================================
#                       FRAME 3 Top
# ================================================================================
lblMeal = Label(f3Top,font=("arial",22,'bold'), text="الحلو")
lblMeal.grid(row=0, column=0)

halawa_sada = Checkbutton(f3Top, text=sql_fetch_item_name("halawa_sada"), variable=var19, onvalue=1, offvalue=0, font=("arial",9, 'bold'),
 command=lambda: comand(var19,txthalawa_sada,varhalawa_sada))
halawa_sada.grid(row=1, column=0, sticky = W)
txthalawa_sada = Entry(f3Top, font=("arial",9, 'bold'), bd=8, textvariable = varhalawa_sada, width=4, justify="right",state=DISABLED)
txthalawa_sada.grid(row=1, column=2)

halawa_keshta = Checkbutton(f3Top, text=sql_fetch_item_name("halawa_keshta"), variable=var20, onvalue=1, offvalue=0, font=("arial",9, 'bold'),
 command=lambda: comand(var20,txthalawa_keshta,varhalawa_keshta))
halawa_keshta.grid(row=2, column=0, sticky = W)
txthalawa_keshta = Entry(f3Top, font=("arial",9, 'bold'), bd=8, textvariable = varhalawa_keshta, width=4, justify="right",state=DISABLED)
txthalawa_keshta.grid(row=2, column=2)

halawa_cery = Checkbutton(f3Top, text=sql_fetch_item_name("halawa_cery"), variable=var21, onvalue=1, offvalue=0, font=("arial",9, 'bold'),
 command=lambda: comand(var21,txthalawa_cery,varhalawa_cery))
halawa_cery.grid(row=3, column=0, sticky = W)
txthalawa_cery = Entry(f3Top, font=("arial",9, 'bold'), bd=8, textvariable = varhalawa_cery, width=4, justify="right",state=DISABLED)
txthalawa_cery.grid(row=3, column=2)

meraba_sada = Checkbutton(f3Top, text=sql_fetch_item_name("meraba_sada"), variable=var22, onvalue=1, offvalue=0, font=("arial",9, 'bold'),
 command=lambda: comand(var22,txtmeraba_sada,varmeraba_sada))
meraba_sada.grid(row=4, column=0, sticky = W)
txtmeraba_sada = Entry(f3Top, font=("arial",9, 'bold'), bd=8, textvariable = varmeraba_sada, width=4, justify="right",state=DISABLED)
txtmeraba_sada.grid(row=4, column=2)

meraba_keshta = Checkbutton(f3Top, text=sql_fetch_item_name("meraba_keshta"), variable=var23, onvalue=1, offvalue=0, font=("arial",9, 'bold'),
 command=lambda: comand(var23,txtmeraba_keshta,varmeraba_keshta))
meraba_keshta.grid(row=5, column=0, sticky = W)
txtmeraba_keshta = Entry(f3Top, font=("arial",9, 'bold'), bd=8, textvariable = varmeraba_keshta, width=4, justify="right",state=DISABLED)
txtmeraba_keshta.grid(row=5, column=2)

meraba_cery = Checkbutton(f3Top, text=sql_fetch_item_name("meraba_cery"), variable=var24, onvalue=1, offvalue=0, font=("arial",9, 'bold'),
 command=lambda: comand(var24,txtmeraba_cery,varmeraba_cery))
meraba_cery.grid(row=6, column=0, sticky = W)
txtmeraba_cery = Entry(f3Top, font=("arial",9, 'bold'), bd=8, textvariable = varmeraba_cery, width=4, justify="right",state=DISABLED)
txtmeraba_cery.grid(row=6, column=2)

hunny_sada = Checkbutton(f3Top, text=sql_fetch_item_name("hunny_sada"), variable=var25, onvalue=1, offvalue=0, font=("arial",9, 'bold'), 
 command=lambda: comand(var25,txthunny_sada,varhunny_sada))
hunny_sada.grid(row=7, column=0, sticky = W)
txthunny_sada = Entry(f3Top, font=("arial",9, 'bold'), bd=8, textvariable = varhunny_sada, width=4, justify="right",state=DISABLED)
txthunny_sada.grid(row=7, column=2)

hunny_keshta = Checkbutton(f3Top, text=sql_fetch_item_name("hunny_keshta"), variable=var26, onvalue=1, offvalue=0, font=("arial",9, 'bold'),
 command=lambda: comand(var26,txthunny_keshta,varhunny_keshta))
hunny_keshta.grid(row=8, column=0, sticky = W)
txthunny_keshta = Entry(f3Top, font=("arial",9, 'bold'), bd=8, textvariable = varhunny_keshta, width=4, justify="right",state=DISABLED)
txthunny_keshta.grid(row=8, column=2)

hunny_cery = Checkbutton(f3Top, text=sql_fetch_item_name("hunny_cery"), variable=var27, onvalue=1, offvalue=0, font=("arial",9, 'bold'), 
 command=lambda: comand(var27,txthunny_cery,varhunny_cery))
hunny_cery.grid(row=9, column=0, sticky = W)
txthunny_cery = Entry(f3Top, font=("arial",9, 'bold'), bd=8, textvariable = varhunny_cery, width=4, justify="right",state=DISABLED)
txthunny_cery.grid(row=9, column=2)

kokteil_helw = Checkbutton(f3Top, text=sql_fetch_item_name("kokteil_helw"), variable=var28, onvalue=1, offvalue=0, font=("arial",9, 'bold'),
 command=lambda: comand(var28,txtkokteil_helw,varkokteil_helw))
kokteil_helw.grid(row=10, column=0, sticky = W)
txtkokteil_helw = Entry(f3Top, font=("arial",9, 'bold'), bd=8, textvariable = varkokteil_helw, width=4, justify="right",state=DISABLED)
txtkokteil_helw.grid(row=10, column=2)
#================================================================================
#                       FRAME 2 BOTTOM
# ================================================================================
lblTotal = Label(f3Bottom, font=("arial", 12, 'bold'), text = "Total", bd=16, width=6, anchor='e')
lblTotal.grid(row=0,column=1)
txtTotal = Entry(f3Bottom, font=("arial", 12, 'bold'), bd=8, textvariable = varTotal, width=6, justify="right",state=DISABLED)
txtTotal.grid(row=0, column=2)
#======================================================================================================================
#                                     BUTTONS
#======================================================================================================================
btnprice=Button(f3Bottom,padx=18,pady=1, bd=14 ,fg="black",font=('arial' ,9,'bold'),width=10, text="SHOW ITEM PRICE", command = prompet_for_item_id)
btnprice.grid(row=0, column=0)

btnTotal = Button(f3Bottom, padx=18, pady=1, bd=14, fg="black", font=("arial", 9, 'bold'),
 width=10,text="TOTAL COST", command = TotalCost).grid(row=1, column=0)

btnReset=Button(f3Bottom,padx=15,pady=1,bd=14,fg="black",font=('arial',10,'bold'),width=3,text="RESET", command=Reset)
btnReset.grid(row=1,column=2)

btnExit=Button(f3Bottom,padx=15,pady=1,bd=14,fg="black",font=('arial',10,'bold'),width=3,text="EXIT", command = iExit)
btnExit.grid(row=1,column=1)

btnReceipt=Button(f3Bottom,padx=15,pady=2,bd=14,fg="black",font=('arial',9,'bold'),width=3,text="RECEIPT", command = lambda: Receipt(False))
btnReceipt.grid(row=2,column=1)

btnReceipt=Button(f3Bottom,padx=30,pady=2,bd=14,fg="black",font=('arial',10,'bold'),width=6,text="DELIVERY COST", command = add_delivery_cost)
btnReceipt.grid(row=2,column=0)
#================================================================================
#                       FRAME 4
# ================================================================================
lblMeal = Label(f4,font=("arial",14,'bold'), text="اللحوم والجريل")
lblMeal.grid(row=0, column=0)

borger_sada = Checkbutton(f4, text=sql_fetch_item_name("borger_sada"), variable=var48, onvalue=1, offvalue=0, font=("arial",9, 'bold'),
 command=lambda: comand(var48,txtborger_sada,varborger_sada))
borger_sada.grid(row=1, column=0, sticky = W)
txtborger_sada = Entry(f4, font=("arial", 9, 'bold'), bd=8, textvariable = varborger_sada, width=4, justify="right",state=DISABLED)
txtborger_sada.grid(row=1, column=2)

borger_eggs = Checkbutton(f4, text=sql_fetch_item_name("borger_eggs"), variable=var49, onvalue=1, offvalue=0, font=("arial",9, 'bold'),
 command=lambda: comand(var49,txtborger_eggs,varborger_eggs))
borger_eggs.grid(row=2, column=0, sticky = W)
txtborger_eggs = Entry(f4, font=("arial", 9, 'bold'), bd=8, textvariable = varborger_eggs, width=4, justify="right",state=DISABLED)
txtborger_eggs.grid(row=2, column=2)

borger_eggs_roomy = Checkbutton(f4, text=sql_fetch_item_name("borger_eggs_roomy"), variable=var50, onvalue=1, offvalue=0, font=("arial",9, 'bold'),
 command=lambda: comand(var50,txtborger_eggs_roomy,varborger_eggs_roomy))
borger_eggs_roomy.grid(row=3, column=0, sticky = W)
txtborger_eggs_roomy = Entry(f4, font=("arial", 9, 'bold'), bd=8, textvariable = varborger_eggs_roomy, width=4, justify="right",state=DISABLED)
txtborger_eggs_roomy.grid(row=3, column=2)

kofta_sada = Checkbutton(f4, text=sql_fetch_item_name("kofta_sada"), variable=var51, onvalue=1, offvalue=0, font=("arial",9, 'bold'),
 command=lambda: comand(var51,txtkofta_sada,varkofta_sada))
kofta_sada.grid(row=4, column=0, sticky = W)
txtkofta_sada = Entry(f4, font=("arial", 9, 'bold'), bd=8, textvariable = varkofta_sada, width=4, justify="right",state=DISABLED)
txtkofta_sada.grid(row=4, column=2)

kebda = Checkbutton(f4, text=sql_fetch_item_name("kebda"), variable=var52, onvalue=1, offvalue=0, font=("arial",9, 'bold'),
 command=lambda: comand(var52,txtkebda,varkebda))
kebda.grid(row=5, column=0, sticky = W)
txtkebda = Entry(f4, font=("arial", 9, 'bold'), bd=8, textvariable = varkebda, width=4, justify="right",state=DISABLED)
txtkebda.grid(row=5, column=2)

checken_baneh = Checkbutton(f4, text=sql_fetch_item_name("checken_baneh"), variable=var53, onvalue=1, offvalue=0, font=("arial",9, 'bold'), 
 command=lambda: comand(var53,txtchecken_baneh,varchecken_baneh))
checken_baneh.grid(row=6, column=0, sticky = W)
txtchecken_baneh = Entry(f4, font=("arial", 9, 'bold'), bd=8, textvariable = varchecken_baneh, width=4, justify="right",state=DISABLED)
txtchecken_baneh.grid(row=6, column=2)

roomy_baneh = Checkbutton(f4, text=sql_fetch_item_name("roomy_baneh"), variable=var54, onvalue=1, offvalue=0, font=("arial",9, 'bold'),
 command=lambda: comand(var54,txtroomy_baneh,varroomy_baneh))
roomy_baneh.grid(row=7, column=0, sticky = W)
txtroomy_baneh = Entry(f4, font=("arial", 9, 'bold'), bd=8, textvariable = varroomy_baneh, width=4, justify="right",state=DISABLED)
txtroomy_baneh.grid(row=7, column=2)

cheese_borger_double = Checkbutton(f4, text=sql_fetch_item_name("cheese_borger_double"), variable=var55, onvalue=1, offvalue=0, font=("arial",9, 'bold'),
 command=lambda: comand(var55,txtcheese_borger_double,varcheese_borger_double))
cheese_borger_double.grid(row=8, column=0, sticky = W)
txtcheese_borger_double = Entry(f4, font=("arial", 9, 'bold'), bd=8, textvariable = varcheese_borger_double, width=4, justify="right",state=DISABLED)
txtcheese_borger_double.grid(row=8, column=2)

farm_nar = Checkbutton(f4, text=sql_fetch_item_name("farm_nar"), variable=var56, onvalue=1, offvalue=0, font=("arial",9, 'bold'),
 command=lambda: comand(var56,txtfarm_nar,varfarm_nar))
farm_nar.grid(row=9, column=0, sticky = W)
txtfarm_nar = Entry(f4, font=("arial", 9, 'bold'), bd=8, textvariable = varfarm_nar, width=4, justify="right",state=DISABLED)
txtfarm_nar.grid(row=9, column=2)

alagreek = Checkbutton(f4, text=sql_fetch_item_name("alagreek"), variable=var57, onvalue=1, offvalue=0, font=("arial",9, 'bold'), 
 command=lambda: comand(var57,txtalagreek,varalagreek))
alagreek.grid(row=10, column=0, sticky = W)
txtalagreek = Entry(f4, font=("arial", 9, 'bold'), bd=8, textvariable = varalagreek, width=4, justify="right",state=DISABLED)
txtalagreek.grid(row=10, column=2)

ta3_nar = Checkbutton(f4, text=sql_fetch_item_name("ta3_nar"), variable=var58, onvalue=1, offvalue=0, font=("arial",9, 'bold'), 
 command=lambda: comand(var58,txtta3_nar,varta3_nar))
ta3_nar.grid(row=11, column=0, sticky = W)
txtta3_nar = Entry(f4, font=("arial", 9, 'bold'), bd=8, textvariable = varta3_nar, width=4, justify="right",state=DISABLED)
txtta3_nar.grid(row=11, column=2)

roomy_cheese_nar = Checkbutton(f4, text=sql_fetch_item_name("roomy_cheese_nar"), variable=var59, onvalue=1, offvalue=0, font=("arial",9, 'bold'), 
 command=lambda: comand(var59,txtroomy_cheese_nar,varroomy_cheese_nar))
roomy_cheese_nar.grid(row=12, column=0, sticky = W)
txtroomy_cheese_nar = Entry(f4, font=("arial", 9, 'bold'), bd=8, textvariable = varroomy_cheese_nar, width=4, justify="right",state=DISABLED)
txtroomy_cheese_nar.grid(row=12, column=2)

lanchon_nar = Checkbutton(f4, text=sql_fetch_item_name("lanchon_nar"), variable=var60, onvalue=1, offvalue=0, font=("arial",9, 'bold'), 
 command=lambda: comand(var60,txtlanchon_nar,varlanchon_nar))
lanchon_nar.grid(row=13, column=0, sticky = W)
txtlanchon_nar = Entry(f4, font=("arial", 9, 'bold'), bd=8, textvariable = varlanchon_nar, width=4, justify="right",state=DISABLED)
txtlanchon_nar.grid(row=13, column=2)

roomy_cery_chebs_nar = Checkbutton(f4, text=sql_fetch_item_name("roomy_cery_chebs_nar"), variable=var61, onvalue=1, offvalue=0, font=("arial",9, 'bold'), 
command=lambda: comand(var61,txtroomy_cery_chebs_nar,varroomy_cery_chebs_nar))
roomy_cery_chebs_nar.grid(row=14, column=0, sticky = W)
txtroomy_cery_chebs_nar = Entry(f4, font=("arial", 9, 'bold'), bd=8, textvariable = varroomy_cery_chebs_nar, width=4, justify="right",state=DISABLED)
txtroomy_cery_chebs_nar.grid(row=14, column=2)

roomy_lanchon_nar = Checkbutton(f4, text=sql_fetch_item_name("roomy_lanchon_nar"), variable=var62, onvalue=1, offvalue=0, font=("arial",9, 'bold'), 
command=lambda: comand(var62,txtroomy_lanchon_nar,varroomy_lanchon_nar))
roomy_lanchon_nar.grid(row=15, column=0, sticky = W)
txtroomy_lanchon_nar = Entry(f4, font=("arial", 9, 'bold'), bd=8, textvariable = varroomy_lanchon_nar, width=4, justify="right",state=DISABLED)
txtroomy_lanchon_nar.grid(row=15, column=2)

kresby = Checkbutton(f4, text=sql_fetch_item_name("kresby"), variable=var63, onvalue=1, offvalue=0, font=("arial",9, 'bold'), 
command=lambda: comand(var63,txtkresby,varkresby))
kresby.grid(row=16, column=0, sticky = W)
txtkresby = Entry(f4, font=("arial", 9, 'bold'), bd=8, textvariable = varkresby, width=4, justify="right",state=DISABLED)
txtkresby.grid(row=16, column=2)

cheese_kresby = Checkbutton(f4, text=sql_fetch_item_name("cheese_kresby"), variable=var64, onvalue=1, offvalue=0, font=("arial",9, 'bold'), 
command=lambda: comand(var64,txtcheese_kresby,varcheese_kresby))
cheese_kresby.grid(row=17, column=0, sticky = W)
txtcheese_kresby = Entry(f4, font=("arial", 9, 'bold'), bd=8, textvariable = varcheese_kresby, width=4, justify="right",state=DISABLED)
txtcheese_kresby.grid(row=17, column=2)

kebda_eskandarany = Checkbutton(f4, text=sql_fetch_item_name("kebda_eskandarany"), variable=var65, onvalue=1, offvalue=0, font=("arial",9, 'bold'), 
command=lambda: comand(var65,txtkebda_eskandarany,varkebda_eskandarany))
kebda_eskandarany.grid(row=18, column=0, sticky = W)
txtkebda_eskandarany = Entry(f4, font=("arial", 9, 'bold'), bd=8, textvariable = varkebda_eskandarany, width=4, justify="right",state=DISABLED)
txtkebda_eskandarany.grid(row=18, column=2)

borger_double = Checkbutton(f4, text=sql_fetch_item_name("borger_double"), variable=var66, onvalue=1, offvalue=0, font=("arial",9, 'bold'), 
command=lambda: comand(var66,txtborger_double,varborger_double))
borger_double.grid(row=19, column=0, sticky = W)
txtborger_double = Entry(f4, font=("arial", 9, 'bold'), bd=10, textvariable = varborger_double, width=4, justify="right",state=DISABLED)
txtborger_double.grid(row=19, column=1)

borger_farm = Checkbutton(f3Top, text=sql_fetch_item_name("borger_farm"), variable=var68, onvalue=1, offvalue=0, font=("arial",9, 'bold'), 
command=lambda: comand(var68,txtborger_farm,varborger_farm))
borger_farm.grid(row=12, column=0, sticky = W)
txtborger_farm = Entry(f3Top, font=("arial",9, 'bold'), bd=8, textvariable = varborger_farm, width=4, justify="right",state=DISABLED)
txtborger_farm.grid(row=12, column=1)

txt_list = [
txtveeta,txtbaket_botatos,txtneston,txtcery,txtroomy_cheese,txtroomy_lanchon,txtveeta_keshta,txtlanchon,txtbeef,txtsandwich_sohba,txtmix_meats,
txtomlet_neston,txtomlet_lanchon,txtroomy_cery_farm,txtroomy_cery,txtlanchon_veta,txtveeta_eggs,txtrolls_mekseeky,txtcheese_makli,
txtfoul, txtfoul_ta3, txtfoul_sogok, txteggs_rolls_big, txteggs_rolls_small, txtfoul_zebda, txtfoul_neston, txtfoul_eggs, txtfoul_keshta,
txtta3, txtta3_chebs, txtbotatos_clo_slo, txtomlet_egg, txtneston_eggs, txtta3_eggs, txtchebs, txtbotatos_farm, txtomlet_farm, txtboiled_eggs, 
txthalawa_sada, txthalawa_keshta, txthalawa_cery, txtmeraba_sada, txtmeraba_keshta, txtmeraba_cery, txthunny_sada, txthunny_keshta, 
txthunny_cery, txtkokteil_helw, txtborger_sada, txtborger_eggs, txtborger_eggs_roomy, txtkofta_sada, txtkebda, txtchecken_baneh, txtroomy_baneh,
txtcheese_borger_double, txtfarm_nar, txtalagreek, txtta3_nar, txtroomy_cheese_nar, txtlanchon_nar, txtroomy_cery_chebs_nar,
txtroomy_lanchon_nar, txtkresby, txtcheese_kresby, txtkebda_eskandarany, txtborger_double, txtborger_farm, txtTotal]

item_list  = [veeta,baket_botatos,neston,cery,roomy_cheese,roomy_lanchon,veeta_keshta,lanchon,beef,sandwich_sohba,mix_meats,
omlet_neston,omlet_lanchon,roomy_cery_farm,roomy_cery,lanchon_veta,veeta_eggs,rolls_mekseeky,cheese_makli,
foul, foul_ta3, foul_sogok, eggs_rolls_big, eggs_rolls_small, foul_zebda, foul_neston, foul_eggs, foul_keshta,
ta3, ta3_chebs, botatos_clo_slo, omlet_egg, neston_eggs, ta3_eggs, chebs, botatos_farm, omlet_farm, boiled_eggs, 
halawa_sada, halawa_keshta, halawa_cery, meraba_sada, meraba_keshta, meraba_cery, hunny_sada, hunny_keshta, 
hunny_cery, kokteil_helw, borger_sada, borger_eggs, borger_eggs_roomy, kofta_sada, kebda, checken_baneh, roomy_baneh,
cheese_borger_double, farm_nar, alagreek, ta3_nar, roomy_cheese_nar, lanchon_nar, roomy_cery_chebs_nar,
roomy_lanchon_nar, kresby, cheese_kresby, kebda_eskandarany, borger_double, borger_farm]

root.mainloop()
