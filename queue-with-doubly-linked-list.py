class Node(object):
    def __init__(self, data, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

class Queue(object):
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, data):
        node = Node(data, None, None)
        if self.tail is None:
            self.tail = node
            self.head = node
        else:
            self.tail.prev = node
            node.next = self.tail
            self.tail = node
        self.size += 1

    def dequeue(self):
        current = self.head
        if current is None:
            return None
        elif self.size > 1:
            self.head = current.prev
            self.head.next = None
            self.size -= 1
            return current.data
        elif self.size == 1:
            self.head = None
            self.tail = None
            self.size -= 1
            return current.data

    def __str__(self):
        str_representation = "["
        current = self.tail
        if current is not None:
            while current.next is not None:
                str_representation += str(current.data) + ", "
                current = current.next
            str_representation += str(current.data) + "]"
        else:
            str_representation += "]"
        return str_representation


if __name__ == "__main__":
    q = Queue()
    q.enqueue("Hello")
    q.enqueue("Bello")
    q.enqueue(4)
    print(q)
    q.dequeue()
    q.dequeue()
    q.dequeue()
    print(q)