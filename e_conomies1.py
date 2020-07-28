from tkinter import Tk,PhotoImage,Label,StringVar,Entry
import tkinter

root=Tk()

def labels(text):
    l=Label(root,text=text)
    l.pack()                                    #puts the label named "Please make a choice"
    return l

def btn_crt():
    pass


def init(): #window 

   
    root.title('E-conomies')  #gives the window this specific name
    root.geometry("400x300")  #the width and height of the window
    root.iconphoto(False,PhotoImage(file='pig_money.png')) #replaces the icon of feather that tkinter has by default anad puts this image in its place
    root.configure(bg='pink')  #gives the window the specific background color 
    l=labels("se spaso")                   #calls the labels function
    l.configure(bg='purple')
    root.mainloop()
    



if __name__=="__main__":    #just in case I use this file in the future as a module
    init()             