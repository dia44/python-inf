vysky=[]
for i in range (1,11):
    vyska=int(input('Zadaj '+str(i)+'. výšku:'))
    vysky.append(vyska)
vysky.sort()
sucet=0
for prvok in vysky:
    sucet=sucet+int(prvok)
priemer=sucet/len(vysky)
median=(vysky[4]+vysky[5])/2
print('Výšky žiakov usporiadané vzostupne:',vysky)
print('Priemerná výška žiakov:',round(priemer,2))
print('Medián výšky žiakov je:',median)
