
import sys 
sys.path.append('./service')  
import helper, funcion

# Funcion donde se invoca la funcion, se obtiene la validacion de datos
def main():
    if helper.validador_datos():
        get_mensaje = funcion.recibir_edades(helper.edad_juan, helper.edad_mario, helper.edad_pedro)
        print (get_mensaje)
    else:
        print ('\033[93m' + "Los datos no son validos\n" + '\033[0m')
