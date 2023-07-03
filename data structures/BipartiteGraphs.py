from Graph import Graph
from Queue import Queue


class BipartiteGraph(Graph):
    def __init__(self, vertices, edges):
        super().__init__(vertices, edges)
        graph = Graph(vertices, edges)
        self.vertices = graph.vertices
        self.edges = graph.edges

    def get_two_color(self) -> list:
        queue = Queue()
        queue.enqueue(self.vertices[0])
        colors = ["Uncolored"] * len(self.vertices)
        processed = [False] * len(self.vertices)

        while queue.size != 0:
            vertex = queue.dequeue()
            colors[vertex] = "White" if colors[vertex] == "Uncolored" else colors[vertex]

            current = self.adjacency_list[vertex].head
            while current is not None:
                if not processed[current.data]:
                    queue.enqueue(current.data)
                    colors[current.data] = "Black" if colors[vertex] == "White" else "White"
                current = current.next
            processed[vertex] = True
        return colors
