from util import TreeNode


def find_leftmost_child(root):
    while root and root.left:
        root = root.left
    return root


def find_successor_stupid_recursion(root, node):
    if root is None:
        return False, None

    if not root.left and not root.right and root.value == node:
        return True, None

    if root.right and root.value == node:
        suc = find_leftmost_child(root.right)
        return True, suc

    left, left_node = False, None
    right, right_node = False, None

    if root.value > node:
        left, left_node = find_successor_stupid_recursion(root.left, node)
    else:
        right, right_node = find_successor_stupid_recursion(root.right, node)

    if left and not left_node:
        return True, root

    if left:
        return left, left_node
    if right:
        return right, right_node
    return False, None


def find_successor(root, x):
    if not root:
        return
    parent = None
    while root:
        if root.value > x:
            parent = root
            root = root.left
        elif root.value < x:
            root = root.right
        else:
            if root.right:
                return find_leftmost_child(root.right)
            else:
                return parent
    return None


def main():
    root = TreeNode.construct_BST([20, 10, 5, 1, 7, 15, 30, 25, 35, 32, 40])
    print(find_successor_stupid_recursion(root, 40))
    print(find_successor(root, 40))


if __name__ == '__main__':
    main()