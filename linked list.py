class linkedlist:
    def __init__(self):
        self.head = None

    def printlist(self):
        printmoko = self.head
        while printmoko is not None:
            print(printmoko.data)
            printmoko = printmoko.next

    def athead(self, newdata):
        NewNode = Node(newdata)
        if self.head is None:
            NewNode = Node(newdata)
            NewNode.next = self.head
            self.Head = NewNode
    
    def inpos(self,newelement,position):
        NewNode = Node(newelement)
        if position <= 1:
            print("\n position should be >=1")
        elif (position == 1):
            NewNode.next = self.head
            self.head = NewNode
        else:
            temp = self.head
            for i in range(1,position-1):
                if (temp != None):
                    temp = temp.next
            if (temp != None):
                NewNode.next = temp.next
                temp.next = NewNode
            else:
                print("List is null")
    
    def searchelement (self, searchValue):
        temp = self.headval
        found = 0
        i = 0
        if (temp != None):
            while (temp != None):
                i += 1
                if (temp.dataval == searchValue):
                    found += 1
                    break
                temp = temp.nextval
            if (found == 1):
                print(searchValue, "is found at index = ", i)
            else:
                print(searchValue, "is not found in the list.")
        else:
            print("The list is empty.")
        
    def deleteNode(self, key):
        temp = self.head
        if (temp is not None):
            if (temp.data == key):
                self.head = temp.next
                temp = None
                return
        while (temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if (temp == None):
            return
        prev.next = temp.next
        temp = None

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def InsertToEmptyList(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
        else:
            print("The list is empty")

    def InsertToEnd(self, data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        while n.next is not None:
            n = n.next
        new_node = Node(data)
        n.next = new_node
        new_node.prev = n

    def DeleteAtStart(self):
        if self.start_node is None:
            print("The Linked lis is empty, no element to delete")
            return
        if self.start_node.next is None:
            self.start_node = None
            return
        self.start_node = self.start_node.next
        self.start_prev = None

    def delete_at_end(self):
        if self.start_node is None:
            print("The Linked lis is empty, no element to delete")
            return
        if self.start_node.next is None:
            self.start_node = None
            return
        n = self.start_node
        while n.next is not None:
            n = n.next
        n.prev.next = None

    def Display(self):
        if self.start_node is None:
            print("The list is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                print("Element is: ", n.item)
                n = n.next
        print("\n")

list1 = linkedlist()
list1.head = Node("Data")
e2 = Node("Structure")
e3 = Node("Python")

list1.head.next = e2
e2.next = e3

list1.athead("Welcome to")
# list1.printlist()

list1.athead("Linked List")
list1.printlist()