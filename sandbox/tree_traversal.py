from Trees import *

def visit(root):
    print(root)

def inorder_r(root):
    if root:
        inorder_r(root.left)
        visit(root)
        inorder_r(root.right)

def preorder_r(root):
    if root:
        visit(root)
        preorder_r(root.left)
        preorder_r(root.right)

def postorder_r(root):
    if root:
        postorder_r(root.left)
        postorder_r(root.right)
        visit(root)

def preorder_i(root):
    ret = []
    stack = [root]
    while stack:
        node = stack.pop()
        ret.append(node.val)
        if node.right: stack.append(node.right)
        if node.left: stack.append(node.left)
    return ret

def inorder_i(root):
    node = root
    s = []
    done = False
    while not done:
        if node:
            s.append(node)
            node = node.left
        else:
            if s:
                node = s.pop()
                visit(node)
                node = node.right
            else:
                done = True

def postorder_i(root):
    pass

if __name__ == '__main__':
    tree = deserialize('[25,11,33,6,20,29,39,2,9,12,22,null,null,35,43,null,null,null,null,null,19]')
    # drawtree(tree)
    # print('tree is' + (' ' if is_bst(tree) else ' not ') + 'a BST')
    t = preorder_i(tree)
    print(t)