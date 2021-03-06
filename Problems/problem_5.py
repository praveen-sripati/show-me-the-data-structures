#!/usr/bin/env python
# coding: utf-8

# # Problem 5: Blockchain

# In[75]:


import hashlib
import datetime


# Block of BlockChain
class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(data)
        self.block_number = 0
        self.left = None
        self.right = None
        
    def calc_hash(self, data):
        sha = hashlib.sha256()
        hash_str = data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

# BlockChain implemented using Doubly Linked List         
class BlockChain:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.current_block = 0
    
    # Adds Block in BlockChain
    def add_block(self, data):
        
        if data == "" or data is None:
            return None
        
        # Creates timestamp - UTC (formerly GMT)
        timestamp = datetime.datetime.utcnow()
        timestamp = timestamp.strftime("%H:%M %d/%m/%Y")
        
        if self.head is None:  # If BlockChain has no elements
            previous_hash = None
            block = Block(timestamp, data, previous_hash)
            self.head = block 
            self.tail = block
            block.block_number = self.current_block
            self.current_block += 1
        else:  # If BlockChain has one or more elements
            previous_hash = self.tail.hash
            block = Block(timestamp, data, previous_hash)
            block.left = self.tail
            self.tail.right = block
            self.tail = block
            block.block_number = self.current_block
            self.current_block += 1
    
    # Pop a Block from the BlockChain
    def pop_block(self):
        if self.head is None: # If BlockChain has no elements
            return "Empty!"
        elif self.head.right is None:  # If BlockChain has only one element
            data = self.head.data
            self.head = None
            self.tail = None
            self.current_block -= 1
            return data
        else:   # If BlockChain has more than one element
            data = self.tail.data
            self.tail = self.tail.left
            self.tail.right = None
            self.current_block -= 1
            return data
        
    def get_head(self):
        return self.head
    
    def get_tail(self):
        return self.tail
    
    # Display blocks in a BlockChain
    def display(self):
        current_node = self.head
        if not current_node:
            return "Empty!"
        while current_node:
            print("----------------------------------------------------------------------------------")
            print("| Timestamp: " + str(current_node.timestamp) + (" " * (80-len(" Timestamp: " + str(current_node.timestamp)))) + "|" )
            print("| Data: " + str(current_node.data) + (" " * (80-len(" Data: " + str(current_node.data)))) + "|" )
            print("| SHA256 Hash: " + str(current_node.hash) + (" " * (80-len(" SHA256 Hash: " + str(current_node.hash)))) + "|" )
            print("| Prev_hash: " + str(current_node.previous_hash) + (" " * (80-len(" Prev_hash: " + str(current_node.previous_hash)))) + "|" )
            print("| Block_number: " + str(current_node.block_number) + (" " * (80-len(" Block_number: " + str(current_node.block_number)))) + "|" )
            print("----------------------------------------------------------------------------------")
            print("                                        ↓")
            if not current_node.right:
                print("                                       NULL")
            current_node = current_node.right
        


# # Test Cases

# In[76]:


block_chain = BlockChain()


# In[77]:


block_chain.add_block("Hello!")
block_chain.add_block("It's nice to meet u!")
block_chain.add_block("Have a nice day :)")


# In[78]:


block_chain.display()
# Expected Output: Hello! -> It's nice to meet u! -> Have a nice day :) ->


# In[79]:


block_chain.pop_block()
# Expected Output: Have a nice day :)


# In[80]:


block_chain.display()
# Expected Output: Hello! -> It's nice to meet u! ->


# In[81]:


block_chain.pop_block()
# Expected Output: It's nice to meet u!


# In[82]:


block_chain.display()
# Expected Output: Hello! ->


# In[83]:


block_chain.pop_block()
# Expected Output: Hello!


# In[84]:


block_chain.display()
# Expected Output: Empty!


# ## Edge Test Cases

# In[85]:


# Empty Input
block_chain.add_block("")
block_chain.display()
# Expected Output: It's Me Again xD ->


# In[86]:


# None Input
block_chain.add_block(None)
block_chain.display()
# Expected Output: It's Me Again xD ->


# In[87]:


# Large Input
large_input = ""
for i in range(10000):
    large_input += "a"

block_chain.add_block(large_input)
block_chain.display()

