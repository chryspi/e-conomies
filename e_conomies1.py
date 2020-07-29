from tkinter import Tk,PhotoImage,Label,StringVar,Entry,Frame,OptionMenu,Button,END,messagebox
import tkinter
import json

root=Tk()
ch=StringVar(root)


root.title('E-conomies')                                     #gives the window this specific name
root.geometry("600x400")                                    #the width and height of the window
root.iconphoto(False,PhotoImage(file='pig_money.png'))     #replaces the icon of feather that tkinter has by default anad puts this image in its place
root.configure(bg='pink')                                 #gives the window the specific background color 

with open("my_economies1.json",encoding="utf-8") as j_son:
        dict_arxeiou=json.load(j_son)
        bal=dict_arxeiou["balance"]

dict_entries=dict_arxeiou      #make a dictionary with the values of the dict_arxeiou dictionary


(one,two,five,ten,twenty,fifty,euro1,euro2)=(Entry(root),Entry(root),Entry(root),Entry(root),Entry(root),Entry(root),Entry(root),Entry(root))

l=Label(root,text="one-cents:")
l.place(x=0,y=0)
one.place(x=0,y=25)
l=Label(root,text="two-cents:")
l.place(x=150,y=0)
two.place(x=150,y=25)
l=Label(root,text="five-cents:")
l.place(x=300,y=0)
five.place(x=300,y=25)
l=Label(root,text="ten-cents:")
l.place(x=450,y=0)
ten.place(x=450,y=25)
l=Label(root,text="twenty-cents:")
l.place(x=0,y=50)
twenty.place(x=0,y=75)
l=Label(root,text="fifty-cents:")
l.place(x=150,y=50)
fifty.place(x=150,y=75)
l=Label(root,text="1-euros:")
l.place(x=300,y=50)
euro1.place(x=300,y=75)
l=Label(root,text="2-euros:")
l.place(x=450,y=50)
euro2.place(x=450,y=75)
new_bal=0.0
def put_in_file():
       dict_entries["1_cents"]=one.get()
       dict_entries["2_cents"]=two.get()    
       dict_entries["5_cents"]=five.get()
       dict_entries["10_cents"]=ten.get()
       dict_entries["20_cents"]=twenty.get()
       dict_entries["50_cents"]=fifty.get()
       dict_entries["1_euro"]=euro1.get()
       dict_entries["2_euros"]=euro2.get()
       
       for key in dict_entries:
           if(dict_entries[key]==""):dict_entries[key]=0
           else:
               try:
                   dict_entries[key]=int(dict_entries[key])
               except:
                   dict_entries[key]=0




b=Button(root,text="Submit",command=put_in_file)
b.place(x=530/2,y=100)
b.configure(bg="light pink")





def labels(text):
    l=Label(root,text=text)
    l.pack()
    l.configure(bg='pink')                                   
    return l



C=Label(text=f"Balance = {bal}")
C.configure(bg="pink")
C.place(x=255,y=150)


choices=["Balance","Deposit","Withdraw","Zero"]
ch.set(choices[0])
popupMenu = OptionMenu(root, ch, *choices)
popupMenu.config(width=10, font=('Helvetica', 12))
popupMenu.configure(bg='pale violet red')
popupMenu.place(x=255,y=200)

root.mainloop()
new_bal=dict_entries["1_cents"]/100+dict_entries["2_cents"]*2/100+dict_entries["5_cents"]*5/100+dict_entries["10_cents"]*10/100+dict_entries["20_cents"]*20/100+dict_entries["50_cents"]*50/100+dict_entries["1_euro"]+dict_entries["2_euros"]*2
print(dict_entries)
print(new_bal)
"""
def apothikefsi():
    if B["text"]=="Deposit":
        new_bal=quantity+bal
    elif B["text"]=="Withdraw":
        new_bal=bal-quantity
        if new_bal<0:new_bal=bal
    print(f"new_bal={new_bal}")
    with open ('my_economies.json','w+',encoding='utf-8') as fe:
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

"""
