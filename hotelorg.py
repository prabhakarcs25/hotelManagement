from tkinter import *
import pymysql
from tkinter import messagebox,filedialog
from  tkinter import ttk
from datetime import datetime
pk=Tk()
width=pk.winfo_screenwidth()
# print(width)
height=pk.winfo_screenheight()
# print(height)


## data base connection

tazTV=ttk.Treeview(height=10,columns=('item name''rate','type'))

tazTV1=ttk.Treeview(height=10,columns=('Date''name','type','rate','total'))


## for char input

def only_char_input(P):

    if P.isalpha() or P=='':

        return True

    return False

callback=pk.register(only_char_input)

## for digit input

def only_numeric_input(P):

    if P.isdigit() or P=='':

        return True

    return False

callback2=pk.register(only_numeric_input)


def dbconfig():
    global conn, mycursor

    conn=pymysql.connect(host="localhost",user="root",db="my_collage")
    mycursor=conn.cursor()

### clear screen

def clear_screen():
    global pk

    for widgets in pk.winfo_children():

        widgets.grid_remove()


### log out

def logout():

    clear_screen()

    mainheading()

    loginwindow()

def mainheading():
    label=Label(pk,text='Hotel SINGH Management System ',fg='white',bg='red',
                font=('arial',50,'bold'),padx=500,pady=20)
    label.grid(row=0,columnspan=4)

usernameVar=StringVar()
passwordVar=StringVar()

# ----------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------
def loginwindow():

    usernameVar.set('')

    passwordVar.set('')

    labellogin=Label(pk,text='Admin Login ',fg='red',bg='yellow', font=('arial',70,'bold','underline'))

    labellogin.grid(row=1,column=1, columnspan=2,padx=60,pady=50)


    usernamelabel=Label(pk,text='Admin Id',font=('arial',45,'bold'))

    usernamelabel.grid(row=2,column=1,padx=0,pady=10)


    passwordlabel = Label(pk, text='Admin Password',font=('arial',45,'bold'))

    passwordlabel.grid(row=3, column=1, padx=30, pady=10)


    usernameEntry=Entry(pk,textvariable=usernameVar, font=('arial',45,'bold'))

    usernameEntry.grid(row=2,column=2,padx=30,pady=10)


    passwordEntry=Entry(pk,show='*',textvariable=passwordVar, font=('arial',45,'bold'))

    passwordEntry.grid(row=3,column=2,padx=30,pady=10)


    loginButton=Button(pk,text='Log-In',width=20,height=2,fg='white',bg='Green',bd=3,font=('arial',15,'bold'),command=adminlogin )

    loginButton.grid(row=4, column=1,columnspan=2, padx=30, pady=10,)


def welcomewindow():

    clear_screen()

    mainheading()

    welcome = Label(pk, text='Welcome To My Restaurant',fg='red',bg='yellow', font=('arial',40,'bold','underline'))

    welcome.grid(row=1, column=1, columnspan=2, padx=60, pady=20)

    logoutButton = Button(pk, text='Logout', width=20, height=2, fg='white', bg='red',font=('arial',20,'bold','underline'), bd=5, command=logout )

    logoutButton.grid(row=2, column=1, columnspan=2, padx=30, pady=10, )


    managementRest = Button(pk, text='Manage Hotel', width=20, height=2, fg='White',bg='green',font=('arial',20,'bold','underline'), bd=2, command=additemwindow)

    managementRest.grid(row=3, column=1, columnspan=2, padx=30, pady=10, )


    billGen = Button(pk, text='Bill Generation', width=20, height=2, fg='red',bg='yellow',font=('arial',20,'bold','underline'), bd=10, command=billwindow)

    billGen.grid(row=4, column=1, columnspan=2, padx=30, pady=10, )
    




itemnameVar=StringVar()

itemrateVar=StringVar()

itemtypeVar=StringVar()

#3 back

def back():

    clear_screen()

    mainheading()

    welcomewindow()


###### bill window

global x

x=datetime.now()

datetimeVar=StringVar()

datetimeVar.set(x)

custmernameVar=StringVar()

mobileVar=StringVar()

combovariable=StringVar()

baserate=StringVar()

cost=StringVar()

qtyvariable=StringVar()


######## combodata

def combo_input():

    dbconfig()

    mycursor.execute('select item_name from itemlist')

    data=[]

    for row in mycursor.fetchall():

        data.append(row[0])
    return data

####### optionCallBack

def optionCallBack(*args):
    global itemname

    itemname=combovariable.get()

    #print(itemname)
    aa=ratelist()
    print(aa)
    baserate.set(aa)

    global v

    for i in aa:

        for j in i:

            v=j

##### otion call back2

def optionCallBack2(*args):
    global qty
    qty = qtyvariable.get()
    final = int(v)*int(qty)
    cost.set(final)

##### ratelist

def ratelist():

    dbconfig()

    que2='select item_rate from itemlist where item_name=%s'

    val=(itemname)

    mycursor.execute(que2,val)

    data=mycursor.fetchall()
    print(data)
    return data

##########

def billwindow():

    clear_screen()

    mainheading()

    billitem=Label(pk, text="Genrate Bill",bg='Red',fg='blue', font=("ariel", 35,"bold","underline"))

    billitem.grid(row=1, column=1, columnspan=2, padx=60, pady=20)


    logoutButton = Button(pk, text='Logout', width=20, height=2, fg='green', bd=5, command=logout)

    logoutButton.grid(row=3, column=0, columnspan=1, )


    backButton = Button(pk, text='Back', width=20, height=2, fg='green', bd=5, command=back)

    backButton.grid(row=4, column=0, columnspan=1, )


    printButton = Button(pk, text='Print Bill', width=20, height=2, fg='green', bd=5, command=printbill)

    printButton.grid(row=5, column=0, columnspan=1, )


    datetimelabel=Label(pk,text='Date & Time',font=('arial', 25, 'bold'))

    datetimelabel.grid(row=2,column=1,padx=20,pady=5)


    datetimeEntry=Entry(pk,textvariable=datetimeVar,font=('arial', 25, 'bold'))

    datetimeEntry.grid(row=2, column=2, padx=20, pady=5)


    custmernamelabel = Label(pk, text='Custmer Name', font=('arial', 25, 'bold'))

    custmernamelabel.grid(row=3, column=1, padx=20, pady=5)


    custmernameEntry = Entry(pk, textvariable=custmernameVar, font=('arial', 25, 'bold'))

    custmernameEntry.grid(row=3, column=2, padx=20, pady=5)

    custmernameEntry.configure(validate='key', validatecommand=(callback, '%P'))


    mobilelabel = Label(pk, text='Contact No', font=('arial', 25, 'bold'))

    mobilelabel.grid(row=4, column=1, padx=20, pady=5)


    mobileEntry = Entry(pk, textvariable=mobileVar, font=('arial', 25, 'bold'))

    mobileEntry.grid(row=4, column=2, padx=20, pady=5)

    mobileEntry.configure(validate='key', validatecommand=(callback2, '%P'))


    selectlabel = Label(pk, text='Select Item', font=('arial', 25, 'bold'))

    selectlabel.grid(row=5, column=1, padx=20, pady=5)


    l=combo_input()

    c=ttk.Combobox(pk,values=l,textvariable=combovariable,font=('arial', 25, 'bold'))

    c.set('Select Item')

    combovariable.trace('w',optionCallBack)

    c.grid(row=5,column=2,padx=20,pady=5)


    ratelabel = Label(pk, text='Item Rate', font=('arial', 25, 'bold'))

    ratelabel.grid(row=6, column=1, padx=20, pady=5)


    rateEntry = Entry(pk, textvariable=baserate, font=('arial', 25, 'bold'))

    rateEntry.grid(row=6, column=2, padx=20, pady=5)


    qtylabel = Label(pk, text='Select Quantity', font=('arial', 25, 'bold'))

    qtylabel.grid(row=7, column=1, padx=20, pady=5)


    global qtyvariable

    l2 = [1,2,3,4,5]

    qty = ttk.Combobox(pk, values=l2, textvariable=qtyvariable, font=('arial', 25, 'bold'))

    qty.set('Select Quantity')

    qtyvariable.trace('w', optionCallBack2)

    qty.grid(row=7, column=2, padx=20, pady=5)


    costlabel = Label(pk, text='Cost', font=('arial', 25, 'bold'))

    costlabel.grid(row=8, column=1, padx=20, pady=5)


    costEntry = Entry(pk, textvariable=cost, font=('arial', 25, 'bold'))

    costEntry.grid(row=8, column=2, padx=20, pady=5)


    billbutton=Button(pk,text='Save Bill',width=20,height=2,bd=10,fg='red',bg='yellow',command=savebill)

    billbutton.grid(row=9,column=2,padx=20,pady=5)

#########save bill

def savebill():

    dt=datetimeVar.get()

    custname=custmernameVar.get()

    mobile=mobileVar.get()

    item_name=itemname

    itemrate=v

    itemqty=qtyvariable.get()

    total=cost.get()

    dbconfig()

    insqu="insert into bill(datetime,custmer_name,contact_no,item_name,item_rate,item_qlt,cost)""values(%s,%s,%s,%s,%s,%s,%s)"

    val=(dt,custname,mobile,item_name,itemrate,itemqty,total)

    mycursor.execute(insqu,val)
    conn.commit()

    messagebox.showinfo('save data ','bill saved successfully')

    custmernameVar.set('')

    mobileVar.set('')

    itemnameVar.set('')
    cost.set('')


##### print

def printbill():

    clear_screen()

    mainheading()

    printitem = Label(pk, text='Bill Details ', fg='green', font=('arial', 30, 'bold'))

    printitem.grid(row=1, column=1, columnspan=2, padx=60, pady=20)


    logoutButton = Button(pk, text='Logout', width=20, height=2, fg='green', bd=5, command=logout)

    logoutButton.grid(row=1, column=0, columnspan=1, )


    backButton = Button(pk, text='Back', width=20, height=2, fg='green', bd=5, command=back)

    backButton.grid(row=1, column=3, columnspan=1, )


    clickbutton = Button(pk, text='Double Click To Treeview Print Bill ', fg='green', font=('arial', 30, 'bold'))

    clickbutton.grid(row=2, column=1, columnspan=3, padx=40, pady=20)


    ###triview

    tazTV1.grid(row=5, column=0, columnspan=4)

    style = ttk.Style(pk)

    style.theme_use('clam')

    style.configure('Treeview', fieldbackground='green')

    scrollbarr = Scrollbar(pk, orient='vertical', command=tazTV.yview)

    scrollbarr.grid(row=5, column=5, sticky='NSE')


    tazTV1.configure(yscrollcommand=scrollbarr.set)

    tazTV1.heading('#0', text='Date/time')

    tazTV1.heading('#1', text='name')

    tazTV1.heading('#2', text='mobile')

    tazTV1.heading('#3', text='Selected Food')

    tazTV1.heading('#4', text='total Cost')
    displaybill()



########### display bill #####

def displaybill():

    # to delet already insterted data

    records = tazTV1.get_children()

    for x in records:

        tazTV1.delete(x)


    conn = pymysql.connect(host='localhost', user='root', db='my_collage')

    mycursor = conn.cursor(pymysql.cursors.DictCursor)

    query1 = 'select * from bill'

    mycursor.execute(query1)

    data = mycursor.fetchall()

    # print(data)

    for row in data:

        tazTV1.insert('', 'end', text=row['datetime'], values=(row['custmer_name'], row['contact_no'],row['item_name'],row['item_rate'],row['item_qlt'],row['cost']))
    conn.close()

    tazTV1.bind('<Double-1>', OnDoubleClick2)


#######OnDoubleClick2

def OnDoubleClick2(event):

    item = tazTV1.selection()

    global itemnameVar11

    itemnameVar11 = tazTV1.item(item, 'text')

    item_detail1 = tazTV1.item(item, 'values')
    receipt()


####### receipt

def receipt():
    billstring=''

    billstring+='==========Singh Hotel Bill===========\n\n'

    billstring += '===========Custmer Details===========\n\n'

    dbconfig()

    query='select * from bill where datetime="{}";'.format(itemnameVar11)

    mycursor.execute(query)

    data=mycursor.fetchall()
    # print(data)

    for row in data:

        billstring+="{}{:<20}{:<10}\n".format('date/Time','',row[0])

        billstring += "{}{:<20}{:<10}\n".format('Custmer Name', '', row[1])

        billstring += "{}{:<20}{:<10}\n".format('Contact No', '', row[2])

        billstring += "\n=========== Item Details ==========\n"

        # billstring +="{:<15}{:<15}{:<15}{:<15}".format('Item Name','Rate','Quantity','Total Cost')

        # billstring+="\n{:<10}{:<10}{:<25}{:<25}".format(row[3],row[4],row[5],row[6])

        billstring+="{}{:<10}{:<10}\n".format('Item Name','',row[3])

        billstring += "{}{:<15}{:<10}\n".format('Item Rate', '', row[4])

        billstring += "{}{:<15}{:<10}\n".format('Quantity', '', row[5])

        # billstring += "{}{:<20}{:<10}\n".format('Total Cost', '', row[6])



        billstring+="\n====================================\n"

        billstring+="{}{:<10}{:<15}{:<10}\n".format('Total Cost','','',row[6])

        billstring+="\n\n ==== Thanks Please Visit Again ====\n"

    billfile=filedialog.asksaveasfile(mode='w',defaultextension='.text')

    if billfile is None:

        messagebox.showerror('File Name Error','Invalid File Name')

    else:

        billfile.write(billstring)

        billfile.close()



########








def additemwindow():

    clear_screen()

    mainheading()

    additem = Label(pk, text='Insert Item ', fg='white',bg='blue', font=('arial', 45, 'bold','underline'))

    additem.grid(row=1, column=1, columnspan=2, pady=20)


    itemnamelabel=Label(pk,text='Item Name',font=('arial', 35, 'bold'))

    itemnamelabel.grid(row=2,column=1, pady=20)


    itemratelabel = Label(pk, text='Item Rate', font=('arial', 35, 'bold'))

    itemratelabel.grid(row=3, column=1, pady=20)


    itemtypelabel = Label(pk, text='Item type', font=('arial', 35, 'bold'))

    itemtypelabel.grid(row=4, column=1, pady=20)


    itemnameEntry=Entry(pk,textvariable=itemnameVar, font=('arial', 15, 'bold'))

    itemnameEntry.grid(row=2,column=2)

    # for validation

    itemnameEntry.configure(validate='key',validatecommand=(callback,'%P'))


    itemrateEntry = Entry(pk, textvariable=itemrateVar, font=('arial', 15, 'bold'))

    itemrateEntry.grid(row=3, column=2)

    itemrateEntry.configure(validate='key', validatecommand=(callback2, '%P'))


    itemtypeEntry = Entry(pk, textvariable=itemtypeVar, font=('arial', 15, 'bold'))

    itemtypeEntry.grid(row=4, column=2)

    itemtypeEntry.configure(validate='key', validatecommand=(callback, '%P'))


    additembutton=Button(pk,text='Add Item',width=20,height=2,fg='green',font='bold',bd=5,command=additemprocess)

    additembutton.grid(row=3,column=3,columnspan=1)


    updatebutton=Button(pk, text='Update', width=20, height=2, fg='green',font='bold',bg='white', bd=5, command=updateitem)

    updatebutton.grid(row=4, column=3,columnspan=1)


    deletbutton = Button(pk, text='delete', width=20, height=2,bg='white', fg='green',font='bold', bd=5, command=deletitem)

    deletbutton.grid(row=5, column=3,columnspan=1, pady=20)


    logoutButton = Button(pk, text='Logout', width=20, height=2, fg='red',bg='white',font='bold',bd=5, command=logout)

    logoutButton.grid(row=3, column=0 )


    backButton = Button(pk, text='Back', width=20, height=2,bg='white', fg='green',font='bold', bd=5, command=back)

    backButton.grid(row=2, column=3 )



####

    tazTV.grid(row=8,column=0,columnspan=3)

    style=ttk.Style(pk)

    style.theme_use('clam')

    style.configure('Treeview',fieldbackground='green')

    scrollbarr=Scrollbar(pk,orient='vertical',command=tazTV.yview)

    scrollbarr.grid(row=8,column=2,sticky='NSE')


    tazTV.configure(yscrollcommand=scrollbarr.set)

    tazTV.heading('#0',text='item name')

    tazTV.heading('#1', text='rate')

    tazTV.heading('#2', text='type')


    getItemInTreeview()




def additemprocess():

    name=itemnameVar.get()

    rate=itemrateVar.get()

    type=itemtypeVar.get()

    dbconfig()

    query='insert into itemlist(item_name,item_rate,item_type)values(%s,%s,%s)'

    val=(name,rate,type)

    mycursor.execute(query,val)
    conn.commit()

    messagebox.showinfo('save item','item saved successfully')

    itemnameVar.set('')

    itemrateVar.set('')

    itemtypeVar.set('')

    getItemInTreeview()


########

def getItemInTreeview():

    # to delet already insterted data

    records=tazTV.get_children()

    for x in records:

        tazTV.delete(x)


    conn=pymysql.connect(host='localhost',user='root',db='my_collage')

    mycursor=conn.cursor(pymysql.cursors.DictCursor)

    query1='select * from itemlist'

    mycursor.execute(query1)

    data=mycursor.fetchall()

    #print(data)

    for row in data:

        tazTV.insert('','end',text=row['item_name'],values=(row['item_rate'],row['item_type']))
    conn.close()

    tazTV.bind('<Double-1>',OnDoubleClick)



########## doubleclick

def OnDoubleClick(event):

    item=tazTV.selection()

    itemnameVar1=tazTV.item(item,'text')

    item_detail = tazTV.item(item, 'values')

    itemnameVar.set(itemnameVar1)

    itemrateVar.set(item_detail[0])

    itemtypeVar.set(item_detail[1])


#############

### update

def updateitem():

    name=itemnameVar.get()

    rate=itemrateVar.get()

    type=itemtypeVar.get()

    dbconfig()

    que='update itemlist set item_rate=%s,item_type=%s where item_name=%s'

    val=(rate,type,name)

    mycursor.execute(que,val)
    conn.commit()

    messagebox.showinfo('updation confirmation','Item updated successfully')

    itemnameVar.set('')

    itemrateVar.set('')

    itemtypeVar.set('')

    getItemInTreeview()

##### delete item

def deletitem():

    name=itemnameVar.get()

    rate=itemrateVar.get()

    type=itemtypeVar.get()

    dbconfig()

    que1='delete from  itemlist where item_name=%s'

    val=(name)

    mycursor.execute(que1,val)
    conn.commit()

    messagebox.showinfo('delete confirmation','Item deleted successfully')

    itemnameVar.set('')

    itemrateVar.set('')

    itemtypeVar.set('')

    getItemInTreeview()



def adminlogin():
    dbconfig()
    username=usernameVar.get()
    password=passwordVar.get()
    que='select * from user_info where user_id=%s and user_pass=%s'
    val=(username,password)
    mycursor.execute(que,val)
    data=mycursor.fetchall()
    flag=False
    for row in data:
        flag=True
    conn.close()
    if flag==True:
        welcomewindow()
    else:
        messagebox.showerror('Invalid user credential','Either user name or password incorrect')
        usernameVar.set('')
        passwordVar.set('')
mainheading()
loginwindow()

pk.title('Hotel Singh management system')
pk.geometry('%dx%d+0+0'%(width,height))
pk.mainloop()





