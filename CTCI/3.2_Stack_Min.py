import sys


class StackMin:
    class StackNode:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.sub_min = None

        def __str__(self):
            return "{}: next min is {}".format(self.data, self.sub_min)

        __repr__ = __str__

    def __init__(self):
        self.top = None
        self.min = sys.maxsize

    def push(self, data):
        node = StackMin.StackNode(data)
        node.sub_min = self.min
        if data < self.min:
            self.min = data
        node.next = self.top
        self.top = node

    def pop(self):
        if not self.top:
            return None
        self.min = self.top.sub_min
        t = self.top
        self.top = self.top.next
        return t

    def get_min(self):
        if self.min == sys.maxsize:
            return None
        return self.min

    def print_stack(self):
        print("--------start--------")
        temp = self.top
        while temp:
            print(temp)
            temp = temp.next
        print("---------end----------")


class StackMin2:
    class StackNode:
        def __init__(self, data):
            self.data = data
            self.next = None

        def __str__(self):
            return "{} ->".format(self.data)

        __repr__ = __str__

    def __init__(self):
        self.top = None
        self.mins = []

    def push(self, data):
        node = StackMin2.StackNode(data)
        node.next = self.top
        self.top = node
        if len(self.mins) == 0 or data < self.mins[-1].data:
            self.mins.append(node)

    def pop(self):
        if not self.top:
            return None
        node = self.top
        if len(self.mins) > 0 and node == self.mins[-1]:
            self.mins.pop()
        self.top = self.top.next
        return node

    def get_min(self):
        if len(self.mins) == 0:
            return None
        return "The min is: {}".format(self.mins[-1].data)

    def print_stack(self):
        print("--------start--------")
        temp = self.top
        while temp:
            print(temp, end="")
            temp = temp.next
        print()
        print("---------end----------")


def main():
    stack = StackMin()
    stack.push(4)
    stack.push(3)
    stack.push(5)
    stack.push(2)
    stack.print_stack()  # 2, 5, 3, 4
    print(stack.pop())  # 2
    print(stack.get_min())  # 3
    print(stack.pop())  # 5
    stack.push(1)
    stack.print_stack()  # 1, 3, 4
    print(stack.get_min())  # 1
    print(stack.pop())  # 1
    print(stack.get_min())  # 3
    print(stack.pop())  # 3
    print(stack.pop())  # 4
    print(stack.pop())  # None
    # print(stack.pop())
    # print(stack.pop())
    print("-------------------------------------------------------")
    stack = StackMin2()
    stack.push(4)
    stack.push(3)
    stack.push(5)
    stack.push(2)
    stack.print_stack()  # 2, 5, 3, 4
    print(stack.pop())  # 2
    print(stack.get_min())  # 3
    print(stack.pop())  # 5
    stack.push(1)
    stack.print_stack()  # 1, 3, 4
    print(stack.get_min())  # 1
    print(stack.pop())  # 1
    print(stack.get_min())  # 3
    print(stack.pop())  # 3
    print(stack.pop())  # 4
    print(stack.pop())  # None

if __name__ == '__main__':
    main()