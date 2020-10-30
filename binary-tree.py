class Node(object):
    def __init__ (self, data):
        self.data = data
        self.right_child = None
        self.left_child = None


class Tree(object):
    '''
    Binary search tree: the value at any node in the tree is greater than the values in all the nodes
    of its left sub-tree, and less than or equal to the values of all the nodes of the right sub-tree
    Important 
    '''
    def __init__(self):
        self.root_node = None

    def insert(self, data):
        new_node = Node(data)
        if self.root_node is None:
            self.root_node = new_node
        else:
            current = self.root_node
            parent = None
            while True:
                parent = current
                if new_node.data < parent.data:
                    current = current.left_child
                    if current is None:
                        parent.left_child = new_node
                        return
                else:
                    current = current.right_child
                    if current is None:
                        parent.right_child = new_node
                        return

    def get_node_with_parent(self, data):
        parent = None
        current = self.root_node
        if current is None:
            return(parent, None)
        while True:
            if current.data == data:
                return (parent, current)
            elif current.data > data:
                parent = current
                current = current.left_child
            else:
                parent = current
                current = current.right_child
        return (parent, current)

    def remove(self, data):
        parent, node = self.get_node_with_parent(data)

        if parent is None and node is None:
            return False

        children_count = 0

        if node.left_child and node.right_child:
            children_count = 2
        elif (node.left_child is None) and (node.right_child is None):
            children_count = 0
        else:
            children_count = 1
        
        if children_count == 0:
            if parent:
                if parent.right_child is node:
                    parent.right_child = None
                else:
                    parent.right_child = None
            else:
                self.root_node = None
        elif children_count == 1:
            next_node = None
            if node.left_child:
                next_node = node.left_child
            else:
                next_node = node.right_child
            
            if parent:
                if parent.left_child is node:
                    parent.left_child = next_node
                else:
                    parent.right_child = next_node
            else:
                self.root_node = next_node
        else:
            parent_of_leftmost_node = node
            leftmost_node = node.right_child
            while leftmost_node.left_child:
                parent_of_leftmost_node = leftmost_node
                leftmost_node = leftmost_node.left_child
            node.data = leftmost_node.data
            if parent_of_leftmost_node.left_child == leftmost_node:
                parent_of_leftmost_node.left_child = leftmost_node.right_child
            else:
                parent_of_leftmost_node.right_child = leftmost_node.right_child
        
    def search(self, data):
        current = self.root_node
        while True:
            if current is None:
                return None
            elif current.data is data:
                return data
            elif current.data > data:
                current = current.left_child
            else:
                current = current.right_child
            




if __name__ == "__main__":
    t = Tree()
    t.insert(1)
    t.insert(2)
    t.insert(5)
    t.insert(4)
    t.insert(3)
    t.get_node_with_parent(1)
    t.search(3)
    t.remove(4)
    print("Hello")


    

