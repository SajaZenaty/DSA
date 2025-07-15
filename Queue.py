from node import node
# This code implements a queue using a linked list.
class Queue_LinkedList:
    def __init__(self):
        self.front=None
        self.rear=None
        self.size=0
        
        
#Time Complexity: O(1) for enqueue and dequeue   
    def enqueue(self,data):
        new_node=node(data)
        if self.size == 0:
            self.front=self.rear=new_node
        else:
            self.rear.next=new_node
            self.rear=new_node
        self.size+=1
        
    def dequeue(self):
        if self.size==0:
            return None
        removed_node = self.front.data
        self.front=self.front.next
        self.size-=1
        return removed_node
            
    def peek(self):
        if self.size==0:
            return None
        return self.front.data
    
    def is_empty(self):
        return self.size==0
    
    def get_size(self):
        return self.size
    
    def __str__(self):
        current=self.front
        st  = 'Queue: '
        while current:
            st += str(current.data) + ' -> '
            current = current.next
        st += 'None'
        return st
    
# This code implements a queue using simple array.   
class Queue_array:
    def __init__(self,capacity):
        self.capacity = capacity
        self.size=0
        self.queue = [None] * capacity
        self.front =0
        self.rear = 0 
        
         
    def is_empty(self):
        return self.size==0
    
    def is_full(self):
        return self.size == self.capacity
    
    def enqueue(self,data):
        if self.is_full():
            return "Queue is full"
        self.queue[self.rear]=data
        self.rear+=1
        self.size+=1
        
    def dequeue(self):
        if self.is_empty():
            return "Queue is Empty"
        removed_element = self.queue[self.front]
        self.front+=1
        self.size-=1
        return removed_element
            
# This code implements a queue using a circular array.       
class Queue_circular_array():  
    def __init__(self,capacity):
        self.capacity = capacity
        self.size=0
        self.queue = [None] * capacity
        self.front =0
        self.rear = 0 
        
         
    def is_empty(self):
        return self.size==0
    
    def is_full(self):
        return  self.size == self.capacity 
    
    def enqueue(self,data):
        if self.is_full():
            return "Queue is full"
        self.queue[self.rear]=data
        self.rear = (self.rear + 1)% self.capacity
        self.size+=1
        
    def dequeue(self):
        if self.is_empty():
            return "Queue is Empty"
        removed_element = self.queue[self.front]
        self.queue[self.front]=None
        self.front=(self.front+1)%self.capacity
        self.size-=1
        return removed_element
    
    def peek(self):
        if self.is_empty():
            return None
        return self.queue[self.front]
    
    def __str__(self):
        if self.is_empty():
            return "Queue: Empty"

        result = "Queue: "
        index = self.front
        for _ in range(self.size):
            result += str(self.queue[index]) + " -> "
            index = (index + 1) % self.capacity
        result += "None"
        return result

                

if __name__ == "__main__":
    queue = Queue_LinkedList()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print(queue) 
    print(queue.dequeue())  
    print(queue.peek())  
    print(queue.is_empty())  
    print(queue.get_size()) 
    print(queue) 
    print('-----------------------')
    queue2 = Queue_circular_array(5)
    queue2.enqueue(10)
    queue2.enqueue(20)
    queue2.enqueue(30)
    print(queue2) 
    print(queue2.dequeue()) 
    queue2.enqueue(40)
    print(queue2.peek())  
    print(queue2.is_empty())  
    
    print(queue2) 
    
    
     
    
        
        