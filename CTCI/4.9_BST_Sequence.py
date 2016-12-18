"""
A binary search tree was created by traversing through an array from left to right.
print all possible arrays

==> root has be the first one in the array, the sequence of left and right can be exchanged
"""
from util import TreeNode


def find_sequence(root):
    # print(root)
    if not root:
        return None

    left = find_sequence(root.left)
    right = find_sequence(root.right)

    def weave(root, left, right):
        if not left and not right:
            return [[root]]
        result = []
        if not left:
            for r in right:
                result.append([root] + r)
        elif not right:
            for l in left:
                result.append([root] + l)
        else:
            for l in left:
                for r in right:
                    result.append([root] + l + r)
                    result.append([root] + r + l)
        return result
    result = weave(root, left, right)
    # print(left)
    return result


def main():
    preorder = [20, 10, 5, 15, 30]
    root = TreeNode.construct_BST(preorder)
    root.print_tree()
    result = find_sequence(root)
    for r in result:
        print(r)
    preorder = [2, 1, 3]
    root = TreeNode.construct_BST(preorder)
    root.print_tree()
    result = find_sequence(root)
    for r in result:
        print(r)

if __name__ == '__main__':
    main()