import numpy as np
import random
from sklearn.model_selection import StratifiedShuffleSplit

def amostragem_aleatoria_simples(dataframe, amostras):
    return dataframe.sample(n = amostras)

def amostragem_estratificada(dataframe, percentual, coluna):
    nova_base = StratifiedShuffleSplit(test_size = percentual)
    for _, t in nova_base.split(dataframe, coluna):
        novo_df = dataframe.iloc[t]
    return novo_df

def amostragem_agrupamento(dataframe, numero_grupos):
    intervalo = len(dataframe) / numero_grupos
    grupos = []
    id_grupo = 0
    contagem = 0
    for _ in dataframe.iterrows():
        grupos.append(id_grupo)
        contagem += 1
        if contagem > intervalo:
            contagem = 0
            id_grupo += 1

    dataframe['grupo'] = grupos
    random.seed(1)
    grupo_selecionado = random.randint(0, numero_grupos)
    return dataframe[dataframe['grupo'] == grupo_selecionado]


def amostragem_reservatorio(dataframe, amostras):
    stream = []
    for i in range(len(dataframe)):
        stream.append(i)
    i = 0
    tamanho = len(dataframe)
    reservatorio = [0] * amostras
    for i in range(amostras):
        reservatorio[i] = stream[i]
    while i < tamanho:
        j = random.randrange(i + 1)
        if j < amostras:
            reservatorio[j] = stream[i]
        i += 1
    return dataframe.iloc[reservatorio]

def amostragem_sistematica(dataframe, amostras):
    intervalo = len(dataframe) // amostras
    random.seed(1)
    inicio = random.randint(0, intervalo)
    indices = np.arange(inicio, len(dataframe), step = intervalo)
    amostra_sistematica = dataframe.iloc[indices]
    return amostra_sistematica