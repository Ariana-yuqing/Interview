from util import TreeNode


def print_node(root, dis):
    if root is None:
        return
    if dis == 0:
        print(root)
    else:
        dis -= 1
        print_node(root.left, dis)
        print_node(root.right, dis)


def find(cur, t, x):
    if cur is None:
        return False, 0
    if cur is not None:
        if cur.value == t.value:
            return True, 0
        else:
            l, lc = find(cur.left, t, x)
            r, rc = find(cur.right, t, x)
            if l is True:
                if lc + 1 == x:
                    print(cur)
                print_node(cur.right, x - lc - 2)
                return True, lc + 1
            if r is True:
                if rc + 1 == x:
                    print(cur)
                print_node(cur.left, x - rc - 2)
                return True, rc + 1
        return False, 0




def main():
    root = TreeNode.construct_BST([20, 10, 5, 1, 7, 15, 30, 25, 35, 32, 40])
    root.print_tree()
    find(root, TreeNode(5), 5)

if __name__ == '__main__':
    main()

