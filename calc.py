from classes import Point
from classes import Element
from classes import Load
from pars import pars
import numpy as np

# Arquivo de entrada
arquivo = "entrada.txt"

point_list, element_list, load_list = pars(arquivo)

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
print(v_carregamento)