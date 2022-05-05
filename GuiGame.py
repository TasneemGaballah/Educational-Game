from asyncio.windows_events import NULL
from cProfile import label
from cgitb import text
from lib2to3.pgen2.token import LEFTSHIFT
from multiprocessing.connection import wait
from optparse import Option
from sqlite3 import Time
from time import time
from tkinter import *
from tkinter.font import BOLD
from turtle import color, delay, left, right
from tkinter import messagebox

import instructions as ins
import ArabLevels
import DB_name

#--------Create the main app window------------
global eduApp
eduApp = Tk()

#--------Change app text----------
eduApp.title("Nadeen Project")

#--------Set dimensions-----------
eduApp.attributes('-fullscreen', True)
eduApp.config(background="#7d7bc5")

#--------Icon--------
p = PhotoImage(file= "P\\logo.png")
eduApp.iconphoto(False,p)

#--------Image-----------
#-------Background--------
bg = PhotoImage(file="P\\page.png")
back = Label(eduApp,image=bg)
back.place(x=0,y=0,relwidth=1 ,relheight=1)

#--------Write label--------
tit = Label(eduApp , text="Welcome To Nadeen Edu. Game"
                    ,font=("Courier",18,BOLD),fg="#4c2b50",bg="#c9a0dc")
#--------Place the text into the main window-----
tit.pack(fill=X)

#--------Frame--------
fr1 = Frame(eduApp,width='300',height='450',bg="#f5deb3")
fr1.pack(pady=100)

#------------Write label------------
tit1 = Label(fr1 , text="Welcome to Nadeen Game"
                    ,height=2,font=("Comic Sans MS",26,BOLD),fg="Black",bg= "#b46567",underline=0)
#------------Place the text into the main window--------
tit1.pack()
#------------Write label-------------
tit2 = Label(fr1 , text="You will start an Education Game \nBe ready >-<"
                    ,height=2,font=("Comic Sans MS",26,BOLD),fg="#bb4c6e",bg="#f5deb3",underline=0)
#------------Place the text into the main window---------
tit2.pack()

#------------Name variables-------------
global name
name = StringVar()
#------------Set default value foe name--------
name.set("Enter Your name")
#------------Creat the input for name-----------
nameInput = Entry(fr1, width=24,font=("Arial",11)
                        ,background="#aa99aa",textvariable=name)
nameInput.pack()

def play1():
    eduApp.destroy()
    ins.intru()

def play2():
    eduApp.destroy()
    ArabLevels.view()

def save_name():
    #------get name------
    newName= name.get()
    DB_name.x = newName
    if newName!="Enter Your name":
        Label(fr1, text= "Nice to meet you, "+ newName).pack(after=btn)
        btnn = Button(fr1, text= "English Game",width=11,height=1,font=("Comic Sans MS",12,BOLD) 
                ,relief = GROOVE ,bg="#aa99aa",fg="Black", borderwidth=2,command= play1)
        btnn.pack(pady=10,before=btn1)
        btn3 = Button(fr1, text= "Arabic Game",width=11,height=1,font=("Comic Sans MS",12,BOLD) 
                ,relief = GROOVE ,bg="#aa99aa",fg="Black", borderwidth=2,command= play2)
        btn3.pack(pady=10,after=btnn)
    #messagebox.showinfo("Welcome To Our Game", newName)

def Help():
    Label(fr1, text= "To log out press Exit bottom").pack(before=exit_button)

#---------create the login button---------
btn = Button(fr1, text= "Log In",width=5,height=1,font=("Cooper",10,BOLD) 
                ,relief = GROOVE ,bg="#e91e63",fg="white", borderwidth=2,command= save_name)
btn.pack(pady=10)
#---------create the Help button---------
btn1 = Button(fr1, text= "Help",width=5,height=1,font=("Cooper",10,BOLD) 
                ,relief = GROOVE ,bg="#e91e63",fg="white", borderwidth=2,command= Help)
btn1.pack()
#------------Button for closing-----------
exit_button = Button(fr1, text="Exit",width=5,height=1,font=("Cooper",10,BOLD) 
            ,relief = GROOVE ,bg="#e91e63",fg="white", borderwidth=2, command=eduApp.destroy)
exit_button.pack()

#---------Run app infinitely-----------
eduApp.mainloop()