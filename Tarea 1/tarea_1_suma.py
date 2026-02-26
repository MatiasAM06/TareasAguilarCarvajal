def suma(a, b):
    """Código para demostrar 3 errores detectados por
    Flake 8 (ya en su versión corregida).
    Su función es sumar dos inputs y si es
    mayor a 10 imprime /Mayor a 10/ y regresa el resultado"""
    resultado = a+b
    if (resultado > 10):
        print("Mayor a diez")
    return resultado

