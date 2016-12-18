"""
    Given a sorted array(unique elements), create a binary tree with minimal height
    Use the median as root, recursively create the tree
"""
from util import TreeNode


def create_min_tree(l, start, end):
    """
    :param l: list, increasing, distinct
    :param start: int
    :param end: int
    :return: t: tree
    """
    if start > end:
        return None

    mid = int((start + end) / 2)
    root = TreeNode(l[mid])
    root.left = create_min_tree(l, start, mid - 1)
    root.right = create_min_tree(l, mid + 1, end)
    return root


def main():
    tree = create_min_tree([1, 2, 3, 4, 5, 6, 7, 8, 9], 0, 8)
    tree.print_tree()


if __name__ == '__main__':
    main()
