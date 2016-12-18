class SetOfStacks:
    class Stack:
        class StackNode:
            def __init__(self, data):
                self.data = data
                self.next = None
                self.prev = None

            def __str__(self):
                return "{} ->".format(self.data)

            __repr__ = __str__

        def __init__(self):
            self.top = None
            self.bottom = None
            self.length = 0

        def push(self, data):
            node = SetOfStacks.Stack.StackNode(data)
            if self.length == 0:
                self.bottom = node
            node.next = self.top
            if self.top:
                self.top.prev = node
            self.top = node
            self.length += 1

        def pop(self):
            if self.length == 0:
                return None
            node = self.top
            self.top = self.top.next
            self.length -= 1
            return node

        def popAt(self, ind):
            if not self.top:
                return None
            cur = self.bottom

            for i in range(ind):
                cur = cur.prev
                # print()
                # print(cur.prev)
            temp = cur
            # print("cur: {}".format(cur))
            if cur.prev:
                cur.prev.next = cur.next
            return temp

        def print_stack(self):
            temp = self.top
            while temp:
                print(temp, end="")
                temp = temp.next
            print()

    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []
        self.top = None
        self.length = 0  # might not needed

    def push(self, data):
        if len(self.stacks) == 0 or self.stacks[-1].length >= self.capacity:
            newStack = SetOfStacks.Stack()
            self.stacks.append(newStack)
        self.stacks[-1].push(data)

    def popAt(self, ind):
        stack_num = int(ind / self.capacity)
        ele_num = int(ind % self.capacity)

        if stack_num >= len(self.stacks) or ele_num >= self.stacks[stack_num].length:
            return "Out of range"
        # print(ind, stack_num, ele_num)
        temp = self.stacks[stack_num].popAt(ele_num)
        for i in range(1, len(self.stacks) - stack_num):
            prev_stack = self.stacks[stack_num + i - 1]
            cur_stack = self.stacks[stack_num + i]
            cur_stack.bottom.next = prev_stack.top
            prev_stack.top = cur_stack.bottom
            cur_stack.bottom = cur_stack.bottom.prev
            cur_stack.bottom.prev = None
        self.stacks[-1].length -= 1
        if self.stacks[-1].length == 0:
            self.stacks.pop()
        return temp

    def pop(self):
        if len(self.stacks) == 0:
            return None
        cur_stack = self.stacks[-1]
        temp = cur_stack.top
        cur_stack.length -= 1
        if cur_stack.length == 0:
            self.stacks.pop()
        cur_stack.top = cur_stack.top.next
        return temp

    def print_stack(self):
        for i in range(len(self.stacks)):
            print("-----stack {}------".format(i))
            self.stacks[i].print_stack()


def main():
    stack = SetOfStacks(2)
    stack.push(0)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.print_stack()  # 4, 3, 2, 1, 0
    print("Remove last element: {}".format(stack.pop()))  # 4
    stack.print_stack()
    print("Remove the element at 2: {}".format(stack.popAt(2)))  # 2
    print("Remove last element: {}".format(stack.pop()))  # 3
    stack.print_stack()  # 1, 0
    stack.push(5)
    stack.push(6)
    stack.push(7)
    stack.push(8)
    stack.print_stack()
    print("Remove last element: {}".format(stack.pop()))  # 8
    print("Remove the element at 7: {}".format(stack.popAt(7)))  # Out of range
    print("Remove the element at 4: {}".format(stack.popAt(4)))  # 7
    print("Remove last element: {}".format(stack.pop()))  # 6
    print("Remove last element: {}".format(stack.pop()))  # 5
    print("Remove last element: {}".format(stack.pop()))  # 1
    print("Remove last element: {}".format(stack.pop()))  # 0
    print("Remove last element: {}".format(stack.pop()))  # None


if __name__ == '__main__':
    main()

