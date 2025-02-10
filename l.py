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
    
    def Findtail(self):
        if(self.head == None):
            return
        tmp = self.head
        while(tmp.next):
            tmp = tmp.next
        return tmp
    
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
        if(self.head == None):
            self.head = self.tail = New_Node
            return

        tmp = self.Findtail()
        New_Node.prev = tmp
        tmp.next = New_Node
        self.tail = New_Node

    def InsertAtIndex(self, position, data):
        New_Node = self.CreateNode(data)
        if(self.head == None or self.tail == None or position == 0):
            self.InsertNode(data)
            return
        

        tmp = self.head
        for i in range(position-1):
            tmp = tmp.next
        tmp_next = tmp.next
        if(tmp_next == None):
            self.AppendNode(data)
            return
        tmp.next = New_Node
        New_Node.prev = tmp
        tmp_next.prev = New_Node
        New_Node.next = tmp_next


    def PrintNodes(self):
        tmp = self.head
        while(tmp):
            print(tmp.data)
            tmp = tmp.next

llist = LinkedList()
llist.InsertNode("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
llist.AppendNode("a")
llist.AppendNode("a")
llist.AppendNode("a")
llist.InsertAtIndex(0,"b")
llist.PrintNodes()