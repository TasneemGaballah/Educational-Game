from tkinter import *
from tkinter.font import BOLD
from tkinter import messagebox
from turtle import left, right

import CheckAnswerE
import Transform

class game:

    chance = 5
    counter = 0

    def Game():
        
        global top
        top = Tk()

        top.title('Question One')
        top.attributes('-fullscreen', True)
        top.config(background="#7d7bc5")
        
        t = Label(top , text="Welcome To Level Five"
                    ,font=("Courier",16,BOLD),fg="#4c2b50",bg="#c9a0dc")
        t.pack(fill=X)
        #--------Icon--------
        p = PhotoImage(file= "P\\page1.png")
        top.iconphoto(False,p)

        #-------Background--------
        bg = PhotoImage(file="P\\page.png")
        back = Label(top,image=bg)
        back.place(x=0,y=0,relwidth=1 ,relheight=1)
        #place the text into the main window
        #frame
        global fr2
        fr2 = Frame(top,width='1000',height='850',bg="#f5deb3")
        fr2.pack(pady=20)
        #cnvas = Canvas(fr2,bg="#f5deb3",width='800',height='550')
        # Button for closing
        exit_button = Button(fr2, text="Exit",width=5,height=1,font=("Comic Sans MS",10,BOLD) 
                    ,relief = GROOVE ,bg="#e91e63",fg="white", borderwidth=2, command=top.destroy)
        exit_button.pack(side=BOTTOM)
        q1 = Label(fr2, text="where is the black hair"
                    ,font=("Comic Sans MS",28,BOLD),fg="#4c2b50",bg="#ff8b00")
        q1.pack(fill=X , pady=30)
        #image
        photo5 = PhotoImage(file ='P\\black.png') #########
        photo6 = PhotoImage(file='P\\baby.png')
        photo7 = PhotoImage(file='P\\baby.png')
        photo8 = PhotoImage(file='P\\baby.png')
        #command
        def bW():
            CheckAnswerE.WrongAnswer("L5") 
        def bR():
            CheckAnswerE.RightAnswer("L5")
        #create the choose button
        btn1 = Button(fr2, image= photo5,width=250,height=150 
                        ,relief = GROOVE ,bg="#98f5ff", borderwidth=2,command= bW)
        btn1.pack(pady=50,side= LEFT)
        btn2 = Button(fr2, image= photo6,width=250,height=150 
                        ,relief = GROOVE ,bg="#98f5ff", borderwidth=2,command= bR)
        btn2.pack(pady=50,after=btn1 , side= RIGHT)
        btn3 = Button(fr2, image= photo7,width=250,height=150  
                        ,relief = GROOVE ,bg="#98f5ff", borderwidth=2,command= bW)
        btn3.pack(pady= 10, side= LEFT)
        btn4 = Button(fr2, image= photo8,width=250,height=150 
                        ,relief = GROOVE ,bg="#98f5ff", borderwidth=2,command= bW)
        btn4.pack(pady=10 , side= RIGHT)
        #cnvas.pack()
        top.mainloop()

    def nextQ1():
        global top1
        top1 = Tk()
        top1.title('Question One')
        top1.attributes('-fullscreen', True)
        top1.config(background="#7d7bc5")
        #--------Icon--------
        p = PhotoImage(file= "P\\page1.png")
        top1.iconphoto(False,p)

        #-------Background--------
        bg = PhotoImage(file="P\\page.png")
        back = Label(top1,image=bg)
        back.place(x=0,y=0,relwidth=1 ,relheight=1)
        #frame
        fr2 = Frame(top1,width='800',height='650',bg="#f5deb3")
        fr2.pack(pady=20)
        #image
        q1 = Label(fr2, text="where is the black hair"
                    ,font=("Comic Sans MS",28,BOLD),fg="#4c2b50",bg="#ff8b00")
        q1.pack(fill=X , pady=30)
        #image
        photo5 = PhotoImage(file ='P\\black.png') #########
        photo6 = PhotoImage(file='P\\baby.png')
        photo7 = PhotoImage(file='P\\baby.png')
        photo8 = PhotoImage(file='P\\baby.png')
        #command
        def bW():
            CheckAnswerE.WrongAnswer2("L5") 
        def bR():
            CheckAnswerE.RightAnswer2("L5")
        #create the choose button
        btn1 = Button(fr2, image= photo5,width=250,height=150 
                        ,relief = GROOVE ,bg="#98f5ff", borderwidth=2,command= bW)
        btn1.pack(pady=50,side= LEFT)
        btn2 = Button(fr2, image= photo6,width=250,height=150 
                        ,relief = GROOVE ,bg="#98f5ff", borderwidth=2,command= bR)
        btn2.pack(pady=50,after=btn1 , side= RIGHT)
        btn3 = Button(fr2, image= photo7,width=250,height=150  
                        ,relief = GROOVE ,bg="#98f5ff", borderwidth=2,command= bW)
        btn3.pack(pady= 10, side= LEFT)
        btn4 = Button(fr2, image= photo8,width=250,height=150 
                        ,relief = GROOVE ,bg="#98f5ff", borderwidth=2,command= bW)
        btn4.pack(pady=10 , side= RIGHT)
        #cnvas.pack()
        top.mainloop()

    def nextQ2():
        global top2
        top2 = Tk()
        top2.title('Question Three')
        top2.attributes('-fullscreen', True)
        top2.config(background="#7d7bc5")
        #--------Icon--------
        p = PhotoImage(file= "P\\page1.png")
        top2.iconphoto(False,p)

        #-------Background--------
        bg = PhotoImage(file="P\\page.png")
        back = Label(top2,image=bg)
        back.place(x=0,y=0,relwidth=1 ,relheight=1)
        #frame
        fr2 = Frame(top2,width='800',height='650',bg="#f5deb3")
        fr2.pack(pady=20)
        q1 = Label(fr2, text="where is the black hair"
                    ,font=("Comic Sans MS",28,BOLD),fg="#4c2b50",bg="#ff8b00")
        q1.pack(fill=X , pady=30)
        #image
        photo5 = PhotoImage(file ='P\\black.png') #########
        photo6 = PhotoImage(file='P\\baby.png')
        photo7 = PhotoImage(file='P\\baby.png')
        photo8 = PhotoImage(file='P\\baby.png')
        #command
        def bW():
            CheckAnswerE.WrongAnswer3("L5") 
        def bR():
            CheckAnswerE.RightAnswer3("L5")
        #create the choose button
        btn1 = Button(fr2, image= photo5,width=250,height=150 
                        ,relief = GROOVE ,bg="#98f5ff", borderwidth=2,command= bW)
        btn1.pack(pady=50,side= LEFT)
        btn2 = Button(fr2, image= photo6,width=250,height=150 
                        ,relief = GROOVE ,bg="#98f5ff", borderwidth=2,command= bR)
        btn2.pack(pady=50,after=btn1 , side= RIGHT)
        btn3 = Button(fr2, image= photo7,width=250,height=150  
                        ,relief = GROOVE ,bg="#98f5ff", borderwidth=2,command= bW)
        btn3.pack(pady= 10, side= LEFT)
        btn4 = Button(fr2, image= photo8,width=250,height=150 
                        ,relief = GROOVE ,bg="#98f5ff", borderwidth=2,command= bW)
        btn4.pack(pady=10 , side= RIGHT)
        #cnvas.pack()
        top.mainloop()

    def nextQ3():
        global top3
        top3 = Tk()
        top3.title('Question Four')
        top3.attributes('-fullscreen', True)
        top3.config(background="#7d7bc5")
        #--------Icon--------
        p = PhotoImage(file= "P\\page1.png")
        top3.iconphoto(False,p)

        #-------Background--------
        bg = PhotoImage(file="P\\page.png")
        back = Label(top3,image=bg)
        back.place(x=0,y=0,relwidth=1 ,relheight=1)
        #frame
        fr2 = Frame(top3,width='800',height='650',bg="#f5deb3")
        fr2.pack(pady=20)
        q1 = Label(fr2, text="where is the black hair"
                    ,font=("Comic Sans MS",28,BOLD),fg="#4c2b50",bg="#ff8b00")
        q1.pack(fill=X , pady=30)
        #image
        photo5 = PhotoImage(file ='P\\black.png') #########
        photo6 = PhotoImage(file='P\\baby.png')
        photo7 = PhotoImage(file='P\\baby.png')
        photo8 = PhotoImage(file='P\\baby.png')
        #command
        def bW():
            CheckAnswerE.WrongAnswer4("L5") 
        def bR():
            CheckAnswerE.RightAnswer4("L5")
        #create the choose button
        btn1 = Button(fr2, image= photo5,width=250,height=150 
                        ,relief = GROOVE ,bg="#98f5ff", borderwidth=2,command= bW)
        btn1.pack(pady=50,side= LEFT)
        btn2 = Button(fr2, image= photo6,width=250,height=150 
                        ,relief = GROOVE ,bg="#98f5ff", borderwidth=2,command= bR)
        btn2.pack(pady=50,after=btn1 , side= RIGHT)
        btn3 = Button(fr2, image= photo7,width=250,height=150  
                        ,relief = GROOVE ,bg="#98f5ff", borderwidth=2,command= bW)
        btn3.pack(pady= 10, side= LEFT)
        btn4 = Button(fr2, image= photo8,width=250,height=150 
                        ,relief = GROOVE ,bg="#98f5ff", borderwidth=2,command= bW)
        btn4.pack(pady=10 , side= RIGHT)
        
        top.mainloop()
    
    def nextQ4():
        global top4
        top4 = Tk()
        top4.title('Question Four')
        top4.attributes('-fullscreen', True)
        top4.config(background="#7d7bc5")
        #--------Icon--------
        p = PhotoImage(file= "P\\page1.png")
        top4.iconphoto(False,p)

        #-------Background--------
        bg = PhotoImage(file="P\\page.png")
        back = Label(top4,image=bg)
        back.place(x=0,y=0,relwidth=1 ,relheight=1)
        #frame
        fr2 = Frame(top4,width='800',height='650',bg="#f5deb3")
        fr2.pack(pady=20)
        btn = Button(fr2, text= "Next Level",width=12,height=1,font=("Comic Sans MS",14,BOLD) 
                        ,relief = GROOVE ,bg="#4c3946",fg="white", borderwidth=2,command= game.nextLevel)
        btn.pack(side=BOTTOM)
        q1 = Label(fr2, text="where is the black hair"
                    ,font=("Comic Sans MS",28,BOLD),fg="#4c2b50",bg="#ff8b00")
        q1.pack(fill=X , pady=30)
        #image
        photo5 = PhotoImage(file ='P\\black.png') #########
        photo6 = PhotoImage(file='P\\baby.png')
        photo7 = PhotoImage(file='P\\baby.png')
        photo8 = PhotoImage(file='P\\baby.png')
        #command
        def bW():
            CheckAnswerE.WrongAnswer5("L5") 
        def bR():
            CheckAnswerE.RightAnswer5("L5")
        #create the choose button
        btn1 = Button(fr2, image= photo5,width=250,height=150 
                        ,relief = GROOVE ,bg="#98f5ff", borderwidth=2,command= bW)
        btn1.pack(pady=50,side= LEFT)
        btn2 = Button(fr2, image= photo6,width=250,height=150 
                        ,relief = GROOVE ,bg="#98f5ff", borderwidth=2,command= bR)
        btn2.pack(pady=50,after=btn1 , side= RIGHT)
        btn3 = Button(fr2, image= photo7,width=250,height=150  
                        ,relief = GROOVE ,bg="#98f5ff", borderwidth=2,command= bW)
        btn3.pack(pady= 10, side= LEFT)
        btn4 = Button(fr2, image= photo8,width=250,height=150 
                        ,relief = GROOVE ,bg="#98f5ff", borderwidth=2,command= bW)
        btn4.pack(pady=10 , side= RIGHT)
        #cnvas.pack()
        
        top.mainloop()

    def nextLevel ():
        top4.destroy()
        #Transform.backToHome()
        