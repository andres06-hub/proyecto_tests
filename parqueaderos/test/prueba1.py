# Importamos el path
import sys
# Importamos programas
sys.path.append('./programas')

import helper,parqueadero

# import helper,parqueadero
# from ..programas import parqueadero, helper

# Obtenemos el booleano retornado de la funcion validar datos de /heleper
def main():
    if helper.validar_datos():
        '''Le pasamos el el indice obtenido y obtenemos el numero de la lista de numeros generados'''
        valor_obtenido = parqueadero.calcular_parqueadero(helper.dato1, helper.dato2)
        print(f"El cliente deqbe de pagar :: {valor_obtenido}")
        print(f"HH = {helper.dato1} \nMM = {helper.dato2}")
        
    else:
        print('\033[93m' + '\n-> Los datos son incorrectos\n' + '\033[0m')




