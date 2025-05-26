import tkinter, random
canvas=tkinter.Canvas(width=800,height=600,bg='lightblue')
canvas.pack()
for i in range (1000):
    dlzka=random.randint(10,50)
    if dlzka < 20:
        farba='yellow'
    else:
        farba='green'
    canvas.create_line(i,600,i,600-dlzka,fill=farba)

for i in range (500):
    x=random.randint(10,300)
    y=random.randint(10,300)
    farby=random.choice(['blue','red','purple','yellow','white'])
    canvas.create_line(0,0,x,y,fill=farby)
