import networkx
import matplotlib.pyplot as plt

def input_edges_list():
    """считывает список рёбер в форме:
    в первой строке N - число рёбер,
    затем следует N строк из двух слов и одного числа
    слова - названия вершин, концы ребра, а число - его вес
    
    return граф в форме словаря рёбер и соответствующих им весов
    """
    N = int(input('Введите количество рёбер:'))
    G = {}
    for i in range(N):
        vertex1, vertex2, weight = input().split()
        weight = float(weight)
        G[(vertex1, vertex2)] = weight
    return G
    
def edges_list_to_adjacency_list(E):
    """E - граф в форме словаря рёбер и соответствующих им весов
    return граф в форме словаря словарей смежности с весами
    """
    G = {}
    for vertex1, vertex2 in E:
        weight = E[(vertex1, vertex2)]
        # добавляю ребро (vertex1, vertex2)
        if vertex1 not in G:
            G[vertex1] = {vertex2:weight}
        else:  # значит такая вершина уже встречалась
            G[vertex1][vertex2] = weight
        # граф не направленный, поэтому добавляю ребро (vertex2, vertex1)
        if vertex2 not in G:
            G[vertex2] = {vertex1:weight}
        else:  # значит такая вершина уже встречалась
            G[vertex2][vertex1] = weight
    return G


def dfs(G, start, called = set(), skelet = set()):
    called.add(start)
    for neighbour in G[start]:
        if neighbour not in called:
            dfs(G, neighbour, called, skelet)
            skelet.add((start, neighbour))



s = """A B 1
B D 1
B C 2
C A 2
C D 3
D E 5""".split('\n')
E = {}
for line in s:
    a, b, weight = line.split()
    E[(a, b)] = int(weight)

A = edges_list_to_adjacency_list(E)

called = set()
skelet = set()
dfs(A, 'A', called, skelet)
print(called)
print(skelet)

G = networkx.Graph(A)
position = networkx.spring_layout(G) # positions for all nodes
networkx.draw(G, position)
networkx.draw_networkx_labels(G, position)
networkx.draw_networkx_edge_labels(G, position, edge_labels=E)
# нарисуем остовное дерево:
networkx.draw_networkx_edges(G, position, edgelist=skelet,
                             width=5, alpha=0.5, edge_color='red')

plt.show() # display
