from tkinter import *
from tkinter.font import BOLD
from tkinter import messagebox
import A1 , A2 , A3 , A4 , A5
import DB_name

def view():
    global topp
    topp = Tk()
    topp.title(f'{DB_name.x} بأي مستوى تريد ان تبدأ؟')
    topp.attributes('-fullscreen', True)
    topp.config(background="#7d7bc5")
    
    #--------Icon--------
    p = PhotoImage(file= "P\\page1.png")
    topp.iconphoto(False,p)

    #-------Background--------
    bg = PhotoImage(file="P\\arab1.png")
    back = Label(topp,image=bg)
    back.place(x=0,y=0,relwidth=1 ,relheight=1)
    #place the text into the main window
    #frame
    global fr
    fr = Frame(topp,width='800',height='650',bg="#f5deb3")
    fr.pack(pady=20)

    t = Label(topp , text=f"مرحبا بك في لعبة اللغة العربية يا {DB_name.x}",font=("Calibri",24,BOLD),fg="#4c2b50",bg="#c9a0dc")
    t.pack(side= TOP ,fill=X)
    
    #Buttons functions
    def b1():
        topp.destroy()
        A1.game.Game()

    def b2():
        topp.destroy()
        A2.game.Game()

    def b3():
        topp.destroy()
        A3.game.Game()

    def b4():
        topp.destroy()
        A4.game.Game()

    def b5():
        topp.destroy()
        A5.game.Game()

    #create the choose button
    btn1 = Button(fr, text= "المستوى الأول",width=11,height=2,font=("Calibri",24,BOLD)
                    ,relief = GROOVE ,bg="#ff8b00",fg="white", borderwidth=2 , command=b1)
    btn1.pack()
    btn2 = Button(fr, text= "المستوى الثاني",width=11,height=2,font=("Calibri",24,BOLD)
                    ,relief = GROOVE ,bg="#ff8b00",fg="white", borderwidth=2, command=b2)
    btn2.pack()
    btn3 = Button(fr, text= "المستوى الثالث",width=11,height=2,font=("Calibri",24,BOLD) 
                    ,relief = GROOVE ,bg="#ff8b00",fg="white", borderwidth=2, command=b3)
    btn3.pack()
    btn4 = Button(fr, text= "المستوى الرابع",width=11,height=2,font=("Calibri",24,BOLD)
                    ,relief = GROOVE ,bg="#ff8b00",fg="white", borderwidth=2, command=b4)
    btn4.pack()
    btn4 = Button(fr, text= "المستوى الخامس",width=11,height=2,font=("Calibri",24,BOLD)
                    ,relief = GROOVE ,bg="#ff8b00",fg="white", borderwidth=2, command=b5)
    btn4.pack()
            
    # Button for closing
    exit_button = Button(fr, text="الخروج من اللعبة",width=11,height=2,font=("Calibri",20,BOLD) 
                ,relief = GROOVE ,bg="#e91e63",fg="white", borderwidth=2, command=topp.destroy)
    exit_button.pack(side=BOTTOM)

    topp.mainloop()