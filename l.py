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
        if(self.head == None):
            self.head = New_Node
            return
        New_Node.next = self.head
        self.head.prev = New_Node
        self.head = New_Node
    
    def AppendNode(self, data):
        New_Node = self.CreateNode(data)
        if(self.tail == None):
            self.tail = New_Node
            return
        New_Node.prev = self.tail
        self.tail.next = New_Node
        self.tail = New_Node
    
    def PrintNodes(self):
        tmp = self.head
        while(tmp):
            print(tmp.data)
            tmp = tmp.next

llist = LinkedList()
print("\n")
llist.InsertNode("a")
llist.InsertNode("d")
llist.InsertNode("c")
llist.InsertNode("b")
llist.PrintNodes()