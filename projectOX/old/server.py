import socket
import sys
import tkinter.messagebox
from _thread import *
from threading import *
from tkinter import *

#http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter
#port = 7000





def text_change_online():
    lblPlayerO["text"] = 'Host    O '
    lblPlayerX["text"] = 'Player X '
    #show ip
    lblIPHost.grid(row=1,column=0)
    entryHost.grid(row=1,column=1,padx=5)
    btnConnect1.grid(row=1,column=2)
    MainFrame.grid(row=2, column=0,padx=30)

def text_change_online_PvP():
    lblPlayerO["text"] = 'Player  O'
    lblPlayerX["text"] = 'Player  X'
    #show ip
    lblIPHost.grid(row=1,column=0)
    entryHost.grid(row=1,column=1,padx=5)
    btnConnect1.grid(row=1,column=2)
    MainFrame.grid(row=2, column=0,padx=30)

def acceptconnect():
    #w8 for client
    soc.listen(5)
    global c,add,c2,add2,mode
    if(mode == 'pvp'):
        print ("== ::SERVER Established")
        c , add = soc.accept()
        print("connection from", add[0])
        c2 , add2 = soc.accept()
        print("connection from", add2[0])
        start_new_thread(ClientReceive2,(c,c2,"O"))
        start_new_thread(ClientReceive2,(c2,c,"X"))
        reset()
    else:
        print ("== ::SERVER Established")
        c , add = soc.accept()
        print("connection from", add[0])
        start_new_thread(ClientReceive,(c,))
        reset()
        



#Variable root for TK
root = Tk()
root.title(" GAME OX PROJECT ")
w=1120
h=680
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

hallf = []

#CAL POSITION
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)-50

root.geometry('%dx%d+%d+%d' % (w,h,x,y))
root.configure(background = '#DAF7A6')

  
def NewGame_HvP():
    global soc,host_ip
    global c
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
    try:
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostname()
        port = 7000
        soc.bind((host, port))
    except:
        print("Error with connection!")

def NewGame_PvP():
    global soc,host_ip,mode
    global c,c2
    mode='pvp'
    reset()
    PlayerX.set(0)
    PlayerO.set(0)
    text_change_online_PvP()
    try:
        soc=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = socket.gethostname()
        port = 7000
        soc.bind((host, port))
    except:
        print("Error with connection!")

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


def openhof():
    
    
    w2 = 1280
    h2 = 720
    #CAL POSITION
    x2 = (ws/2) - (w2/2)
    y2 = (hs/2) - (h2/2)-50

    window =Tk()
    window.geometry('%dx%d+%d+%d' % (w2,h2,x2,y2))
    window.title("Hall of Fame")
    window.configure(background = 'bisque2')
    Topfr = Frame(window, bg = 'bisque2',width=100, height=50)
    Topfr.pack(side=TOP)
    MainFrame = Frame(window, bg = '#2b5797',width=200, height=500)
    MainFrame.pack(side=TOP)
    #### Top Frame #####
    TopHFrame = Frame(MainFrame, bg = 'black',width=200, height=500)
    TopHFrame.pack(side=TOP)
    lblTitle = Label(TopHFrame,font=('arial',50,'bold'), text="Hall of Fame", bd=15,bg="tomato2",fg="Cornsilk",justify=CENTER)
    lblTitle.grid(row=0,column=0)
    #### Middle #####
    MiddleHFrame = Frame(MainFrame, bg = '#B22222',width=200, height=500)
    MiddleHFrame.pack(side=TOP)

    MHFrame = Frame(MiddleHFrame, bg = 'white',width=200, height=500)
    MHFrame.pack(side=TOP)

    MHFrameLeft = Frame(MHFrame, bg = 'black',width=200, height=500)
    MHFrameLeft.pack(side=LEFT)

    MHFrameRight = Frame(MHFrame, bg = 'tomato2',width=200, height=500)
    MHFrameRight.pack(side=RIGHT)

    labels = []
    lblIP = Label(MHFrameLeft,font=('arial',20,'bold'), text="IP",bg="White",width=15,borderwidth=2, relief="solid")
    lblIP.grid(row=0,column=0)
    lblScore = Label(MHFrameRight,font=('arial',20,'bold'), text="Score",bg="White",width=15,borderwidth=2, relief="solid")
    lblScore.grid(row=0,column=1)
    lblplaycount = Label(MHFrameRight,font=('arial',20,'bold'), text="play count",bg="White",width=15,borderwidth=2, relief="solid")
    lblplaycount.grid(row=0,column=2)
    for i in range(len(hallf)):
        label = Label(MHFrameLeft,font=('arial',20,'bold'), text=hallf[i][0],bd=2,fg="black",width=15, relief="solid")
        label.grid(row=i+1,column=0)
        label2 = Label(MHFrameRight,font=('arial',20,'bold'), text=hallf[i][1],bd=2,fg="black",width=15, relief="solid")
        label2.grid(row=i+1,column=1)
        label3 = Label(MHFrameRight,font=('arial',20,'bold'), text=hallf[i][2],bg="White",width=15,borderwidth=2, relief="solid")
        label3.grid(row=i+1,column=2)
        labels.append(label)
        labels.append(label2)
        labels.append(label3)
    #score.txt (Player score)############################    

    
    for i in range(len(hallf)): 
        out = open("score.txt","w",encoding="utf-8")                     
        out.write(str(hallf[i][0])+"/"+str(hallf[i][1])+"/"+str(hallf[i][2])+"/"+str(len(hallf))+"\n")
        out.close()
        print("send_score.txt")
    #score.txt (Player score)###############
        



    ##### Button to exit hallframe #####
    def close_window ():
        window.destroy()
    BottomHFrame = Frame(MainFrame, bg = 'lime green',width=700, height=100)
    BottomHFrame.pack(side=TOP)
    btnPG = Button(BottomHFrame, text="Exit", font=('Times 15 bold'), height = 1, width=15,bg="#edb44e",command=close_window)
    btnPG.grid(row=2,column=0)


menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Host Vs Player", command=NewGame_HvP)
filemenu.add_command(label="Player Vs Player", command=NewGame_PvP)
filemenu.add_command(label="Reset", command=reset)
filemenu.add_command(label="Hall Of Frame", command=openhof)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)



root.config(menu=menubar)

#GET IP HOST
try:
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
except:
    print("Can't get hostname or IP")
mode = ''


#---- Frame ----#
TopTop = Frame(root, bg = '#DAF7A6', pady=2,width=1350, height=100, relief=RIDGE)
TopTop.grid(row=0, column=0)

Title = Label(TopTop,font=('arial',50,'bold'), text="Game OX (Server)", bd=15,bg='#008080',justify=CENTER,relief="raised")
Title.grid(row=0,column=0)

#### IP player#####
BottomFrame = Frame(root, pady=2,width=1350, height=100, relief=RIDGE,bg ='#DAF7A6')
BottomFrame.grid(row=1, column=0)
lblFake = Label(BottomFrame,font=('arial',12,'bold'), text="", bd=21,bg="#DAF7A6",fg="Cornsilk",justify=CENTER)
lblFake.grid(row=1,column=0)
lblIPHost = Label(BottomFrame,font=('arial',12,'bold'), text="IP", bd=21,bg="#B22222",fg="Cornsilk",justify=CENTER)
lblIPHost.grid(row=1,column=0)
lblIPHost.grid_remove()
entryHost = Label(BottomFrame,font=('arial',12,'bold'), text=str(host_ip),bd=21,bg="#B22222",fg="Cornsilk",justify=CENTER)
entryHost.grid(row=1,column=1)
entryHost.grid_remove()
btnConnect1 = Button(BottomFrame,text="Host", font=('Times 22 bold'), height = 1, width=20,bg="#edb44e",command=acceptconnect)
btnConnect1.grid(row=1,column=2,padx=5)
btnConnect1.grid_remove()

##### middle ####
MainFrame = Frame(root, pady=2,width=20, height=200, relief=RIDGE,bg ='#00FFFF')
MainFrame.grid(row=2, column=0,padx=30)


LeftFrame = Frame(MainFrame , bd=10, width=200, height=200,pady=5,padx=10,bg="#00FFFF" , relief=RIDGE)
LeftFrame.pack(side=LEFT,expand = True, fill = BOTH)

RightFrame = Frame(MainFrame , bd=10, width=200, height=300,padx=10,pady=20,bg="#00FFFF" , relief=RIDGE)
RightFrame.pack(side=RIGHT,expand = True, fill = BOTH)

RightFrame1 = Frame(RightFrame , bd=10, width=200, height=200,padx=10,pady=2,bg="#edb44e" , relief=RIDGE)
RightFrame1.grid(row=0,column=0)
RightFrame1.grid_columnconfigure(0, weight=1)


##### set player #####
PlayerX=IntVar()
PlayerO=IntVar()

PlayerX.set(0)
PlayerO.set(0)

player = 2
count = 0


isWin = 0
isDraw = 0

##------ text field -------
lblPlayerO = Label(RightFrame1,font=('arial',26,'bold'), text="Player1  X", padx=2,pady=2,bg="#edb44e")
lblPlayerO.grid(row=0,column=0,sticky=W)
txtPlayerO=Label(RightFrame1,font=('arial',26,'bold'), bd=2,fg="black",textvariable= PlayerO, width=14,
                 justify=CENTER).grid(row=0,column=1)


lblPlayerX = Label(RightFrame1,font=('arial',26,'bold'), text="Player2  O", padx=2,pady=2,bg="#edb44e")
lblPlayerX.grid(row=1,column=0,sticky=W)
txtPlayerX=Label(RightFrame1,font=('arial',26,'bold'), bd=2,fg="black",textvariable= PlayerX, width=14,
                 justify=CENTER).grid(row=1,column=1)



def check (num): #check btn 
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

    if (b1==b2 and b2==b3 and b1=='O')or(b1==b2 and b2==b3 and b1=='X'):
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
    elif (b4==b5 and b5==b6 and b4=='O')or(b4==b5 and b5==b6 and b4=='X'):
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
    elif (b7==b8 and b8==b9 and b7=='O')or(b7==b8 and b8==b9 and b7=='X'):
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
    elif (b1==b4 and b4==b7 and b1=='O')or(b1==b4 and b4==b7 and b1=='X'):
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
    elif (b2==b5 and b5==b8 and b2=='O')or(b2==b5 and b5==b8 and b2=='X'):
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
    elif (b3==b6 and b6==b9 and b3=='O')or(b3==b6 and b6==b9 and b3=='X'):
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
    elif (b1==b5 and b5==b9 and b1=='O')or(b1==b5 and b5==b9 and b1=='X'):
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
    elif (b3==b5 and b5==b7 and b3=='O')or(b3==b5 and b5==b7 and b3=='X'):
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
    elif count == 9:
        tkinter.messagebox.showinfo("Game Ended","Draw !!!!")
        isDraw = 1
        send(num,count,isWin,isDraw)
        count = 0
        reset()

#func of messaging congrats
def win(player):
    tkinter.messagebox.showinfo("Game Ended", player+" is Winner!!!!")
    if(player=="X"):
        for i in range(len(hallf)):
            if hallf[i][0]==add[0]:
                hallf[i][1]=hallf[i][1]+1
                hallf[i][2]=hallf[i][2]+1
                return 0
        hallf.append([add[0],1,1])
    else:
        for i in range(len(hallf)):
            if hallf[i][0]==add[0]:
                hallf[i][2]=hallf[i][2]+1
                return 0
        hallf.append([add[0],0,1])


def lose():
    tkinter.messagebox.showinfo("Game Ended", "You lose !!!")
    for i in range(len(hallf)):
        if hallf[i][0]==add[0]:
            hallf[i][1]=hallf[i][1]+1
            hallf[i][2]=hallf[i][2]+1
            return 0
    hallf.append([add[0],1,1])
    reset()




##### set click O X && reset new game ####
buttons = StringVar()
click = True
draw = 0

def checker(buttons):
    global click
    if buttons["text"] == " " and click == True:
        buttons["text"] = "X"
        click = False
        scorekeeper()
    elif buttons["text"] == " " and click == False:
        buttons["text"] = "O"
        click = True
        scorekeeper()

def scorekeeper():
    global draw
    draw +=1
    print("Draw point: ",draw)
    if(button1["text"]=="X" and button2["text"]=="X" and button3["text"]=="X"):
        button1.configure(background="PaleGreen1")
        button2.configure(background="PaleGreen1")
        button3.configure(background="PaleGreen1")
        n = int(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Game Ended", "X is Winner!!!!")
        draw = 0
        reset()

    elif(button4["text"]=="X" and button5["text"]=="X" and button6["text"]=="X"):
        button4.configure(background="PaleGreen1")
        button5.configure(background="PaleGreen1")
        button6.configure(background="PaleGreen1")
        n = int(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Game Ended", "X is Winner!!!!")
        draw = 0
        reset()

    elif(button7["text"]=="X" and button8["text"]=="X" and button9["text"]=="X"):
        button7.configure(background="PaleGreen1")
        button8.configure(background="PaleGreen1")
        button9.configure(background="PaleGreen1")
        n = int(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Game Ended", "X is Winner!!!!")
        draw = 0
        reset()

    elif(button3["text"]=="X" and button5["text"]=="X" and button7["text"]=="X"):
        button3.configure(background="PaleGreen1")
        button5.configure(background="PaleGreen1")
        button7.configure(background="PaleGreen1")
        n = int(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Game Ended", "X is Winner!!!!")
        draw = 0
        reset()

    elif(button1["text"]=="X" and button5["text"]=="X" and button9["text"]=="X"):
        button1.configure(background="PaleGreen1")
        button5.configure(background="PaleGreen1")
        button9.configure(background="PaleGreen1")
        n = int(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Game Ended", "X is Winner!!!!")
        draw = 0
        reset()

    elif(button1["text"]=="X" and button4["text"]=="X" and button7["text"]=="X"):
        button1.configure(background="PaleGreen1")
        button4.configure(background="PaleGreen1")
        button7.configure(background="PaleGreen1")
        n = int(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Game Ended", "X is Winner!!!!")
        draw = 0
        reset()

    elif(button2["text"]=="X" and button5["text"]=="X" and button8["text"]=="X"):
        button2.configure(background="PaleGreen1")
        button5.configure(background="PaleGreen1")
        button8.configure(background="PaleGreen1")
        n = int(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Game Ended", "X is Winner!!!!")
        draw = 0
        reset()

    elif(button3["text"]=="X" and button6["text"]=="X" and button9["text"]=="X"):
        button3.configure(background="PaleGreen1")
        button6.configure(background="PaleGreen1")
        button9.configure(background="PaleGreen1")
        n = int(PlayerX.get())
        score = (n+1)
        PlayerX.set(score)
        tkinter.messagebox.showinfo("Game Ended", "X is Winner!!!!")
        draw = 0
        reset()


    #### O side ###
    if(button1["text"]=="O" and button2["text"]=="O" and button3["text"]=="O"):
        button1.configure(background="PaleGreen1")
        button2.configure(background="PaleGreen1")
        button3.configure(background="PaleGreen1")
        n = int(PlayerO.get())
        score = (n+1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Game Ended", "O is Winner!!!!")
        draw = 0
        reset()

    elif(button4["text"]=="O" and button5["text"]=="O" and button6["text"]=="O"):
        button4.configure(background="PaleGreen1")
        button5.configure(background="PaleGreen1")
        button6.configure(background="PaleGreen1")
        n = int(PlayerO.get())
        score = (n+1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Game Ended", "O is Winner!!!!")
        draw = 0
        reset()

    elif(button7["text"]=="O" and button8["text"]=="O" and button9["text"]=="O"):
        button7.configure(background="PaleGreen1")
        button8.configure(background="PaleGreen1")
        button9.configure(background="PaleGreen1")
        n = int(PlayerO.get())
        score = (n+1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Game Ended", "O is Winner!!!!")
        draw = 0
        reset()

    elif(button3["text"]=="O" and button5["text"]=="O" and button7["text"]=="O"):
        button3.configure(background="PaleGreen1")
        button5.configure(background="PaleGreen1")
        button7.configure(background="PaleGreen1")
        n = int(PlayerO.get())
        score = (n+1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Game Ended", "O is Winner!!!!")
        draw = 0
        reset()

    elif(button1["text"]=="O" and button5["text"]=="O" and button9["text"]=="O"):
        button1.configure(background="PaleGreen1")
        button5.configure(background="PaleGreen1")
        button9.configure(background="PaleGreen1")
        n = int(PlayerO.get())
        score = (n+1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Game Ended", "O is Winner!!!!")
        draw = 0
        reset()

    elif(button1["text"]=="O" and button4["text"]=="O" and button7["text"]=="O"):
        button1.configure(background="PaleGreen1")
        button4.configure(background="PaleGreen1")
        button7.configure(background="PaleGreen1")
        n = int(PlayerO.get())
        score = (n+1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Game Ended", "O is Winner!!!!")
        draw = 0
        reset()

    elif(button2["text"]=="O" and button5["text"]=="O" and button8["text"]=="O"):
        button2.configure(background="PaleGreen1")
        button5.configure(background="PaleGreen1")
        button8.configure(background="PaleGreen1")
        n = int(PlayerO.get())
        score = (n+1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Game Ended", "O is Winner!!!!")
        draw = 0
        reset()

    elif(button3["text"]=="O" and button6["text"]=="O" and button9["text"]=="O"):
        button3.configure(background="PaleGreen1")
        button6.configure(background="PaleGreen1")
        button9.configure(background="PaleGreen1")
        n = int(PlayerO.get())
        score = (n+1)
        PlayerO.set(score)
        tkinter.messagebox.showinfo("Game Ended", "O is Winner!!!!")
        draw = 0
        reset()

    elif(draw==9):
        tkinter.messagebox.showinfo("Draw !!!!","Game Ended")
        reset()
        draw = 0




def enable_button():
    #set btn is normal state
    button1['state'] = 'normal'
    button2['state'] = 'normal'
    button3['state'] = 'normal'
    button4['state'] = 'normal'
    button5['state'] = 'normal'
    button6['state'] = 'normal'
    button7['state'] = 'normal'
    button8['state'] = 'normal'
    button9['state'] = 'normal'

#flag to chose player
turn =1
#fun of button command 1
def clicked1():
    global turn
    global count
    global isWin
    global isDraw
    global isDraw
    if button1["text"]==" ":
        if turn ==1:
            count +=1
            turn =2
            button1["text"] ='O'
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
            button2["text"] ='O'
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
            button3["text"] ='O'
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
            button4["text"] ='O'
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
            button5["text"] ='O'
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
            button6["text"] ='O'
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
            button7["text"] ='O'
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
            button8["text"] ='O'
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
            button9["text"] ='O'
            send(9,count,isWin,isDraw)
        check(9)


#list of the buttons pressed
butList = list()

############# Set & Draw 3x3 button ######

button1 = Button(LeftFrame, text=" ", font=('Times 26 bold'),state=DISABLED, height = 3, width=7,bg='#dc3545', command=clicked1)
button1.grid(row=1,column=0, stick = S+N+E+W)

button2 = Button(LeftFrame, text=" ", font=('Times 26 bold'),state=DISABLED, height = 3, width=7,bg='#ffc107', command=clicked2)
button2.grid(row=1,column=1, stick = S+N+E+W)

button3 = Button(LeftFrame, text=" ", font=('Times 26 bold'),state=DISABLED, height = 3, width=7,bg='#dc3545', command=clicked3)
button3.grid(row=1,column=2, stick = S+N+E+W)

button4 = Button(LeftFrame, text=" ", font=('Times 26 bold'),state=DISABLED, height = 3, width=7,bg='#ffc107', command=clicked4)
button4.grid(row=2,column=0, stick = S+N+E+W)

button5 = Button(LeftFrame, text=" ", font=('Times 26 bold'),state=DISABLED, height = 3, width=7,bg='#dc3545', command=clicked5)
button5.grid(row=2,column=1, stick = S+N+E+W)

button6 = Button(LeftFrame, text=" ", font=('Times 26 bold'),state=DISABLED, height = 3, width=7,bg='#ffc107', command=clicked6)
button6.grid(row=2,column=2, stick = S+N+E+W)

button7 = Button(LeftFrame, text=" ", font=('Times 26 bold'),state=DISABLED, height = 3, width=7,bg='#dc3545', command=clicked7)
button7.grid(row=3,column=0, stick = S+N+E+W)

button8 = Button(LeftFrame, text=" ", font=('Times 26 bold'),state=DISABLED, height = 3, width=7,bg='#ffc107', command=clicked8)
button8.grid(row=3,column=1, stick = S+N+E+W)

button9 = Button(LeftFrame, text=" ", font=('Times 26 bold'),state=DISABLED, height = 3, width=7,bg='#dc3545', command=clicked9)
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
    print("send score O: ",PlayerO.get())
    print("status win: ",isWin)
    print("status draw: ",isDraw)
    

    
    print("-----------------------------------------------------")
    try:
        c.sendall(str.encode("\n".join([str(x), str(count), str(PlayerO.get()), str(isWin), str(isDraw)])))
    except:
        print("Error with sendall function")
#print
def send2(x,count,isWin,isDraw,who):
    
    print("send count: " ,count)
    print("send score O: ",PlayerO.get())
    print("status win: ",isWin)
    print("status draw: ",isDraw)
    print("-----------------------------------------------------")
    
    try:
        who.sendall(str.encode("\n".join([str(x), str(count), str(PlayerO.get()), str(isWin), str(isDraw)])))
       
    except:
        print("Error with sendall function")
#test send txt

    
   
    
 






#fun to receive actions
def ClientReceive(c):
    global PlayerO
    global turn
    global count
    global soc
    global isWin
    global isDraw
    turn = 1
    while True:
        try:
            x,cout,scoreX,win,draw = [int(i) for i in c.recv(2048).decode('ascii').split('\n')]
        except:
            print("Error with receive function")
        PlayerX.set(scoreX)
        x = x-1
        butList[x]["text"]= "X"
        isWin = win
        isDraw = draw

        print("score X is : ",scoreX)
        print("count from client: ",cout)
        print("status win: ",isWin)
       
        print("-----------------------------------------------------")
        count = cout
        if(win == 1):
            lose()
            reset()
        elif(draw == 1):
            tkinter.messagebox.showinfo("Game Ended", "Draw !!!")
            reset()
        turn = 1
        print("now count: " ,count)

def ClientReceive2(c,c2,mark):
    global PlayerO
    global turn
    global count
    global soc
    global isWin
    global isDraw
    global hallf
    
    turn = 1
    while True:
        try:
            x,cout,scoreX,win,draw = [int(i) for i in c.recv(2048).decode('ascii').split('\n')]
        except:
            print("Error with receive function")
        send2(x,cout,win,draw,c2)
        print(x,cout,win,draw)
       
        PlayerX.set(scoreX)
        x = x-1
        butList[x]["text"]= mark
        isWin = win
        isDraw = draw
        print("score X is : ",scoreX)
        print("count from client: ",cout)
        print("status win: ",isWin)
        print("-----------------------------------------------------")
        count = cout
        if(win == 1):
            if(mark=="O"):
                PlayerO.set(int(PlayerO.get())+1)
                tmp=0;
                for i in range(len(hallf)):
                    if hallf[i][0]==add[0]:
                        hallf[i][1]=hallf[i][1]+1
                        hallf[i][2]=hallf[i][2]+1
                        tmp=1
                        break
                if tmp==0:
                    hallf.append([add[0],1,1])
                tmp=0;
                for i in range(len(hallf)):
                    if hallf[i][0]==add2[0]:
                        hallf[i][2]=hallf[i][2]+1
                        tmp=1
                        break
                if tmp==0:
                    hallf.append([add2[0],0,1])
            else:
                PlayerX.set(int(PlayerX.get())+1)
                tmp=0;
                for i in range(len(hallf)):
                    if hallf[i][0]==add2[0]:
                        hallf[i][1]=hallf[i][1]+1
                        hallf[i][2]=hallf[i][2]+1
                        tmp=1
                        break
                if tmp==0:
                    hallf.append([add2[0],1,1])
                tmp=0;
                for i in range(len(hallf)):
                    if hallf[i][0]==add[0]:
                        hallf[i][2]=hallf[i][2]+1
                        tmp=1
                        break
                if tmp==0:
                    hallf.append([add[0],0,1])
            tkinter.messagebox.showinfo("Game Ended",mark+" is winner !!!")
            reset()
        elif(draw == 1):
            tkinter.messagebox.showinfo("Game Ended", "Draw !!!")
            reset()
        turn = 1
        print("now count: " ,count)
        
        
        



root.resizable(width=False, height=False)
root.mainloop()