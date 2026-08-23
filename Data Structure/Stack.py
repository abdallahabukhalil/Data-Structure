class Node:
    def __init__(self, value, node = None):
        self.element = value
        self.previous = node


class Stack:
    def __init__(self):
        self.__top = None
        self.__counter = 0

    def IsEmpty(self): return self.__counter == 0

    def Size(self): return self.__counter

    def Push(self, *values):
        for value in values:
            newnode = Node(value, self.__top)
            self.__top = newnode

            self.__counter += 1

    def Pop(self):
        if self.__counter == 0:
            print("ERROR: The Stack is Empty")
        else:
            output = self.__top.element
            self.__top = self.__top.previous

            self.__counter -= 1

            return output
        
    def Print(self):
        p = self.__top
        
        while p != None:
            print(f"{p.element}, " if p.previous != None else f"{p.element}", end = "")
            
            p = p.previous
        
        print("]")

Q = Stack()
Q.Push(5, 6, 7, 8)
Q.Pop()
Q.Print()