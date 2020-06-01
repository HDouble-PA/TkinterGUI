from tkinter import *
root=Tk()

def convert():
	a=x.get()
	b=a*1387.75
	lab=Label(root,text="MMK"+str(b),font=("Arial",25)).place(x=10,y=200)

def reverse():
	a=x.get()
	b=a/1387.75
	lab=Label(root,text="$ "+str(b),font=("Arial",25)).place(x=100,y=240)


root.title("Currency Converter")
root.geometry("400x350")

lab1=Label(root,text="Hello! Welcome To Currency Converter",font=("Arial Rounded MT",16),fg='red')
lab1.pack(fill="y",pady=20)

ent=Label(root,text="Enter your amount in Dollor!",font=('Arial 20 bold'))
ent.place(x=10,y=50)

x=IntVar()
ent_box=Entry(root,width=55,textvariable=x)
ent_box.place(x=10,y=90,height=40)


But1=Button(root,text="Convert",width=12,height=1,bg="red",command=convert)
But1.place(x=20,y=150)

But2=Button(root,text="Reverse",width=12,height=1,bg="blue",command=reverse)
But2.place(x=140,y=150)


root.mainloop()