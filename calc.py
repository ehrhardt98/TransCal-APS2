import math
import numpy as np
from classes import Point
from classes import Element
from classes import Load
from classes import Rigidez
from parca import pars
from Functions import calcSenCos
from Functions import matrixMaker
from Functions import superMatrixMaker
from Functions import contornoMaker
from Functions import strain_stressMaker
from Functions import reactionsMaker
from gauss import gauss
from jacobi import obe_j

# Arquivo de entrada


def calc(point_list, element_list, load_list, method='gauss', ite=5000):

    element_list, point_list = calcSenCos(element_list, point_list)
    matrix_list = []
    for i in element_list:
        matrix_list.append(matrixMaker(i))
    superMatrix = superMatrixMaker(matrix_list, len(point_list))

    v_carregamento = []
    contador = 0
    for i in point_list:
        if i.name == load_list[contador].point:
            v_carregamento.append([int(load_list[contador].intensity_x)])
            v_carregamento.append([int(load_list[contador].intensity_y)])
            contador += 1
        else:
            v_carregamento.append([0])
            v_carregamento.append([0])
    v_carregamento = np.array(v_carregamento, dtype=float)
    v_deslocamento = []
    for i in point_list:
        linha = []
        if i.x_fixed:
            linha.append(0)
            v_deslocamento.append(linha)
            linha = []
        else:
            linha.append(-1)
            v_deslocamento.append(linha)
            linha = []
        if i.y_fixed:
            linha.append(0)
            v_deslocamento.append(linha)
            linha = []
        else:
            linha.append(-1)
            v_deslocamento.append(linha)
            linha = []
    v_deslocamento = np.array(v_deslocamento, dtype=float)
    for i in range(0, len(v_deslocamento)):
        if v_deslocamento[i][0] == 0:
            v_carregamento[i][0] = -0.001
    matrixContorno, v_carregamento_contorno = contornoMaker(
        superMatrix, v_deslocamento, v_carregamento)

    if method == 'gauss':
        v_deslocamento_metodo = gauss(
            ite, 0.0001, matrixContorno, v_carregamento_contorno)
    else:
        v_deslocamento_metodo = obe_j(
            ite, 0.0001, matrixContorno, v_carregamento_contorno)

    contador = 0

    for i in range(0, len(v_deslocamento)):
        if v_deslocamento[i][0] != 0:
            v_deslocamento[i][0] = v_deslocamento_metodo[contador]
            contador += 1
    contador = 0
    for i in point_list:
        i.x_displacement = v_deslocamento[contador][0]
        contador += 1
        i.y_displacement = v_deslocamento[contador][0]
        contador += 1
    lista_tensao, lista_deformacao = strain_stressMaker(element_list)

    contador = 0
    for i in element_list:
        i.strain = lista_tensao[contador]
        i.stress = lista_deformacao[contador]
        contador += 1

    lista_reactions, v_carregamento = reactionsMaker(
        superMatrix, v_deslocamento, v_carregamento)

    contador = 0
    for i in point_list:
        if i.x_fixed:
            i.x_reaction = round(lista_reactions[contador][0], 4)
            contador += 1
        if i.y_fixed:
            i.y_reaction = round(lista_reactions[contador][0], 4)
            contador += 1

    return point_list, element_list, load_list
