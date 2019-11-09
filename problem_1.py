class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        

class LRU_Cache:

    def __init__(self, capacity):
        # Initialize class variables
        self.hashtable = dict()
        self.total_items = 0
        self.capacity = capacity
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        node = self.hashtable.get(key)
        
        if node is None:
            return -1
        
        self.move_to_front(node)
        self.print_list()
        return node.value

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        node = self.hashtable.get(key)
        
        if node is None:
            new_node = Node(key, value)
            
            self.hashtable[key] = new_node
            self.add_front(new_node)
            self.total_items += 1
            
            if self.total_items > self.capacity:
                self.remove_entry()
            
        else:
            node.value = value
            self.move_to_front(node)
            
        self.print_list()
       
    def move_to_front(self, node):
        self.remove_back(node)
        self.add_front(node)
    
    def remove_entry(self):
        tail = self.pop_tail()
        del self.hashtable[tail.key]
        self.total_items -= 1
        
    def pop_tail(self):
        tail_item = self.tail.prev
        self.remove_back(tail_item)
        
        return tail_item
    
    def remove_back(self, node):
        # Re-wire the node for removing the prev
        saved_prev = node.prev
        saved_next = node.next
        
        saved_prev.next = saved_next
        saved_next.prev = saved_prev
    
    def add_front(self, node):
        # Wire up the new node being to be inserted
        
        # Wire the current node prev to the head
        node.prev = self.head;
        # Wire the current node next to the previous head next
        node.next = self.head.next;
        # Wire the previous head next previous value to the current node
        self.head.next.prev = node;
        # Wire the head next to the current node
        self.head.next = node;
        
    def print_list(self):
        head = self.head
        print('====')
        while head:
            print(head.value)
            head = head.next
        print('====')

our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
