class Result:
    def __init__(self, node, isAnc, dis):
        self.node = node
        self.isAnc = isAnc
        self.dis = dis

    def __str__(self):
        return '{}, {}, {}'.format(self.node, self.isAnc, self.dis)


class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val

    def __str__(self):
        return "Node({})".format(self.val)


def find_dis(root, p, q):
    if not root:
        return

    if root == p and root == q:
        return Result(root, True, 0)

    left = find_dis(root.left, p, q)
    right = find_dis(root.right, p, q)

    print(root)
    print(left)
    print(right)
    print('-------------')
    if left and left.isAnc:
        return left
    if right and right.isAnc:
        return right

    if root == p or root == q:
        if not left and right:
            return Result(root, True, right.dis)
        if not right and left:
            return Result(root, True, left.dis)
        else:
            return Result(root, False, 1)

    if not left and right:
        return Result(right.node, False, right.dis + 1)
    if not right and left:
        return Result(left.node, False, left.dis + 1)

    if left and right:
        return Result(root, True, left.dis + right.dis)


def construct():
    global preorder
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
    global preorder
    preorder = [20, 10, 5, 1, 7, 15, 30, 25, 35, 32, 40]
    root = construct()
    print(preorder[4])
    print(preorder[1])
    print('----------------')
    print(find_dis(root, preorder[4], preorder[1]))

if __name__ == '__main__':
    main()



