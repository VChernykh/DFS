"""
    Depth First Search
    start - НАЧАЛЬНАЯ ТОЧКА (кортеж): start = {'a': ('b','c')}
    peaks - СЛОВАРЬ ТОЧЕК (словарь кортежей): peaks = {'a':('b','c'), 'b':(), 'c':()}. peak - элемент словаря (кортеж)
    done - СПИСОК ПОСЕЩЕННЫХ ТОЧЕК (список)
    point - ЭЛЕМЕНТЫ peak, вершины соединенные с peak
"""


def DFS(start, peaks, done):
    for peak, point in start.items():
        
        if peak not in done:
            yield peak, point
            done.append(peak)
            for i in point:
                
                new_point={ i : peaks[i]}
                
                for point in DFS(new_point, peaks, done):
                    
                    if point not in done:
                        yield done
