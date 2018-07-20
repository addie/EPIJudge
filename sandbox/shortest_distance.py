from collections import deque


class Graph:
    def __init__(self, n):
        self.size = n
        self.__graph_dict = {}
        for i in range(n):
            self.add_vertex(i)

    def add_vertex(self, vertex):
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def connect(self, vertex1, vertex2):
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]
        if vertex2 in self.__graph_dict:
            self.__graph_dict[vertex2].append(vertex1)
        else:
            self.__graph_dict[vertex2] = [vertex1]

    def find_all_distances(self, start):
        distances = self.__bfs(start)
        for node in self.__graph_dict:
            if node != start:
                print(distances[node], end=" ")

    def __bfs(self, start):
        q = deque()
        q.append(start)
        distances = [-1] * self.size
        distances[start] = 0
        while q:
            node = q.popleft()
            for neighbor in self.__graph_dict[node]:
                if distances[neighbor] < 0:
                    distances[neighbor] = distances[node] + 6
                    q.append(neighbor)
        return distances

if __name__ == '__main__':

    a = [(4, 2), (3, 1)]
    b = [[(1, 2), (1,3)], [(2, 3)]]
    c = [1, 2]

    for i in range(len(c)):
        n, m = a[i]
        graph = Graph(n)
        for j in range(len(b[i])):
            x, y = b[i][j]
            graph.connect(x - 1, y - 1)
        s = c[i]
        graph.find_all_distances(s - 1)
        print()


