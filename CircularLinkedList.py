class Node:
    __slots__ = 'val', 'next'
    
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        
class CircularLinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0
    
    def __len__(self):
        return self.size
    
    def add_first(self, val):
        new_node = Node(val)
        if self.is_empty():
            new_node.next = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.tail.next = new_node
        
        self.head = new_node
        self.size += 1

    def add_at(self, val, pos):
        new_node = Node(val)
        if pos == 1:
            self.add_first(val)
            return
        if pos == len(self) + 1:
            self.add_last(val)
            return
        p = self.head
        idx = 1
        while idx < pos - 1:
            p = p.next
            idx += 1
        new_node.next = p.next
        p.next = new_node
        self.size += 1
    
    def add_last(self, val):
        new_node = Node(val)
        if self.is_empty():
            self.head = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
    
        self.tail = new_node
        self.size += 1
        
    def remove_first(self):
        if self.is_empty():
            print('The list is empty!')
            return
        if len(self)==1:
            self.head = None
            self.tail = None
            self.size -= 1
            return
        e = self.head.val
        self.tail.next = self.head.next
        self.head = self.head.next
        self.size -= 1
        return e
    
    def remove_at(self, pos):
        if pos == 1:
            self.remove_first()
            return
        if pos == len(self):
            self.remove_last()
            return
        p = self.head
        idx = 1
        while idx < pos - 1:
            p = p.next
            idx += 1
        p.next = p.next.next
        self.size -= 1
    
    def remove_last(self):
        if self.is_empty():
            print('The list is empty!')
            return
        
        if len(self)==1:
            self.head = None
            self.tail = None
            self.size -= 1
            return
        
        p = self.head
        idx = 1
        
        while idx < len(self) - 1:
            p = p.next
            idx += 1
        e = p.next.val
        p.next = self.head
        self.tail = p
        self.size -= 1
        return e
    
    def display(self):
        if self.is_empty():
            print('[]')
            return
        else:
            show = '['
            p = self.head
            idx = 0
            while idx < len(self):
                show += f'{p.val},'
                p = p.next
                idx += 1
            show = show[:-1] + ']'
            print(show)

if __name__ == '__main__':
    C = CircularLinkedList()
    C.add_last(1)
    C.add_last(2)
    C.add_last(3)
    C.add_last(4)
    C.add_last(5)
    C.add_last(6)
    C.add_last(7)
    C.add_last(8)
    C.add_last(9)
    C.add_last(10)
    # C.add_first('adding to the third')
    # C.add_first('adding to the second')
    # C.add_first('adding to the first')
    # C.add_at('last', 10)
    # C.remove_last()
    # C.remove_last()
    # C.remove_last()
    # C.remove_last()
    # C.remove_last()
    # C.remove_last()
    # C.remove_last()
    # C.remove_last()
    # C.remove_last()
    # C.remove_at(1)
    # C.remove_at(10)
    # C.remove_at(5)
    C.display()
