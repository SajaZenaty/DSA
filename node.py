class node :
# each node in linked list has data item and address of the next node 
# by default we put next as None
    def __init__(self,data):
        self.data = data
        self.next = None