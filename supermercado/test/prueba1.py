
import sys
sys.path.append('./programa')
import helper, funcion

# Main que inicializa el programa
def main():
    if helper.validar_datos():
        # Pamos los datos a la funcion
        get_valor_funcion = funcion.supermercado(helper.dato1, helper.dato2) 
        print(f'\nDatos :: {get_valor_funcion}')

    else:
        print('\033[93m' + "\nXXX Los datos ingresados son incorrectos XXX\n" + '\033[0m')

    
