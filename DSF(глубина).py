#Depth First Search

y, x = [int(elem) for elem in input().split(' ')]              #чтение размеров матрицы смежности
matrix = [[int(j) for j in input().split()] for i in range(y)] #чтение матрицы смежности
visited = []           #список посещенных вершин

"""
matrix = [[0,1,1,0,0], #матрица смежности, задающая граф
          [1,0,0,1,0],
          [1,0,0,0,0],
          [0,1,0,0,1],
          [0,0,0,1,0]] 
"""

def DFS(top):
    visited.append(top)
    print(top)         #вывод порядка обхода вершин 
    for i in range(1, len(matrix) + 1):
        if (i not in visited) and (matrix[top - 1][i - 1] == 1):
            DFS(i)
