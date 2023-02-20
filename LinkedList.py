class Node:
    __slots__ = 'data', 'next'
    
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def add_first(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1
        
    def insert_at(self, data, position):
        new_node = Node(data)
        idx = 1
        p = self.head
        while idx < position - 1:
            p = p.next
            idx += 1
        new_node.next = p.next
        p.next = new_node
        self.size += 1
        
    def add_last(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.size += 1
    
    def remove_first(self):
        if self.is_empty():
            print('The linked list is empty.')
            return
        
        e = self.head.data
        self.head = self.head.next
        
        if self.is_empty():
            self.tail = None
        self.size -= 1
        return e
        
    def remove_last(self):
        if self.is_empty():
            print('The linked list is empty.')
        p = self.head
        idx = 1
        while idx < len(self) - 1:
            p = p.next
            idx += 1
        self.tail = p
        e = p.next.data
        self.tail.next = None
        self.size -= 1
        return e
    
    def remove_at(self, position):
        if position == 1:
            self.remove_first()
            return
        p = self.head
        idx = 1
        while idx < position - 1:
            p = p.next
            idx += 1
        e = p.next.data
        p.next = p.next.next
        self.size -= 1
        return e
            
    def search(self, key):
        p = self.head
        idx = 1
        while p:
            if p.data == key:
                return idx
            else:
                p = p.next
                idx += 1
        return -1
    
    def display(self):
        show = '['
        p = self.head
        while p:
            show += f'{p.data},'
            p = p.next
        show = show[:-1] + ']'
        print(show)

if __name__ == '__main__':
    LL = LinkedList()
    LL.add_last('a')
    LL.add_last('b')
    LL.add_last('c')
    LL.add_last('d')
    LL.add_last('e')
    LL.add_last('f')
    LL.add_first('first')
    LL.insert_at(12, 4)
    LL.add_last('last')
    LL.remove_first()
    LL.remove_last()
    LL.remove_at(2)
    LL.display()
