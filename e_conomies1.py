from tkinter import Tk,PhotoImage,Label,StringVar,Entry,Frame,OptionMenu,Button,END,messagebox
import tkinter
import json

root=Tk()
ch=StringVar(root)


root.title('E-conomies')                                     #gives the window this specific name
root.geometry("600x400")                                    #the width and height of the window
root.iconphoto(False,PhotoImage(file='pig_money.png'))     #replaces the icon of feather that tkinter has by default anad puts this image in its place
root.configure(bg='purple')                                 #gives the window the specific background color 

with open("my_economies.json",encoding="utf-8") as j_son:
        dict_arxeiou=json.load(j_son)                          #takes the my_economies json file values and stores it in this dictionary
        bal=dict_arxeiou["balance"]                            #the bal variable takes the value of the balance key

dict_entries=dict_arxeiou      #make a dictionary with the values of the dict_arxeiou dictionary

#here I create the entries of the coins
(one,two,five,ten,twenty,fifty,euro1,euro2)=(Entry(root),Entry(root),Entry(root),Entry(root),Entry(root),Entry(root),Entry(root),Entry(root))

l=Label(root,text="one-cents:")        #here put the labels in  specific spots with the use of place method
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
       dict_entries["1_cents"]=one.get()        #here we put the entry values in a dictionary called dict_entries
       dict_entries["2_cents"]=two.get()    
       dict_entries["5_cents"]=five.get()
       dict_entries["10_cents"]=ten.get()
       dict_entries["20_cents"]=twenty.get()
       dict_entries["50_cents"]=fifty.get()
       dict_entries["1_euro"]=euro1.get()
       dict_entries["2_euros"]=euro2.get()
       one.delete(0, 'end')
       two.delete(0, 'end')
       five.delete(0, 'end')
       ten.delete(0, 'end')
       twenty.delete(0, 'end')
       fifty.delete(0, 'end')
       euro1.delete(0, 'end')
       euro2.delete(0, 'end')
       for key in dict_entries:
           if(dict_entries[key]==""):dict_entries[key]=0           #in case an entry has a "" as a value, we put the value zero in its key in the dictionary, so that we don't get errors
           else:
               try:
                   dict_entries[key]=int(dict_entries[key])
               except:
                   dict_entries[key]=0
                   
       if b["text"]=="Deposit":                                        #if we our choice is "deposit"
            for key in dict_entries:                                   #we add to the file's dictionary values the ones of the entries dictionary
                dict_arxeiou[key]+=dict_entries[key]
       elif b["text"]=="Withdraw":                                    #in the same logic with this of the deposition, we subtract in case of withdrawal
            for key in dict_entries:
                if dict_arxeiou[key]-dict_entries[key]>=0:
                    dict_arxeiou[key]=dict_arxeiou[key]-dict_entries[key]
                else:
                    tkinter.messagebox.showerror(title="Balance Problem",message="You don't have the amount of money for this withdrawal")
       new_bal=dict_entries["1_cents"]/100+dict_entries["2_cents"]*2/100+dict_entries["5_cents"]*5/100+dict_entries["10_cents"]*10/100+dict_entries["20_cents"]*20/100+dict_entries["50_cents"]*50/100+dict_entries["1_euro"]+dict_entries["2_euros"]*2
       dict_entries["balance"]=new_bal #check later
       C["text"]=f"Balance = {new_bal}" 
       with open ('my_economies.json','w+') as fe:
           json.dump(dict_arxeiou,fe,indent=9)        
       




b=Button(root,text="Deposit",command=put_in_file)
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


choices=["Deposit","Withdraw","Zero"]
ch.set(choices[0])

def ch_getter(selection):
    if selection=="Withdraw":
        b["text"]="Withdrawal"
    if selection=="Deposit":
        b["text"]="Deposit"
    if selection=="Zero":
        b["text"]="Zero"


selection=ch.get()
popupMenu = OptionMenu(root, ch, *choices,command=ch_getter)
popupMenu.config(width=10, font=('Helvetica', 12))
popupMenu.configure(bg='pale violet red')
popupMenu.place(x=255,y=200)




root.mainloop()

print(dict_entries)


"""

if __name__=="__main__":    #just in case I use this file in the future as a module
    init()             

"""
