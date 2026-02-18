
import time
import threading

class Queue:
    def __init__(self):
        self.buffer = []
    
    def enqueue (self, value):
        self.buffer.insert(0, value)
        
    def dequeue (self):
        return self.buffer.pop()
        
    def is_empty(self):
        if len(self.buffer) == 0:
            return True
        else:
            return False
            
    # here we gonna define size limit function for the Queue
    def size(self):
        return len(self.buffer)

# Thread 1: Place orders every 0.5 seconds
def place_orders(q):
    orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']
    for order in orders:
        print(f"Placing order: {order}")
        q.enqueue(order)
        time.sleep(0.5)

# Thread 2: Serve orders every 2 seconds
def serve_orders(q):
    time.sleep(1)  # Start 1 second after place_orders
    
    while True:
        if not q.is_empty():
            order = q.dequeue()
            print(f"Serving order: {order}")
            time.sleep(2)
        else:
            # No more orders to serve
            break


# Main execution
q = Queue()

# Create threads
t1 = threading.Thread(target=place_orders, args=(q,))
t2 = threading.Thread(target=serve_orders, args=(q,))

# Start threads
t1.start()
t2.start()


t2.join()
print("All orders processed!")
