znamky_str=input("Zadaj známky a oddeľ ich medzerami: ").split()
znamky=[]
for z in znamky_str:
    znamky.append(int(z)) 
priemer=sum(znamky)/len(znamky)
if 5 in znamky:
    prospech='Neprospel'
elif priemer <= 1.5 and max(znamky)<3 :
    prospech='Prospel s vyznamenaním'
elif priemer <= 2:
    prospech="Prospel veľmi dobre"
else:
    prospech="Prospel"

for znak in znamky:
    print(znak)
    
print(round(priemer,2))
print(prospech)
