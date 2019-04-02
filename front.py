from anastruct import SystemElements
import numpy as np
from parca import pars
from calc import calc
from unparser import unpars
import sys

import argparse
parser = argparse.ArgumentParser(description='Solves a truss structure')
parser.add_argument('-m', type=str, default='gauss',
                    help='Resolution method as a string (gauss or jacobi)')
parser.add_argument('-ite', type=int, default='5000',
                    help='Number of iterations')
parser.add_argument('-file', type=str, default='entrada.txt',
                    help='Input file path')
args = parser.parse_args()

ss = SystemElements()
element_type = 'truss'


if __name__ == "__main__":
    point_list, element_list, load_list = pars(args.file)
    exagero = 10000

    for i in element_list:
        for j in point_list:
            if i.incidences_i == j.name:
                i.incidences_i = j
            elif i.incidences_f == j.name:
                i.incidences_f = j

    for i in element_list:
        inicial = i.incidences_i
        final = i.incidences_f
        ss.add_element(location=[[inicial.x, inicial.y], [final.x, final.y]])

    # for i in range(1, len(point_list)+1):
    #     j = i+1
    #     for j in range(len(point_list)+1):
    #         for element in element_list:
    #             inicial = element.incidences_i
    #             final = element.incidences_f
    #             if i == int(inicial.name) and j == int(final.name):
    #                 ss.add_element(location=[[inicial.x,inicial.y], [final.x, final.y]])

    for i in point_list:
        ponto = ss.find_node_id([i.x, i.y])
        if i.x_fixed == True and i.y_fixed == False:
            ss.add_support_roll(node_id=ponto, direction=1)
        elif i.x_fixed == False and i.y_fixed == True:
            ss.add_support_roll(node_id=ponto, direction=2)
        elif i.x_fixed == True and i.y_fixed == True:
            ss.add_support_fixed(node_id=ponto)

    for i in load_list:
        ponto = ss.find_node_id(
            [point_list[int(i.point)-1].x, point_list[int(i.point)-1].y])
        ss.point_load(node_id=ponto, Fx=int(
            i.intensity_x), Fy=int(i.intensity_y))

    ss.show_structure()
    ss.solve()
    ss.show_displacement()
    # point_list, element_list, load_list = calc(point_list, element_list, load_list)

    point_list, element_list, load_list = calc(
        point_list, element_list, load_list, args.m, args.ite)

    for i in element_list:
        inicial_x = float(i.incidences_i.x) + \
            i.incidences_i.x_displacement * exagero
        inicial_y = float(i.incidences_i.y) + \
            i.incidences_i.y_displacement * exagero
        final_x = float(i.incidences_f.x) + \
            i.incidences_f.x_displacement * exagero
        final_y = float(i.incidences_f.y) + \
            i.incidences_f.y_displacement * exagero
        ss.add_element(location=[[inicial_x, inicial_y], [final_x, final_y]])

    ss.show_structure()

    unpars(point_list, element_list)
