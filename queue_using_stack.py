class MyQueue(object):

    def __init__(self):
        self.out_stack = []
        self.in_stack = []

    def push(self, x):
        if not self.out_stack:
            self.out_stack.append(x)
        else:
            self.in_stack.append(x)

    def pop(self):
        ret = self.out_stack.pop()

        for _ in range(len(self.in_stack) - 1):
            self.out_stack.append(self.in_stack.pop())
        self.in_stack, self.out_stack = self.out_stack, self.in_stack

        return ret

    def peek(self):
        return self.out_stack[0]

    def empty(self):
        return not self.in_stack and not self.out_stack

# Your MyQueue object will be instantiated and called as such:
if __name__ == '__main__':
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    obj.push(4)
    param_1 = obj.pop()
    obj.push(5)
    param_2 = obj.pop()
    param_3 = obj.pop()
    param_4 = obj.pop()
    print(param_4)