from Trees import deserialize
from Trees import drawtree
import collections

class Solution1:
    def findClosestLeaf(self, root, k):
        graph = collections.defaultdict(list)
        def dfs(node, par = None):
            if node:
                graph[node].append(par)
                graph[par].append(node)
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)
        queue = collections.deque(node for node in graph
                                  if node and node.val == k)
        seen = set(queue)

        while queue:
            node = queue.popleft()
            if node:
                if len(graph[node]) <= 1:
                    return node.val
                for nei in graph[node]:
                    if nei not in seen:
                        seen.add(nei)
                        queue.append(nei)

class Solution2:
    def findClosestLeaf(self, root, k):
        memo = {}

        def closest_leaf(root):
            if root not in memo:
                if not root:
                    ans = float('inf'), None
                elif not root.left and not root.right:
                    ans = 0, root
                else:
                    d1, leaf1 = closest_leaf(root.left)
                    d2, leaf2 = closest_leaf(root.right)
                    ans = min(d1, d2) + 1, leaf1 if d1 < d2 else leaf2
                memo[root] = ans
            return memo[root]

        # Search for node.val == k
        path = []

        def dfs(node):
            if not node:
                return
            if node.val == k:
                path.append(node)
                return True
            path.append(node)
            ans1 = dfs(node.left)
            if ans1: return True
            ans2 = dfs(node.right)
            if ans2: return True
            path.pop()

        dfs(root)
        dist, leaf = float('inf'), None
        for i, node in enumerate(path):
            d0, leaf0 = closest_leaf(node)
            d0 += len(path) - 1 - i
            if d0 < dist:
                dist = d0
                leaf = leaf0

        return leaf.val


if __name__ == '__main__':
    t = deserialize('[2,1,3,0,7,9,4,5,null,33,10,null,null,6,8,null,null,null,null,17]')
    s1,s2 = Solution1(), Solution2()
    n = s1.findClosestLeaf(t, 7)
    print(n)
    n = s2.findClosestLeaf(t, 7)
    print(n)