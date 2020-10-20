class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack(object):
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        node = Node(data)
        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node
        self.size += 1

    def pop(self):
        if self.top is None:
            return None
        else:
            data = self.top.data
            self.size -= 1
            if self.top.next is None:
                self.top = None
            else:
                self.top = self.top.next
            return data                

    def peek(self):
        if self.top is None:
            return None
        else:
            return self.top.data

if __name__ == "__main__":
    s = Stack()
    s.push('Data1')
    s.push('Data2')
    s.push('Data3')
    pe = s.peek()
    print(pe)
    po = s.pop()
    print(po)
