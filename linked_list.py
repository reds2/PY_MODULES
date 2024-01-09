class Node:
    def __init__(self,d):
        self.data = d
        self.next = None



class LinkedList:
    def __init__(self):
        self.head = None
        self.iteration = None

    def __iter__(self):
        if not self.head:
            raise StopIteration
        return self.head.next
    
    def __next__(self):
        #TODO
        pass
    def pop(self):
        if not self.head:
            return
        self.head = self.head.next

    def popBack(self):
        if not self.head:
            return
        temp = self.head
        while temp.next:
            temp = temp.next
            if not temp.next.next:
                break
        temp.next = None
         
    def push(self, d):
        new_node = Node(d)
        new_node.next = self.head
        self.head = new_node

    def pushBack(self,d):
        new_node = Node(d)
        if not self.head:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last=last.next
        last.next = new_node

    append = pushBack
    
    def length(self):
        temp = self.head
        counter = 0
        while temp:
            temp = temp.next
            counter+=1
        return counter

    def print(self):
        temp = self.head
        while temp:
            print(temp.data,end="->")
            temp = temp.next

    def getNode(self,i):
        temp = self.head
        for _ in range(i):
            temp = temp.next
        return temp.data

    

    def __next__(self):
        pass

if __name__ == "__main__":

    l = LinkedList()

    for i in range(6):
        l.push(i)
    for i in range(6):
        l.append(i)
    for i in range(3):
        l.pop()
    for i in range(3):
        l.popBack()

    l.print()
    print("\n",l.getNode(2))
    
    #for i in l:
    #    print(i)
    l.print()
