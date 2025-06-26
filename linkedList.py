from node import node
class linkedlist:
    def __init__(self):
        self.head=None
        self.length = 0
        
#Time Complexity O(1)
    def insert_at_start(self,data):
        new_node = node(data)
        new_node.next= self.head
        self.head=new_node
        self.length += 1
        
#Time Complexity O(n)        
    def insert_at_end(self,data):
        new_node = node(data)
        if self.head is None :
            self.head= new_node
            self.length += 1
            return
        current= self.head
        while  current.next is not None:
             current =  current.next 
        current.next = new_node
        self.length += 1
        
#Time Complexity O(n)
    def insert_at_index(self,index,data):
        new_node= node(data)
        if index == 0:
            self.insert_at_start(data)
            return 
        count = 0 
        current=self.head     
        while current is not None and count<index - 1:
            current = current.next
            count += 1
        if current is None:
            print("Index out of bounds , Insertion at last")
            self.insert_at_end(data)
            return
        new_node.next = current.next
        current.next = new_node
        self.length += 1
 
#Time Complexity O(1)       
    def  delete_from_start(self):
        if self.head is None:
            print("List is empty ")
            return
        self.head = self.head.next
        self.length -= 1
        
#Time Complexity O(n)   
    def delete_from_end(self):
        if self.head is None:
            print("List is empty ")
            return
        if self.head.next is None:
            self.head = None
            self.length -= 1
            return
        current = self.head
        while current.next.next is not None:
            current=current.next
            
        current.next = None
        self.length -= 1
        
#Time Complexity O(n)      
    def delete_node(self,data):
        if self.head is None:
            print("List is empty ")
            return
        if self.head.data == data:
            self.head = self.head.next
            self.length -= 1
            return
        current = self.head
        while current.next is not None and current.next.data != data:
            current = current.next
        if current.next is None:
            print("Node with data", data, "not found.")
            return
        current.next = current.next.next
        self.length -= 1
  
#Time Complexity O(n)      
    def find_middle(self):
        if self.head is None:
            return None
        slow = fast = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow.data
    
#Time Complexity O(n) 
    @staticmethod
    def merge_two_sorted_lists(ls1: "linkedlist", ls2: "linkedlist") -> "linkedlist":
        new_list = linkedlist()
        current1 = ls1.head
        current2 = ls2.head

        while current1 and current2:
            if current1.data < current2.data:
                new_list.insert_at_end(current1.data)
                current1 = current1.next
            else:
                new_list.insert_at_end(current2.data)
                current2 = current2.next

        while current1:
            new_list.insert_at_end(current1.data)
            current1 = current1.next

        while current2:
            new_list.insert_at_end(current2.data)
            current2 = current2.next

        return new_list

        
                    
        
        
        
#Time Complexity O(n)           
    def remove_duplicates(self):
        current = self.head
        while current is not None and current.next is not None:
            if current.data == current.next.data:
                current.next = current.next.next
            else:
                current = current.next   
        return self 
    
#Time Complexity O(n)                
    def  reverse(self): 
        if self.head is None:
            print("The linked list is Empty ")
            return 
        if self.head.next is None:
            return self
        prev = None
        current = self.head
        
        while current is not None:
            after = current.next
            current.next = prev
            prev = current
            current = after 
        self.head = prev
        return self
    
            
          
#Time Complexity O(n)        
    def search(self,data):
        current=self.head
        while current is not None:
            if current.data==data:
                return True
            current = current.next
        return False
    
    
            
                    
    
            
                
        
        
    def __str__(self):
            current = self.head
            result = []
            while current is not None:
                result.append(current.data)
                current = current.next
            return " -> ".join(map(str, result))
        
        