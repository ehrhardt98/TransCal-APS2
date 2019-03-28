import math
import numpy as np
from classes import Point
from classes import Element
from classes import Load
from classes import Rigidez


def calcSenCos(lista_elementos,lista_pontos):
    for i in lista_elementos:
        for j in lista_pontos:
            if i.incidences_i == j.name:
                i.incidences_i = j
            elif i.incidences_f == j.name:
                i.incidences_f = j
    
    for i in lista_elementos:
        x_total = float(i.incidences_f.x)-float(i.incidences_i.x)
        y_total = float(i.incidences_f.y)-float(i.incidences_i.y)
        if x_total == 0:
            i.comprimento = y_total
        elif y_total == 0:
            i.comprimento = x_total
        else:
            i.comprimento = math.sqrt(math.pow(x_total,2) + math.pow(y_total,2))
        angle = math.atan2(y_total,x_total)
        i.cos = round(math.cos(angle),4)
        i.sen = round(math.sin(angle),4)
    return lista_elementos,lista_pontos

def matrixMaker(elemento):
    matrix_teste = [[1,2,-1,-2],[2,3,-2,-3],[-1,-2,1,2],[-2,-3,2,3]]
    matrix_resposta = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    vetor_gdl = [elemento.incidences_i.gdl[0], elemento.incidences_i.gdl[1], elemento.incidences_f.gdl[0], elemento.incidences_f.gdl[1]]
    multiplier = float(elemento.elast) * float(elemento.area) / elemento.comprimento
    for i in range(0,4):
        for j in range(0,4):
            matrix_resposta[i][j] = Rigidez()
            matrix_resposta[i][j].gdl[0] = vetor_gdl[i]
            matrix_resposta[i][j].gdl[1] = vetor_gdl[j]

            if abs(matrix_teste[i][j]) == 1:
                matrix_resposta[i][j].value = math.pow(elemento.cos,2) * multiplier
            elif abs(matrix_teste[i][j]) == 2:
                matrix_resposta[i][j].value = elemento.cos * elemento.sen * multiplier
            elif abs(matrix_teste[i][j]) == 3:
                matrix_resposta[i][j].value = math.pow(elemento.sen,2) * multiplier
            if matrix_teste[i][j]<0:
                matrix_resposta[i][j].value *= -1
    return matrix_resposta

def superMatrixMaker(lista_matrizes, n_nodes):
    size = n_nodes*2
    superMatrix = []
    for i in range(0,size):
        linha = []
        for j in range(0,size):
            linha.append(0)
        superMatrix.append(linha)
    for matriz in lista_matrizes:
        for i in matriz:
            for j in i:
                gdl = j.gdl
                superMatrix[gdl[0]-1][gdl[1]-1] += round(j.value,4)
    #print(np.array(superMatrix))
    return np.array(superMatrix)

def contornoMaker(superMatrix, vetorDisplace, vetorLoad):
    matrizContorno = []
    vetorLoadContorno = []
    for i in range(0,len(superMatrix)):
        linha = []
        if vetorDisplace[i][0] !=0:
            vetorLoadContorno.append(vetorLoad[i])
        for j in range(0,len(superMatrix)):
            if (vetorDisplace[j][0] != 0) & (vetorDisplace[i][0] != 0):
                linha.append(superMatrix[i][j])
        if vetorDisplace[i][0] != 0:
            matrizContorno.append(linha)
    return np.array(matrizContorno), np.array(vetorLoadContorno)

def strain_stressMaker(lista_elementos):
    lista_tensao = []
    lista_deformacao = []
    for i in lista_elementos:
        vetor_deslocamento = []
        vetor_deslocamento.append(i.incidence_i.x_displacement)
        vetor_deslocamento.append(i.incidence_i.y_displacement)
        vetor_deslocamento.append(i.incidence_f.x_displacement)
        vetor_deslocamento.append(i.incidence_f.y_displacement)
        vetor_angle = [-i.cos, -i.sen, i.cos, i.sen]
        somatoria = 0
        for i in range(0,4):
            somatoria += vetor_angle[i] * vetor_deslocamento[i]
        tensao = somatoria /i.comprimento
        deformacao = somatoria * i.elast / i.comprimento
        lista_tensao.append(tensao)
        lista_deformacao.append(deformacao)
    return lista_tensao, lista_deformacao
    


            



