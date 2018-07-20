class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

    def __repr__(self):
        return 'Node({})'.format(self.label)

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        visited, stack = set(), [node]
        while stack:
            current = stack.pop()
            new_cur = UndirectedGraphNode(current.label)
            visited.add(current)
            for neighbor in current.neighbors:
                if neighbor not in visited:
                    stack.append(neighbor)
                    new_cur.neighbors.append(UndirectedGraphNode(neighbor.label))

        return new_cur

if __name__ == '__main__':
    s = Solution()
    node1 = UndirectedGraphNode(1)
    node4 = UndirectedGraphNode(4)
    node5 = UndirectedGraphNode(5)
    node6 = UndirectedGraphNode(6)
    node1.neighbors = [node4, node6, node5]
    node6.neighbors = [node1, node5]
    node5.neighbors = [node1, node6]
    node4.neighbors = [node1]
    new = s.cloneGraph(node1)
    print(new)