class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BinaryTree:
    def __init__(self):
        self.root = None
        
def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left) , height(node.right))

def balance(node):
    if node is None:
        return 0
    return height(node.left) - height(node.right)

#Exercise 1: Validate AVL Tree
def isAVL(node):
    if node is None :
        return True
    if balance(node) not in [0,1,-1]:
        return False
    return isAVL(node.left) and isAVL(node.right)



#Exercise 2: Range Search in AVL Tree
def range_search(root,low,high):
    if root is None :
        return [] 
    my_list = []
    if root.data > low :
       my_list+= range_search(root.left,low,high)
    if low <= root.data <= high:
        my_list.append(root.data)
    if root.data < high:
        my_list += range_search(root.right, low, high)

    return my_list
#Exercise 3: Find k-th Smallest Element in AVL Tree 
def kth_smallest(root, k):

    def in_order(node):
        if not node:
            return []
        return in_order(node.left) + [node.data] + in_order(node.right)
    elements = in_order(root)

    if 1 <= k <= len(elements):
        return elements[k - 1]
    else:
        return "k is out of bounds"
 
def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

# --- TESTING ---
values = [40, 20, 60, 10, 30, 50, 70]
tree1 = BinaryTree()
for v in values:
    tree1.root = insert(tree1.root, v)

# Test Range Search
print("Range search (25 to 65):", range_search(tree1.root, 25, 65))  # Expected: [30, 40, 50, 60]

values = [50, 30, 70, 20, 40, 60, 80]
tree2 = BinaryTree()
for v in values:
    tree2.root = insert(tree2.root, v)
    
# Test kth smallest
print("4th smallest element:", kth_smallest(tree2.root, 4))  # Expected: 50

# Optional: Check if it's a valid AVL Tree
print("Is AVL Tree?:", isAVL(tree2.root))       