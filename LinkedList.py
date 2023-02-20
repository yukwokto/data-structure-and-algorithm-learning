class Node:
    __slots__ = 'data', 'next'
    
    def __init__(self, data, next=None):
        self.data = data
        self.next = None
        

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    # insert operation
    def add_head(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.tail = new_node
        else:
            new_node.next = self.head
        self.head = new_node
        self.size += 1
    
    def insert_at(self, data, pos):
        if pos == 1:
            self.add_head(data)
            return
        new_node = Node(data)
        p = self.head
        idx = 1
        while idx < pos - 1:
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
    
    # delete opeartion
    def delete_head(self):
        if self.is_empty():
            print('The linked list is empty.')
            return
        
        e = self.head.data
        self.head = self.head.next
        
        if self.is_empty():
            self.tail = None
        self.size -= 1
        return e
    
    def delete_at(self, pos):
        if self.is_empty():
            print('The linked list is empty.')
            return
        if pos == 1:
            self.delete_head()
            return
        p = self.head
        idx = 1
        while idx < pos - 1:
            p = p.next
            idx += 1
        e = p.next.data
        p.next = p.next.next
        self.size -= 1
        return e
        
    def delete_tail(self):
        if self.is_empty():
            print('The linked list is empty.')
            return
        if self.size == 1:
            self.delete_head()
            return
        
        p = self.head
        idx = 1
        while idx < len(self) - 1:
            p = p.next
            idx += 1
        e = p.next.data
        self.tail = p
        self.tail.next = None
        self.size -= 1
        return e
    
    def search(self, key):
        p = self.head
        idx = 1
        while p:
            if p.data == key:
                return idx
            p = p.next
            idx += 1
        return -1
        
    def display(self):
        if self.is_empty():
            print('[]')
            return
        shown = '['
        p = self.head
        while p:
            shown += f'{p.data},'
            p = p.next
        shown = shown[:-1]+']'
        print(shown)
        
if __name__ == '__main__':
    LL = LinkedList()
    LL.add_last(1)
    LL.add_last(2)
    LL.add_last(3)
    LL.add_last(4)
    LL.add_last(5)
    LL.add_last(6)
    LL.add_last(7)
    LL.delete_at(1)
    LL.display()
