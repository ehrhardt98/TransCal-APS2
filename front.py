from anastruct import SystemElements
import numpy as np
from parca import pars
from calc import calc
from unparser import unpars

ss = SystemElements()
element_type = 'truss'


if __name__ == "__main__":
    point_list, element_list, load_list = pars("entrada.txt")
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
        if inicial.x_fixed == True and inicial.y_fixed == False:
            ss.add_support_roll(node_id=int(i.name), direction=1)
        elif inicial.x_fixed == False and inicial.y_fixed == True:
            ss.add_support_roll(node_id=int(i.name), direction=2)
        elif inicial.x_fixed == True and inicial.y_fixed == True:
            ss.add_support_fixed(node_id=int(i.name))

    for i in load_list:
        ss.point_load(node_id=int(i.point), Fx=int(i.intensity_x), Fy=int(i.intensity_y))

    ss.show_structure()

    point_list, element_list, load_list = calc(point_list, element_list, load_list)

    for i in element_list:
        inicial_x = float(i.incidences_i.x) + i.incidences_i.x_displacement * exagero
        inicial_y = float(i.incidences_i.y) + i.incidences_i.y_displacement * exagero
        final_x = float(i.incidences_f.x) + i.incidences_f.x_displacement * exagero
        final_y = float(i.incidences_f.y) + i.incidences_f.y_displacement * exagero
        ss.add_element(location=[[inicial_x, inicial_y], [final_x, final_y]])

    ss.show_structure()

    unpars(point_list, element_list)