#!/usr/bin/env python
# coding: utf-8

# # Problem 6: Union and Intersection

# In[2]:


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
        return remove_duplicates(llist_2)
    elif llist_2_curr is None:  # If list_2 is empty return union of the list
        return remove_duplicates(llist_1)
    else:  # If Both lists has elements return union of both the lists
        llist_union = LinkedList()
        llist_union_dict = {}
        
        llist_1_set = remove_duplicates(llist_1) # Removes duplicates of list_1
        llist_2_set = remove_duplicates(llist_2) # Removes duplicates of list_2
        
        llist_1_set_curr = llist_1_set.head
        llist_2_set_curr = llist_2_set.head
        
        while llist_1_set_curr:  # Appends list1 elements in the Union LinkedList
            llist_union_dict[llist_1_set_curr.value] = llist_1_set_curr.value
            llist_union.append(llist_1_set_curr)
            llist_1_set_curr = llist_1_set_curr.next
            
        while llist_2_set_curr:  # Appends list2 elements in the Union LinkedList if they are not in list1
            if not llist_2_set_curr.value in llist_union_dict:
                llist_union.append(llist_2_set_curr.value)
            llist_2_set_curr = llist_2_set_curr.next
                
        return llist_union
    
def intersection(llist_1, llist_2):

    llist_1_curr = llist_1.head
    llist_2_curr = llist_2.head
    
    # If one of the list is empty returns None
    if llist_1_curr is None or llist_2_curr is None:
        return None
    else: 
        # Checks list size for optimization
        # if list_1 is having less size than
        # we just traverse list_1 cuz we will
        # traverse less nodes
        if llist_1.size() < llist_2.size():  
            llist_intersec = llist_intersection(llist_1, llist_2)
            if llist_intersec.head:
                return llist_intersec
            else:
                return None
        elif llist_2.size() < llist_1.size(): # If llist_2 size is less than llist_1
            llist_intersec = llist_intersection(llist_2, llist_1)
            if llist_intersec.head:
                return llist_intersec
            else:
                return None
        
# Helper function to remove duplicates from the llist returns llist
def remove_duplicates(llist):    
    llist_set = LinkedList()
    llist_dict = dict()
    
    llist_curr = llist.head
    while llist_curr:
        if not llist_curr.value in llist_dict:
            llist_dict[llist_curr.value] = llist_curr.value
            llist_set.append(llist_curr.value)
        llist_curr = llist_curr.next
    return llist_set

# Helper function for finding intersection of two lists returns llist of intersection
def llist_intersection(llist_one, llist_two):
    
    llist_intersec = LinkedList()  
    llist_dict = {}
    llist_one_set = remove_duplicates(llist_one) # Removes duplicates of llist_1
    llist_two_set = remove_duplicates(llist_two) # Removes duplicates of llist_2
    
    llist_one_curr = llist_one_set.head
    llist_two_curr = llist_two_set.head
    
    while llist_one_curr: # Traverse llist_1
        llist_dict[llist_one_curr.value] = llist_one_curr.value  # Adds llist_1 elements to dictionary
        llist_one_curr = llist_one_curr.next
    
    while llist_two_curr: # Traverse llist_2
        if llist_dict.get(llist_two_curr.value):  # Checks if list_2 element is present in dictionary
            llist_intersec.append(llist_two_curr.value)  # Appends element if it is common in both lists
        llist_two_curr = llist_two_curr.next
        
    return llist_intersec


# # Test Cases

# In[3]:


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
#   Union - 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 32 -> 9 -> 1 -> 11 -> 21 ->
#   Intersection - 6 -> 4 -> 


# In[4]:


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
#   Union - 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> 32 -> 9 -> 1 -> 11 -> 
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


# In[6]:


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


# In[7]:


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
#   Intersection - 3 -> 2 ->


# In[3]:


# Test Case 6

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
#   Union - 2 -> 3 ->   
#   Intersection - 3 -> 2 ->

