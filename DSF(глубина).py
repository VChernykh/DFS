#Depth First Search
visited = []           #список посещенных вершин
matrix = [[0,1,1,0,0], #матрица смежности, задающая граф
          [1,0,0,1,0],
          [1,0,0,0,0],
          [0,1,0,0,1],
          [0,0,0,1,0]] 
"""
    Данный граф выглядит так:

                    1
                   / \
                  2   3
                 / 
                4   
               /
              5 
"""

def DFS(top):
    visited.append(top)
    print(top)         #вывод порядка обхода вершин 
    for i in range(1, len(matrix) + 1):
        if (i not in visited) and (matrix[top - 1][i - 1] == 1):
            DFS(i)
