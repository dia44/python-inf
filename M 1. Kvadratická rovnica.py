import math
a=int(input('Zadaj koeficient a kvadratickej rovnice:'))
b=int(input('Zadaj koeficient b kvadratickej rovnice:'))
c=int(input('Zadaj koeficient c kvadratickej rovnice:'))
D=b**2-4*a*c
if D > 0:
    x1=(-b+math.sqrt(D))/(2*a)
    x2=(-b-math.sqrt(D))/(2*a)
    print('rovnica má dva korene:','x1=',x1,'x2=',x2)
elif D == 0:
    x=-b/(2*a)
    print('rovnica má jeden koreň:','x=',x)
else:
    print('rovnica nemá riešenie')
