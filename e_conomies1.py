from tkinter import Tk,PhotoImage,Label,StringVar,Entry,Frame,OptionMenu,Button
import tkinter

root=Tk()
ch=StringVar(root)

with open ('my_economies.txt','r+',encoding='utf-8') as fe:
        bal=fe.read()                                           #reads the balance of the text file and puts it in a float type variable
        bal=float(bal)

def labels(text):
    l=Label(root,text=text)
    l.pack()
    l.configure(bg='pink')                                   
    return l

E=Entry(root)

B=Button(root,text="Submit")

B.configure(bg="light pink")


def ch_commander(ch):
    print(ch)
     
def btn_commander(sel):
    ch_commander(sel)

def Balance():
    B.destroy()
    E.destroy()
    B=labels(f"Balance = {bal}")



def Withdrawal():
    
    B["text"]="Withdraw"
    E.pack()
    B.pack()

def Deposition():
    B["text"]="Deposit"
    E.pack()
    B.pack()


def ch_getter(sel):
    if sel=="Balance":
        Balance()
    if sel=="Withdraw":
        Withdrawal()
    if sel=="Deposit":
        Deposition()

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
    
    

    
    

    
    


    root.mainloop()
    



if __name__=="__main__":    #just in case I use this file in the future as a module
    init()             
