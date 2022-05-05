from tkinter import *
from tkinter.font import BOLD
import DB_name
import EngLevels

def intru():
    #--------Create the instructions app window------------
    global inst
    inst = Tk()
    #--------Change app text----------
    inst.title("Instructions Game")
    #--------Set dimensions-----------
    inst.attributes('-fullscreen', True)
    inst.config(background="#7d7bc5")

    #--------Icon--------
    p = PhotoImage(file= "P\\logo.png")
    inst.iconphoto(False,p)

    #--------Image-----------
    #-------Background--------
    bg = PhotoImage(file="P\\page.png")
    back = Label(inst,image=bg)
    back.place(x=0,y=0,relwidth=1 ,relheight=1)

    #--------Write label--------
    tit = Label(inst , text=f"Welcome {DB_name.x} To Nadeen Edu. Game Instructions"
                        ,font=("Courier",18,BOLD),fg="#4c2b50",bg="#c9a0dc")
    #--------Place the text into the main window-----
    tit.pack(fill=X)

    #--------Frame--------
    fr1 = Frame(inst,width='1000',height='1050')
    fr1.pack(pady=100)

    #------------Write label------------
    tit1 = Label(fr1 , text=f'1)An Educational game, learn while playing!\n2)Fun avtivities for children.            \n'
                        ,height=4,font=("Comic Sans MS",26,BOLD),fg="#0d8767",underline=0)
    #------------Place the text into the main window--------
    tit1.pack()
    #------------Write label------------
    tit2 = Label(fr1 , text=f'3)Safe, interactive, and inspirational.  \n4)Full featured with no ADS.                 \n'
                        ,height=3,font=("Comic Sans MS",26,BOLD),fg="#0d8767",underline=0)
    #------------Place the text into the main window--------
    tit2.pack()
    def b1():
        inst.destroy()
        EngLevels.view()

    btn1 = Button(fr1, text= "GO To Game Levels",width=17,height=1,font=("Comic Sans MS",24,BOLD)
                    ,relief = GROOVE ,bg="#0d8767",fg="white", borderwidth=2 , command=b1)
    btn1.pack()

    #------------Button for closing-----------
    exit_button = Button(fr1, text="Exit",width=7,height=1,font=("Cooper",14,BOLD) 
                ,relief = GROOVE ,bg="#e91e63",fg="white", borderwidth=2, command=inst.destroy)
    exit_button.pack()

    #---------Run app infinitely-----------
    inst.mainloop()