import heapq


class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, task, priority):
        heapq.heappush(self.queue, (-priority, task))

    def dequeue(self):
        return heapq.heappop(self.queue)[1]

    def is_empty(self):
        return not bool(self.queue)


class Cable:
    def __init__(self, size: int, name: str):
        self.size = size
        self.name = name

    def _compare(self, other, method):
        try:
            return method(self.size, other.size)
        except (AttributeError, TypeError):
            return NotImplemented

    def __lt__(self, other):
        return self._compare(other, lambda s, o: s < o)

    def __le__(self, other):
        return self._compare(other, lambda s, o: s <= o)

    def __eq__(self, other):
        return self._compare(other, lambda s, o: s == o)

    def __ge__(self, other):
        return self._compare(other, lambda s, o: s >= o)

    def __gt__(self, other):
        return self._compare(other, lambda s, o: s > o)

    def __ne__(self, other):
        return self._compare(other, lambda s, o: s != o)


def main():
    cable_list = list(map(lambda x: Cable(x, str(x)), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    heapq.heapify(cable_list)
    while len(cable_list) > 2:
        cable1 = heapq.heappop(cable_list)
        cable2 = heapq.heappop(cable_list)
        print(f"Connecting {cable1.name} and {cable2.name}")
        new_cable = Cable(cable1.size + cable2.size, f"({cable1.name}x{cable2.name})")
        heapq.heappush(cable_list, new_cable)
    print(f"Result = {cable_list[0].name}x{cable_list[1].name}")


if __name__ == '__main__':
    main()
