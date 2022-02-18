from numbers import Number
import sys
sys.path.append('./tests')

import prueba2

# Obtenemos el dato de las listas creadas
dato = prueba2.list_num[prueba2.lista_index[0]]

def validar_datos():
    if not isinstance(dato, Number):
        # Not is number
        return False
    # Is number
    return True
