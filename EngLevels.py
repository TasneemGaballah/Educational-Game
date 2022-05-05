from tkinter import *
from tkinter.font import BOLD
from tkinter import messagebox

import L1 ,L2 ,L3 , L4 , L5 , L6
import DB_name

def view():

    global topp
    topp = Tk()

    topp.title(f'Which Level do you want,{DB_name.x}?')
    topp.attributes('-fullscreen', True)
    topp.config(background="#7d7bc5")
    
    #--------Icon--------
    p = PhotoImage(file= "P\\page1.png")
    topp.iconphoto(False,p)

    #-------Background--------
    bg = PhotoImage(file="P\\page.png")
    back = Label(topp,image=bg)
    back.place(x=0,y=0,relwidth=1 ,relheight=1)

    #frame
    global fr
    fr = Frame(topp,width='800',height='650',bg="#f5deb3")
    fr.pack(pady=20)

    # Button for closing
    exit_button = Button(fr, text="Exit",width=9,height=2,font=("Comic Sans MS",20,BOLD) 
                ,relief = GROOVE ,bg="#e91e63",fg="white", borderwidth=2, command=topp.destroy)
    exit_button.pack(side=BOTTOM )

    t = Label(fr , text=f"Welcome To English game ,{DB_name.x}",font=("Courier",18,BOLD),fg="#4c2b50",bg="#c9a0dc")
    t.pack(side= TOP ,fill=X, pady=20)

    t1 = Label(fr , text=f'Which Level do you want,{DB_name.x}?',font=("Courier",18,BOLD),fg="white",bg="#0b5394")
    t1.pack(after=t,side= TOP ,fill=X , pady=80)

    #Buttons functions
    def b1():
        topp.destroy()
        L1.game.Game()

    def b2():
        topp.destroy()
        L2.game.Game()

    def b3():
        topp.destroy()
        L3.game.Game()

    def b4():
        topp.destroy()
        L4.game.Game()
    
    def b5():
        topp.destroy()
        L5.game.Game()
    
    def b6():
        topp.destroy()
        L6.game.Game()

    #create the choose button
    btn1 = Button(fr, text= "Level 1",width=8,height=2,font=("Comic Sans MS",24,BOLD)
                    ,relief = GROOVE ,bg="#ff8b00",fg="white", borderwidth=2 , command=b1)
    btn1.pack(pady=80,side= LEFT)
    btn2 = Button(fr, text= "Level 2",width=8,height=2,font=("Comic Sans MS",24,BOLD)
                    ,relief = GROOVE ,bg="#ff8b00",fg="white", borderwidth=2, command=b2)
    btn2.pack(pady=80,after=btn1 , side= LEFT)
    btn3 = Button(fr, text= "Level 3",width=8,height=2,font=("Comic Sans MS",24,BOLD) 
                    ,relief = GROOVE ,bg="#ff8b00",fg="white", borderwidth=2, command=b3)
    btn3.pack(pady= 80 , after=btn2 , side=LEFT)
    btn4 = Button(fr, text= "Level 4",width=8,height=2,font=("Comic Sans MS",24,BOLD)
                    ,relief = GROOVE ,bg="#ff8b00",fg="white", borderwidth=2, command=b4)
    btn4.pack( after=btn3,pady= 80, side= LEFT)
    btn5 = Button(fr, text= "Level 5",width=8,height=2,font=("Comic Sans MS",24,BOLD) 
                    ,relief = GROOVE ,bg="#ff8b00",fg="white", borderwidth=2, command=b5)
    btn5.pack(pady= 80, after=btn4, side= LEFT)
    btn6 = Button(fr, text= "Level 6",width=8,height=2,font=("Comic Sans MS",24,BOLD)
                    ,relief = GROOVE ,bg="#ff8b00",fg="white", borderwidth=2, command=b6)
    btn6.pack( after=btn5,pady= 80, side= LEFT)
    
    topp.mainloop()