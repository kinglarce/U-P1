class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

import hashlib

class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(data)

    def calc_hash(self, data):
        sha = hashlib.sha256()
        hash_str = data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()
    
    def update(self, timestamp, new_data):
        self.timestamp = timestamp
        self.data = new_data
        self.hash = self.calc_hash(new_data)

import datetime  

timestamp = datetime.datetime.now(datetime.timezone.utc).strftime("%H:%M %m/%d/%Y %Z")

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def get_node(self, value, prev_hash=None):
        block = Block(timestamp, value, prev_hash)
        return Node(block)
        
    def add(self, value):
        if value is None:
            return None

        if self.head is None:
            self.head = self.get_node(value)
            self.tail = self.head 
            return self.head.value.hash
        
        tail = self.tail
        tail.next = self.get_node(value, tail.value.hash)
        self.tail = tail.next

        return tail.next.value.hash
    
    def get_latest(self):
        if self.head is None:
            return 'No record'
        
        tail = self.head
        while tail.next:
            tail = tail.next
        return tail.value.data
    
    def update(self, hash, new_data):
        tail = self.head
        while tail:
            if tail.value.hash == hash:
                tail.value.update(timestamp, new_data)
                return tail.value.data
            tail = tail.next
        return 'No record'
    
    def is_chain_valid(self):
        if self.head is None:
            return 'No record'
        tail = self.head
        while tail.next:
            if tail.value.hash != tail.next.value.previous_hash:
                return False
            tail = tail.next
        
        return True

# Test case 1

blockchain = LinkedList()
print(blockchain.add('data1'))
print(blockchain.add('data2'))
print(blockchain.add('data3'))
print(blockchain.add('data4'))
print(blockchain.get_latest()) # Expected: data4
print(blockchain.is_chain_valid()) # Expected: True

# Test case 2

blockchain = LinkedList()
print(blockchain.add('input1'))
print(blockchain.add('input2'))
print(blockchain.add('input3'))
print(blockchain.is_chain_valid()) # Expected: True
blockchain.update('124d8541ff3d7a18b95432bdfbecd86816b86c8265bff44ef629765afb25f06b', 'ZZZZ')
print(blockchain.is_chain_valid()) # Expected: False

# Test case 3

blockchain = LinkedList()
print(blockchain.add(None)) # Expected: None
print(blockchain.add(None)) # Expected: None
print(blockchain.add('input3')) # Expected: <The hash value of "input3"> 
