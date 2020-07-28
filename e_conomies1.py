from tkinter import Tk,PhotoImage,Label,StringVar,Entry,Frame,OptionMenu,Button,END
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

C=Label(text=f"Balance = {bal}")
C.configure(bg="pink")

def apothikefsi():
    quantity=E.get()
    E.delete(0, END)
    quantity=float(quantity)
    if B["text"]=="Deposit":
        new_bal=quantity+bal
    elif B["text"]=="Withdraw":
        new_bal=bal-quantity
        if new_bal<0:new_bal=bal
    print(f"new_bal={new_bal}")
    with open ('my_economies.txt','w+',encoding='utf-8') as fe:
        fe.write(str(new_bal))                                          
    C["text"]=f"Balance = {bal}"

def Withdrawal():
    B["text"]="Withdraw"
    E.pack()
    B.pack()
    B["command"]=apothikefsi

def Zeros():
    with open ('my_economies.txt','w+',encoding='utf-8') as fe:
        fe.write("0.0")                                          
        

def Deposition():
    B["text"]="Deposit"
    E.pack()
    B.pack()
    B["command"]=apothikefsi


def Balance():
    with open ('my_economies.txt','r',encoding='utf-8') as fe:
        bal=fe.read()                                           #reads the balance of the text file and puts it in a float type variable
        bal=float(bal)
    C["text"]=f"Balance = {bal}"
    C.pack()
    
def ch_getter(sel):
    if sel=="Balance":
        Balance()
    if sel=="Withdraw":
        Withdrawal()
    if sel=="Deposit":
        Deposition()
    if sel=="Zero":
        Zeros()

def init(): #window 
    
    root.title('E-conomies')                                     #gives the window this specific name
    root.geometry("400x300")                                    #the width and height of the window
    root.iconphoto(False,PhotoImage(file='pig_money.png'))     #replaces the icon of feather that tkinter has by default anad puts this image in its place
    root.configure(bg='pink')                                 #gives the window the specific background color 
    
    l=labels("Please make a choice:")                       #calls the labels function

                                                          #creates the choice variable of the dropdown menu
    choices=["Balance","Deposit","Withdraw","Zero"]
    ch.set(choices[0])
                                                          #sets the choice initially to "Balance"
    popupMenu = OptionMenu(root, ch, *choices,command=ch_getter)
    popupMenu.config(width=90, font=('Helvetica', 12))
    popupMenu.configure(bg='pale violet red')
    popupMenu.pack()
    
    

    
    

    
    


    root.mainloop()
    



if __name__=="__main__":    #just in case I use this file in the future as a module
    init()             
