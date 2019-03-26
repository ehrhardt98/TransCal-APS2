import math
import numpy

def calcSenCos(lista_elementos,lista_pontos):
    for i in lista_elementos:
        for j in lista_pontos:
            if int(i.incidences_i) == j.name:
                i.incidences_i = j
            elif int(i.incidences_f) == j.name:
                i.incidences_f = j
    for i in lista_elementos:
        x_total = i.incidences_f.x-i.incidences_i.x
        y_total = i.incidences_f.y-i.incidences_i.y
        angle = math.atan2(y_total,x_total)
        i.cos = math.cos(angle)
        i.sen = math.sin(angle)

def matrixMaker(elemento):
    matrix_teste = np.array([[1,2,-1,-2],[2,3,-2,-3],[-1,-2,1,2],[-2.-3,2,3]])
    matrix_resposta = np.zeros(4,4)
    for i in range(0,4):
        for j in range(0,4):
            if matrix_teste[i][j] == 1:
                matrix_resposta[i][j] = math.pow(elemento.cos,2)
            elif matrix_teste[i][j] == 2:
                matrix_resposta[i][j] = elemento.cos * elemento.sen
            elif matrix_teste[i][j] == 3:
                matrix_resposta[i][j] = math.pow(elemento.sen,2)
            if matrix_teste[i][j]<0:
                matrix_resposta[i][j] *= -1
    return matrix_resposta

def superMatrixMaker(lista_matrizes, n_nodes):
    size = n_nodes*2
    superMatrix = np.zeros(size,size)
    for matriz in lista_matrizes:
        for i in range(0,size):
            for j in range(0,size):
                gbl = matriz[i][j].gbl
                superMatrix[gbl[0]][gbl[1]] += matriz[i][j]
    return superMatrix


            



