import math
import numpy as np
from classes import Point
from classes import Element
from classes import Load
from classes import Rigidez
from parser import pars
from functions import calcSenCos
from functions import matrixMaker
from functions import superMatrixMaker

# Arquivo de entrada
arquivo = "entrada.txt"

point_list, element_list, load_list = pars(arquivo)

element_list, point_list = calcSenCos(element_list, point_list)
matrix_list = []
for i in element_list:
    matrix_list.append(matrixMaker(i))
superMatrix = superMatrixMaker(matrix_list,3)

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
#print(v_carregamento)