class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

    def __str__(self):
        return "Node({})".format(self.val)


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
        if cur.val == t.val:
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


def construct(preorder):
    if len(preorder) == 0:
        return None
    preorder = [Node(v) for v in preorder]
    s = []
    s.append(preorder[0])
    i = 1
    while i < len(preorder):
        top = s[-1]
        node = preorder[i]
        if node.val < top.val:
            top.left = node
        else:
            while len(s) != 0 and s[-1].val < node.val:
                parent = s.pop()
            parent.right = node
        s.append(node)
        i += 1
    return preorder[0]


def main():
    root = construct([20, 10, 5, 1, 7, 15, 30, 25, 35, 32, 40])
    find(root, Node(5), 3)

if __name__ == '__main__':
    main()

