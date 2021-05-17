from tkinter import *
from tkinter import messagebox
import random
import time
import os,sys

root = Tk()
root.geometry("1600x900+0+0")
root.title("ร้านอาหารวิศวะ ศรีราชา")

#read menu & price
try:
    name = open("menu.txt", "r")
    tax = open("tax.txt","r")
    
except FileNotFoundError:
    print("No such file or directory : menu.txt or tax.txt")
    sys.exit(1)
##---- Menu Price ----
priceList = []
menuList = []
for line in name:
    menu, price = line.split()
    menuList.append(menu)
    priceList.append(int(price))
    
##---- tax service ----
taxList = []
for line2 in tax:
    a, price = line2.split()
    taxList.append(float(price))

##print(priceList)
##print(menuList)
##print(taxList)
name.close()
tax.close()

##----- FRAME OPTION -----

Tops = Frame(root,width = 1600, height = 50 , bg="powder blue",relief = SUNKEN)
Tops.pack(side=TOP)

f1 = Frame(root,width=800,height = 700,relief=SUNKEN)
f1.pack(side=LEFT)

f2 = Frame(root,width=300,height=700,relief=SUNKEN)
f2.pack(side=RIGHT)


##----- TIME -----

localtime = time.asctime(time.localtime(time.time()))

lblInfo = Label(Tops,font=('TH Sarabun New',50,'bold')
            ,text="ร้านอาหารวิศวะ ศรีราชา" ,fg = "blue",bd=10,
            anchor='w')
lblInfo.grid(row=0,column=0)

lblInfo = Label(Tops,font=('TH Sarabun New',20,'bold')
            ,text=localtime,fg = "blue",bd=10,
            anchor='w')
lblInfo.grid(row=1,column=0)

##----- Dedined Varible and Functional -----

textinput = StringVar()
operator = ""

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    textinput.set(operator)

def btnClearDisplay():
    global operator
    operator = ""
    textinput.set(operator)

def btnEqualInput():
    global operator
    Cal = str(eval(operator))
    textinput.set(Cal)
    operator = ""

def CalculateTotal():
    x = random.randint(12908,508763)
    randomRef = str(x)
    rand.set(randomRef)


    CoMenu1 = Menu1.get()
    CoMenu2 = Menu2.get()
    CoMenu3 = Menu3.get()
    CoMenu4 = Menu4.get()
    CoMenu5 = Menu5.get()
    CoD = Drinks.get()

    checkList = [CoMenu1,CoMenu2,CoMenu3,CoMenu4,CoMenu5,CoD]
    for i in range(len(checkList)):
        try:
            checkList[i] = float(checkList[i])
        except:
            checkList[i]  = 0
            

    CostofMenu1 = checkList[0]  * priceList[0]
    CostofMenu2 = checkList[1]  * priceList[1]
    CostofMenu3 = checkList[2]  * priceList[2]
    CostofMenu4 = checkList[3]  * priceList[3]
    CostofMenu5 = checkList[4]  * priceList[4]
    CostofDrinks = checkList[5]  * priceList[5]

    CostofMeal = CostofMenu1 + CostofMenu2 + CostofMenu3 + CostofMenu4 + CostofMenu5 + CostofDrinks
    CostofMealB = "B", str('%.2f' %CostofMeal)
    
    Ser_Charge = CostofMeal*taxList[1]
    PayTax = (CostofMeal + Ser_Charge) * taxList[0]
    TotalCost = CostofMeal + Ser_Charge + PayTax

    Service_Charge.set(("B", str('%.2f' %Ser_Charge)))
    Cost.set(CostofMealB)
    Tax.set(("B", str('%.2f' %PayTax)))
    Subtotal.set(("B", str('%.2f' %(CostofMeal+Ser_Charge))))
    Total.set(("B", str('%.2f' %TotalCost)))

def qExit():
    qExit= messagebox.askyesno("Quit System!!!", "Do you want to quit?")
    if qExit > 0:
        root.destroy()
        return 

def Reset():
    rand.set("")
    Menu1.set("")
    Menu2.set("")
    Menu3.set("")
    Menu4.set("")
    Menu5.set("")
    Subtotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    Cost.set("")

##----- Cal Frame -----
txtDisplay = Entry(f2,font=('TH Sarabun New',20,'bold')
            ,textvariable = textinput,bd = 30 ,insertwidth = 4
            ,bg = "powder blue",justify = 'right')
txtDisplay.grid(columnspan = 4)

    ##--- Row 0 ---
btn7 = Button(f2,padx=16,pady=16,bd=8,fg="black",
        font=('TH Sarabun New',20,'bold'),text = '7',bg = 'powder blue'
        ,command=lambda:btnClick(7)).grid(row=2,column=0)

btn8 = Button(f2,padx=16,pady=16,bd=8,fg="black",
        font=('TH Sarabun New',20,'bold'),text = '8',bg = 'powder blue'
        ,command=lambda:btnClick(8)).grid(row=2,column=1)

btn9 = Button(f2,padx=16,pady=16,bd=8,fg="black",
        font=('TH Sarabun New',20,'bold'),text = '9',bg = 'powder blue'
        ,command=lambda:btnClick(9)).grid(row=2,column=2)

Addition = Button(f2,padx=16,pady=16,bd=8,fg="black",
        font=('TH Sarabun New',20,'bold'),text = '+',bg = 'powder blue'
        ,command=lambda:btnClick("+")).grid(row=2,column=3)

    ##--- Row 1 ---
btn4 = Button(f2,padx=16,pady=16,bd=8,fg="black",
        font=('TH Sarabun New',20,'bold'),text = '4',bg = 'powder blue'
        ,command=lambda:btnClick(4)).grid(row=3,column=0)

btn5 = Button(f2,padx=16,pady=16,bd=8,fg="black",
        font=('TH Sarabun New',20,'bold'),text = '5',bg = 'powder blue'
        ,command=lambda:btnClick(5)).grid(row=3,column=1)

btn6 = Button(f2,padx=16,pady=16,bd=8,fg="black",
        font=('TH Sarabun New',20,'bold'),text = '6',bg = 'powder blue'
        ,command=lambda:btnClick(6)).grid(row=3,column=2)

Minus = Button(f2,padx=16,pady=16,bd=8,fg="black",
        font=('TH Sarabun New',20,'bold'),text = '-',bg = 'powder blue'
        ,command=lambda:btnClick("-")).grid(row=3,column=3)

    ##--- Row 3 ---
btn1 = Button(f2,padx=16,pady=16,bd=8,fg="black",
        font=('TH Sarabun New',20,'bold'),text = '1',bg = 'powder blue'
        ,command=lambda:btnClick(1)).grid(row=4,column=0)

btn2 = Button(f2,padx=16,pady=16,bd=8,fg="black",
        font=('TH Sarabun New',20,'bold'),text = '2',bg = 'powder blue'
        ,command=lambda:btnClick(2)).grid(row=4,column=1)

btn3 = Button(f2,padx=16,pady=16,bd=8,fg="black",
        font=('TH Sarabun New',20,'bold'),text = '3',bg = 'powder blue'
        ,command=lambda:btnClick(3)).grid(row=4,column=2)

Multiply = Button(f2,padx=16,pady=16,bd=8,fg="black",
        font=('TH Sarabun New',20,'bold'),text = '*',bg = 'powder blue'
        ,command=lambda:btnClick("*")).grid(row=4,column=3)
    ##--- Row 4 ---
btn0 = Button(f2,padx=16,pady=16,bd=8,fg="black",
        font=('TH Sarabun New',20,'bold'),text = '0',bg = 'powder blue'
        ,command=lambda:btnClick(0)).grid(row=5,column=0)

btnC = Button(f2,padx=16,pady=16,bd=8,fg="black",
        font=('TH Sarabun New',20,'bold'),text = 'C',bg = 'powder blue'
        ,command=btnClearDisplay).grid(row=5,column=1)

btnE = Button(f2,padx=16,pady=16,bd=8,fg="black",
        font=('TH Sarabun New',20,'bold'),text = '=',bg = 'powder blue'
        ,command=btnEqualInput).grid(row=5,column=2)

Division = Button(f2,padx=16,pady=16,bd=8,fg="black",
        font=('TH Sarabun New',20,'bold'),text = '/',bg = 'powder blue'
        ,command=lambda:btnClick("/")).grid(row=5,column=3)

##---- res variable ---
rand = StringVar()
Menu1 = StringVar()
Menu2 = StringVar()
Menu3 = StringVar()
Menu4 = StringVar()
Menu5 = StringVar()
Subtotal = StringVar()
Total = StringVar()
Service_Charge = StringVar()
Drinks = StringVar()
Tax = StringVar()
Cost = StringVar()
#============================= Resturant Info 1 ======================

lblReference = Label(f1,font=('TH Sarabun New',18,'bold'),text="Reference", bd=16, anchor='w')
lblReference.grid(row=0,column=0)
txtReference= Entry(f1,font=('TH Sarabun New',18,'bold'),textvariable=rand,bd=10,insertwidth=4,
bg="powder blue",justify= 'right')
txtReference.grid(row=0,column=1)

lblMenu1 = Label(f1,font=('TH Sarabun New',18,'bold'),text=menuList[0]+"*"+ str(priceList[0]), bd=16, anchor='w')
lblMenu1.grid(row=1,column=0)
txtMenu1= Entry(f1,font=('TH Sarabun New',18,'bold'),textvariable=Menu1,bd=10,insertwidth=4,
bg="powder blue",justify= 'right')
txtMenu1.grid(row=1,column=1)

lblMenu2 = Label(f1,font=('TH Sarabun New',18,'bold'),text=menuList[1]+"*"+ str(priceList[1]), bd=16, anchor='w')
lblMenu2.grid(row=2,column=0)
txtMenu2= Entry(f1,font=('TH Sarabun New',18,'bold'),textvariable=Menu2,bd=10,insertwidth=4,
bg="powder blue",justify= 'right')
txtMenu2.grid(row=2,column=1)

lblMenu3 = Label(f1,font=('TH Sarabun New',18,'bold'),text=menuList[2]+"*"+ str(priceList[2]), bd=16, anchor='w')
lblMenu3.grid(row=3,column=0)
txtMenu3= Entry(f1,font=('TH Sarabun New',18,'bold'),textvariable=Menu3,bd=10,insertwidth=4,
bg="powder blue",justify= 'right')
txtMenu3.grid(row=3,column=1)

lblMenu4 = Label(f1,font=('TH Sarabun New',18,'bold'),text=menuList[3]+"*"+ str(priceList[3]), bd=16, anchor='w')
lblMenu4.grid(row=4,column=0)
txtMenu4= Entry(f1,font=('TH Sarabun New',18,'bold'),textvariable=Menu4,bd=10,insertwidth=4,
bg="powder blue",justify= 'right')
txtMenu4.grid(row=4,column=1)

lblMenu5 = Label(f1,font=('TH Sarabun New',18,'bold'),text=menuList[4]+"*"+ str(priceList[4]), bd=16, anchor='w')
lblMenu5.grid(row=5,column=0)
txtMenu5= Entry(f1,font=('TH Sarabun New',18,'bold'),textvariable=Menu5,bd=10,insertwidth=4,
bg="powder blue",justify= 'right')
txtMenu5.grid(row=5,column=1)

lblDrink = Label(f1,font=('TH Sarabun New',18,'bold'),text=menuList[5]+"*"+ str(priceList[5]), bd=16, anchor='w')
lblDrink.grid(row=0,column=2)

#============================= Resturant Info 2 ======================
txtDrink= Entry(f1,font=('TH Sarabun New',18,'bold'),textvariable=Drinks,bd=10,insertwidth=4,
bg="powder blue",justify= 'right')
txtDrink.grid(row=0,column=3)

lblCost = Label(f1,font=('TH Sarabun New',18,'bold'),text="จำนวนเงิน", bd=16, anchor='w')
lblCost.grid(row=1,column=2)
txtCost= Entry(f1,font=('TH Sarabun New',18,'bold'),textvariable=Cost,bd=10,insertwidth=4,
bg="powder blue",justify= 'right')
txtCost.grid(row=1,column=3)

lblService = Label(f1,font=('TH Sarabun New',18,'bold'),text="ค่าบริการ", bd=16, anchor='w')
lblService.grid(row=2,column=2)
txtService= Entry(f1,font=('TH Sarabun New',18,'bold'),textvariable=Service_Charge,bd=10,insertwidth=4,
bg="powder blue",justify= 'right')
txtService.grid(row=2,column=3)

lblSubTotal = Label(f1,font=('TH Sarabun New',18,'bold'),text="จำนวนเงินรวม", bd=16, anchor='w')
lblSubTotal.grid(row=3,column=2)
txtSubTotal= Entry(f1,font=('TH Sarabun New',18,'bold'),textvariable=Subtotal,bd=10,insertwidth=4,
bg="powder blue",justify= 'right')
txtSubTotal.grid(row=3,column=3)

lblStateTax = Label(f1,font=('TH Sarabun New',18,'bold'),text="ภาษี", bd=16, anchor='w')
lblStateTax.grid(row=4,column=2)
txtStateTax= Entry(f1,font=('TH Sarabun New',18,'bold'),textvariable=Tax,bd=10,insertwidth=4,
bg="powder blue",justify= 'right')
txtStateTax.grid(row=4,column=3)

lblTotalCost = Label(f1,font=('TH Sarabun New',18,'bold'),text="จำนวนเงินรวมภาษี", bd=16, anchor='w')
lblTotalCost.grid(row=5,column=2)
txtTotalCost= Entry(f1,font=('TH Sarabun New',18,'bold'),textvariable=Total,bd=10,insertwidth=4,
bg="powder blue",justify= 'right')
txtTotalCost.grid(row=5,column=3)

#=====================Button=================
btnTotal=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('TH Sarabun New',18,'bold'),width=10,text="Total",bg="powder blue",command=CalculateTotal).grid(row=7,column=1)
btnReset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('TH Sarabun New',18,'bold'),width=10,text="Reset",bg="powder blue",command=Reset).grid(row=7,column=2)
btnExit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('TH Sarabun New',18,'bold'),width=10,text="Exit",bg="powder blue",command=qExit).grid(row=7,column=3)



root.mainloop()
