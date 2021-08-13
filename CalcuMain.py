from tkinter import *
root=Tk()

root.title('Calculator')
root.configure(background='black')
root.maxsize(width=313,height=415)
root.iconbitmap('calculate.ico')

# ENTRY FIELD
equation=StringVar()
ent=Entry(root,textvariable=equation,width=50)
ent.grid(row=0,column=0, columnspan=3,padx=5,pady=5)

# BUTTON ACTIONS
expression= ""

def button_click(number):
    global expression
    expression= expression + number
    equation.set(expression)

def button_equal():
    try:
        global expression
        calc= str(eval(expression))

        equation.set(calc)


    except:
        equation.set("SYNTAX ERROR")
        expression= ""


def button_clear():
    global expression
    expression= ""
    equation.set("")



# BUTTONS
butn1=Button(root,text='1',padx=40,pady=20,bg='maroon',fg='white',command=lambda:button_click('1'))
butn2=Button(root,text='2',padx=40,pady=20,bg='maroon',fg='white',command=lambda:button_click('2'))
butn3=Button(root,text='3',padx=40,pady=20,bg='maroon',fg='white',command=lambda:button_click('3'))
butn4=Button(root,text='4',padx=40,pady=20,bg='maroon',fg='white', command=lambda:button_click('4'))
butn5=Button(root,text='5',padx=40,pady=20,bg='maroon',fg='white', command=lambda:button_click('5'))
butn6=Button(root,text='6',padx=40,pady=20,bg='maroon',fg='white', command=lambda:button_click('6'))
butn7=Button(root,text='7',padx=40,pady=20,bg='maroon',fg='white', command=lambda:button_click('7'))
butn8=Button(root,text='8',padx=40,pady=20,bg='maroon',fg='white', command=lambda:button_click('8'))
butn9=Button(root,text='9',padx=40,pady=20,bg='maroon',fg='white', command=lambda:button_click('9'))
butn0=Button(root,text='0',padx=40,pady=20,bg='maroon',fg='white', command=lambda:button_click('0'))
butnAdd=Button(root,text='+',padx=39,pady=20,command=lambda:button_click('+'))
butnSub=Button(root,text='-',padx=40.5,pady=19,command=lambda:button_click('-'))
butnMul=Button(root,text='x',padx=40,pady=20,command=lambda:button_click('*'))
butnDiv=Button(root,text='/',padx=40,pady=20,command=lambda:button_click('/'))
butnEqual=Button(root,text='=',padx=91,pady=20, command=button_equal,)
butnClear=Button(root,text='Clear',padx=82,pady=19,command=button_clear,)

# PLACING BUTTONS
butn1.grid(row=3,column=0)
butn2.grid(row=3,column=1)
butn3.grid(row=3,column=2)

butn4.grid(row=2,column=0)
butn5.grid(row=2,column=1)
butn6.grid(row=2,column=2)

butn7.grid(row=1,column=0)
butn8.grid(row=1,column=1)
butn9.grid(row=1,column=2)

butn0.grid(row=4,column=0)
butnMul.grid(row=4,column=1)
butnDiv.grid(row=4,column=2)

butnClear.grid(row=5,column=1, columnspan=2)
butnAdd.grid(row=5,column=0)


butnEqual.grid(row=6,column=1, columnspan=2)
butnSub.grid(row=6,column=0)

root.mainloop()