import heapq


class Heap:
    def __init__(self):
        self.queue = []

    def enqueue(self, vertex, priority):
        heapq.heappush(self.queue, (priority, vertex))

    def dequeue(self):
        return heapq.heappop(self.queue)

    def is_empty(self):
        return not bool(self.queue)


def dijkstra(graph, start):
    distances = {start: 0}
    vertexes_to_process = Heap()
    vertexes_to_process.enqueue(start, 0)

    while not vertexes_to_process.is_empty():
        distance_to_current_vertex, current_vertex = vertexes_to_process.dequeue()

        if current_vertex in distances and distances[current_vertex] < distance_to_current_vertex:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = distance_to_current_vertex + weight

            if neighbor not in distances:
                distances[neighbor] = distance
                vertexes_to_process.enqueue(neighbor, distance)
            elif distances[neighbor] > distance:
                distances[neighbor] = distance
                vertexes_to_process.enqueue(neighbor, distance)

    return distances


def main3():
    # Приклад графа у вигляді словника
    graph = {
        'A': {'B': 5, 'C': 10},
        'B': {'A': 5, 'D': 3},
        'C': {'A': 10, 'D': 2},
        'D': {'B': 3, 'C': 2, 'E': 4},
        'E': {'D': 4}
    }

    # Виклик функції для вершини A
    print(dijkstra(graph, 'A'))
