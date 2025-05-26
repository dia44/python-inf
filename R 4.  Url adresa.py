a=input('Zadaj URL adresu:')

##if '://' in a:
##    p=a.split('://')[0]
##else:
##    print('Chybná URL adresa')
p=a.split('://')[0]
d=a.split('://')[1]
n=d.split('.')[-1]

print('protokol použitej služby:',p)
print('doména najvyššej úrovne:',n)
print('doménová adresa servera:',d)
