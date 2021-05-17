import socket
import sys
import tkinter.messagebox
from _thread import *
from threading import *
from tkinter import *
from tkinter import ttk

#Object of TK fun
root =Tk()
root.title(" GAME OX CLIENT")#title of window
w=625
h=680
half=[]
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
     # calculate position x, y
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)-50

root.geometry('%dx%d+%d+%d' % (w,h,x, y))
root.configure(background = '#DAF7A6')

def NewGame_HvP():
    global soc
    reset()
    PlayerX.set(0)
    PlayerO.set(0)
    text_change_online()
    enable_button()
    try:
        button1['command'] = clicked1
        button2['command'] = clicked2
        button3['command'] = clicked3
        button4['command'] = clicked4
        button5['command'] = clicked5
        button6['command'] = clicked6
        button7['command'] = clicked7
        button8['command'] = clicked8
        button9['command'] = clicked9
    except:
        print("Error with clicked function ")

    soc=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def NewGame_PvP():
    global soc
    # soc.close()
    reset()
    PlayerX.set(0)
    PlayerO.set(0)
    text_change_online_PvP()
    enable_button()
    try:
        button1['command'] = clicked1
        button2['command'] = clicked2
        button3['command'] = clicked3
        button4['command'] = clicked4
        button5['command'] = clicked5
        button6['command'] = clicked6
        button7['command'] = clicked7
        button8['command'] = clicked8
        button9['command'] = clicked9
    except:
        print("Error with clicked function ")

    soc=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def reset():
    global count
    global turn
    global draw
    global isWin
    global isDraw
    button1['text']=" "
    button2['text']=" "
    button3['text']=" "
    button4['text']=" "
    button5['text']=" "
    button6['text']=" "
    button7['text']=" "
    button8['text']=" "
    button9['text']=" "

    button1.configure(background="#dc3545")
    button2.configure(background="#ffc107")
    button3.configure(background="#dc3545")
    button4.configure(background="#ffc107")
    button5.configure(background="#dc3545")
    button6.configure(background="#ffc107")
    button7.configure(background="#dc3545")
    button8.configure(background="#ffc107")
    button9.configure(background="#dc3545")
    count = 0
    draw = 0
    turn = 1
    isWin = 0
    isDraw = 0

    print("-----------------------reset-------------------------")

# ---------- Menu Bar ---------- #
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Host Vs Player", command=NewGame_HvP)
filemenu.add_command(label="Player Vs Player", command=NewGame_PvP)
#filemenu.add_command(label="Reset", command=reset)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)



root.config(menu=menubar)

# ---------- GET IP HOST ---------- #
try:
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
except:
    print("Cannot get hostname or IP")

test_ip = StringVar()

def text_change_online():
    lblPlayerO["text"] = 'Host    O'
    lblPlayerX["text"] = 'Player  X'
    lblIP.grid(row=1,column=0)
    entryPlayer.grid(row=1,column=1)
    btnConnect.grid(row=1,column=2,padx=5)
    MainFrame.grid(row=2, column=0,padx=30)

def text_change_online_PvP():
    lblPlayerO["text"] = 'Player  O'
    lblPlayerX["text"] = 'Player  X'
    lblIP.grid(row=1,column=0)
    entryPlayer.grid(row=1,column=1)
    btnConnect.grid(row=1,column=2,padx=5)
    MainFrame.grid(row=2, column=0,padx=30)

def connect():
    soc.connect((test_ip.get(),7000))
    receive=Thread(target=receive_thread,args=(soc,))
    receive.start()
    reset()

TopTop = Frame(root, bg = '#DAF7A6', pady=2,width=1350, height=100, relief=RIDGE)
TopTop.grid(row=0, column=0,sticky="")

Title = Label(TopTop,font=('arial',30,'bold'), text="Game OX (CLIENT)", bd=15,bg='#008080',justify=CENTER,relief="raised")
Title.grid(row=0,column=0)

#### IP player#####
BottomFrame = Frame(root,width=1350, height=100, relief=RIDGE,bg ='#DAF7A6')
BottomFrame.grid(row=1, column=0,sticky="")
lblFake = Label(BottomFrame,font=('arial',12,'bold'), text="", bd=21,bg='#DAF7A6',fg="Cornsilk",justify=CENTER) #for not push down
lblFake.grid(row=1,column=0)
lblIP = Label(BottomFrame,font=('arial',10,'bold'), text="IP", bd=21,bg="#B22222",fg="Cornsilk",justify=CENTER)
lblIP.grid(row=0,column=0)
lblIP.grid_forget()
entryPlayer = Entry(BottomFrame,font=('arial',10,'bold'),textvariable=test_ip, bd=21,bg="#B22222",fg="Cornsilk",justify=CENTER)
entryPlayer.grid(row=0,column=1)
entryPlayer.grid_forget()
btnConnect = Button(BottomFrame,text="Play", font=('Times 21 bold'), height = 1, width=20,bg="#edb44e",command=connect)
btnConnect.grid(row=0,column=2,padx=5)
btnConnect.grid_forget()

##### middle ####
MainFrame = Frame(root, pady=2,width=20, height=200, relief=RIDGE,bg ='#00FFFF')
MainFrame.grid(row=2, column=0,padx=30)

LeftFrame = Frame(MainFrame , bd=10, width=200, height=200,pady=5,padx=10,bg='#00FFFF' , relief=RIDGE)
LeftFrame.pack()


##### set player #####
PlayerX=IntVar()
PlayerO=IntVar()

PlayerX.set(0)
PlayerO.set(0)


#flag to no. of 10 action to terminated
count = 0
isWin = 0
isDraw = 0

##------ text field -------
lblPlayerO = Label(LeftFrame,font=('arial',26,'bold'), text="Player1  X", padx=2,pady=2,bg="#edb44e")
lblPlayerX = Label(LeftFrame,font=('arial',26,'bold'), text="Player2  O", padx=2,pady=2,bg="#edb44e")


# ---------- Check btn for sure ---------- #
def check (num): 
    global count
    global isWin
    global isDraw

    b1 = button1["text"]
    b2 = button2["text"]
    b3 = button3["text"]
    b4 = button4["text"]
    b5 = button5["text"]
    b6 = button6["text"]
    b7 = button7["text"]
    b8 = button8["text"]
    b9 = button9["text"]

    if (b1==b2 and b2==b3 and b1=='O'):
        button1.configure(background="PaleGreen1")
        button2.configure(background="PaleGreen1")
        button3.configure(background="PaleGreen1")
        n = int(PlayerO.get())
        score = (n+1)
        PlayerO.set(score)
        isWin = 1
        send(num,count,isWin,isDraw)
        count = 0
        win(b1)
        reset()
    elif (b1==b2 and b2==b3 and b1=='X'):
        button1.configure(background="PaleGreen1")
        button2.configure(background="PaleGreen1")
        button3.configure(background="PaleGreen1")
        n = int(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        isWin = 1
        send(num,count,isWin,isDraw)
        count = 0
        win(b1)
        reset()

    elif (b4==b5 and b5==b6 and b4=='O'):
        button4.configure(background="PaleGreen1")
        button5.configure(background="PaleGreen1")
        button6.configure(background="PaleGreen1")
        n = int(PlayerO.get())
        score = (n+1)
        PlayerO.set(score)
        isWin = 1
        send(num,count,isWin,isDraw)
        count = 0
        win(b4)
        reset()

    elif (b4==b5 and b5==b6 and b4=='X'):
        button4.configure(background="PaleGreen1")
        button5.configure(background="PaleGreen1")
        button6.configure(background="PaleGreen1")
        n = int(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        isWin = 1
        send(num,count,isWin,isDraw)
        count = 0
        win(b4)
        reset()

    elif (b7==b8 and b8==b9 and b7=='O'):
        button7.configure(background="PaleGreen1")
        button8.configure(background="PaleGreen1")
        button9.configure(background="PaleGreen1")
        n = int(PlayerO.get())
        score = (n+1)
        PlayerO.set(score)
        isWin = 1
        send(num,count,isWin,isDraw)
        count = 0
        win(b7)
        reset()

    elif (b7==b8 and b8==b9 and b7=='X'):
        button7.configure(background="PaleGreen1")
        button8.configure(background="PaleGreen1")
        button9.configure(background="PaleGreen1")
        n = int(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        isWin = 1
        send(num,count,isWin,isDraw)
        count = 0
        win(b7)
        reset()
        
    elif (b1==b4 and b4==b7 and b1=='O'):
        button1.configure(background="PaleGreen1")
        button4.configure(background="PaleGreen1")
        button7.configure(background="PaleGreen1")
        n = int(PlayerO.get())
        score = (n+1)
        PlayerO.set(score)
        isWin = 1
        send(num,count,isWin,isDraw)
        count = 0
        win(b1)
        reset()

    elif (b1==b4 and b4==b7 and b1=='X'):
        button1.configure(background="PaleGreen1")
        button4.configure(background="PaleGreen1")
        button7.configure(background="PaleGreen1")
        n = int(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        isWin = 1
        send(num,count,isWin,isDraw)
        count = 0
        win(b1)
        reset()
        
    elif (b2==b5 and b5==b8 and b2=='O'):
        button2.configure(background="PaleGreen1")
        button5.configure(background="PaleGreen1")
        button8.configure(background="PaleGreen1")
        n = int(PlayerO.get())
        score = (n+1)
        PlayerO.set(score)
        isWin = 1
        send(num,count,isWin,isDraw)
        count = 0
        win(b2)
        reset()
        
    elif (b2==b5 and b5==b8 and b2=='X'):
        button2.configure(background="PaleGreen1")
        button5.configure(background="PaleGreen1")
        button8.configure(background="PaleGreen1")
        n = int(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        isWin = 1
        send(num,count,isWin,isDraw)
        count = 0
        win(b2)
        reset()

    elif (b3==b6 and b6==b9 and b3=='O'):
        button3.configure(background="PaleGreen1")
        button6.configure(background="PaleGreen1")
        button9.configure(background="PaleGreen1")
        n = int(PlayerO.get())
        score = (n+1)
        PlayerO.set(score)
        isWin = 1
        send(num,count,isWin,isDraw)
        count = 0
        win(b3)
        reset()

    elif (b3==b6 and b6==b9 and b3=='X'):
        button3.configure(background="PaleGreen1")
        button6.configure(background="PaleGreen1")
        button9.configure(background="PaleGreen1")
        n = int(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        isWin = 1
        send(num,count,isWin,isDraw)
        count = 0
        win(b3)
        reset()
        
    elif (b1==b5 and b5==b9 and b1=='O'):
        button1.configure(background="PaleGreen1")
        button5.configure(background="PaleGreen1")
        button9.configure(background="PaleGreen1")
        n = int(PlayerO.get())
        score = (n+1)
        PlayerO.set(score)
        isWin = 1
        send(num,count,isWin,isDraw)
        count = 0
        win(b1)
        reset()

    elif (b1==b5 and b5==b9 and b1=='X'):
        button1.configure(background="PaleGreen1")
        button5.configure(background="PaleGreen1")
        button9.configure(background="PaleGreen1")
        n = int(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        isWin = 1
        send(num,count,isWin,isDraw)
        count = 0
        win(b1)
        reset()
    
    elif (b3==b5 and b5==b7 and b3=='O'):
        button3.configure(background="PaleGreen1")
        button5.configure(background="PaleGreen1")
        button7.configure(background="PaleGreen1")
        n = int(PlayerO.get())
        score = (n+1)
        PlayerO.set(score)
        isWin = 1
        send(num,count,isWin,isDraw)
        count = 0
        win(b3)
        reset()

    elif (b3==b5 and b5==b7 and b3=='X'):
        button3.configure(background="PaleGreen1")
        button5.configure(background="PaleGreen1")
        button7.configure(background="PaleGreen1")
        n = int(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        isWin = 1
        send(num,count,isWin,isDraw)
        count = 0
        win(b3)
        reset()
        
    elif count == 9:
        tkinter.messagebox.showinfo("Game Ended","Draw !!!!")
        isDraw = 1
        send(num,count,isWin,isDraw)
        count = 0
        reset()
        

#fun of messaging congrats
def win(player):
    tkinter.messagebox.showinfo("Game Ended", player+" is Winner!!!!")
    
def lose():
    tkinter.messagebox.showinfo("Game Ended", "You lose !!!")
    reset()


# ---------- set click O X && reset new game  ---------- #
buttons = StringVar()
click = True
draw = 0

def enable_button():
    button1['state'] = 'normal'
    button2['state'] = 'normal'
    button3['state'] = 'normal'
    button4['state'] = 'normal'
    button5['state'] = 'normal'
    button6['state'] = 'normal'
    button7['state'] = 'normal'
    button8['state'] = 'normal'
    button9['state'] = 'normal'


#flag to choose player
turn =1
#fun of button command 1
def clicked1():
    global turn
    global count
    global isWin
    global isDraw
    if button1["text"]==" ":
        if turn ==1:
            count +=1
            turn =2
            button1["text"] ='X'
            send(1,count,isWin,isDraw)
        check(1)
#fun of button command 2
def clicked2():
    global turn
    global count
    global isWin
    global isDraw
    if button2["text"]==" ":
        if turn ==1:
            count +=1
            turn =2
            button2["text"] ='X'
            send(2,count,isWin,isDraw)
        check(2)
#fun of button command 3
def clicked3():
    global turn
    global count
    global isWin
    global isDraw
    if button3["text"]==" ":
        if turn ==1:
            count +=1
            turn =2
            button3["text"] ='X'
            send(3,count,isWin,isDraw)
        check(3)
#fun of button command 4
def clicked4():
    global turn
    global count
    global isWin
    global isDraw
    if button4["text"]==" ":
        if turn ==1:
            count +=1
            turn =2
            button4["text"] ='X'
            send(4,count,isWin,isDraw)
        check(4)
#fun of button command 5
def clicked5():
    global turn
    global count
    global isWin
    global isDraw
    if button5["text"]==" ":
        if turn ==1:
            count +=1
            turn =2
            button5["text"] ='X'
            send(5,count,isWin,isDraw)
        check(5)
#fun of button command 6
def clicked6():
    global turn
    global count
    global isWin
    global isDraw
    if button6["text"]==" ":
        if turn ==1:
            count +=1
            turn =2
            button6["text"] ='X'
            send(6,count,isWin,isDraw)
        check(6)
#fun of button command 7
def clicked7():
    global turn
    global count
    global isWin
    global isDraw
    if button7["text"]==" ":
        if turn ==1:
            count +=1
            turn =2
            button7["text"] ='X'
            send(7,count,isWin,isDraw)
        check(7)
#fun of button command 8
def clicked8():
    global turn
    global count
    global isWin
    global isDraw
    if button8["text"]==" ":
        if turn ==1:
            count +=1
            turn =2
            button8["text"] ='X'
            send(8,count,isWin,isDraw)
        check(8)
#fun of button command 9
def clicked9():
    global turn
    global count
    global isWin
    global isDraw
    if button9["text"]==" ":
        if turn ==1:
            count +=1
            turn =2
            button9["text"] ='X'
            send(9,count,isWin,isDraw)
        check(9)



#list of the buttons pressed
butList = list()
############# Draw 3x3 button ######
button1 = Button(LeftFrame, text=" ", font=('Times 26 bold'),state=DISABLED, height = 3, width=8,bg='#dc3545', command=clicked1)
button1.grid(row=1,column=0, stick = S+N+E+W)

button2 = Button(LeftFrame, text=" ", font=('Times 26 bold'),state=DISABLED, height = 3, width=8,bg='#ffc107', command=clicked2)
button2.grid(row=1,column=1, stick = S+N+E+W)

button3 = Button(LeftFrame, text=" ", font=('Times 26 bold'),state=DISABLED, height = 3, width=8,bg='#dc3545', command=clicked3)
button3.grid(row=1,column=2, stick = S+N+E+W)

button4 = Button(LeftFrame, text=" ", font=('Times 26 bold'),state=DISABLED, height = 3, width=8,bg='#ffc107', command=clicked4)
button4.grid(row=2,column=0, stick = S+N+E+W)

button5 = Button(LeftFrame, text=" ", font=('Times 26 bold'),state=DISABLED, height = 3, width=8,bg='#dc3545', command=clicked5)
button5.grid(row=2,column=1, stick = S+N+E+W)

button6 = Button(LeftFrame, text=" ", font=('Times 26 bold'),state=DISABLED, height = 3, width=8,bg='#ffc107', command=clicked6)
button6.grid(row=2,column=2, stick = S+N+E+W)

button7 = Button(LeftFrame, text=" ", font=('Times 26 bold'),state=DISABLED, height = 3, width=8,bg='#dc3545', command=clicked7)
button7.grid(row=3,column=0, stick = S+N+E+W)

button8 = Button(LeftFrame, text=" ", font=('Times 26 bold'),state=DISABLED, height = 3, width=8,bg='#ffc107', command=clicked8)
button8.grid(row=3,column=1, stick = S+N+E+W)

button9 = Button(LeftFrame, text=" ", font=('Times 26 bold'),state=DISABLED, height = 3, width=8,bg='#dc3545', command=clicked9)
button9.grid(row=3,column=2, stick = S+N+E+W)

#Appending buttons to a List
butList.append(button1)
butList.append(button2)
butList.append(button3)
butList.append(button4)
butList.append(button5)
butList.append(button6)
butList.append(button7)
butList.append(button8)
butList.append(button9)

#fun for sending actions
def send(x,count,isWin,isDraw):
    global c
    print("send count: " ,count)
    print("send score X: ",PlayerX.get())
    print("status win: ",isWin)
    print("status draw: ",isDraw)
    print("-----------------------------------------------------")
    try:
        soc.sendall(str.encode("\n".join([str(x), str(count), str(PlayerX.get()), str(isWin), str(isDraw)])))
    except:
        reset()
        print("error fuc send")
        print("Error with sendall function")
        tkinter.messagebox.showwarning("Warnning", "Plz connect again")
        print("Plz connect again")

#fun to receive actions
def receive_thread(s):
    global PlayerX
    global turn
    global count
    global soc
    global isWin
    global isDraw
    turn = 1
    while True:
        try:
            x,cout,scoreO,win,draw = [int(i) for i in soc.recv(2048).decode('ascii').split('\n')]
        except:
            print("error fuc receive_thread")
            print("Error with receive function")
            print("Player Disconected")
            tkinter.messagebox.showwarning("Warnning", "Server Maintenance")
            break
            
        try:
            PlayerO.set(scoreO)
            x = x-1
            butList[x]["text"] = "O"
            isWin = win
            isDraw = draw

            print("score O is : ",scoreO)
            print("count from server: ",cout)
            print("status win: ",isWin)
            print("-----------------------------------------------------")
            count = cout
            if(win == 1):
                lose()
                reset()
            elif(draw == 1):
                tkinter.messagebox.showinfo("Game Ended", "Draw !!!")
                reset()
                break
            turn = 1
            print("now count: " ,count)
        except:
            print("Player Disconected")
            tkinter.messagebox.showwarning("Warnning", "Server Maintenance")
            break

root.resizable(width=False, height=False)
root.mainloop()
