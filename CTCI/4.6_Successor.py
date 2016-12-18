"""
Find the next node(in-order successor) of a given node in a BST(with a link to parent)
==> the leftmost children of the right child
==> if no right child, return the parent
"""
from util import TreeNodeWithParents


def find_successor(root, v):
    if not root:
        return None

    # find the node first
    node = root.find_node(v)
    if not node:
        return None

    if not node.right:
        if node.parent.left == node:
            return node.parent
        else:
            # go up until the node is on the left branch instead of right
            cur = node.parent
            while cur and cur.right == node:
                node = cur
                cur = cur.parent
            return cur

    def find_leftmost_child(root):
        cur = root
        while cur and cur.left:
            cur = cur.left
        return cur

    return find_leftmost_child(node.right)

def main():
    preorder = [20, 10, 5, 1, 7, 15, 16, 30, 25, 35, 32, 40]
    root = TreeNodeWithParents.construct_BST(preorder)
    root.print_tree()
    print('7->', find_successor(root, 7))
    print('16->', find_successor(root, 16))
    print('40->', find_successor(root, 40))
    print('-----------------')
    preorder = [20, 10, 5, 1, 7, 15, 30]
    root = TreeNodeWithParents.construct_BST(preorder)
    root.print_tree()
    print('10->', find_successor(root, 10))
    print('15->', find_successor(root, 15))
    print('-----------------')


if __name__ == '__main__':
    main()
