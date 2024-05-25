class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    @staticmethod
    def insert_after(prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def get_middle(self) -> Node:
        v = []
        current = self.head
        while current:
            v.append(current)
            current = current.next
        return v[len(v) // 2]


def merge_sort(linked_list: LinkedList):
    if linked_list.head is None:
        return linked_list
    if linked_list.head.next is None:
        return linked_list
    left = LinkedList()
    right = LinkedList()
    middle = linked_list.get_middle()

    current = linked_list.head
    append_to_left = True
    while current:
        if current == middle:
            append_to_left = False
        if append_to_left:
            left.insert_at_end(current.data)
        else:
            right.insert_at_end(current.data)
        current = current.next

    return merge(merge_sort(left), merge_sort(right))


def merge(left: LinkedList, right: LinkedList):
    merged = LinkedList()

    left_current = left.head
    right_current = right.head

    while left_current and right_current:
        if left_current.data <= right_current.data:
            merged.insert_at_end(left_current.data)
            left_current = left_current.next
        else:
            merged.insert_at_end(right_current.data)
            right_current = right_current.next

    while left_current:
        merged.insert_at_end(left_current.data)
        left_current = left_current.next

    while right_current:
        merged.insert_at_end(right_current.data)
        right_current = right_current.next

    return merged


def main1():
    llist = LinkedList()

    # Вставляємо вузли в початок
    llist.insert_at_beginning(5)
    llist.insert_at_beginning(10)
    llist.insert_at_beginning(15)

    # Вставляємо вузли в кінець
    llist.insert_at_end(20)
    llist.insert_at_end(25)

    # Друк зв'язного списку
    print("Зв'язний список:")
    llist.print_list()

    llist.reverse()
    print("Зв'язний список зворотній:")
    llist.print_list()
    print("Відсортований список:")
    merge_sort(llist).print_list()
