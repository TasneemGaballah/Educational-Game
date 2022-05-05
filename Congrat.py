from tkinter import *
from tkinter.font import BOLD
import DB_name
import EngLevels

def con(score):
    #--------Create the instructions app window------------
    global msbox
    msbox = Toplevel()
    #--------Change app text----------
    msbox.title("congratulations")
    #--------Set dimensions-----------
    #msbox.attributes('-fullscreen', True)
    msbox.geometry("400x400")
    msbox.config(background="#7d7bc5")

    #--------Icon--------
    p = PhotoImage(file= "P\\logo.png")
    msbox.iconphoto(False,p)

    #--------Image-----------
    #-------Background--------
    bg = PhotoImage(file="P\\s4.png")
    back = Label(msbox,image=bg)
    back.place(x=0,y=0,relwidth=1 ,relheight=1)

    #--------Write label--------
    tit = Label(msbox , text=f"Congratulations {DB_name.x}"
                        ,font=("Courier",18,BOLD),fg="#4c2b50",bg="#c9a0dc")
    #--------Place the text into the main window-----
    tit.pack(fill=X)

    #--------Frame--------
    fr1 = Frame(msbox,width='1000',height='1050')
    fr1.pack(pady=100)

    #------------Write label------------
    tit1 = Label(fr1 , text=f'Game Complete\nScore:\n{score}/5'
                        ,height=4,font=("Comic Sans MS",26,BOLD),fg="#0d8767",underline=0)
    #------------Place the text into the main window--------
    tit1.pack()
    
    def b1():
        msbox.destroy()
        EngLevels.view()

    btn1 = Button(fr1, text= "GO To Game Levels",width=17,height=1,font=("Comic Sans MS",24,BOLD)
                    ,relief = GROOVE ,bg="#0d8767",fg="white", borderwidth=2 , command=b1)
    btn1.pack()

    #------------Button for closing-----------
    exit_button = Button(fr1, text="Exit",width=7,height=1,font=("Cooper",14,BOLD) 
                ,relief = GROOVE ,bg="#e91e63",fg="white", borderwidth=2, command=msbox.destroy)
    exit_button.pack()

    #---------Run app infinitely-----------
    msbox.mainloop()