v=u=input('Zadaj vetu:')
ička='iyíýIÍYÝ'
for znak in ička:
    v=v.replace(znak,'-')
print(v)

n=input('napíš vetu gramaticky správne:')

if n == u :
    print('správne')
else:
    vystup=''
    for povodne, nove in zip(u,n):
        if povodne != nove:
            vystup=vystup+'!'
        else:
            vystup=vystup+nove
    print('Nesprávne! Chybné písmená sú označené')
    print(vystup)

