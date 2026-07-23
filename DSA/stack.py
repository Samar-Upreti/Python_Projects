class stack:

    def __init__(self):
        self.s = []

    def len(self):
        return len(self.s)

    def push(self,value):
        self.s.insert(0,value)

    def peek(self):
        if len(self.s) == 0:
            raise Exception("Stack is Empty")
        else:
            return self.s[0]

    def pop(self):
        if len(self.s) == 0:
            raise Exception("Stack is Empty")
        else:
            return self.s.pop(0)

if __name__ == "__main__":
    stk = stack()
    stk.push(10)
    stk.push(11)
    print(stk.peek())
    print(stk.pop())
    print(stk.peek())
    