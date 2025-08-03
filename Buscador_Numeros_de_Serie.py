import re
import os
import time
import datetime
from pathlib import Path
import math

inicio = time.time()
ruta = 'C:\\Users\\PC\\OneDrive\\Desktop\\Mi_Gran_Directorio'
mi_patron = re.compile(r'N\D{3}-\d{5}')  # Compilar patrón una sola vez
hoy = datetime.date.today()
nros_encontrados = []
archivos_encontrados = []


def buscar_numero(archivo, patron):
    """Busca el patrón en un archivo y devuelve el match o cadena vacía"""
    try:
        with open(archivo, 'r', encoding='utf-8', errors='ignore') as este_archivo:
            texto = este_archivo.read()
            resultado = patron.search(texto)  # Usar patrón compilado
            return resultado if resultado else ''
    except (OSError, IOError, PermissionError):
        return ''


def crear_listas():
    """Recorre el directorio y busca el patrón en todos los archivos"""
    for carpeta, subcarpeta, archivo in os.walk(ruta):
        for a in archivo:
            ruta_archivo = Path(carpeta, a)
            resultado = buscar_numero(ruta_archivo, mi_patron)
            if resultado != '':
                nros_encontrados.append(resultado.group())
                archivos_encontrados.append(a.title())


def mostrar_todo():
    """Muestra todos los resultados encontrados"""

    indice = 0
    print('-' * 50)
    print(f'Fecha de Búsqueda: {hoy.day}/{hoy.month}/{hoy.year}')
    print('\n')
    print('ARCHIVO\t\t\tNRO. SERIE')
    print('-------\t\t\t----------')

    # Usar enumerate en lugar de índice manual
    for archivo in enumerate(archivos_encontrados):
        print(f'{archivo}\t{nros_encontrados[indice]}')

    print('\n')
    print(f'Números encontrados: {len(nros_encontrados)}')  # Corregir typo

    fin = time.time()
    duracion = fin - inicio
    print(f'Duración de la búsqueda: {math.ceil(duracion)} segundos')
    print('-' * 50)


# Ejecutar programa
crear_listas()
mostrar_todo()