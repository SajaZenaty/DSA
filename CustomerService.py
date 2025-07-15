from node import node
from Queue import Queue_LinkedList
class customer_service():
    def __init__(self):
        self.service_Queue = Queue_LinkedList()
        
    def arrive_customer(self,name):
        self.service_Queue.enqueue(name)
        print(f"Arriving:{name}")
       
        
    def serving_customers(self):
        while not self.service_Queue.is_empty():
            served = self.service_Queue.dequeue()
            print(f"Serving: {served}")
        print("All customers served.")
        
if __name__=="__main__":
    c =customer_service()
    c.arrive_customer('Alice') 
    c.arrive_customer('Bob')
    c.arrive_customer('Carol')
    c.serving_customers()
   


    
        
        
        
        
    