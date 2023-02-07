def divisaConverter(money,value):
    if (money==0 or money==0.0):
        raise Exception("El valor del dinero es vacio ")
    else:
        return round(money*value)

