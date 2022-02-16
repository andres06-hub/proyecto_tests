
# Se define la funcion 


def supermercado(docenas, precio):
    precio_producto = docenas * precio
    # Si docenas < 3
    if not docenas > 3:
        monto_des = 0.10 * precio_producto
        # Su obsequio es 0 
        obsequio = 0 
        # monto a pagar
        monto_pag = precio_producto - monto_des
        # *** Retornamos valor
        return {"monto_pagar":monto_pag}
    # !! Si la docenas son mayos a 3
    monto_des = 0.15 * precio_producto
    # Se le obsequia 1 producto por cada docena en exceso sobre 3
    if docenas > 3:
        obsequio = docenas - 3
    # monto a pagar 
    monto_pag = precio_producto -monto_des
    # *** Retornamos valores
    return {
        "monto_pagar": monto_pag,
        "obsequio": obsequio
    }
