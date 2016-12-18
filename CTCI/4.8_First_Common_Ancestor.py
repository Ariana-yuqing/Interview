"""
 with no links to parent:
 start from the root, search for p and q, return the first node with p and q present on two branches respectively
"""
from util import TreeNode


def search1(root, p, q):

    def search1_helper(root, p, q):
        """
        :return: (p_check, q_check, ancestor)
        """
        if not root:
            return False, False, None
        p_check, q_check = False, False

        p_check_l, q_check_l, ancestor_l = search1_helper(root.left, p, q)
        p_check_r, q_check_r, ancestor_r = search1_helper(root.right, p, q)

        if ancestor_l:
            return True, True, ancestor_l
        if ancestor_r:
            return True, True, ancestor_r

        if root.value == p or p_check_l or p_check_r:
            p_check = True
        if root.value == q or q_check_l or q_check_r:
            q_check = True
        if p_check and q_check:
            return p_check, q_check, root
        else:
            return p_check, q_check, None

    _, _, ancestor = search1_helper(root, p, q)
    return ancestor


def main():
    preorder = [20, 10, 5, 1, 7, 15, 16, 30, 25, 35, 32, 40]
    root = TreeNode.construct_BST(preorder)
    root.print_tree()
    print("20, 7 => " + str(search1(root, 20, 7)))
    print("1, 16 => " + str(search1(root, 1, 16)))
    print("1, 40 => " + str(search1(root, 1, 40)))
    print("25, 40 => " + str(search1(root, 25, 40)))


if __name__ == '__main__':
    main()