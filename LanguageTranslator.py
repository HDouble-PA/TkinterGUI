from googletrans import Translator
from tkinter import *

root=Tk()
root.geometry("500x500")

opVar=StringVar()
text=StringVar()

opVar.set("Choose your language")
OptionList=['en','zh','hi']

#text=""

#trans=Translator()
#detect=trans.detect(text)  #Detected from user
#print(detect)

#Translated language
#translated=trans.translate(text,dest="el")
#print(translated )

lab1=Label(root,text="Hello! Tkinter Translator....",font=("Cambria Math",13),fg="blue")
lab1.grid(row=0,column=0,sticky="n")

#text by user
ent1=Entry(root,font=("Times New Roman",13),fg="red",width=50,textvariable=text)
ent1.grid(row=1,column=0,sticky="n",pady=2)

Opmenu=OptionMenu(root,opVar,*OptionList)
Opmenu.grid(row=2,column=0)


def fun():
	txt1=text.get()
	#print(a)
	option_Value=opVar.get()
	translator=Translator()

	Det=translator.detect(txt1)
	Detlab=Label(root,text=f'DETECTED LANGUAGE IS {Det.lang}',font=("Times New Roman",13),fg="black") 
	Detlab.grid(row=4,column=0,sticky="n",pady=2)

	translated=translator.translate(txt1,dest=option_Value)
	print(translated)

	txt=Text(root,height=20,width=80)
	txt.grid(row=5,column=0,sticky="n")
	txt.insert(INSERT,translated)

but1=Button(root,text="TRANSLATE",font=("Times New Roman",12),fg="blue",command=fun) 
but1.grid(row=3,column=0,sticky="n",pady=2)

root.mainloop()