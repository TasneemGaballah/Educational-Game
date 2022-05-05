from tkinter import *
from tkinter.font import BOLD
from tkinter import messagebox

import CheckAnswerA
import ArabLevels

class game:

    chance = 5
    counter = 0

    def Game():

        global top
        top = Tk()

        top.title('السؤال الأول')
        top.attributes('-fullscreen', True)
        top.config(background="#7d7bc5")
        
        #--------Icon--------
        p = PhotoImage(file= "P\\page1.png")
        top.iconphoto(False,p)

        #-------Background--------
        bg = PhotoImage(file="P\\arab1.png")
        back = Label(top,image=bg)
        back.place(x=0,y=0,relwidth=1 ,relheight=1)
        #place the text into the main window
        #frame
        global fr2
        fr2 = Frame(top,width='800',height='650',bg="#f5deb3")
        fr2.pack(pady=20)
        t = Label(fr2 , text="مرحباً بك في المستوى الثاني",font=("Calibri",22,BOLD),fg="#4c2b50",bg="#c9a0dc")
        t.pack(fill=X, side= TOP)
        
        # Button for closing
        exit_button = Button(fr2, text="الخروج",width=8,height=1,font=("Calibri",14,BOLD) 
                    ,relief = GROOVE ,bg="#e91e63",fg="white", borderwidth=2, command=top.destroy)
        exit_button.pack(side=BOTTOM)

        q1 = Label(fr2, text= "مرحباً بك في المستوى الأول"
                    ,font=("Calibri",22,BOLD),fg="#4c2b50",bg="#ff8b00")
        q1.pack(fill=X , pady=30)
        
        def bW():
            CheckAnswerA.WrongAnswer("A2") 
        def bR():
            CheckAnswerA.RightAnswer("A2")
        #create the choose button
        btn1 = Button(fr2, text= "Red hair",width=12,height=1,font=("Calibri",14,BOLD) 
                        ,relief = GROOVE ,bg="#98f5ff",fg="black", borderwidth=2,command= bW)
        btn1.pack()
        btn2 = Button(fr2, text= "Black hair",width=12,height=1,font=("Calibri",14,BOLD) 
                        ,relief = GROOVE ,bg="#98f5ff",fg="black", borderwidth=2,command= bR)
        btn2.pack()
        btn3 = Button(fr2, text= "Brown hair",width=12,height=1,font=("Calibri",14,BOLD) 
                        ,relief = GROOVE ,bg="#98f5ff",fg="black", borderwidth=2,command= bW)
        btn3.pack()
        btn4 = Button(fr2, text= "Blond hair",width=12,height=1,font=("Calibri",14,BOLD) 
                        ,relief = GROOVE ,bg="#98f5ff",fg="black", borderwidth=2,command= bW)
        btn4.pack()
        
        top.mainloop()

    def nextQ1():

        global top1
        top1 = Tk()

        top1.title('السؤال الثاني')
        top1.attributes('-fullscreen', True)
        top1.config(background="#7d7bc5")
        #--------Icon--------
        p = PhotoImage(file= "P\\page1.png")
        top1.iconphoto(False,p)

        #-------Background--------
        bg = PhotoImage(file="P\\arab1.png")
        back = Label(top1,image=bg)
        back.place(x=0,y=0,relwidth=1 ,relheight=1)
        #frame
        fr2 = Frame(top1,width='800',height='650',bg="#f5deb3")
        fr2.pack(pady=20)
        
        q1 = Label(fr2, text= "هنا السؤال"
                    ,font=("Calibri",22,BOLD),fg="#4c2b50",bg="#ff8b00")
        q1.pack(fill=X , pady=30)

        def bW():
            CheckAnswerA.WrongAnswer2("A2") 
        def bR():
            CheckAnswerA.RightAnswer2("A2")
        #create the choose button
        btn1 = Button(fr2, text= "bags",width=12,height=1,font=("Calibri",14,BOLD)
                        ,relief = GROOVE ,bg="#ff8b00",fg="white", borderwidth=2,command= bW)
        btn1.pack()
        btn2 = Button(fr2, text= "shoses",width=12,height=1,font=("Calibri",14,BOLD)
                        ,relief = GROOVE ,bg="#ff8b00",fg="white", borderwidth=2,command= bW)
        btn2.pack()
        btn3 = Button(fr2, text= "glasses",width=12,height=1,font=("Calibri",14,BOLD) 
                        ,relief = GROOVE ,bg="#ff8b00",fg="white", borderwidth=2,command= bR)
        btn3.pack()
        btn4 = Button(fr2, text= "Tablet",width=12,height=1,font=("Calibri",14,BOLD)
                        ,relief = GROOVE ,bg="#ff8b00",fg="white", borderwidth=2,command= bW)
        btn4.pack()

        top1.mainloop()

    def nextQ2():

        global top2
        top2 = Tk()

        top2.title('السؤال الثالث')
        top2.attributes('-fullscreen', True)
        top2.config(background="#7d7bc5")

        #--------Icon--------
        p = PhotoImage(file= "P\\page1.png")
        top2.iconphoto(False,p)

        #-------Background--------
        bg = PhotoImage(file="P\\arab1.png")
        back = Label(top2,image=bg)
        back.place(x=0,y=0,relwidth=1 ,relheight=1)

        #frame
        fr3 = Frame(top2,width='800',height='650',bg="#f5deb3")
        fr3.pack(pady=20)

        q1 = Label(fr3, text= "هنا السؤال"
                    ,font=("Calibri",22,BOLD),fg="#4c2b50",bg="#ff8b00")
        q1.pack(fill=X , pady=30)
        
        def bW():
            CheckAnswerA.WrongAnswer3("A2") 
        def bR():
            CheckAnswerA.RightAnswer3("A2")
        #create the choose button
        btn1 = Button(fr3, text= "bags",width=12,height=1,font=("Calibri",14,BOLD)
                        ,relief = GROOVE ,bg="#ff8b00",fg="white", borderwidth=2,command= bW)
        btn1.pack()
        btn2 = Button(fr3, text= "shoses",width=12,height=1,font=("Calibri",14,BOLD)
                        ,relief = GROOVE ,bg="#ff8b00",fg="white", borderwidth=2,command= bW)
        btn2.pack()
        btn3 = Button(fr3, text= "Baby",width=12,height=1,font=("Calibri",14,BOLD) 
                        ,relief = GROOVE ,bg="#ff8b00",fg="white", borderwidth=2,command= bR)
        btn3.pack()
        btn4 = Button(fr3, text= "Tablet",width=12,height=1,font=("Calibri",14,BOLD)
                        ,relief = GROOVE ,bg="#ff8b00",fg="white", borderwidth=2,command= bW)
        btn4.pack()

        top2.mainloop()

    def nextQ3():

        global top3
        top3 = Tk()

        top3.title('السؤال الرابع')
        top3.attributes('-fullscreen', True)
        top3.config(background="#7d7bc5")

        #--------Icon--------
        p = PhotoImage(file= "P\\page1.png")
        top3.iconphoto(False,p)

        #-------Background--------
        bg = PhotoImage(file="P\\arab1.png")
        back = Label(top3,image=bg)
        back.place(x=0,y=0,relwidth=1 ,relheight=1)

        #frame
        fr2 = Frame(top3,width='800',height='650',bg="#f5deb3")
        fr2.pack(pady=20)

        q1 = Label(fr2, text= "هنا السؤال"
                    ,font=("Calibri",22,BOLD),fg="#4c2b50",bg="#ff8b00")
        q1.pack(fill=X , pady=30)

        def bW():
            CheckAnswerA.WrongAnswer4("A2") 
        def bR():
            CheckAnswerA.RightAnswer4("A2")
        #create the choose button
        btn1 = Button(fr2, text= "bags",width=12,height=1,font=("Calibri",14,BOLD)
                        ,relief = GROOVE ,bg="#ff8b00",fg="white", borderwidth=2,command= bW)
        btn1.pack()
        btn2 = Button(fr2, text= "shoses",width=12,height=1,font=("Calibri",14,BOLD)
                        ,relief = GROOVE ,bg="#ff8b00",fg="white", borderwidth=2,command= bW)
        btn2.pack()
        btn3 = Button(fr2, text= "eyes",width=12,height=1,font=("Calibri",14,BOLD) 
                        ,relief = GROOVE ,bg="#ff8b00",fg="white", borderwidth=2,command= bR)
        btn3.pack()
        btn4 = Button(fr2, text= "Tablet",width=12,height=1,font=("Calibri",14,BOLD)
                        ,relief = GROOVE ,bg="#ff8b00",fg="white", borderwidth=2,command= bW)
        btn4.pack()

        top3.mainloop()
    
    def nextQ4():

        global top4
        top4 = Tk()

        top4.title('السؤال الخامس')
        top4.attributes('-fullscreen', True)
        top4.config(background="#7d7bc5")

        #--------Icon--------
        p = PhotoImage(file= "P\\page1.png")
        top4.iconphoto(False,p)

        #-------Background--------
        bg = PhotoImage(file="P\\arab1.png")
        back = Label(top4,image=bg)
        back.place(x=0,y=0,relwidth=1 ,relheight=1)

        #frame
        fr2 = Frame(top4,width='800',height='650',bg="#f5deb3")
        fr2.pack(pady=20)

        q1 = Label(fr2, text= "هنا السؤال"
                    ,font=("Calibri",22,BOLD),fg="#4c2b50",bg="#ff8b00")
        q1.pack(fill=X , pady=30)

        def bW():
            CheckAnswerA.WrongAnswer5("A2") 
        def bR():
            CheckAnswerA.RightAnswer5("A2")
        #create the choose button
        btn1 = Button(fr2, text= "bags",width=12,height=1,font=("Comic Sans MS",14,BOLD)
                        ,relief = GROOVE ,bg="#ff8b00",fg="white", borderwidth=2,command= bW)
        btn1.pack()
        btn2 = Button(fr2, text= "shoses",width=12,height=1,font=("Comic Sans MS",14,BOLD)
                        ,relief = GROOVE ,bg="#ff8b00",fg="white", borderwidth=2,command= bW)
        btn2.pack()
        btn3 = Button(fr2, text= "eyes",width=12,height=1,font=("Comic Sans MS",14,BOLD) 
                        ,relief = GROOVE ,bg="#ff8b00",fg="white", borderwidth=2,command= bR)
        btn3.pack()
        btn4 = Button(fr2, text= "Tablet",width=12,height=1,font=("Comic Sans MS",14,BOLD)
                        ,relief = GROOVE ,bg="#ff8b00",fg="white", borderwidth=2,command= bW)
        btn4.pack()
        btn = Button(fr2, text= "Next Level",width=12,height=1,font=("Comic Sans MS",14,BOLD) 
                        ,relief = GROOVE ,bg="#4c3946",fg="white", borderwidth=2,command= game.nextLevel)
        btn.pack(side=BOTTOM)

        top4.mainloop()

    def nextLevel ():
        top4.destroy()
        #ArabLevels.view()
        