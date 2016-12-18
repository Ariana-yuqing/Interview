"""
    Given a binary tree, create a linked list of all node at each depth.
    Use BFS: need a list to store all of the nodes at current depth
"""
from util import LinkedListNode, TreeNode


def create_linked_list_from_BT(root):
    if not root:
        return []

    result = []
    current = [root]

    while len(current) > 0:
        v_list = [c.value for c in current]
        cur_list = LinkedListNode.construct_linked_list(v_list)
        result.append(cur_list)
        temp = current
        current = []
        for node in temp:
            if node.left:
                current.append(node.left)
            if node.right:
                current.append(node.right)
    return result


def main():
    preorder = [20, 10, 5, 1, 7, 15, 30, 25, 35, 32, 40]
    root = TreeNode.construct_BST(preorder)
    root.print_tree()
    result = create_linked_list_from_BT(root)
    for r in result:
        r.print_linked_list()
    print('-----------------')
    preorder = [20, 10, 5, 1, 7, 15, 30]
    root = TreeNode.construct_BST(preorder)
    result = create_linked_list_from_BT(root)
    for r in result:
        r.print_linked_list()
    print('-----------------')
    postorder = [None, None, None, 3, 2, None, None, 6, None, 7, 5]
    root = TreeNode.construct_postorder(postorder)
    root.print_tree()
    result = create_linked_list_from_BT(root)
    for r in result:
        r.print_linked_list()


if __name__ == '__main__':
    main()
