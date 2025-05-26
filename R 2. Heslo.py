heslo=input('Zadaj heslo:')
znaky='*$@#'
cisla='0123456789'
if len(heslo) < 8:
        print('Heslo musí mať minimálne 8 znakov.')
elif heslo[0] in znaky or heslo[0] in cisla:
        print('Heslo musí začínať písmenom.')
elif not any(znak in heslo for znak in znaky):
    print('Heslo musí obsahovať aspoň jeden špeciálny znak (*, $, @, #).')
elif not any(cislo in heslo for cislo in cisla):
    print('Heslo musí obsahovať aspoň jednu číslicu.')
else:
    print('Heslo je bezpečné.')
