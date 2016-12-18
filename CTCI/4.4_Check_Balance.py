"""
    Balanced Tree: a tree such that the heights of the two subtrees of any node never differ by more than one
    Check each child recursively, send back the depth
"""
from util import TreeNode


def check_balance(root):
    depth = check_balance_helper(root)
    return depth, depth != -1


def check_balance_helper(root):
    if not root:
        return 0
    l_dep = check_balance_helper(root.left)
    r_dep = check_balance_helper(root.right)

    if l_dep == -1 or r_dep == -1 or abs(l_dep - r_dep) > 1:
        return -1

    return max(l_dep, r_dep) + 1


def main():
    preorder = [20, 10, 5, 1, 7, 15, 30, 25, 35, 32, 40]
    root = TreeNode.construct_BST(preorder)
    root.print_tree()
    print(check_balance(root))
    print('-----------------')
    preorder = [20, 10, 5, 1, 7, 15, 30]
    root = TreeNode.construct_BST(preorder)
    root.print_tree()
    print(check_balance(root))
    print('-----------------')
    postorder = [None, None, None, 3, 2, None, None, 6, None, 7, 5]
    root = TreeNode.construct_postorder(postorder)
    root.print_tree()
    print(check_balance(root))

if __name__ == '__main__':
    main()


