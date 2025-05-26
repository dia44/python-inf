z=input('Zadaj číslo a požadovanú sústavu prevodu:')
cifry='0123456789ABCDEF'
z=z.split(' ')
cislo=int(z[0])
sustava=int(z[1])
vysledok=''
while cislo > 0:
    zvysok=cislo%sustava
    vysledok=cifry[zvysok]+vysledok
    cislo=cislo//sustava
print(z[0],'=('+vysledok+')',sustava)
