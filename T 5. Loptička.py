import tkinter
canvas=tkinter.Canvas(width=500,height=500)
canvas.pack()
x=50
y=50
p=5
bezi=False
def lopta():
    global y,p,bezi
    canvas.create_oval(x,y,x+30,y+30,fill='red',tags='lopta')
    canvas.move('lopta',0,p)
    y=y+p
    if y >= 500 or y <= 0:
        p=p*-1
    if bezi:
        canvas.after(50,lopta)
def akcia():
    global bezi
    if not bezi:
        bezi=True
    lopta()
    
def stop():
    global bezi
    bezi=False
    canvas.delete('lopta')
    
tl1=tkinter.Button(text="AKCIA", command=akcia)
tl1.pack()

tl2=tkinter.Button(text="STOP", command=stop)
tl2.pack()
