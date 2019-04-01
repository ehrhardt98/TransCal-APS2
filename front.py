from anastruct import SystemElements
import numpy as np
from parca import pars
from calc import calc
from unparser import unpars

# ss = SystemElements()
# element_type = 'truss'
# ss.add_element(location=[[0,0],[3,4]])
# ss.add_element(location=[[3,4],[8,4]])

# ss.add_support_hinged(node_id=1)
# ss.add_support_fixed(node_id=3)

# ss.q_load(element_id=2, q=-10)

# ss.show_structure()

if __name__ == "__main__":
    point_list, element_list, load_list = pars("entrada.txt")
    print(point_list)
    point_list, element_list, load_list = calc(point_list, element_list, load_list)
    unpars(point_list, element_list)