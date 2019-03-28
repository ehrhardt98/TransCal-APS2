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
v_carregamento = np.array(v_carregamento)
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
v_deslocamento = np.array(v_deslocamento)
print(v_deslocamento)

matrixContorno, v_carregamento_contorno = contornoMaker(superMatrix, v_deslocamento, v_carregamento)
print(matrixContorno)
print(v_carregamento_contorno)

