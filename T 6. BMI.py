import tkinter
canvas=tkinter.Canvas(width=500,height=500)
canvas.pack()

label1 = tkinter.Label(text='HMOTNOSŤ(kg)')
label1.pack(side='left')
entry1=tkinter.Entry()
entry1.pack(side='left')

label2 = tkinter.Label(text='VÝŠKA(cm)')
label2.pack(side='left')
entry2=tkinter.Entry()
entry2.pack(side='left')

def vypocitaj_BMI():
    canvas.delete('all')
    hmotnosť=int(entry1.get())
    výška=int(entry2.get())
    BMI=round(hmotnosť/(výška/100)**2,2)
    if BMI<18.5:
        v='podvaha'
    elif 18.5 <=BMI<25 :
        v='normalna hmotnost'
    elif 25<=BMI<30 :
        v='nadvaha'
    else:
        v='obezita'
    canvas.create_text(250,250,text='BMI='+str(BMI)+' - '+v)
button=tkinter.Button(text='Vypočítať BMI', command=vypocitaj_BMI)
button.pack()
