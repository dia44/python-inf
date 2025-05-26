import tkinter
canvas=tkinter.Canvas(width=200,height=200)
canvas.pack()
x=100
y=100
canvas.create_oval(x-10,y-10,x+10,y+10,fill='brown',tags='had')
def vpravo(event):
    global x
    if x < 200:
        canvas.move('had',5,0)
        x=x+5
    else:
        x=0
        canvas.delete('all')
        canvas.create_oval(x-10,y-10,x+10,y+10,fill='brown',tags='had')
    
canvas.bind_all('<Right>',vpravo)
def vlavo(event):
    global x
    if x > 0:
        canvas.move('had',-5,0)
        x=x-5
    else:
        x=200
        canvas.delete('all')
        canvas.create_oval(x-10,y-10,x+10,y+10,fill='brown',tags='had')
    
canvas.bind_all('<Left>',vlavo)
def dole(event):
    global y
    if y < 200:
        canvas.move('had',0,5)
        y=y+5
    else:
        y=0
        canvas.delete('all')
        canvas.create_oval(x-10,y-10,x+10,y+10,fill='brown',tags='had')
    
canvas.bind_all('<Down>',dole)
def hore(event):
    global y
    if y > 0:
        canvas.move('had',0,-5)
        y=y-5
    else:
        y=200
        canvas.delete('all')
        canvas.create_oval(x-10,y-10,x+10,y+10,fill='brown',tags='had')
    
canvas.bind_all('<Up>',hore)

























