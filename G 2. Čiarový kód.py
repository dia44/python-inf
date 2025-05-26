import tkinter, random
canvas=tkinter.Canvas(height=200,width=170)
canvas.pack()
kod=[]
for i in range (8):
    k=random.randint(1,9)
    kod.append(k)
for prvok in kod:
    print(prvok,end='')
x=50
canvas.create_line(x,50,x,145,width=kod[0])
x=x+10
for i in range (1,7):
    canvas.create_line(x,50,x,130,width=kod[i])
    x=x+10
canvas.create_line(x,50,x,145,width=kod[7])
canvas.create_text(85,142,text=kod,font=('Arial 6'))
