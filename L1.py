from tkinter import *
from tkinter.font import BOLD
from tkinter import messagebox
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
        fr2 = Frame(top,width='800',height='650',bg="#f5deb3")
        fr2.pack(pady=20)
        t = Label(fr2 , text="Welcome To Level ONE",font=("Courier",18,BOLD),fg="#4c2b50",bg="#c9a0dc")
        t.pack(fill=X, side= TOP)
        #cnvas = Canvas(fr2,bg="#f5deb3",width='800',height='550')
        # Button for closing
        exit_button = Button(fr2, text="Exit",width=5,height=1,font=("Comic Sans MS",10,BOLD) 
                    ,relief = GROOVE ,bg="#e91e63",fg="white", borderwidth=2, command=top.destroy)
        exit_button.pack(side=BOTTOM)
        #image
        photo5 = PhotoImage(file ='P1\\angry.png') 
        photo5.configure(height=365 , width= 345)
        #photoimage = photo5.subsample(2, 2)
        p2=Label(fr2, image=photo5)
        p2.pack(pady=20)
        def bW():
            CheckAnswerE.WrongAnswer("L1") 
        def bR():
            CheckAnswerE.RightAnswer("L1")
        #create the choose button
        btn1 = Button(fr2, text= "Happy",width=12,height=1,font=("Comic Sans MS",14,BOLD)
                        ,relief = GROOVE ,bg="#98f5ff",fg="black", borderwidth=2,command= bW)
        btn1.pack()
        btn2 = Button(fr2, text= "ANGRY",width=12,height=1,font=("Comic Sans MS",14,BOLD)
                        ,relief = GROOVE ,bg="#98f5ff",fg="black", borderwidth=2,command= bR)
        btn2.pack()
        btn3 = Button(fr2, text= "unhappy",width=12,height=1,font=("Comic Sans MS",14,BOLD)
                        ,relief = GROOVE ,bg="#98f5ff",fg="black", borderwidth=2,command= bW)
        btn3.pack()
        btn4 = Button(fr2, text= "sad",width=12,height=1,font=("Comic Sans MS",14,BOLD)
                        ,relief = GROOVE ,bg="#98f5ff",fg="black", borderwidth=2,command= bW)
        btn4.pack()
        #cnvas.pack()
        top.mainloop()

    def nextQ1():
        global top1
        top1 = Tk()
        top1.title('Question Two')
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
        photo = PhotoImage(file="P1\\sleep.png")
        photo.configure(height=365 , width= 345)
        #photoimage = photo.subsample(2, 2)
        p2=Label(fr2, image=photo)
        p2.pack()
        def bW():
            CheckAnswerE.WrongAnswer2("L1") 
        def bR():
            CheckAnswerE.RightAnswer2("L1")
        #create the choose button
        btn1 = Button(fr2, text= "Play",width=12,height=1,font=("Comic Sans MS",14,BOLD)
                        ,relief = GROOVE ,bg="#ff8b00",fg="white", borderwidth=2,command= bW)
        btn1.pack()
        btn2 = Button(fr2, text= "Sick",width=12,height=1,font=("Comic Sans MS",14,BOLD)
                        ,relief = GROOVE ,bg="#ff8b00",fg="white", borderwidth=2,command= bW)
        btn2.pack()
        btn3 = Button(fr2, text= "Sleep",width=12,height=1,font=("Comic Sans MS",14,BOLD)
                        ,relief = GROOVE ,bg="#ff8b00",fg="white", borderwidth=2,command= bR)
        btn3.pack()
        btn4 = Button(fr2, text= "Hungry",width=12,height=1,font=("Comic Sans MS",14,BOLD)
                        ,relief = GROOVE ,bg="#ff8b00",fg="white", borderwidth=2,command= bW)
        btn4.pack()
        top1.mainloop()

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
        fr3 = Frame(top2,width='800',height='650',bg="#f5deb3")
        fr3.pack(pady=20)
        #image
        photo = PhotoImage(file="P1\\sick.png")
        photo.configure(height=365 , width= 345)
        #photoimage = photo.subsample(2, 2)
        p2=Label(fr3, image=photo)
        p2.pack()
        def bW():
            CheckAnswerE.WrongAnswer3("L1") 
        def bR():
            CheckAnswerE.RightAnswer3("L1")
        #create the choose button
        btn3 = Button(fr3, text= "sick",width=12,height=1,font=("Comic Sans MS",14,BOLD)
                        ,relief = GROOVE ,bg="#ff8b00",fg="white", borderwidth=2,command= bR)
        btn3.pack()
        btn1 = Button(fr3, text= "play",width=12,height=1,font=("Comic Sans MS",14,BOLD)
                        ,relief = GROOVE ,bg="#ff8b00",fg="white", borderwidth=2,command= bW)
        btn1.pack()
        btn2 = Button(fr3, text= "sleep",width=12,height=1,font=("Comic Sans MS",14,BOLD)
                        ,relief = GROOVE ,bg="#ff8b00",fg="white", borderwidth=2,command= bW)
        btn2.pack()
        btn4 = Button(fr3, text= "thirsty",width=12,height=1,font=("Comic Sans MS",14,BOLD)
                        ,relief = GROOVE ,bg="#ff8b00",fg="white", borderwidth=2,command= bW)
        btn4.pack()
        top2.mainloop()

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
        #image
        photo = PhotoImage(file="P1\\hungry.png")
        photo.configure(height=365 , width= 345)
        #photoimage = photo.subsample(2, 2)
        p2=Label(fr2, image=photo)
        p2.pack()
        def bW():
            CheckAnswerE.WrongAnswer4("L1") 
        def bR():
            CheckAnswerE.RightAnswer4("L1")
        #create the choose button
        btn1 = Button(fr2, text= "sleep",width=12,height=1,font=("Comic Sans MS",14,BOLD)
                        ,relief = GROOVE ,bg="#ff8b00",fg="white", borderwidth=2,command= bW)
        btn1.pack()
        btn2 = Button(fr2, text= "sick",width=12,height=1,font=("Comic Sans MS",14,BOLD)
                        ,relief = GROOVE ,bg="#ff8b00",fg="white", borderwidth=2,command= bW)
        btn2.pack()
        btn4 = Button(fr2, text= "play",width=12,height=1,font=("Comic Sans MS",14,BOLD)
                        ,relief = GROOVE ,bg="#ff8b00",fg="white", borderwidth=2,command= bW)
        btn4.pack()
        btn3 = Button(fr2, text= "Hungry",width=12,height=1,font=("Comic Sans MS",14,BOLD)
                        ,relief = GROOVE ,bg="#ff8b00",fg="white", borderwidth=2,command= bR)
        btn3.pack()
        top3.mainloop()
    
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
        #image
        photo = PhotoImage(file="P1\\headache.png")
        photo.configure(height=365 , width= 345)
        #photoimage = photo.subsample(2, 2)
        p2=Label(fr2, image=photo)
        p2.pack()
        def bW():
            CheckAnswerE.WrongAnswer5("L1") 
        def bR():
            CheckAnswerE.RightAnswer5("L1")
        #create the choose button
        btn1 = Button(fr2, text= "thirsty",width=12,height=1,font=("Comic Sans MS",14,BOLD)
                        ,relief = GROOVE ,bg="#ff8b00",fg="white", borderwidth=2,command= bW)
        btn1.pack()
        btn2 = Button(fr2, text= "eat",width=12,height=1,font=("Comic Sans MS",14,BOLD)
                        ,relief = GROOVE ,bg="#ff8b00",fg="white", borderwidth=2,command= bW)
        btn2.pack()
        btn3 = Button(fr2, text= "headache",width=12,height=1,font=("Comic Sans MS",14,BOLD)
                        ,relief = GROOVE ,bg="#ff8b00",fg="white", borderwidth=2,command= bR)
        btn3.pack()
        btn4 = Button(fr2, text= "play",width=12,height=1,font=("Comic Sans MS",14,BOLD)
                        ,relief = GROOVE ,bg="#ff8b00",fg="white", borderwidth=2,command= bW)
        btn4.pack()
        btn = Button(fr2, text= "BackTo Home",width=12,height=1,font=("Comic Sans MS",14,BOLD) 
                        ,relief = GROOVE ,bg="#4c3946",fg="white", borderwidth=2,command= game.nextLevel)
        btn.pack(side=BOTTOM)
        top4.mainloop()

    def nextLevel ():
        top4.destroy()
        #Transform.backToHome()
        