#!/usr/bin/env python
# coding: utf-8

# # Problem 6: Union and Intersection

# In[1]:


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
    
    llist_union = LinkedList()
    llist_1_curr = llist_1.head
    llist_2_curr = llist_2.head
    
    # If Both lists are empty return None
    if llist_1_curr is None and llist_2_curr is None:
        return None
    
    if llist_1_curr is None:  # If list_1 is empty return union of the list
        llist_2_set = remove_duplicates(llist_2)
        for value in llist_2_set:
            llist_union.append(value)
        return llist_union
        
    elif llist_2_curr is None:  # If list_2 is empty return union of the list
        llist_1_set = remove_duplicates(llist_1)
        for value in llist_1_set:
            llist_union.append(value)
            
    else:  # If Both lists has elements return union of both the lists
        
        llist_1_set = remove_duplicates(llist_1) # Removes duplicates of list_1
        llist_2_set = remove_duplicates(llist_2) # Removes duplicates of list_2
        
        for value in llist_1_set:
            llist_union.append(value)
        
        for value in llist_2_set:
            if value not in llist_1_set:
                llist_union.append(value)
                
        return llist_union
    
def intersection(llist_1, llist_2):
    
    llist_intersection = LinkedList()

    llist_1_curr = llist_1.head
    llist_2_curr = llist_2.head
    
    # If one of the list is empty returns None
    if llist_1_curr is None or llist_2_curr is None:
        return None
    
    else: 
        llist_1_set = remove_duplicates(llist_1) # Removes duplicates of list_1
        llist_2_set = remove_duplicates(llist_2) # Removes duplicates of list_2
        
        for value in llist_1_set:
            if value in llist_2_set:
                llist_intersection.append(value)
        
        return llist_intersection
        
# Helper function to remove duplicates from the llist returns set
def remove_duplicates(llist):    
    llist_set = set()
    
    llist_curr = llist.head
    while llist_curr:
        llist_set.add(llist_curr.value)
        llist_curr = llist_curr.next
        
    return llist_set


# # Test Cases

# In[2]:


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Expected Output: 
#   Union - 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 32 -> 1 -> 9 -> 11 -> 21 -> 
#   Intersection - 4 -> 6 -> 


# In[3]:


# Test case 2

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Expected Output: 
#   Union - 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 21 -> 32 -> 1 -> 9 -> 11 -> 
#   Intersection - 4 -> 6 -> 21 -> 


# In[5]:


# Test case 3

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

# Expected Output: 
#   Union - 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 
#   Intersection - None


# In[4]:


# Test case 4

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [2,3]
element_2 = [3,2,2]

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print (union(linked_list_5, linked_list_6))
print (intersection(linked_list_5, linked_list_6))

# Expected Output: 
#   Union - 2 -> 3 ->   
#   Intersection - 3 -> 2 ->


# # Edge Test Cases

# In[5]:


# Test case 5

linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = []
element_2 = [3,2,2]

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

print (union(linked_list_7, linked_list_8))
print (intersection(linked_list_7, linked_list_8))

# Expected Output: 
#   Union - 2 -> 3 ->   
#   Intersection - None


# In[7]:


# Test Case 6 - Empty lists

linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

print (union(linked_list_7, linked_list_8))
print (intersection(linked_list_7, linked_list_8))

# Expected Output: 
#   Union - None
#   Intersection - None


# In[12]:


# Test Case 7 - Large Input

linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_1 = [_ for _ in range(5000)]
element_2 = [_ for _ in range(5000)]

for i in element_1:
    linked_list_7.append(i)

for i in element_2:
    linked_list_8.append(i)

print("Union")
print (union(linked_list_7, linked_list_8))
print()
print("Intersection")
print (intersection(linked_list_7, linked_list_8))

# Expected Output: 
#   Union - None
#   Intersection - None


# In[ ]:




