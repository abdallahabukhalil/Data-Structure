class Node:
    def __init__(self, value, node = None):
        self.element = value
        self.next = node


class Queue:
    def __init__(self):
        self.__front = None
        self.__rear = None
        self.__counter = 0

    def IsEmpty(self): return self.__counter == 0
    
    def Size(self): return self.__counter

    def Enqueue(self, *values):
        for value in values:
            newnode = Node(value)
        
            if self.__counter == 0:
                self.__front = self.__rear = newnode
        
            else:
                self.__rear.next = newnode
                self.__rear = newnode
        
            self.__counter += 1

    def Dequeue(self):
        if self.__counter == 0:
            print("Error: The Queue is Empty")
        
        else:
            output = self.__front.element
            self.__front = self.__front.next
            self.__counter -= 1
            
            if self.__counter == 0:
                self.__rear = None
            
            return output
        
    def Print(self):
        p = self.__front
        
        print("[", end = "")
        
        while p != None:
            print(f"{p.element}, " if p != self.__rear else f"{p.element}", end = "")

            p = p.next

        print("]")


Q = Queue()


Q.Enqueue(5,6)
Q.Print()
print(Q.Size())