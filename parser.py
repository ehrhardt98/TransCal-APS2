from classes import Point
from classes import Element
from classes import Load


with open("entrada.txt", 'r') as entrada:
    all_lines = entrada.readlines()

# Remove \n e elementos vazios
l = []
for e in all_lines:
    a = e[:-1]
    if a != "":
        l.append(a)

# Divide por "topico"
ll = []
temp = 0
for i in range(len(l)):
    if l[i][0] == "*" and (temp != 0 or i != 0):
        ll.append(l[temp:i])
        temp = i
ll.append(l[temp:i])

# Separa os "topicos" da lista de "topicos"
coordinates = ll[0]
del coordinates[0]
element_groups = ll[1]
del element_groups[0]
incidences = ll[2]
del incidences[0]
materials = ll[3]
del materials[0]
geometric_properties = ll[4]
del geometric_properties[0]
bcnodes = ll[5]
del bcnodes[0]
loads = ll[6]
del loads[0]

# Split nos itens dos "topicos"
for e in range(len(coordinates)):
    coordinates[e] = coordinates[e].split()
for e in range(len(element_groups)):
    element_groups[e] = element_groups[e].split()
for e in range(len(incidences)):
    incidences[e] = incidences[e].split()
for e in range(len(materials)):
    materials[e] = materials[e].split()
for e in range(len(geometric_properties)):
    geometric_properties[e] = geometric_properties[e].split()
for e in range(len(bcnodes)):
    bcnodes[e] = bcnodes[e].split()
for e in range(len(loads)):
    loads[e] = loads[e].split()

# Cria os pontos e guarda em point_list
point_list = []
for i in range(int(coordinates[0][0])):
    name = coordinates[i+1][0] #name
    x = coordinates[i+1][1] #x
    y = coordinates[i+1][2] #y
    point_list.append(Point(name, x, y))

element_list = []
for i in range(int(element_groups[0][0])):
    name = element_groups[i+1][0] #name
    mtype = element_groups[i+1][2] #mtype
    element_list.append(Element(name, mtype))

for i in range(len(incidences)):
    for e in element_list:
        if incidences[i][0] == e.name:
            e.incidences_i = incidences[i][1]
            e.incidences_f = incidences[i][2]

for e in element_list:
    print(e.incidences_i)
    print(e.incidences_f)
    print("")

print(materials)