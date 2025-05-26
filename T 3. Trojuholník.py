import tkinter, math
canvas=tkinter.Canvas(width=500,height=500)
canvas.pack()

def trojuholnik():
    canvas.delete('all')
    a=int(entry1.get())
    b=int(entry2.get())
    c=round(math.sqrt(a**2+b**2),2)
    canvas.create_polygon(100,400,100,400-b,100+a,400,fill='',outline='black')
    canvas.create_text((100+100+a)/2,410,text='a='+str(a))
    canvas.create_text(80,(400-b+400)/2,text='b='+str(b))
    canvas.create_text(a+b,(400-b+400)/2,text='c='+str(c))

label1=tkinter.Label(text='a=')
label1.pack(side='left')
entry1=tkinter.Entry()
entry1.pack(side='left')

label2=tkinter.Label(text='b=')
label2.pack(side='left')
entry2=tkinter.Entry()
entry2.pack(side='left')

tl=tkinter.Button(text='vykresli tojuholník',command=trojuholnik)
tl.pack()





























