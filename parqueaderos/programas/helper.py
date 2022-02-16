
# Archivo que se encarga de validar si  hay datos de la
from ast import Num
from numbers import Number
import sys
sys.path.append('./test')
import prueba2


dato1 = prueba2.list_num[prueba2.lista_index[0]]
dato2 = prueba2.list_num[prueba2.lista_index[1]]

def validar_datos():
    if not isinstance(dato1, Number) and isinstance(dato2, Number):
        # Not is number False
        return False
    # Is number True
    return True



