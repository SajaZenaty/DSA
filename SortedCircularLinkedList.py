from node import node
class SortedCircularLinkedList:
    def __init__(self):
        self.head = None
        
    def insert(self,data):
        new_node = node(data)
        #insertion if the list is empty
        if self.head is None:
            self.head=new_node
            new_node.next=self.head
            return
        
        current = self.head
        
        #insertion if the new node is smaller than the head
        if new_node.data < self.head.data:
           
            while current.next != self.head:
                current = current.next
            new_node.next = self.head
            current.next = new_node
            self.head = new_node
            return
        #insertion in the middle position or at the end
        while current.next != self.head and current.next.data<new_node.data:
            current = current.next
        new_node.next = current.next
        current.next = new_node
        
         
    
    
    def display(self):
            if self.head is None:
                print("List is empty.")
                return

            current = self.head
            while True:
                print(current.data, end=" -> ")
                current = current.next
                if current == self.head:
                    break
            print("(back to head)")
        
        
def main():
    ll = SortedCircularLinkedList()
    ll.insert(10)
    ll.insert(20)
    ll.insert(30)
    ll.insert(5)
    ll.insert(15)
    ll.insert(25)
    ll.display()
    
if __name__ == "__main__":
    main()       
            
            
        

           
                
                
            
            
                          
                   
                        
                                              
                        
            
                
        
    