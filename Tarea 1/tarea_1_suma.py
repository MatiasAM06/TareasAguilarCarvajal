def suma(a, b):
    """Código para demostrar 3 errores detectados por Flake 8,
    su función es sumar dos inputs y si es
    mayor a 10 imprime /Mayor a 10/ y regresa el resultado"""
    # Error 1:no hay whitespace despues de "resultado"
    resultado= a+b
    # Error 2:no hay whitespace despues de "if"
    # Error 3: multiple stataments on one line
    if(resultado > 10): print("Mayor a diez")
    return resultado
