
from numbers import Number

import sys
sys.path.append('./tests')

import prueba2

edad_juan = prueba2.list_num[prueba2.lista_index[0]]
edad_mario = prueba2.list_num[prueba2.lista_index[1]]
edad_pedro = prueba2.list_num[prueba2.lista_index[2]]

def validador_datos():
    if not isinstance(edad_juan, Number) and isinstance(edad_mario, Number) and isinstance(edad_pedro, Number):
        #Not is number
        return False
        # Is number
    return True