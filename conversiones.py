import sys

def convertir_moneda(tasa_sol, tasa_peso_argentino, tasa_dolar, valor_pesos_chilenos):
    """
    Convierte un valor en pesos chilenos a Soles, Pesos Argentinos y Dólares.

    Args:
        tasa_sol (float): Tasa de conversión a Soles.
        tasa_peso_argentino (float): Tasa de conversión a Pesos Argentinos.
        tasa_dolar (float): Tasa de conversión a Dólares.
        valor_pesos_chilenos (float): Valor en pesos chilenos a convertir.

    Returns:
        dict: Un diccionario con el valor convertido en las tres monedas.
    """
    return {
        "Soles": valor_pesos_chilenos * tasa_sol,
        "Pesos Argentinos": valor_pesos_chilenos * tasa_peso_argentino,
        "Dólares": valor_pesos_chilenos * tasa_dolar
    }

if __name__ == "__main__":
    tasa_sol = float(sys.argv[1])
    tasa_peso_argentino = float(sys.argv[2])
    tasa_dolar = float(sys.argv[3])
    valor_pesos_chilenos = float(sys.argv[4])

    conversiones = convertir_moneda(tasa_sol, tasa_peso_argentino, tasa_dolar, valor_pesos_chilenos)
    print(f"Los {valor_pesos_chilenos} pesos equivalen a:")
    for moneda, valor in conversiones.items():
        print(f"{valor} {moneda}")
