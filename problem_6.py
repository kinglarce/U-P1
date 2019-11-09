class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string 


    def append(self, value):
        if value is None:
            return None

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    linked_list = LinkedList()
    uniq_dict = dict()
    
    llist_1_tail = llist_1.head
    while llist_1_tail:
        uniq_dict[llist_1_tail.value] = 0
        llist_1_tail = llist_1_tail.next
    
    llist_2_tail = llist_2.head
    while llist_2_tail:
        if llist_2_tail.value in uniq_dict:
            uniq_dict[llist_2_tail.value] = 1
        llist_2_tail = llist_2_tail.next
    
    for key, value in uniq_dict.items():
        if value > 0:
            linked_list.append(key)
    
    return linked_list

def intersection(llist_1, llist_2):
    # Your Solution Here
    linked_list = LinkedList()
    uniq_set = set()
    
    llist_1_tail = llist_1.head
    while llist_1_tail:
        uniq_set.add(llist_1_tail.value)
        llist_1_tail = llist_1_tail.next
    
    llist_2_tail = llist_2.head
    while llist_2_tail:
        uniq_set.add(llist_2_tail.value)
        llist_2_tail = llist_2_tail.next
        
    for value in uniq_set:
        linked_list.append(value)
    
    return linked_list

# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2)) # Expected: 4 -> 6 -> 21 ->
print (intersection(linked_list_1,linked_list_2)) # Expected: 32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 ->

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4)) # Expected: ""(Empty) since both the linkedlist has unique values
print (intersection(linked_list_3,linked_list_4)) # Expected: 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 ->

# Test case 3

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

linked_list_5.append(None)
linked_list_6.append(None)

print (union(linked_list_5,linked_list_6)) # Expected: ""(Empty)
print (intersection(linked_list_5,linked_list_6)) # Expected: ""(Empty)