import tkinter, random, math
canvas=tkinter.Canvas(width=500,height=500)
canvas.pack()

def obdlznik():
    for i in range (6000):
        x=random.randrange(0,500)
        y=random.randrange(0,500)
        if x<=250 and y<=250:
            canvas.create_oval(x-5,y-5,x+5,y+5,fill='red')
        elif x<=250 and y>=250:
            canvas.create_oval(x-5,y-5,x+5,y+5,fill='yellow')
        elif x>=250 and y<=250:
            canvas.create_oval(x-5,y-5,x+5,y+5,fill='green')
        else:
            canvas.create_oval(x-5,y-5,x+5,y+5,fill='blue')
def kruh():
    r=80
    p=160
    q=240
    canvas.create_oval(250-r,250-r,250+r,250+r)
    canvas.create_oval(250-p,250-p,250+p,250+p)
    canvas.create_oval(250-q,250-q,250+q,250+q)
    for i in range (6000):
        xs=random.randrange(0,500)
        ys=random.randrange(0,500)
        vz=math.sqrt((250-xs)**2+(250-ys)**2)
        if vz <= r :
            canvas.create_oval(xs-5,ys-5,xs+5,ys+5,fill='red')
        elif p > vz > r :
            canvas.create_oval(xs-5,ys-5,xs+5,ys+5,fill='green')
        elif p < vz <= q:
            canvas.create_oval(xs-5,ys-5,xs+5,ys+5,fill='yellow')
        else:
            canvas.create_oval(xs-5,ys-5,xs+5,ys+5,fill='blue')
        
def zmaz():
    canvas.delete('all')
    
tl1=tkinter.Button(text='OBDLZNIK',command=obdlznik)
tl1.pack()
tl2=tkinter.Button(text='KRUH',command=kruh)
tl2.pack()
tl3=tkinter.Button(text='ZMAŽ',command=zmaz)
tl3.pack()
