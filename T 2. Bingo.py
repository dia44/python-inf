import tkinter, random
canvas=tkinter.Canvas(width=300,height=400)
canvas.pack()
obrazky=[]

for i in range(1,7):
    obrazky.append(tkinter.PhotoImage(file='kocka_'+str(i)+'.png'))
def hod ():
    canvas.delete("all")
    x=50
    kocky=[]
    for i in range (3):
        p=random.randrange(1,7)
        canvas.create_image(x,50,image=obrazky[p-1])
        x=x+100
        kocky.append(p)
    if kocky[0] == kocky[1] == kocky[2]:
        canvas.create_text(150,200,text='BINGO')
    elif kocky[0]==kocky[1] or kocky[0]==kocky[2] or kocky[1]==kocky[2]:
        canvas.create_text(150,200,text='SUPER')
    else:
        canvas.create_text(150,200,text='NABUDÚCE')

tl=tkinter.Button(text='hod',command=hod)
tl.pack()
