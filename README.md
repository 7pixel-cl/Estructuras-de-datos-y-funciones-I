
# Desafíos de Estructuras de Datos y Funciones

Este proyecto contiene tres programas en Python que resuelven desafíos relacionados con el manejo de estructuras de datos y funciones.

## Archivos

### 1. `conversiones.py`
Este script convierte un valor dado en pesos chilenos a Soles peruanos, Pesos argentinos y Dólares estadounidenses utilizando tasas de conversión proporcionadas.

#### Ejecución
```bash
python conversiones.py <tasa_sol> <tasa_peso_argentino> <tasa_dolar> <valor_pesos_chilenos>
```

#### Ejemplo
```bash
python conversiones.py 0.0046 0.093 0.00013 10000
```

#### Output esperado
```plaintext
Los 10000 pesos equivalen a:
46.0 Soles
930.0 Pesos Argentinos
1.3 Dólares
```

### 2. `word_count.py`
Este script cuenta el número de caracteres y palabras distintas en un texto proporcionado.

#### Ejecución
```bash
python word_count.py assets/lorem_ipsum.txt
```

#### Ejemplo
```bash
python word_count.py lorem_ipsum.txt
```

#### Output esperado
```plaintext
El número de caracteres distintos es: 40
El número de palabras distintas es: 243
```

### 3. `recordatorios.py`
Este script permite modificar una lista de recordatorios de eventos, agregando, editando y eliminando eventos según las instrucciones dadas.

#### Ejecución
```bash
python recordatorios.py
```

#### Output esperado
```plaintext
[['2021-01-01', '11:00', 'Levantarse y ejercitar'],
 ['2021-02-02', '06:00', 'Empezar el año'],
 ['2021-07-16', '13:00', 'No hacer nada es feriado'],
 ['2021-09-18', '16:00', 'Ramadas'],
 ['2021-12-24', '22:00', 'Cena de Navidad'],
 ['2021-12-25', '00:00', 'Navidad'],
 ['2021-12-31', '22:00', 'Cena de Año Nuevo']]
```

## Documentación

Cada archivo incluye docstrings con el estilo Google para facilitar la comprensión de los objetivos y el funcionamiento de las funciones. Esto asegura que el código es fácilmente comprensible y mantenible.

### Ejemplo de docstring:
```python
"""
Modifica una lista de recordatorios agregando, editando y eliminando eventos.

Args:
    recordatorios (list): Lista de eventos a modificar.

Returns:
    list: Lista de eventos modificados.
"""
```

## Estructura del Proyecto

El proyecto está organizado en tres archivos Python, cada uno de ellos responsable de resolver un problema específico mediante el uso de estructuras de datos y funciones. Los archivos están listos para ejecutarse desde la línea de comandos, y cada uno cuenta con una descripción clara en este README sobre cómo utilizarlos.

### Archivos:
- `conversiones.py`
- `word_count.py`
- `recordatorios.py`

## Contribuciones
Las contribuciones son bienvenidas. Si deseas mejorar el proyecto, por favor haz un fork del repositorio y envía un pull request con tus cambios.

## Licencia
Este proyecto está bajo la Licencia MIT. Siéntete libre de utilizarlo y modificarlo según tus necesidades.