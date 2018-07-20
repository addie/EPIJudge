import collections
class BSTNode:
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right

class TreeNode:
    def __init__(self, label=None, edges=None):
        self.label = label
        self.edges = edges

def is_bst(tree, min_val=float('-inf'), max_val=float('inf')):
    if not tree:
        return True
    elif not min_val <= tree.data <= max_val:
        return False
    return is_bst(tree.left, min_val, tree.data) and is_bst(tree.right, tree.data, max_val)


def find_k_largest_elements(tree, k):
    def find_k_largest_elements_helper(tree):
        if tree and len(k_largest) < k:
            find_k_largest_elements_helper(tree.right)
            if len(k_largest) < k:
                k_largest.append(tree.data)
                find_k_largest_elements_helper(tree.left)

    k_largest = []
    find_k_largest_elements_helper(tree)
    return k_largest


def lca_recursive(tree, s, b):
    if s.data == tree.data or b.data == tree.data:
        return tree.data
    if s.data < tree.data < b.data:
        return tree.data
    if s.data < tree.data and b.data < tree.data:
        return lca_recursive(tree.left, s, b)
    if s.data > tree.data and b.data > tree.data:
        return lca_recursive(tree.right, s, b)

def lca_iterative(tree, s, b):
    while tree.data < s.data or tree.data > b.data:
        while tree.data < s.data:
            tree = tree.right
        while tree.data > b.data:
            tree = tree.left

    return tree.data

def lca_postorder(tree, s, b):
    pass

class Edge:
    def __init__(self, root=None, length=None):
        self.root = root
        self.length = length

def diameter(tree):
    class HeightAndDiameter:
        def __init__(self, height=None, diameter=None):
            self.height = height
            self.diameter = diameter

    def compute(t):
        diameter = float('-inf')
        heights = [0.0, 0.0]
        for e in t.edges:
            h_d = compute(e.root)
            if h_d.height + e.length > heights[0]:
                heights = [h_d.height + e.length, heights[0]]
            elif h_d.height + e.length > heights[1]:
                heights[1] = h_d.height + e.length
            diameter = max(diameter, h_d.diameter)

        return HeightAndDiameter(heights[0], max(diameter, heights[0], + heights[1]))

    return compute(tree).diameter if tree else 0

def invertTree(root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if not root or not root.left and not root.right:
        return root

    stack = [root]
    while stack:
        node = stack.pop()
        node.left, node.right = node.right, node.left
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return root

def create_bstree():
    n = BSTNode(19)
    n.left = BSTNode(7)
    n.left.left = BSTNode(3)
    n.left.left.left = BSTNode(2)
    n.left.left.right = BSTNode(5)
    n.left.right = BSTNode(11)
    n.left.right.right = BSTNode(17)
    n.left.right.right.left = BSTNode(13)
    n.right = BSTNode(43)
    n.right.left = BSTNode(23)
    n.right.left.right = BSTNode(37)
    n.right.left.right.left = BSTNode(29)
    n.right.left.right.left.right = BSTNode(31)
    n.right.left.right.right = BSTNode(41)
    n.right.right = BSTNode(47)
    n.right.right.right = BSTNode(53)
    return n
def create_btree():
    tb = TreeNode('B')
    tb.edges = [Edge(tb, 7),Edge(tb, 14),Edge(tb, 73)]
    tc = TreeNode('C')
    return tb

if __name__ == '__main__':
    bstree = create_bstree()
    btree = create_btree
    #print is_bst(tree)
    #print find_k_largest_elements(tree, 3)
    #smaller = tree.left.right.right.left
    #larger = tree.left.right.right
    #print lca_iterative(tree, smaller, larger)
    #print lca_recursive(tree, smaller, larger)
    #print diameter(tree)

    tree = invertTree(bstree)
    print tree.data, tree.left.data, tree.right.data
