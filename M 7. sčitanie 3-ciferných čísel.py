import random
s=0
for i in range (1,6):
    s1=random.randrange(100,1000)
    s2=random.randrange(100,1000)
    print(i,'.', s1,'+',s2,'=')
    vysledok=input('Zadaj výsledok:')
    v=s1+s2
    if v==int(vysledok):
        print('výsledok je správny')
        s=s+1
    else:
        print('nesprávne, správny výsledok je',v)

if s==5:
    print('Tvoja známka je: 1')
elif s==4:
    print('Tvoja známka je: 2')
elif s==3:
    print('Tvoja známka je: 3')
elif s==2:
    print('Tvoja známka je: 4')
else:
    print('Tvoja známka je: 5')
