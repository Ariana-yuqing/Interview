"""
Leetcode 98
Check if a binary tree is a binary search tree
Thoughts: recursively check every subtree
"""
from util import TreeNode


def validate_BST(root):
    def validate_BST_helper(root, min=None, max=None):
        """
        :param root: TreeNode
        :param min: The minimal value for the right children
        :param max: The maximal value for the left children
        :return: isBST: bool
        """
        if not root:
            return True
        # The values of the nodes have to be distinct
        if min is not None and root.value <= min or max is not None and root.value >= max:
            return False

        left = validate_BST_helper(root.left, min, root.value)
        right = validate_BST_helper(root.right, root.value, max)

        return left and right

    return validate_BST_helper(root, None, None)


def main():
    preorder = [20, 10, 5, 11, 7, 15, 30, 25, 35, 32, 40]
    root = TreeNode.construct_BST(preorder)
    root.print_tree()
    print(validate_BST(root))
    print('-----------------')
    preorder = [20, 10, 5, 1, 7, 15, 30]
    root = TreeNode.construct_BST(preorder)
    root.print_tree()
    print(validate_BST(root))
    print('-----------------')
    postorder = [None, None, None, 3, 10, None, None, 6, None, 7, 5]
    root = TreeNode.construct_postorder(postorder)
    root.print_tree()
    print(validate_BST(root))
    print('-----------------')
    postorder = [None, -1, 0]
    root = TreeNode.construct_postorder(postorder)
    root.print_tree()
    print(validate_BST(root))


if __name__ == '__main__':
    main()
