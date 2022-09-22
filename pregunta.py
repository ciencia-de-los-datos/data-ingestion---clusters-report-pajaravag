"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import re


def ingest_data():

    #
    # Inserte su código aquí
    #
    with open('clusters_report.txt') as f:
        data = [line for line in f.readlines()]
    data_1 = data[4:]
    data_1 = [line.replace('\n', '') for line in data_1]
    data_1 = [line.strip() for line in data_1]
    data_word = []
    i = 0
    word = ''
    while i < len(data_1):
        if data_1[i] != '':
            word += ' ' + data_1[i]
        else:
            data_word.append(word)
            word = ''
        i +=1

    data_word = [line.strip() for line in data_word]

    block = []
    for i in data_word:
        regular = re.search(r'(^[0-9]+)\W+([0-9]+)\W+([0-9]+)([!#$%&*+-.^_`|~:\[\]]+)(\d+)(\W+)(.+)', i)
        linea = regular.group(1) + '*' + regular.group(2) + '*' + regular.group(3) + '.' + regular.group(5) + '*' + regular.group(7)
        block.append(linea)
    data_set = [line.split('*') for line in block]
    df = pd.DataFrame(columns = ['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave'])

    principales_palabras_clave = [line[3].replace('    ', ' ') for line in data_set]
    principales_palabras_clave = [line.replace('   ', ' ') for line in principales_palabras_clave]
    principales_palabras_clave = [line.replace('  ', ' ') for line in principales_palabras_clave]
    principales_palabras_clave = [line.replace('.', '') for line in principales_palabras_clave]
    principales_palabras_clave = [line.split(',') for line in principales_palabras_clave]
    principales_palabras_clave = [[element.strip() for element in line] for line in principales_palabras_clave]
    principales_palabras_clave = [', '.join(line) for line in principales_palabras_clave]

    i = 0
    while i < 3:
        df[list(df.columns)[i]] = [element[i] for element in data_set]
        i +=1
    df.principales_palabras_clave = principales_palabras_clave
    df.cluster = df.cluster.astype('int')
    df.cantidad_de_palabras_clave = df.cantidad_de_palabras_clave.astype('int')
    df.porcentaje_de_palabras_clave = df.porcentaje_de_palabras_clave.astype('float')

    return df
