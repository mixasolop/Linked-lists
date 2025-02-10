class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None    
    
    def CreateNode(self, data):
        New_Node = Node(data)
        New_Node.prev = None
        New_Node.next = None
        return New_Node
    
    def InsertNode(self, data):
        New_Node = self.CreateNode(data)
        New_Node.next = self.head
        self.head.prev = New_Node
        self.head = New_Node
    
    def AppendNode(self, data):
        New_Node = self.CreateNode(data)
        New_Node.prev = self.tail
        self.tail.next = New_Node
        self.tail = New_Node