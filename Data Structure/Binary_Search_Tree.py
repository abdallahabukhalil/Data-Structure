class Node:
    def __init__(self, value, Lnode = None, Rnode = None):
        self.element = value
        self.left: Node = Lnode
        self.right: Node = Rnode



class BST:
    def __init__(self):
        self.__root = None

    
    def Insert(self, *values):
        for value in values:
            self.__root = self.__Insert(value, self.__root) 
                
    def __Insert(self, value, node):
        if node is None:
            node = Node(value)
            return node

        else:
            if node.element > value:
                node.left = self.__Insert(value, node.left)

            elif node.element < value:
                node.right = self.__Insert(value, node.right)

            else:
                print(f"ERROR: {value} Can not Exist in More Than One Node")
                return node
            
        difference = self.__Height(node.left) - self.__Height(node.right)

        if difference > 1:
            if node.left.element > value:
                node = self.__OneRound(node, "r")
            
            else:
                node = self.__DoubleRound(node, "r")
        
        elif difference < -1:
            if node.right.element < value:
                node = self.__OneRound(node, "l")
            
            else:
                node = self.__DoubleRound(node, "l")

        return node

    
    def Delete(self, *values):
        for value in values:
            self.__root = self.__Delete(value, self.__root)

    def __Delete(self, value, node):
        if node is not None:
            if node.element > value:
                node.left = self.__Delete(value, node.left)

            elif node.element < value:
                node.right = self.__Delete(value, node.right)

            else:
                if node.right is not None and node.left is not None:
                    min = self.__MinNode(node.right)
                    node.element = min.element
                    node.right = self.__Delete(min.element, node.right)

                elif node.left is not None:
                    node = node.left
                    return node

                elif node.right is not None:
                    node = node.right
                    return node

                else:
                    node = None
                    return node
                
            difference = self.__Height(node.left) - self.__Height(node.right)

            if difference > 1:
                if self.__Height(node.left.left) > self.__Height(self.left.right):
                    node = self.__OneRound(node, "r")

                else:
                    node = self.__DoubleRound(node, "r")

            elif difference < -1:
                if self.__Height(node.right.right) > self.__Height(node.right.left):
                    node = self.__OneRound(node, "l")

                else:
                    node = self.__DoubleRound(node, "l")

        else:
            print(f"ERROR: {value} is not Exist to be Deleted")

        return node
        

    
    def FindParent(self, value):
        return self.__FindParent(value, self.__root)
    
    def __FindParent(self, value, node):
        if node is None:
            print(f"ERROR: {value} has no parent")

        else:
            if node.left.element != value and node.right.element != value:
                if value < node.element:
                    node = self.__FindParent(value, node.left)
                
                elif value > node.element:
                    node = self.__FindParent(value, node.right)

        return node

    
    def Find(self, value):
        return self.__Find(value, self.__root)

    def __Find(self, value, node) -> Node:
        if node is None or node.element == value:
            return node
        
        else:
            if node.element > value:
                return self.__Find(value, node.left)

            else:
                return self.__Find(value, node.right)
            

    def FindLeft(self, node): return node.left


    def FindRight(self,  node): return node.right


    def ReturnValue(self, node): return node.element


    def IsExist(self, value): return self.__Find(value, self.__root) is not None

    
    def IsExternal(self, node): return node.right is None and node.left is None

    
    def Inorder(self):
        result = []
        self.__Inorder(self.__root, result)

        return result

    def __Inorder(self, node, result: list):
        if node is not None:
            self.__Inorder(node.left, result)
            result.append(node.element)
            self.__Inorder(node.right, result)

    
    def Preorder(self):
        result = []
        self.__Preorder(self.__root, result)

        return result
    
    def __Preorder(self, node, result: list):
        if node is not None:
            result.append(node.element)
            self.__Preorder(node.left, result)
            self.__Preorder(node.right, result)


    def Postorder(self):
        result = []
        self.__Postorder(self.__root, result)

        return result
    
    def __Postorder(self, node, result: list):
        if node is not None:
            self.__Postorder(node.left, result)
            self.__Postorder(node.right, result)
            result.append(node.element)
            

    def __MinNode(self, node: Node) -> Node:
        if node.left is None:
            return node
        
        else:
            return self.__MinNode(node.left)
        
    
    def __OneRound(self, node: Node, Direction = "r" or "l"):
        if Direction[0].lower() == "r":
            newnode = Node(node.element, Rnode = node.right)
            node.right = newnode
            node.element = node.left.element
            node.right.left = node.left.right
            node.left = node.left.left

        else:
            newnode = Node(node.element, Lnode = node.left)
            node.left = newnode
            node.element = node.right.element
            node.left.right = node.right.left
            node.right = node.right.right

        return node
    

    def __DoubleRound(self, node : Node, Direction = "r" or "l"):
        if Direction == "r":
            newnode = Node(node.element, Rnode = node.right)
            node.right = newnode
            node.element = node.left.right.element
            node.right.left = node.left.right.right
            node.left.right = node.left.right.left

        else:
            newnode = Node(node.element, Lnode = node.left)
            node.left = newnode
            node.element = node.right.left.element
            node.left.right = node.right.left.left
            node.right.left = node.right.left.right


        return node
    

    def Height(self):
        return self.__Height(self.__root)
    
    def __Height(self, node):

        if node is None:
            return -1
        
        return 1 + max(self.__Height(node.left), self.__Height(node.right))