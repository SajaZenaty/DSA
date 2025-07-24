class BSTnode:
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = BSTnode(data)
        else:
            self._insert(self.root, data)

    def _insert(self, node, data):
        if data < node.data:
            if node.left:
                self._insert(node.left, data)
            else:
                node.left = BSTnode(data)
        else:  
            if node.right:
                self._insert(node.right, data)
            else:
                node.right = BSTnode(data)

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.data, end=' ')
            self.inorder(node.right)
            
    

    def finMin(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def finMax(self, node):
        current = node
        while current.right:
            current = current.right
        return current
    
    def height(self,root):
        if root is None :
            return 0
       
        return 1+max(self.height(root.left),self.height(root.right))
    
    def is_balanced(self,root):
        if root is None:
            return True 
        
        left_height =self.height(root.left) 
        right_height = self.height(root.right)
        
        if abs(left_height-right_height) > 1:
            return False
        left_balanced = self.is_balanced(root.left)
        right_balanced = self.is_balanced(root.right)
             
        return left_balanced and right_balanced
            
            


# ---------------- MAIN FUNCTION ----------------
if __name__ == "__main__":
    
    tree = BST()

   
    values = [1, 2, 3, 4, 5]
    for v in values:
        tree.insert(v)

   
    print("Inorder Traversal:")
    tree.inorder(tree.root)
    print()

   
    min_node = tree.finMin(tree.root)
    max_node = tree.finMax(tree.root)
    print(f"Minimum value: {min_node.data}")
    print(f"Maximum value: {max_node.data}")
    
    print(tree.is_balanced(tree.root))
