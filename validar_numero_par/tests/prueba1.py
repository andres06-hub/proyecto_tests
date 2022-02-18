import sys
sys.path.append("./service")
import helper, funcion

# Se crea funcion principal
def main():
    if helper.validar_datos():
        get_dato_funcion = funcion.recibir_numero(helper.dato) 
        print(f"\n\tEl numero es {get_dato_funcion}\n")
    else:
        print('\033[93m' + "\nLos datos ingresados son invalidos\n" + '\033[0m')