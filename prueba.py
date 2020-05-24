import re 

cadena = '32356'
patron = re.compile('[0-9]{5}')


matcher = patron.match(cadena)
if (matcher):
    print("es codigo postal")
else:
    print("No es un codigo postal")
