class DList(object):
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
        newnode = Node(val)
        
        newnode.next = self.head
        newnode.next.previous = newnode
        self.head = newnode

        if self.tail == None:
            self.tail = newnode
        

    def AddBack(self, val):
        newnode = Node(val)
        
        if self.tail != None:
            newnode.previous = self.tail
            self.tail.next = newnode
            
        else:
            self.head = newnode
            
        self.tail = newnode
        

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
        if current.next == None:
            return self.AddBack(val)
        else:
            newnode = Node(val)

            newnode.previous = current
            newnode.next = current.next

            current.next.previous = newnode
            current.next = newnode



    def InsertBefore(self, before_val, val):
        current = self.head
        found = False

        while current and found is False:
            if current.value == before_val:
                found = True
            else: 
                current = current.next

        if current == None:
            print "not in list, can't insert"
            return "Not in list"
        if current.previous == None:
            return self.AddFront(val)
        else:
            newnode = Node(val)

            newnode.previous = current.previous
            newnode.next = current

            current.previous.next = newnode
            current.previous = newnode

     
    def Remove(self, val):
        current = self.head
        found = False

        while current and found is False:
            if current.value == val:
                found = True
            else: 
                current = current.next

        if current == None:
            print "not in list"
            return "Not in list"
        if current.previous == None:
            self.head = current.next
            current.next.previous = None
        else:
            current.previous.next = current.next
            current.next.previous = current.previous
    

class Node(object):
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None




mylist = DList()


mylist.AddBack('Alice')
mylist.PrintAllVals()

mylist.InsertAfter('Alice', 'Peter')
mylist.PrintAllVals()

mylist.AddBack('Michael')
mylist.PrintAllVals()

mylist.AddFront('Carlos')
mylist.PrintAllVals()

mylist.Remove('Carlos')
mylist.PrintAllVals()

mylist.InsertBefore('Alice', 'Zuly')
mylist.PrintAllVals()

mylist.InsertAfter('Peter', 'John')
mylist.PrintAllVals()

