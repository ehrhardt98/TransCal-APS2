import math
import numpy as np
from classes import Point
from classes import Element
from classes import Load
from classes import Rigidez
from parser import pars
from Functions import calcSenCos
from Functions import matrixMaker
from Functions import superMatrixMaker
from Functions import contornoMaker
from Functions import strain_stressMaker
from Functions import reactionsMaker
from gauss import gauss

# Arquivo de entrada
arquivo = "entrada.txt"

point_list, element_list, load_list = pars(arquivo)

element_list, point_list = calcSenCos(element_list, point_list)
matrix_list = []
for i in element_list:
    matrix_list.append(matrixMaker(i))
superMatrix = superMatrixMaker(matrix_list, len(point_list))

v_carregamento = []
for e in load_list:
    for i in range(len(point_list)):
        if point_list[i].name == e.point:
            temp = [int(e.intensity_x)]
            v_carregamento.append(temp)
            temp = [int(e.intensity_y)]
            v_carregamento.append(temp)
            continue
        temp = [0]
        v_carregamento.append(temp)
        temp = [0]
        v_carregamento.append(temp)
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
for i in range(0,len(v_deslocamento)):
    if v_deslocamento[i][0] == 0:
        v_carregamento[i][0] = -0.001
matrixContorno, v_carregamento_contorno = contornoMaker(superMatrix, v_deslocamento, v_carregamento)

v_deslocamento_metodo = gauss(5000, 0.0001, matrixContorno, v_carregamento_contorno)
contador = 0

for i in range(0,len(v_deslocamento)):
    if v_deslocamento[i][0] != 0:
        v_deslocamento[i][0] = v_deslocamento_metodo[contador]
        contador += 1
contador = 0
for i in point_list:
    i.x_displacement = v_deslocamento[contador]
    contador+=1
    i.y_displacement = v_deslocamento[contador]
    contador+=1
lista_tensao, lista_deformacao = strain_stressMaker(element_list)

contador = 0
for i in element_list:
    i.strain = lista_tensao[contador]
    i.stress = lista_deformacao[contador]

lista_reactions, v_carregamento = reactionsMaker(superMatrix, v_deslocamento, v_carregamento)

contador = 0
for i in point_list:
    if i.x_fixed:
        i.x_reaction = round(lista_reactions[contador][0],4)
        contador +=1
    if i.y_fixed:
        i.y_reaction = round(lista_reactions[contador][0],4)
        contador +=1

