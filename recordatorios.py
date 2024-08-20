from datetime import datetime

def modificar_recordatorios(recordatorios):
    """
    Modifica una lista de recordatorios agregando, editando y eliminando eventos.

    Args:
        recordatorios (list): Lista de eventos a modificar.

    Returns:
        list: Lista de eventos modificados.
    """
    # Agregar el evento del 2 de Febrero de 2021
    recordatorios.insert(1, ['2021-02-02', '06:00', 'Empezar el año'])

    # Editar el evento del 15 de Julio al 16 de Julio
    for evento in recordatorios:
        if evento[0] == '2021-07-15':
            evento[0] = '2021-07-16'

    # Eliminar el evento del Día del Trabajo (1 de Mayo)
    recordatorios = [evento for evento in recordatorios if evento[0] != '2021-05-01']

    # Agregar eventos de Navidad y Año Nuevo
    recordatorios.append(['2021-12-24', '22:00', 'Cena de Navidad'])
    recordatorios.append(['2021-12-31', '22:00', 'Cena de Año Nuevo'])

    # Ordenar los eventos por fecha y hora
    recordatorios.sort(key=lambda x: datetime.strptime(f"{x[0]} {x[1]}", "%Y-%m-%d %H:%M"))

    return recordatorios

if __name__ == "__main__":
    recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
                     ['2021-05-01', "15:00", "No trabajar"],
                     ['2021-07-15', "13:00", "No hacer nada es feriado"],
                     ['2021-09-18', "16:00", "Ramadas"],
                     ['2021-12-25', "00:00", "Navidad"]]

    recordatorios_modificados = modificar_recordatorios(recordatorios)
    for recordatorio in recordatorios_modificados:
        print(recordatorio)