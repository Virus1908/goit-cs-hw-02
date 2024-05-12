import matplotlib.pyplot as plt
import networkx as nx

from collections import deque


def bfs_iterative(graph, start):
    # Ініціалізація порожньої множини для зберігання відвіданих вершин
    visited = set()
    # Ініціалізація черги з початковою вершиною
    queue = deque([start])

    while queue:  # Поки черга не порожня, продовжуємо обхід
        # Вилучаємо першу вершину з черги
        vertex = queue.popleft()
        # Перевіряємо, чи була вершина відвідана раніше
        if vertex not in visited:
            # Якщо не була відвідана, друкуємо її
            print(vertex, end=" ")
            # Додаємо вершину до множини відвіданих вершин
            visited.add(vertex)
            # Додаємо всіх невідвіданих сусідів вершини до кінця черги
            # Операція різниці множин вилучає вже відвідані вершини зі списку сусідів
            queue.extend(set(graph[vertex].keys()) - visited)
    # Повертаємо множину відвіданих вершин після завершення обходу
    return visited


def dfs_iterative(graph, start_vertex):
    visited = set()
    stack = [start_vertex]
    while stack:
        # Вилучаємо вершину зі стеку
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex, end=' ')
            # Відвідуємо вершину
            visited.add(vertex)
            # Додаємо сусідні вершини до стеку
            stack.extend(reversed(list(graph[vertex].keys())))


def dijkstra(graph, start):
    # Ініціалізація відстаней та множини невідвіданих вершин
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.nodes())

    while unvisited:
        # Знаходження вершини з найменшою відстанню серед невідвіданих
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        # Якщо поточна відстань є нескінченністю, то ми завершили роботу
        if distances[current_vertex] == float('infinity'):
            break

        for neighbor in graph[current_vertex].keys():
            # даний граф не зважений, тому вага завжди одиниця
            weight = 1
            distance = distances[current_vertex] + weight

            # Якщо нова відстань коротша, то оновлюємо найкоротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        # Видаляємо поточну вершину з множини невідвіданих
        unvisited.remove(current_vertex)

    return distances


def main():
    # за приклад беремо готовий граф соціальної мережі
    # noinspection PyPep8Naming
    G = nx.krackhardt_kite_graph()
    print("dfs")
    dfs_iterative(G, 1)
    print("\nbfs")
    bfs_iterative(G, 1)
    print("")
    for node in G.nodes():
        print(f"{node} - {dijkstra(G, node)}")
    num_nodes = G.number_of_nodes()
    num_edges = G.number_of_edges()
    is_connected = nx.is_connected(G)
    print(num_nodes)
    print(num_edges)
    print(is_connected)
    print("Betweenness")
    b = nx.betweenness_centrality(G)
    print(b)
    print("Degree centrality")
    d = nx.degree_centrality(G)
    print(d)
    print("Closeness centrality")
    c = nx.closeness_centrality(G)
    print(c)
    nx.draw(G, with_labels=True)
    plt.show()


if __name__ == '__main__':
    main()
