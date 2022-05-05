from tkinter import messagebox
import L1 , L2 , L3 , L4 , L5 , L6
import EngLevels
import Congrat
import pygame

pygame.init()
def WrongAnswer(x):
    if x == "L1":
        L1.game.chance = L1.game.chance - 1
        pygame.mixer.music.load('P\\wrong.mp3')
        pygame.mixer.music.play(loops=0)
        L1.top.destroy()
        L1.game.nextQ1()
    elif x == "L2":
        L2.game.chance = L2.game.chance - 1
        pygame.mixer.music.load('P\\wrong.mp3')
        pygame.mixer.music.play(loops=0)
        L2.top.destroy()
        L2.game.nextQ1()
    elif x == "L3":
        L3.game.chance = L3.game.chance - 1
        pygame.mixer.music.load('P\\wrong.mp3')
        pygame.mixer.music.play(loops=0)
        L3.top.destroy()
        L3.game.nextQ1()
    elif x == "L4" :
        L4.game.chance = L4.game.chance - 1
        pygame.mixer.music.load('P\\wrong.mp3')
        pygame.mixer.music.play(loops=0)
        L4.top.destroy()
        L4.game.nextQ1()
    elif x == "L5" :
        L5.game.chance = L5.game.chance - 1
        pygame.mixer.music.load('P\\wrong.mp3')
        pygame.mixer.music.play(loops=0)
        L5.top.destroy()
        L5.game.nextQ1()
    elif x == "L6" :
        L6.game.chance = L6.game.chance - 1
        pygame.mixer.music.load('P\\wrong.mp3')
        pygame.mixer.music.play(loops=0)
        L6.top.destroy()
        L6.game.nextQ1()
    else:
        messagebox.showinfo("Congratulations", f"{L1.game.chance}\nYou are so smart,Keep going")

def RightAnswer(x):
    #Label(fr2, text= "Great").pack()
    if x == "L1":
        L1.game.counter = L1.game.counter + 1
        pygame.mixer.music.load('P\\Correct-answer.mp3')
        pygame.mixer.music.play(loops=0)
        L1.top.destroy()
        L1.game.nextQ1()
    elif x == "L2" :
        L2.game.counter = L2.game.counter + 1
        pygame.mixer.music.load('P\\Correct-answer.mp3')
        pygame.mixer.music.play(loops=0)
        L2.top.destroy()
        L2.game.nextQ1()
    elif x == "L3" :
        L3.game.counter = L3.game.counter + 1
        pygame.mixer.music.load('P\\Correct-answer.mp3')
        pygame.mixer.music.play(loops=0)
        L3.top.destroy()
        L3.game.nextQ1()
    elif x == "L4":
        L4.game.counter = L4.game.counter + 1
        pygame.mixer.music.load('P\\Correct-answer.mp3')
        pygame.mixer.music.play(loops=0)
        L4.top.destroy()
        L4.game.nextQ1()
    elif x == "L5":
        L5.game.counter = L5.game.counter + 1
        pygame.mixer.music.load('P\\Correct-answer.mp3')
        pygame.mixer.music.play(loops=0)
        L5.top.destroy()
        L5.game.nextQ1()
    elif x == "L6" :
        L6.game.counter = L6.game.counter + 1
        pygame.mixer.music.load('P\\Correct-answer.mp3')
        pygame.mixer.music.play(loops=0)
        L6.top.destroy()
        L6.game.nextQ1()
    
    else:
        messagebox.showinfo("Congratulations", f"{L1.game.counter}\nYou are so smart,Keep going")

def RightAnswer2(x):
    #Label(fr2, text= "Great").pack()
    if x == "L1":
        L1.game.counter = L1.game.counter + 1
        pygame.mixer.music.load('P\\Correct-answer.mp3')
        pygame.mixer.music.play(loops=0)
        L1.top1.destroy()
        L1.game.nextQ2()
    elif x == "L2":
        L2.game.counter = L2.game.counter + 1
        pygame.mixer.music.load('P\\Correct-answer.mp3')
        pygame.mixer.music.play(loops=0)
        L2.top1.destroy()
        L2.game.nextQ2()
    elif x == "L3":
        L3.game.counter = L3.game.counter + 1
        pygame.mixer.music.load('P\\Correct-answer.mp3')
        pygame.mixer.music.play(loops=0)
        L3.top1.destroy()
        L3.game.nextQ2()
    elif x == "L4":
        L4.game.counter = L4.game.counter + 1
        pygame.mixer.music.load('P\\Correct-answer.mp3')
        pygame.mixer.music.play(loops=0)
        L4.top1.destroy()
        L4.game.nextQ2()
    elif x == "L5":
        L5.game.counter = L5.game.counter + 1
        pygame.mixer.music.load('P\\Correct-answer.mp3')
        pygame.mixer.music.play(loops=0)
        L5.top1.destroy()
        L5.game.nextQ2()
    elif x == "L6" :
        L6.game.counter = L6.game.counter + 1
        pygame.mixer.music.load('P\\Correct-answer.mp3')
        pygame.mixer.music.play(loops=0)
        L6.top1.destroy()
        L6.game.nextQ2()
    else:
        messagebox.showinfo("Congratulations", f"{L1.game.counter}\nYou are so smart,Keep going")

def WrongAnswer2(x):
    #Label(fr2, text= "Oops").pack()
    if x == "L1":
        L1.game.chance = L1.game.chance - 1
        pygame.mixer.music.load('P\\wrong.mp3')
        pygame.mixer.music.play(loops=0)
        L1.top1.destroy()
        L1.game.nextQ2()
    elif x == "L2":
        L2.game.chance = L2.game.chance - 1
        pygame.mixer.music.load('P\\wrong.mp3')
        pygame.mixer.music.play(loops=0)
        L2.top1.destroy()
        L2.game.nextQ2()
    elif x == "L3":
        L3.game.chance = L3.game.chance - 1
        pygame.mixer.music.load('P\\wrong.mp3')
        pygame.mixer.music.play(loops=0)
        L3.top1.destroy()
        L3.game.nextQ2()
    elif x == "L4":
        L4.game.chance = L4.game.chance - 1
        pygame.mixer.music.load('P\\wrong.mp3')
        pygame.mixer.music.play(loops=0)
        L4.top1.destroy()
        L4.game.nextQ2()
    elif x == "L5":
        L5.game.chance = L5.game.chance - 1
        pygame.mixer.music.load('P\\wrong.mp3')
        pygame.mixer.music.play(loops=0)
        L5.top1.destroy()
        L5.game.nextQ2()
    elif x == "L6" :
        L6.game.chance = L6.game.chance - 1
        pygame.mixer.music.load('P\\wrong.mp3')
        pygame.mixer.music.play(loops=0)
        L6.top1.destroy()
        L6.game.nextQ2()
    else:
        messagebox.showinfo("Congratulations", f"{L1.game.chance}\nYou are so smart,Keep going")

def RightAnswer3(x):
    #Label(fr2, text= "Great").pack()
    if x == "L1":
        L1.game.counter = L1.game.counter + 1
        pygame.mixer.music.load('P\\Correct-answer.mp3')
        pygame.mixer.music.play(loops=0)
        L1.top2.destroy()
        L1.game.nextQ3()
    elif x == "L2" :
        L2.game.counter = L2.game.counter + 1
        pygame.mixer.music.load('P\\Correct-answer.mp3')
        pygame.mixer.music.play(loops=0)
        L2.top2.destroy()
        L2.game.nextQ3()
    elif x == "L3" :
        L3.game.counter = L3.game.counter + 1
        pygame.mixer.music.load('P\\Correct-answer.mp3')
        pygame.mixer.music.play(loops=0)
        L3.top2.destroy()
        L3.game.nextQ3()
    elif x == "L4" :
        L4.game.counter = L4.game.counter + 1
        pygame.mixer.music.load('P\\Correct-answer.mp3')
        pygame.mixer.music.play(loops=0)
        L4.top2.destroy()
        L4.game.nextQ3()
    elif x == "L5" :
        L5.game.counter = L5.game.counter + 1
        pygame.mixer.music.load('P\\Correct-answer.mp3')
        pygame.mixer.music.play(loops=0)
        L5.top2.destroy()
        L5.game.nextQ3()
    elif x == "L6" :
        L6.game.counter = L6.game.counter + 1
        pygame.mixer.music.load('P\\Correct-answer.mp3')
        pygame.mixer.music.play(loops=0)
        L6.top2.destroy()
        L6.game.nextQ3()
    else:
        messagebox.showinfo("Congratulations", f"{L1.game.counter}\nYou are so smart,Keep going")

def WrongAnswer3(x):
    #Label(fr2, text= "Oops").pack()
    if x == "L1":
        L1.game.chance = L1.game.chance - 1
        pygame.mixer.music.load('P\\wrong.mp3')
        pygame.mixer.music.play(loops=0)
        L1.top2.destroy()
        L1.game.nextQ3()
    elif x == "L2" :
        L2.game.chance = L2.game.chance - 1
        pygame.mixer.music.load('P\\wrong.mp3')
        pygame.mixer.music.play(loops=0)
        L2.top2.destroy()
        L2.game.nextQ3()
    elif x == "L3" :
        L3.game.chance = L3.game.chance - 1
        pygame.mixer.music.load('P\\wrong.mp3')
        pygame.mixer.music.play(loops=0)
        L3.top2.destroy()
        L3.game.nextQ3()
    elif x == "L4" :
        L4.game.chance = L4.game.chance - 1
        pygame.mixer.music.load('P\\wrong.mp3')
        pygame.mixer.music.play(loops=0)
        L4.top2.destroy()
        L4.game.nextQ3()
    elif x == "L5" :
        L5.game.chance = L5.game.chance - 1
        pygame.mixer.music.load('P\\wrong.mp3')
        pygame.mixer.music.play(loops=0)
        L5.top2.destroy()
        L5.game.nextQ3()
    elif x == "L6" :
        L6.game.chance = L6.game.chance - 1
        pygame.mixer.music.load('P\\wrong.mp3')
        pygame.mixer.music.play(loops=0)
        L6.top2.destroy()
        L6.game.nextQ3()
    else:
        messagebox.showinfo("Congratulations", f"{L1.game.chance}\nYou are so smart,Keep going")

def RightAnswer4(x):
    #Label(fr2, text= "Great").pack()
    if x == "L1":
        L1.game.counter = L1.game.counter + 1
        pygame.mixer.music.load('P\\Correct-answer.mp3')
        pygame.mixer.music.play(loops=0)
        L1.top3.destroy()
        L1.game.nextQ4()
    elif x == "L2" :
        L2.game.counter = L2.game.counter + 1
        pygame.mixer.music.load('P\\Correct-answer.mp3')
        pygame.mixer.music.play(loops=0)
        L2.top3.destroy()
        L2.game.nextQ4()
    elif x == "L3" :
        L3.game.counter = L3.game.counter + 1
        pygame.mixer.music.load('P\\Correct-answer.mp3')
        pygame.mixer.music.play(loops=0)
        L3.top3.destroy()
        L3.game.nextQ4()
    elif x == "L4" :
        L4.game.counter = L4.game.counter + 1
        pygame.mixer.music.load('P\\Correct-answer.mp3')
        pygame.mixer.music.play(loops=0)
        L4.top3.destroy()
        L4.game.nextQ4()
    elif x == "L5" :
        L5.game.counter = L5.game.counter + 1
        pygame.mixer.music.load('P\\Correct-answer.mp3')
        pygame.mixer.music.play(loops=0)
        L5.top3.destroy()
        L5.game.nextQ4()
    elif x == "L6" :
        L6.game.counter = L6.game.counter + 1
        pygame.mixer.music.load('P\\Correct-answer.mp3')
        pygame.mixer.music.play(loops=0)
        L6.top3.destroy()
        L6.game.nextQ4()
    else:
        messagebox.showinfo("Congratulations", f"{L1.game.counter}\nYou are so smart,Keep going")

def WrongAnswer4(x):
    #Label(fr2, text= "Oops").pack()
    if x == "L1":
        L1.game.chance = L1.game.chance - 1
        pygame.mixer.music.load('P\\wrong.mp3')
        pygame.mixer.music.play(loops=0)
        L1.top3.destroy()
        L1.game.nextQ4()
    elif x == "L2" :
        L2.game.chance = L2.game.chance - 1
        pygame.mixer.music.load('P\\wrong.mp3')
        pygame.mixer.music.play(loops=0)
        L2.top3.destroy()
        L2.game.nextQ4()
    elif x == "L3" :
        L3.game.chance = L3.game.chance - 1
        pygame.mixer.music.load('P\\wrong.mp3')
        pygame.mixer.music.play(loops=0)
        L3.top3.destroy()
        L3.game.nextQ4()
    elif x == "L4" :
        L4.game.chance = L4.game.chance - 1
        pygame.mixer.music.load('P\\wrong.mp3')
        pygame.mixer.music.play(loops=0)
        L4.top3.destroy()
        L4.game.nextQ4()
    elif x == "L5" :
        L5.game.chance = L5.game.chance - 1
        pygame.mixer.music.load('P\\wrong.mp3')
        pygame.mixer.music.play(loops=0)
        L5.top3.destroy()
        L5.game.nextQ4()
    elif x == "L6" :
        L6.game.chance = L6.game.chance - 1
        pygame.mixer.music.load('P\\wrong.mp3')
        pygame.mixer.music.play(loops=0)
        L6.top3.destroy()
        L6.game.nextQ4()
    else:
        messagebox.showinfo("Congratulations", f"{L1.game.chance}\nYou are so smart,Keep going")

def RightAnswer5(x):
    #Label(fr2, text= "Great").pack()
    if x == "L1":
        L1.game.counter = L1.game.counter + 1
        pygame.mixer.music.load('P\\Correct-answer.mp3')
        pygame.mixer.music.play(loops=0)
        pygame.mixer.music.load('P\\winner.mp3')
        pygame.mixer.music.play(loops=0)
        #L1.top4.destroy()
        Congrat.con(L1.game.counter)
        EngLevels.view()
    elif x == "L2" :
        L2.game.counter = L2.game.counter + 1
        pygame.mixer.music.load('P\\Correct-answer.mp3')
        pygame.mixer.music.play(loops=0)
        pygame.mixer.music.load('P\\winner.mp3')
        pygame.mixer.music.play(loops=0)
        #L2.top4.destroy()
        Congrat.con(L2.game.counter)
        EngLevels.view()
    elif x == "L3" :
        L3.game.counter = L3.game.counter + 1
        pygame.mixer.music.load('P\\Correct-answer.mp3')
        pygame.mixer.music.play(loops=0)
        pygame.mixer.music.load('P\\winner.mp3')
        pygame.mixer.music.play(loops=0)
        #L3.top4.destroy()
        Congrat.con(L3.game.counter)
        EngLevels.view()
    elif x == "L4" :
        L4.game.counter = L4.game.counter + 1
        pygame.mixer.music.load('P\\Correct-answer.mp3')
        pygame.mixer.music.play(loops=0)
        pygame.mixer.music.load('P\\winner.mp3')
        pygame.mixer.music.play(loops=0)
        #L4.top4.destroy()
        Congrat.con(L4.game.counter)
        EngLevels.view()
    elif x == "L5" :
        L5.game.counter = L5.game.counter + 1
        pygame.mixer.music.load('P\\Correct-answer.mp3')
        pygame.mixer.music.play(loops=0)
        pygame.mixer.music.load('P\\winner.mp3')
        pygame.mixer.music.play(loops=0)
        #L5.top4.destroy()
        Congrat.con(L5.game.counter)
        EngLevels.view()
    elif x == "L6" :
        L6.game.counter = L6.game.counter + 1
        pygame.mixer.music.load('P\\Correct-answer.mp3')
        pygame.mixer.music.play(loops=0)
        pygame.mixer.music.load('P\\winner.mp3')
        pygame.mixer.music.play(loops=0)
        #L6.top4.destroy()
        Congrat.con(L6.game.counter)
        EngLevels.view()
    else:
        messagebox.showinfo("Congratulations", f"{L1.game.counter}\nYou are so smart,Keep going")

def WrongAnswer5(x):
    #Label(fr2, text= "Oops").pack()
    if x == "L1":
        L1.game.chance = L1.game.chance - 1
        pygame.mixer.music.load('P\\wrong.mp3')
        pygame.mixer.music.play(loops=0)
        pygame.mixer.music.load('P\\winner.mp3')
        pygame.mixer.music.play(loops=0)
        #L1.top4.destroy()
        Congrat.con(L1.game.chance)
        EngLevels.view()
    elif x == "L2" :
        L2.game.chance = L2.game.chance - 1
        pygame.mixer.music.load('P\\wrong.mp3')
        pygame.mixer.music.play(loops=0)
        pygame.mixer.music.load('P\\winner.mp3')
        pygame.mixer.music.play(loops=0)
        #L2.top4.destroy()
        Congrat.con(L2.game.chance)
        EngLevels.view()
    elif x == "L3" :
        L3.game.chance = L3.game.chance - 1
        pygame.mixer.music.load('P\\wrong.mp3')
        pygame.mixer.music.play(loops=0)
        pygame.mixer.music.load('P\\winner.mp3')
        pygame.mixer.music.play(loops=0)
        #L3.top4.destroy()
        Congrat.con(L3.game.chance)
        EngLevels.view()
    elif x == "L4" :
        L4.game.chance = L4.game.chance - 1
        pygame.mixer.music.load('P\\wrong.mp3')
        pygame.mixer.music.play(loops=0)
        pygame.mixer.music.load('P\\winner.mp3')
        pygame.mixer.music.play(loops=0)
        #L4.top4.destroy()
        Congrat.con(L4.game.chance)
        EngLevels.view()
    elif x == "L5" :
        L5.game.chance = L5.game.chance - 1
        pygame.mixer.music.load('P\\wrong.mp3')
        pygame.mixer.music.play(loops=0)
        pygame.mixer.music.load('P\\winner.mp3')
        pygame.mixer.music.play(loops=0)
        #L5.top4.destroy()
        Congrat.con(L5.game.chance)
        EngLevels.view()
    elif x == "L6" :
        L6.game.chance = L6.game.chance - 1
        pygame.mixer.music.load('P\\wrong.mp3')
        pygame.mixer.music.play(loops=0)
        pygame.mixer.music.load('P\\winner.mp3')
        pygame.mixer.music.play(loops=0)
        #L6.top4.destroy()
        Congrat.con(L6.game.chance)
        EngLevels.view()
    else:
        messagebox.showinfo("Congratulations", f"{L1.game.chance}\nYou are so smart,Keep going")
