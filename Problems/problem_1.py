#!/usr/bin/env python
# coding: utf-8

# # Problem 1: LRU Cache

# In[120]:


# Doubly Linked List Node
class DLLNode:
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

        
# Implementing LRU_Cache using Doubly Linked List
class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.current_size = 0
        self.keys = dict()
        self.head = None
        self.tail = None
    
    # Get an LRU element from the cache
    def get(self, key):
        
        # Retrieve item from provided key. Return -1 if nonexistent.
        if not self.keys.get(key) or self.capacity == 0:
            return -1
        
        node = self.keys.get(key)
        if node: # If key is present
            if node == self.head: # If element is present at the head
                if self.head.right is not None: # If list having more than two elements
                    self.tail.right = self.head
                    self.head = self.head.right
                    self.tail = self.tail.right
                    self.tail.right = None
                    self.head.left = None
                    return node.value
                else: # If list having only one element
                    return node.value
            elif node == self.tail: # If element is present at the tail end
                return node.value
            elif node.left and node.right: # Element present at the rest of the position
                node.left.right = node.right
                node.right.left = node.left
                self.tail.right = node
                node.left = self.tail
                node.right = None
                self.tail = node
                return node.value

        return -1
                
    # Set an element in the cache
    def set(self, key, value):
        if self.capacity == 0:
            return None
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if not self.keys.get(key): # Check whether the key is present in List
            node = DLLNode(key, value)
            if self.current_size < self.capacity:  # If the cache is not at its capacity
                self.keys[key] = node
                if self.head is None: # If cache is empty
                    self.head = node
                    self.tail = node
                    self.current_size += 1
                else: # If cache having elements
                    self.tail.right = node
                    node.left = self.tail
                    self.tail = self.tail.right
                    self.current_size += 1
            elif self.current_size >= self.capacity:  # If the cache is at its full capacity
                self.keys[key] = node
                lru_key = self.head.key
                if self.head.right is None:
                    self.head = node
                    self.tail = node
                    del self.keys[lru_key]
                    return
                self.head = self.head.right
                self.head.left = None
                del self.keys[lru_key]
                self.tail.right = node
                node.left = self.tail
                self.tail = node
                self.tail.right = None
        else: # If the key is already present in cache
            self.keys[key].value = value
            self.get(key)
            return
        
    # Display elements present in the cache
    def display(self):
        currentNode = self.head
        if currentNode is None:
            return print(None)
        while currentNode is not None:
            print(currentNode.value, end=' ')
            currentNode = currentNode.right
            


# # Test Cases

# In[121]:


our_cache = LRU_Cache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.display()
# Expected Output: 1 2 3


# In[122]:


our_cache.set(4, 4);
our_cache.display()
# Expected Output: 1 2 3 4


# In[123]:


our_cache.get(1)
# Expected Output: 1


# In[124]:


our_cache.get(2)
our_cache.display()
# Expected Output: 3 4 1 2


# In[125]:


our_cache.get(9)
# Expected Output: -1


# In[126]:


our_cache.set(5, 5);
our_cache.display()
# Expected Output: 3 4 1 2 5


# In[127]:


our_cache.set(6, 6);
our_cache.display()
# Expected Output: 4 1 2 5 6


# In[128]:


our_cache.set(4,5)
our_cache.display()
# Expected Output: 1 2 5 6 5


# In[129]:


our_cache.get(6)
# Expected Output: 6


# In[130]:


our_cache.get(3)
our_cache.display()
# Expected Output: 4 1 2 5 6


# In[131]:


our_cache.get(5)
# Expected Output: 5


# In[132]:


our_cache.display()
# Expected Output: 1 2 5 6 5


# In[133]:


our_cache.set(23, 33)
our_cache.display()
# Expected Output: 2 5 6 5 33


# In[134]:


our_cache.get(3)
# Expected Output: -1


# In[135]:


our_cache.set(4,5)
our_cache.display()
# Expected Output: 2 6 5 33 5


# # Edge Test Cases

# In[136]:


# Case 1 - Cache capacity 1

our_cache = LRU_Cache(1)


# In[137]:


our_cache.set(1, 1)
our_cache.display()


# In[138]:


our_cache.set(2, 2)
our_cache.display()
# Expected Output: 1 2


# In[139]:


our_cache.set(3, 3)
our_cache.display()
# Expected Output: 2 3


# In[140]:


our_cache.set(2, 4)
our_cache.display()
# Expected Output: 3 4


# In[141]:


our_cache.get(2)


# In[146]:


our_cache.get(2)


# In[147]:


# Case 2 - Empty Cache

our_cache = LRU_Cache(0)


# In[148]:


our_cache.set(1, 1)
our_cache.display()


# In[150]:


our_cache.set(2, 2)
our_cache.display()


# In[149]:


our_cache.get(1)


# In[168]:


# Case 3 - Large Capacity

our_cache = LRU_Cache(5000)


# In[169]:


for i in range(5000):
    our_cache.set(i, i)


# In[170]:


our_cache.display()


# In[171]:


our_cache.get(0)
our_cache.get(254)


# In[172]:


our_cache.display()

