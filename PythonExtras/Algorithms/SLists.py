class SList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def PrintAllVals(self):
        node = self.head
        print "---List Start---"
        while node != None:
            print node.value
            node = node.next
        print "---List End---"
    

    def AddFront(self,val):
        newnode = SLNode(val)
        
        newnode.next = self.head
        self.head = newnode

        if self.tail == None:
            self.tail = newnode
        

    def AddBack(self, val):
        newnode = SLNode(val)
        
        if self.tail != None:
            self.tail.next = newnode
        
        else:
            self.head = newnode
            
        self.tail = newnode
        

    def InsertBefore(self, next_val, val):
        current = self.head
        previous  = None
        found = False

        while current and found is False:
            if current.value == next_val:
                found = True
            else: 
                previous = current
                current = current.next

        if current == None:
            print "not in list, can't insert"
            return "Not in list"
        if previous == None:
            return self.AddFront(val)
        else:
            newnode = SLNode(val)
            previous.next = newnode
            newnode.next = current
    
 
    def InsertAfter(self, after_val, val):
        current = self.head
        found = False

        while current and found is False:
            if current.value == after_val:
                found = True
            else: 
                current = current.next

        if current == None:
            print "not in list, can't insert"
            return "Not in list"
        else:
            newnode = SLNode(val)
            newnode.next = current.next
            current.next = newnode
            
    
    def Remove(self, val):
        current = self.head
        previous  = None
        found = False

        while current and found is False:
            if current.value == val:
                found = True
            else: 
                previous = current
                current = current.next

        if current == None:
            print "not in list"
            return "Not in list"
        if previous == None:
            self.head = current.next
        else:
            previous.next = current.next
    
    
    def ReverseList(self):
        previous = None
        current = self.head
        next_node = current.next

        while current:
            current.next = previous
            previous = current
            current = next_node
            if next_node:
                next_node = current.next

        self.head = previous

        
        



class SLNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None



mylist = SList()






mylist.AddBack('Alice')
mylist.PrintAllVals()

mylist.InsertAfter('Alice', 'Pter')
mylist.PrintAllVals()

mylist.AddBack('Michael')
mylist.PrintAllVals()

mylist.AddFront('Carlos')
mylist.PrintAllVals()

mylist.Remove('Carlos')
mylist.PrintAllVals()

mylist.InsertBefore('Alice', 'Peter')
mylist.PrintAllVals()

mylist.InsertAfter('Peter', 'John')
mylist.PrintAllVals()

mylist.ReverseList()
mylist.PrintAllVals()