
# funcion que recibe 3 edades
def recibir_edades(edad_juan, edad_mario, edad_pedro):
    if(edad_juan == edad_mario and edad_mario == edad_pedro):
        return "Los tres son contemporaneos"
    elif(edad_juan == edad_mario):
        return "Juan y mario son contemporanos"
    elif(edad_juan == edad_pedro):
        return "Juan y Pedro son contemporaneos"
    elif(edad_mario == edad_pedro):
        return "Mario y pedro son contemporanos"
    else:
        return "No hay contemporaneos"


