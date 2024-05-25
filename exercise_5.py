import uuid

import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="#1296F0"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def draw_tree_breadth(tree_root: Node):
    order = 1
    new_root = Node(tree_root.val, to_color(order))
    active_level = []
    order = visit_node_breadth(active_level, new_root, order, tree_root)
    while True:
        next_level = []
        for original_node, new_node in active_level:
            order = visit_node_breadth(next_level, new_node, order, original_node)
        if len(next_level) == 0:
            break
        else:
            active_level = next_level

    draw_tree(new_root)


def visit_node_breadth(nodes_to_append, new_node, order, original_node) -> int:
    if original_node.left:
        order += 1
        new_node.left = Node(original_node.left.val, to_color(order))
        nodes_to_append.append((original_node.left, new_node.left))
    if original_node.right:
        order += 1
        new_node.right = Node(original_node.right.val, to_color(order))
        nodes_to_append.append((original_node.right, new_node.right))
    return order


def draw_tree_depth(tree_root: Node):
    order = 1
    new_root = Node(tree_root.val, to_color(order))
    visit_node_depth(new_root, tree_root, order)
    draw_tree(new_root)
    pass


def visit_node_depth(new_node, original_node, order) -> int:
    if original_node.left:
        order += 1
        new_node.left = Node(original_node.left.val, to_color(order))
        order = visit_node_depth(new_node.left, original_node.left, order)
    if original_node.right:
        order += 1
        new_node.right = Node(original_node.right.val, to_color(order))
        order = visit_node_depth(new_node.right, original_node.right, order)
    return order


def to_color(order: int) -> str:
    hex_str = hex((30 + order * 5) * (1 + 256 + 256 * 256) + 0x300000)[2:]
    return f"#" + hex_str.zfill(6)


def main5():
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.left.right = Node(99)
    root.left.right = Node(10)
    root.left.right.right = Node(10)
    root.left.right.right.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)
    root.right.left.left = Node(3)

    # draw_tree_breadth(root)
    draw_tree_depth(root)
