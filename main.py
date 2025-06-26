from linkedList import linkedlist
def main():
    ll = linkedlist()
    ll.insert_at_end(10)
    ll.insert_at_end(20)
    ll.insert_at_end(60)
    ll.insert_at_end(30)
    ll.insert_at_end(40)
    ll.insert_at_end(50)
    
    print("linked list before Reversing :")
    print(ll)
    
    print("linked list after Reversing :")
    print(ll.reverse())
 
    
   
    

if __name__ == "__main__":
    main()  