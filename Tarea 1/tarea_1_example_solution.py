def encontrar_extremos(entrada):
    """
    Determina el valor mínimo y máximo de una lista numérica.

    Parámetros: entrada : list
        Lista que debe contener únicamente valores numéricos (int o float).
        No se permiten valores de otro tipo.

    Retorna: tuple : (estado, minimo, maximo)

        estado : int
            0     -> Ejecución exitosa
            -600  -> El parámetro no es una lista
            -700  -> La lista contiene elementos no numéricos
            -800  -> La lista está vacía
            -900  -> La lista contiene más de 15 elementos
    """

    # Validar que el parámetro sea una lista
    if not isinstance(entrada, list):
        return -600, None, None

    # Validar que la lista no esté vacía
    if len(entrada) == 0:
        return -800, None, None

    # Validar que la lista no exceda 15 elementos
    if len(entrada) > 15:
        return -900, None, None

    # Validar que todos los elementos sean numéricos (excluyendo bool)
    for elemento in entrada:
        if (
            not isinstance(elemento, (int, float))
            or isinstance(elemento, bool)
        ):
            return -700, None, None

    # Cálculo de extremos
    minimo = min(entrada)
    maximo = max(entrada)

    return 0, minimo, maximo


def filtrar_vocales(cadena, bandera):
     """
    Filtra una cadena de caracteres retornando únicamente vocales
    o consonantes según el valor del parámetro bandera.

    Parámetros:
    ----------
    cadena : str
        Cadena compuesta únicamente por caracteres alfabéticos.
        Longitud máxima permitida: 30 caracteres.
    bandera : bool
        True  -> Retorna únicamente las vocales.
        False -> Retorna únicamente las consonantes.

    Retorna:
    -------
    tuple
        (estado, resultado)

        estado:
            0     -> Éxito
            -100  -> cadena no es tipo str
            -200  -> cadena contiene caracteres no alfabéticos
            -300  -> cadena vacía
            -400  -> cadena mayor a 30 caracteres
            -500  -> bandera no es tipo bool

        resultado:
            str con el filtrado correspondiente o None en caso de error.
    """
    Exito = 0
    Error_Cadena = -100
    Error_Caracter_Invalido = -200
    Error_CadenaVacia = -300
    Error_Longitud = -400
    Error_Bandera = -500

    # Valida que cadena sea una string
    if not isinstance(cadena, str):
        return Error_Cadena, None

    # Valida que cadena no esté vacía
    if cadena == "":
        return Error_CadenaVacia, None

    # Valida que solo tenga letras
    if not cadena.isalpha():
        return Error_Caracter_Invalido, None

    # Valida que cadena tenga longitud máxima 30
    if len(cadena) > 30:
        return Error_Longitud, None

    # Valida que bandera sea booleano
    if not isinstance(bandera, bool):
        return Error_Bandera, None

    vocales = "aeiouAEIOU"

    if bandera:  # Extrae las vocales
        resultado = "".join(c for c in cadena if c in vocales)
    else:  # Extrae las consonantes
        resultado = "".join(c for c in cadena if c not in vocales)

    return Exito, resultado
