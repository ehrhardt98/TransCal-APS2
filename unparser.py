import numpy as np
from classes import Point, Element, Load, Rigidez
from parca import pars
from calc import calc

def unpars(point_list, element_list):

    reaction_list = []
    stress_list = []

    saida = open("saida.txt", "w")
    saida.write("*DISPLACEMENTS")

    for i in range(len(point_list)):
        point = point_list[i]
        if point.x_reaction != 0:
            reaction_list.append("\n" + point.name + " FX " + str(point.x_reaction))
        if point.y_reaction != 0:
            reaction_list.append("\n" + point.name + " FY " + str(point.y_reaction))
            print(type(point.x_displacement))
        text = "\n" + point.name + " " + str(point.x_displacement) + " " + str(point.y_displacement)
        saida.write(text)

    saida.write("\n\n*REACTION_FORCES")

    for j in range(len(reaction_list)):
        saida.write(reaction_list[j])

    saida.write("\n\n*ELEMENT_STRAINS")

    for k in range(len(element_list)):
        element = element_list[k]
        stress_list.append("\n" + element.name + " " + str(element.stress))
        text = "\n" + element.name + " " + str(element.strain)
        saida.write(text)

    saida.write("\n\n*ELEMENT_STRESS")

    for l in range(len(stress_list)):
        saida.write(stress_list[l])

    saida.close()