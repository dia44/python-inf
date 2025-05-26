import random
vyskyt=[0] * 10
for i in range (100):
    cislica=random.randint(0,9)
    vyskyt[cislica]+=1
sucet=0
for i in range(10):
    percento=vyskyt[i]/100*100
    print('čislica',i,round(percento,2),'%')
    sucet+=i*vyskyt[i]
priemer=sucet/100
print('priemerná hodnota číslic je:',round(priemer,2))
