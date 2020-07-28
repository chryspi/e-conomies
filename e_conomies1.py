from tkinter import Tk,PhotoImage,Label,StringVar,Entry,Frame,OptionMenu,Button
import tkinter

root=Tk()
ch=StringVar(root)

def labels(text):
    l=Label(root,text=text)
    l.pack()
    l.configure(bg='pink')                                   
    return l



def ch_commander(ch):
    print(ch)
     
def btn_commander(sel):
    ch_commander(sel)

def Balance(l):
    l["text"]="Balance"



def Withdrawal():
    pass


def Deposition():
    pass



def ch_getter(sel):
    if sel=="Balance":
        Balance(l)

def init(): #window 
    
    root.title('E-conomies')                                     #gives the window this specific name
    root.geometry("400x300")                                    #the width and height of the window
    root.iconphoto(False,PhotoImage(file='pig_money.png'))     #replaces the icon of feather that tkinter has by default anad puts this image in its place
    root.configure(bg='pink')                                 #gives the window the specific background color 
    
    l=labels("Please make a choice:")                       #calls the labels function

                                                          #creates the choice variable of the dropdown menu
    choices=["Balance","Deposit","Withdraw"]
    ch.set(choices[0])
                                                          #sets the choice initially to "Balance"
    popupMenu = OptionMenu(root, ch, *choices,command=ch_getter)
    popupMenu.config(width=90, font=('Helvetica', 12))
    popupMenu.configure(bg='pale violet red')
    popupMenu.pack()
    
    E=Entry(root)
    E.pack()
    B=Button(root,text="Submit")
    B.pack()

    
    

    
    


    root.mainloop()
    



if __name__=="__main__":    #just in case I use this file in the future as a module
    init()             
