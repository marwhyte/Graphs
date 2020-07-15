from util import Stack, Queue


class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()

    def add_edge(self, v1, v2):
        self.vertices[v1].add(v2)


def earliest_ancestor(ancestors, starting_node):
    # Build the graph
    graph = Graph()
    # child should have edge to parent - child points to parent
    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
        graph.add_edge(pair[1], pair[0])
    # to find longest
    earliestAncestor = -1
    maxLength = 1

    # bft or dft
    q = Queue()
    q.enqueue([starting_node])
    while q.size() > 0:
        path = q.dequeue()
        vertex = path[-1]
        # if path is longer or path is same length and node is smaller.
        if (len(path) >= maxLength and earliestAncestor != -1) or (len(path) > maxLength):
            earliestAncestor = vertex
            maxLength = len(path)
        for neighbor in graph.vertices[vertex]:
            path_copy = list(path)
            path_copy.append(neighbor)
            q.enqueue(path_copy)
    # return the earliest ancestor
    return earliestAncestor


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

earliest_ancestor(test_ancestors, 2)
