class LinkedListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return "Node({})->".format(self.val)

    __repr__ = __str__

    def add(self, v):
        cur = self
        while cur and cur.next:
            cur = cur.next
        cur.next = LinkedListNode(v)

    def print_linked_list(self):
        if self is None:
            return
        if self.next is not None:
            print(self, end="")
            self.next.print_linked_list()
        else:
            print(self)

    @staticmethod
    def construct_linked_list(values):
        if len(values) == 0 or values is None:
            return None
        head = LinkedListNode(values[0])
        cur = head
        for v in values[1:]:
            node = LinkedListNode(v)
            cur.next = node
            cur = cur.next
        return head


def print_table(A):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in A]))


class TreeNode:

    def __init__(self, v):
        self.left = None
        self.right = None
        self.value = v

    def __str__(self):
        return "Node({})".format(self.value)

    __repr__ = __str__

    def find_node(self, v):
        if self.value == v:
            return self
        if self.left:
            r = self.left.find_node(v)
            if r:
                return r
        if self.right:
            r = self.right.find_node(v)
            if r:
                return r
        return None

    def print_tree(self, i=0):
        print("  " * i + str(self))
        if self.left:
            self.left.print_tree(i+1)
        if not self.left and self.right:
            print("  " * (i+1) + "None")
        if self.right:
            self.right.print_tree(i+1)
        if self.left and not self.right:
            print("  " * (i+1) + "None")

    @staticmethod
    def construct_BST(preorder):
        if len(preorder) == 0:
            return None
        preorder = [TreeNode(v) for v in preorder]
        s = []
        s.append(preorder[0])
        i = 1
        while i < len(preorder):
            top = s[-1]
            node = preorder[i]
            if node.value < top.value:
                top.left = node
            else:
                while len(s) != 0 and s[-1].value < node.value:
                    parent = s.pop()
                parent.right = node
            s.append(node)
            i += 1

        return preorder[0]

    @staticmethod
    def construct_postorder(postorder=None):
        if not postorder or len(postorder) == 0:
            return None
        for i, v in enumerate(postorder):
            if v is not None:
                postorder[i] = TreeNodeWithParents(v)
        s = [postorder[0]]
        i = 1
        while i < len(postorder):
            if postorder[i] and len(s) > 1:
                postorder[i].right = s.pop()
                postorder[i].left = s.pop()
            s.append(postorder[i])
            i += 1
        return s.pop()


class TreeNodeWithParents(TreeNode):

    def __init__(self, v):
        super().__init__(v)
        self.parent = None

    def __str__(self):
        return "Node({})".format(self.value)

    __repr__ = __str__

    @staticmethod
    def construct_BST(preorder):
        if len(preorder) == 0:
            return None
        preorder = [TreeNodeWithParents(v) for v in preorder]
        s = []
        s.append(preorder[0])
        i = 1
        while i < len(preorder):
            top = s[-1]
            node = preorder[i]
            if node.value < top.value:
                top.left = node
                top.left.parent = top
            else:
                while len(s) != 0 and s[-1].value < node.value:
                    parent = s.pop()
                parent.right = node
                parent.right.parent = parent
            s.append(node)
            i += 1

        return preorder[0]

    @staticmethod
    def construct_postorder(postorder=None):
        if not postorder or len(postorder) == 0:
            return None
        for i, v in enumerate(postorder):
            if v is not None:
                postorder[i] = TreeNode(v)
        s = [postorder[0]]
        i = 1
        while i < len(postorder):
            if postorder[i] and len(s) > 1:
                postorder[i].right = s.pop()
                if postorder[i].right:
                    postorder[i].right.parent = postorder[i]
                postorder[i].left = s.pop()
                if postorder[i].left:
                    postorder[i].left.parent = postorder[i]
            s.append(postorder[i])
            i += 1
        return s.pop()
