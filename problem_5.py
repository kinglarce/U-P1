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
        
    def get_node(self, value, prev_hash=None):
        block = Block(timestamp, value, prev_hash)
        return Node(block)
        
    def add(self, value):
        if self.head is None:
            self.head = self.get_node(value)
            return
        
        tail = self.head
        while tail.next:
            tail = tail.next
        
        tail.next = self.get_node(value, tail.value.hash)
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

blockchain = LinkedList()
print(blockchain.add('data1'))
print(blockchain.add('data2'))
print(blockchain.add('data3'))
print(blockchain.add('data4'))
print(blockchain.get_latest())
print(blockchain.is_chain_valid())
# blockchain.update('ac56d2314f002b1bb8e72dcace35b1805d7e58bda6033ebfbf7c35f35df4d24e', 'zzz')
# blockchain.is_chain_valid()