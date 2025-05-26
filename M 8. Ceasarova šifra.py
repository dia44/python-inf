##t=input('Zadaj text veľkými písmenami, ktorý chceš zašifrovať:')
##n=int(input('Zadaj posun:'))
##vystup=[]
##for znak in t :
##    cislo=ord(znak)
##    p_cislo=cislo+n
##    if p_cislo > 90:
##        p_cislo=p_cislo-26
##
##    p_znak=chr(p_cislo)
##    vystup.append(p_znak)
##for znak in vystup:
##    print(znak,end='')

#if'a'<=znak<='z'
    
t = input('Zadaj text, ktorý chceš zašifrovať: ')
n = int(input('Zadaj posun: '))
vystup = []

for znak in t:
    if 'A' <= znak <= 'Z':
        cislo = ord(znak)
        p_cislo = cislo + n
        if p_cislo > ord('Z'):
            p_cislo=p_cislo-26
        p_znak = chr(p_cislo)
        vystup.append(p_znak)
    elif 'a' <= znak <= 'z':
        cislo = ord(znak)
        p_cislo = cislo + n
        if p_cislo > ord('z'):
            p_cislo -= 26
        p_znak = chr(p_cislo)
        vystup.append(p_znak)
    else:
        vystup.append(znak)  

for znak in vystup:
    print(znak, end='')

