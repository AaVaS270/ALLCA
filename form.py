from tkinter import *
from tkinter import messagebox
win=Tk()



win.minsize(width=300,height=500)
win.maxsize(width=350,height=500)

win.title('Entry Form')
Tit=Label(win,text='JOB APPLICATION FORM',font=('lucidia sans',20),fg='brown')
Tit.pack()

win.iconbitmap('clipboard.ico')

#NAME
name=Label(win,text='Name')
name.place(x=50,y=50)
ent1=Entry(win,text='NAME')
ent1.place(x=100,y=50)

#ADDRESS
Address=Label(win,text='Address')
Address.place(x=50,y=80)
ent2=Entry(win,text='ADDRESS')
ent2.place(x=100,y=80)

#DOB
OPTIONS = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
OPTIONS2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
variable = StringVar(win)
variable.set(OPTIONS[0])
variable2 = StringVar(win)
variable2.set(OPTIONS2[0])

DOB=Label(win,text='Date of birth')
DOB.place(x=20,y=115)
drd1=OptionMenu(win,variable,*OPTIONS)
drd1.place(x=100,y=110)
drd2=OptionMenu(win,variable2,*OPTIONS2)
drd2.place(x=160,y=110)
ent3=Entry(win,text='year')
ent3.place(x=220,y=115)

# GENDER
gnd=Label(win,text='Gender')
gnd.place(x=50,y=145)
var=IntVar()
def sel():
   selection = "" + str(var.get())
   label.config(text = selection)
label = Label(win)

r1=Radiobutton(win,text='MALE',variable=var,value=1,command=sel)
r1.place(x=100,y=145)
r2=Radiobutton(win,text='FEMALE',variable=var,value=2,command=sel)
r2.place(x=160,y=145)
r3=Radiobutton(win,text='OTHER',variable=var,value=3,command=sel)
r3.place(x=230,y=145)

# CONTACT
Contact=Label(win,text="Contact Number")
Contact.place(x=2.5,y=175)
ent4=Entry(win,text='CONTACT')
ent4.place(x=100,y=175)
Email=Label(win,text='E-mail address')
Email.place(x=10,y=205)
ent5=Entry(win,text='EMAIL')
ent5.place(x=100,y=205)

# FOR
OPTIONS10 = ['Office Helper','Salesman','HR Manager']

variable10 = StringVar(win)
variable10.set(OPTIONS10[0])


Post=Label(win,text='Post')
Post.place(x=20,y=245)
drd10=OptionMenu(win,variable10,*OPTIONS10)
drd10.place(x=100,y=235)

# SUBMIT
def confirm():
    click=messagebox.askyesno('ATTENTION!!!',"Are you sure you want to submit?")
    if click== 1:
        Label(win,text="FORM SUBMITTED SUCCESSFULLY",fg='green',font=('arial',15)).place(x=5,y=350)
    else:
        Label(win,text='FORM NOT SUBMMITTED',fg='red',font=('arial',15)).place(x=5,y=350)


Submit=Button(win,text='SUBMIT',padx=5,pady=5,fg='cyan',bg='black',command=confirm)
Submit.place(x=140,y=300)



win.mainloop()