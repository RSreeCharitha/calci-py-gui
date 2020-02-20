from tkinter import *
from tkinter import ttk
############## Functions
def enterNum(x):
    s = inp.get()
    ln = len(s)
    if s == '0':
        inp.delete(0,'end')
        inp.insert(0, str(x))
    #elif x == '.' and s[ln-1] != '.':
     #   inp.insert(ln, x)
    else:
        inp.insert(ln, str(x))

def enterOp(x):
    s = inp.get()
    ln = len(s)
    print(s)
    if s!='0' and (s[ln-1] != '+' and s[ln-1] != '-' and s[ln-1] != '*' and s[ln-1] != '/' and s[ln-1] != '%'):
        inp.insert(ln, str(x))


def operate():
    s = inp.get()
    print(s)
    res = eval(s)
    inp.delete(0,'end')
    inp.insert(0,str(res))

def clear():

    inp.delete(0, 'end')
    inp.insert(0, '0')

##########################
root= Tk()
root.title('Calculator')
b1=ttk.Button(root, text="1", command=lambda x=1:enterNum(x))
b2=ttk.Button(root, text="2",command=lambda x=2:enterNum(x))
b3=ttk.Button(root,text="3",command = lambda x=3:enterNum(x))
b4=ttk.Button(root,text="4",command = lambda x=4:enterNum(x))
b5=ttk.Button(root,text="5",command = lambda x=5:enterNum(x))
b6=ttk.Button(root,text="6",command = lambda x=6:enterNum(x))
b7=ttk.Button(root,text="7",command = lambda x=7:enterNum(x))
b8=ttk.Button(root,text="8",command = lambda x=8:enterNum(x))
b9=ttk.Button(root,text="9",command = lambda x=9:enterNum(x))
b0=ttk.Button(root,text="0",command = lambda x=0:enterNum(x))
bdot=ttk.Button(root,text=".",command = lambda x='.':enterNum(x))


bp=ttk.Button(root,text="+",command = lambda x='+':enterOp(x))
bs=ttk.Button(root,text="-",command = lambda x='-':enterOp(x))
bmu=ttk.Button(root,text="*",command = lambda x='*':enterOp(x))
bd=ttk.Button(root,text="/",command = lambda x='/':enterOp(x))
bmo=ttk.Button(root,text="%",command = lambda x='%':enterOp(x))
beq=ttk.Button(root,text="=",command =operate)

bac = ttk.Button(root,text='AC',command=clear)

inp = ttk.Entry(root,width=22,justify=RIGHT, font = ('courier', 15, 'bold'))
his = ttk.Entry(root,width=22, font = ('courier', 15, 'bold'))
l = ttk.Label(root,text='History')
his.config(state='readonly')

inp.insert(0,'0')

#########Place Geometry
l.place(x=10, y=360)
inp.place(x=10,y=20)
his.place(x=10,y=380)
b1.place(x=10,y=75)
b2.place(x=110,y=75)
b3.place(x=210,y=75)
b4.place(x=10,y=125)
b5.place(x=110,y=125)
b6.place(x=210,y=125)
b7.place(x=10,y=175)
b8.place(x=110,y=175)
b9.place(x=210,y=175)
b0.place(x=10,y=225)
bp.place(x=110,y=225)
bs.place(x=210,y=225)
bd.place(x=10,y=275)
bmu.place(x=110,y=275)
bmo.place(x=210,y=275)
beq.place(x=110,y=325)
bac.place(x=210,y=325)
bdot.place(x=10,y=325)

#######################################

root.geometry("300x420+800+100")
root.mainloop()