from tkinter import messagebox
import A1 , A2 , A3 , A4 , A5
import ArabLevels
import CongratA
import pygame

pygame.init()

def WrongAnswer(x):
    if x == "A1":
        A1.game.chance = A1.game.chance - 1
        pygame.mixer.music.load('P\\wrong.mp3')
        pygame.mixer.music.play(loops=0)
        A1.top.destroy()
        A1.game.nextQ1()
    elif x == "A2":
        A2.game.chance = A2.game.chance - 1
        pygame.mixer.music.load('P\\wrong.mp3')
        pygame.mixer.music.play(loops=0)
        A2.top.destroy()
        A2.game.nextQ1()
    elif x == "A3":
        A3.game.chance = A3.game.chance - 1
        pygame.mixer.music.load('P\\wrong.mp3')
        pygame.mixer.music.play(loops=0)
        A3.top.destroy()
        A3.game.nextQ1()
    elif x == "A4" :
        A4.game.chance = A4.game.chance - 1
        pygame.mixer.music.load('P\\wrong.mp3')
        pygame.mixer.music.play(loops=0)
        A4.top.destroy()
        A4.game.nextQ1()
    elif x == "A5" :
        A5.game.chance = A5.game.chance - 1
        pygame.mixer.music.load('P\\wrong.mp3')
        pygame.mixer.music.play(loops=0)
        A5.top.destroy()
        A5.game.nextQ1()
    else:
        messagebox.showinfo("Congratulations", f"{A1.game.chance}\nYou are so smart,Keep going")

def RightAnswer(x):
    #Label(fr2, text= "Great").pack()
    if x == "A1":
        A1.game.counter = A1.game.counter + 1
        pygame.mixer.music.load('P\\Correct-answer.mp3')
        pygame.mixer.music.play(loops=0)
        A1.top.destroy()
        A1.game.nextQ1()
    elif x == "A2" :
        A2.game.counter = A2.game.counter + 1
        pygame.mixer.music.load('P\\Correct-answer.mp3')
        pygame.mixer.music.play(loops=0)
        A2.top.destroy()
        A2.game.nextQ1()
    elif x == "A3" :
        A3.game.counter = A3.game.counter + 1
        pygame.mixer.music.load('P\\Correct-answer.mp3')
        pygame.mixer.music.play(loops=0)
        A3.top.destroy()
        A3.game.nextQ1()
    elif x == "A4":
        A4.game.counter = A4.game.counter + 1
        pygame.mixer.music.load('P\\Correct-answer.mp3')
        pygame.mixer.music.play(loops=0)
        A4.top.destroy()
        A4.game.nextQ1()
    elif x == "A5":
        A5.game.counter = A5.game.counter + 1
        pygame.mixer.music.load('P\\Correct-answer.mp3')
        pygame.mixer.music.play(loops=0)
        A5.top.destroy()
        A5.game.nextQ1()
    
    else:
        messagebox.showinfo("Congratulations", f"{A1.game.counter}\nYou are so smart,Keep going")

def RightAnswer2(x):
    #Label(fr2, text= "Great").pack()
    if x == "A1":
        A1.game.counter = A1.game.counter + 1
        pygame.mixer.music.load('P\\Correct-answer.mp3')
        pygame.mixer.music.play(loops=0)
        A1.top1.destroy()
        A1.game.nextQ2()
    elif x == "A2":
        A2.game.counter = A2.game.counter + 1
        pygame.mixer.music.load('P\\Correct-answer.mp3')
        pygame.mixer.music.play(loops=0)
        A2.top1.destroy()
        A2.game.nextQ2()
    elif x == "A3":
        A3.game.counter = A3.game.counter + 1
        pygame.mixer.music.load('P\\Correct-answer.mp3')
        pygame.mixer.music.play(loops=0)
        A3.top1.destroy()
        A3.game.nextQ2()
    elif x == "A4":
        A4.game.counter = A4.game.counter + 1
        pygame.mixer.music.load('P\\Correct-answer.mp3')
        pygame.mixer.music.play(loops=0)
        A4.top1.destroy()
        A4.game.nextQ2()
    elif x == "A5":
        A5.game.counter = A5.game.counter + 1
        pygame.mixer.music.load('P\\Correct-answer.mp3')
        pygame.mixer.music.play(loops=0)
        A5.top1.destroy()
        A5.game.nextQ2()
    else:
        messagebox.showinfo("Congratulations", f"{A1.game.counter}\nYou are so smart,Keep going")

def WrongAnswer2(x):
    #Label(fr2, text= "Oops").pack()
    if x == "A1":
        A1.game.chance = A1.game.chance - 1
        pygame.mixer.music.load('P\\wrong.mp3')
        pygame.mixer.music.play(loops=0)
        A1.top1.destroy()
        A1.game.nextQ2()
    elif x == "A2":
        A2.game.chance = A2.game.chance - 1
        pygame.mixer.music.load('P\\wrong.mp3')
        pygame.mixer.music.play(loops=0)
        A2.top1.destroy()
        A2.game.nextQ2()
    elif x == "A3":
        A3.game.chance = A3.game.chance - 1
        pygame.mixer.music.load('P\\wrong.mp3')
        pygame.mixer.music.play(loops=0)
        A3.top1.destroy()
        A3.game.nextQ2()
    elif x == "A4":
        A4.game.chance = A4.game.chance - 1
        pygame.mixer.music.load('P\\wrong.mp3')
        pygame.mixer.music.play(loops=0)
        A4.top1.destroy()
        A4.game.nextQ2()
    elif x == "A5":
        A5.game.chance = A5.game.chance - 1
        pygame.mixer.music.load('P\\wrong.mp3')
        pygame.mixer.music.play(loops=0)
        A5.top1.destroy()
        A5.game.nextQ2()
    else:
        messagebox.showinfo("Congratulations", f"{A1.game.chance}\nYou are so smart,Keep going")

def RightAnswer3(x):
    #Label(fr2, text= "Great").pack()
    if x == "A1":
        A1.game.counter = A1.game.counter + 1
        pygame.mixer.music.load('P\\Correct-answer.mp3')
        pygame.mixer.music.play(loops=0)
        A1.top2.destroy()
        A1.game.nextQ3()
    elif x == "A2" :
        A2.game.counter = A2.game.counter + 1
        pygame.mixer.music.load('P\\Correct-answer.mp3')
        pygame.mixer.music.play(loops=0)
        A2.top2.destroy()
        A2.game.nextQ3()
    elif x == "A3" :
        A3.game.counter = A3.game.counter + 1
        pygame.mixer.music.load('P\\Correct-answer.mp3')
        pygame.mixer.music.play(loops=0)
        A3.top2.destroy()
        A3.game.nextQ3()
    elif x == "A4" :
        A4.game.counter = A4.game.counter + 1
        pygame.mixer.music.load('P\\Correct-answer.mp3')
        pygame.mixer.music.play(loops=0)
        A4.top2.destroy()
        A4.game.nextQ3()
    elif x == "A5" :
        A5.game.counter = A5.game.counter + 1
        pygame.mixer.music.load('P\\Correct-answer.mp3')
        pygame.mixer.music.play(loops=0)
        A5.top2.destroy()
        A5.game.nextQ3()
    else:
        messagebox.showinfo("Congratulations", f"{A1.game.counter}\nYou are so smart,Keep going")

def WrongAnswer3(x):
    #Label(fr2, text= "Oops").pack()
    if x == "A1":
        A1.game.chance = A1.game.chance - 1
        pygame.mixer.music.load('P\\wrong.mp3')
        pygame.mixer.music.play(loops=0)
        A1.top2.destroy()
        A1.game.nextQ3()
    elif x == "A2" :
        A2.game.chance = A2.game.chance - 1
        pygame.mixer.music.load('P\\wrong.mp3')
        pygame.mixer.music.play(loops=0)
        A2.top2.destroy()
        A2.game.nextQ3()
    elif x == "A3" :
        A3.game.chance = A3.game.chance - 1
        pygame.mixer.music.load('P\\wrong.mp3')
        pygame.mixer.music.play(loops=0)
        A3.top2.destroy()
        A3.game.nextQ3()
    elif x == "A4" :
        A4.game.chance = A4.game.chance - 1
        pygame.mixer.music.load('P\\wrong.mp3')
        pygame.mixer.music.play(loops=0)
        A4.top2.destroy()
        A4.game.nextQ3()
    elif x == "A5" :
        A5.game.chance = A5.game.chance - 1
        pygame.mixer.music.load('P\\wrong.mp3')
        pygame.mixer.music.play(loops=0)
        A5.top2.destroy()
        A5.game.nextQ3()
    else:
        messagebox.showinfo("Congratulations", f"{A1.game.chance}\nYou are so smart,Keep going")

def RightAnswer4(x):
    #Label(fr2, text= "Great").pack()
    if x == "A1":
        A1.game.counter = A1.game.counter + 1
        pygame.mixer.music.load('P\\Correct-answer.mp3')
        pygame.mixer.music.play(loops=0)
        A1.top3.destroy()
        A1.game.nextQ4()
    elif x == "A2" :
        A2.game.counter = A2.game.counter + 1
        pygame.mixer.music.load('P\\Correct-answer.mp3')
        pygame.mixer.music.play(loops=0)
        A2.top3.destroy()
        A2.game.nextQ4()
    elif x == "A3" :
        A3.game.counter = A3.game.counter + 1
        pygame.mixer.music.load('P\\Correct-answer.mp3')
        pygame.mixer.music.play(loops=0)
        A3.top3.destroy()
        A3.game.nextQ4()
    elif x == "A4" :
        A4.game.counter = A4.game.counter + 1
        pygame.mixer.music.load('P\\Correct-answer.mp3')
        pygame.mixer.music.play(loops=0)
        A4.top3.destroy()
        A4.game.nextQ4()
    elif x == "A5" :
        A5.game.counter = A5.game.counter + 1
        pygame.mixer.music.load('P\\Correct-answer.mp3')
        pygame.mixer.music.play(loops=0)
        A5.top3.destroy()
        A5.game.nextQ4()
    else:
        messagebox.showinfo("Congratulations", f"{A1.game.counter}\nYou are so smart,Keep going")

def WrongAnswer4(x):
    #Label(fr2, text= "Oops").pack()
    if x == "A1":
        A1.game.chance = A1.game.chance - 1
        pygame.mixer.music.load('P\\wrong.mp3')
        pygame.mixer.music.play(loops=0)
        A1.top3.destroy()
        A1.game.nextQ4()
    elif x == "A2" :
        A2.game.chance = A2.game.chance - 1
        pygame.mixer.music.load('P\\wrong.mp3')
        pygame.mixer.music.play(loops=0)
        A2.top3.destroy()
        A2.game.nextQ4()
    elif x == "A3" :
        A3.game.chance = A3.game.chance - 1
        pygame.mixer.music.load('P\\wrong.mp3')
        pygame.mixer.music.play(loops=0)
        A3.top3.destroy()
        A3.game.nextQ4()
    elif x == "A4" :
        A4.game.chance = A4.game.chance - 1
        pygame.mixer.music.load('P\\wrong.mp3')
        pygame.mixer.music.play(loops=0)
        A4.top3.destroy()
        A4.game.nextQ4()
    elif x == "A5" :
        A5.game.chance = A5.game.chance - 1
        pygame.mixer.music.load('P\\wrong.mp3')
        pygame.mixer.music.play(loops=0)
        A5.top3.destroy()
        A5.game.nextQ4()
    else:
        messagebox.showinfo("Congratulations", f"{A1.game.chance}\nYou are so smart,Keep going")

def RightAnswer5(x):
    #Label(fr2, text= "Great").pack()
    if x == "A1":
        A1.game.counter = A1.game.counter + 1
        pygame.mixer.music.load('P\\Correct-answer.mp3')
        pygame.mixer.music.play(loops=0)
        pygame.mixer.music.load('P\\winner.mp3')
        pygame.mixer.music.play(loops=0)
        #A1.top4.destroy()
        CongratA.con(A1.game.counter)
        ArabLevels.view()
    elif x == "A2" :
        A2.game.counter = A2.game.counter + 1
        pygame.mixer.music.load('P\\Correct-answer.mp3')
        pygame.mixer.music.play(loops=0)
        pygame.mixer.music.load('P\\winner.mp3')
        pygame.mixer.music.play(loops=0)
        #A2.top4.destroy()
        CongratA.con(A2.game.counter)
        ArabLevels.view()
    elif x == "A3" :
        A3.game.counter = A3.game.counter + 1
        pygame.mixer.music.load('P\\Correct-answer.mp3')
        pygame.mixer.music.play(loops=0)
        pygame.mixer.music.load('P\\winner.mp3')
        pygame.mixer.music.play(loops=0)
        #A3.top4.destroy()
        CongratA.con(A3.game.counter)
        ArabLevels.view()
    elif x == "A4" :
        A4.game.counter = A4.game.counter + 1
        pygame.mixer.music.load('P\\Correct-answer.mp3')
        pygame.mixer.music.play(loops=0)
        pygame.mixer.music.load('P\\winner.mp3')
        pygame.mixer.music.play(loops=0)
        #A4.top4.destroy()
        CongratA.con(A4.game.counter)
        ArabLevels.view()
    elif x == "A5" :
        A5.game.counter = A5.game.counter + 1
        pygame.mixer.music.load('P\\Correct-answer.mp3')
        pygame.mixer.music.play(loops=0)
        pygame.mixer.music.load('P\\winner.mp3')
        pygame.mixer.music.play(loops=0)
        #A5.top4.destroy()
        CongratA.con(A5.game.counter)
        ArabLevels.view()
    else:
        messagebox.showinfo("Congratulations", f"{A1.game.counter}\nYou are so smart,Keep going")

def WrongAnswer5(x):
    #Label(fr2, text= "Oops").pack()
    if x == "A1":
        A1.game.chance = A1.game.chance - 1
        pygame.mixer.music.load('P\\wrong.mp3')
        pygame.mixer.music.play(loops=0)
        pygame.mixer.music.load('P\\winner.mp3')
        pygame.mixer.music.play(loops=0)
        #A1.top4.destroy()
        CongratA.con(A1.game.chance)
        ArabLevels.view()
    elif x == "A2" :
        A2.game.chance = A2.game.chance - 1
        pygame.mixer.music.load('P\\wrong.mp3')
        pygame.mixer.music.play(loops=0)
        pygame.mixer.music.load('P\\winner.mp3')
        pygame.mixer.music.play(loops=0)
        #A2.top4.destroy()
        CongratA.con(A2.game.chance)
        ArabLevels.view()
    elif x == "A3" :
        A3.game.chance = A3.game.chance - 1
        pygame.mixer.music.load('P\\wrong.mp3')
        pygame.mixer.music.play(loops=0)
        pygame.mixer.music.load('P\\winner.mp3')
        pygame.mixer.music.play(loops=0)
        #A3.top4.destroy()
        CongratA.con(A3.game.chance)
        ArabLevels.view()
    elif x == "A4" :
        A4.game.chance = A4.game.chance - 1
        pygame.mixer.music.load('P\\wrong.mp3')
        pygame.mixer.music.play(loops=0)
        pygame.mixer.music.load('P\\winner.mp3')
        pygame.mixer.music.play(loops=0)
        #A4.top4.destroy()
        CongratA.con(A4.game.chance)
        ArabLevels.view()
    elif x == "A5" :
        A5.game.chance = A5.game.chance - 1
        pygame.mixer.music.load('P\\wrong.mp3')
        pygame.mixer.music.play(loops=0)
        pygame.mixer.music.load('P\\winner.mp3')
        pygame.mixer.music.play(loops=0)
        #A5.top4.destroy()
        CongratA.con(A5.game.chance)
        ArabLevels.view()
    else:
        messagebox.showinfo("Congratulations", f"{A1.game.chance}\nYou are so smart,Keep going")