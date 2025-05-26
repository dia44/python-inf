import tkinter
canvas=tkinter.Canvas(width=800,height=600)
canvas.pack()
canvas.create_rectangle(0,300,800,600,fill='blue')
def klik(sur):
    x=sur.x
    y=sur.y
    if y<300:
        canvas.create_oval(x,y,x+50,y+50,fill='light blue',tags='bal')
        canvas.create_line(x,y+29,x+25,y+80,tags='bal')
        canvas.create_line(x+50,y+29,x+25,y+80,tags='bal')
        canvas.create_rectangle(x+10,y+80,x+40,y+100,fill='brown',tags='bal')
        balon()
    else:
        canvas.create_polygon(x+120,y-30,x+210,y-30,x+200,y,x+130,y,x+120,y-30,fill='red',tags='lod')
        canvas.create_polygon(x+165,y-95,x+190,y-65,x+165,y-45,x+165,y-95,fill='white',outline='black',tags='lod')
        canvas.create_line(x+165,y-30,x+165,y-95,width=2,tags='lod')
        lodka()

def balon():
    canvas.move('bal',0,5)
    canvas.after(100,balon)
    
def lodka():
    canvas.move('lod',5,0)
    canvas.after(100,lodka)
    
canvas.bind('<Button-1>',klik)

