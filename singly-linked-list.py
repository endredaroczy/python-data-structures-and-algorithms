class Node:

    def __init__ (self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def append(self, data):
        node = Node(data = data)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.head.next = node
            self.head = node
        self.size += 1
    
    def iter(self):
        current = self.tail
        while current:
            n = current.data
            current = current.next
            yield n

    def delete(self, data):
        current = self.tail
        previous = self.tail
        while current:
            if current.data == data:
                if current == self.tail:
                    self.tail = current.next
                else:
                    previous.next = current.next
                self.size -= 1
                return
            previous = current
            current = current.next

    def search(self, data):
        for node in self.iter():
            if data == node:
                return True
        return False               

    def clear(self):
        self.tail = None
        self.head = None

    def __getitem__(self, index):
        if index > self.size - 1:
            raise Exception("Index out of range")
        else:
            current = self.tail
            for _ in range(index):
                current = current.next
            return current.data

    def __setitem__(self, index, data):
        if index > self.size - 1:
            raise Exception("Index out of range")
        else:
            current = self.tail
            for _ in range(index):
                current = current.next
            current.data = data

if __name__ == "__main__":
    s = SinglyLinkedList()
    s.append(1)
    s.append(2)
    s.append(3)
    for i in s.iter():
        print(i)
    print(s[0])
    s[0] = 10
    print(s[0])
    print(s)
    s.clear()
    for i in s.iter():
        print(i)
    print(s)
    