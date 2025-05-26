znamky=[]
while True:
    znamka=int(input('Zadaj známku od 0 do 10:'))
    if znamka == 0:
        break
    elif 0 < znamka <= 10:
        znamky.append(znamka)
    else:
        print("Neplatná známka, zadajte hodnotu medzi 0 a 10.")

znamky.remove(max(znamky))
znamky.remove(min(znamky))
priemer=sum(znamky)/len(znamky)
print('Výsledná známka:',priemer)
