import tkinter, math
canvas=tkinter.Canvas(width=500,height=500)
canvas.pack()
uhol=90
sx=250
sy=250
r=100

def rucicka():
    global uhol
    uhol=uhol-6
    uhol_rad=math.radians(uhol)
    x=sx+math.cos(uhol_rad)*r
    y=sy-math.sin(uhol_rad)*r
    canvas.delete('rucicka')
    canvas.create_line(sx,sy,x,y,tags='rucicka')
    canvas.after(1000, rucicka)

def cifernik(sx,sy,r):
    for i in range(1,13):
        alfa=90-(i*360/12)
        alfa_rad=math.radians(alfa)
        x=sx+math.cos(alfa_rad)*(r+20)
        y=sy-math.sin(alfa_rad)*(r+20)
        canvas.create_text(x,y,text=i)

cifernik(sx,sy,r)
rucicka()
