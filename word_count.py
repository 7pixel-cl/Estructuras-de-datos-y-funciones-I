def contar_palabras_y_caracteres(texto):
    """
    Cuenta los caracteres y palabras distintas en un texto.

    Args:
        texto (str): Texto a analizar.

    Returns:
        dict: Un diccionario con el número de caracteres y palabras distintas.
    """
    caracteres_distintos = len(set(texto))
    palabras_distintas = len(set(texto.split(" ")))
    return {
        "caracteres_distintos": caracteres_distintos,
        "palabras_distintas": palabras_distintas
    }

if __name__ == "__main__":
    import sys

    with open(sys.argv[1], "r") as file:
        texto = file.read()

    conteo = contar_palabras_y_caracteres(texto)
    print(f"El número de caracteres distintos es: {conteo['caracteres_distintos']}")
    print(f"El número de palabras distintas es: {conteo['palabras_distintas']}")
