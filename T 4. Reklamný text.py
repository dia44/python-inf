import tkinter, random
canvas=tkinter.Canvas(width=500,heigh=500)
canvas.pack()

entry=tkinter.Entry()
entry.pack()

def kresli():
    canvas.delete('all')
    slovo=entry.get()
    x=200
    for znak in slovo:
        farba=random.choice(['red','blue','green','pink','purple','yellow'])
        canvas.create_text(x,250,text=znak, fill=farba,font=('Arial',20,'bold'))
        x=x+30
    canvas.after(1000, kresli)
tl=tkinter.Button(text='zobraziť',command=kresli)
tl.pack()
