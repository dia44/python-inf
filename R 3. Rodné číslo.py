r=input('Zadaj rodné číslo(RRMMDD/XXXX):')
den=int(r[4:6])
mesiac=int(r[2:4])
rok=int(r[0:2])

if mesiac > 12:
    pohlavie='žena'
    mesiac=mesiac-50
else:
    pohlavie='muž'

if rok < 54 :
    rok=rok+2000
else:
    rok=rok+1900

print('pohlavie:',pohlavie)
print('dátum narodenia:',str(den)+'.'+str(mesiac)+'.'+str(rok))
