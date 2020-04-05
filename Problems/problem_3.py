#!/usr/bin/env python
# coding: utf-8

# # Problem 3: Huffman Coding

# In[2]:


# Binary Tree Node
class Node(object):
        
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None
        
    def set_value(self, value):
        self.value = value
        
    def get_value(self):
        return self.value
        
    def set_left_child(self, left):
        self.left = left
        
    def set_right_child(self, right):
        self.right = right
        
    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None
    
    def has_right_child(self):
        return self.right != None

    
# Priority queue for tracking nodes
class PriorityQueue:
    
    def __init__(self):
        self.queue = list()
        
    def push(self, data):
        self.queue.append(data)
        self.queue = sorted(self.queue, key=lambda node: node.value)
    
    def pop(self):
        return self.queue.pop(0)
    
    def size(self):
        return len(self.queue)
    

# Binary Tree for huffman coding
class BinaryTree:
    
    def __init__(self):
        self.root = None
        
    def set_root(self, node):
        self.root = node
        
    def get_root(self):
        return self.root


# In[49]:


import sys

# Data encoding
def huffman_encoding(data):
    
    #Assign priority queue to hold characters with their frequency
    p_queue = PriorityQueue()
    
    #Find frequencies of each character
    frequencies = find_frequency(data)
    
    #if data contains only one character with frequency one or more 
    if len(frequencies) == 1:
        btree = BinaryTree()
        btree.root = Node([data[0], frequencies[data[0]]])
        encoded_data = "1" * frequencies[data[0]]  # Assign huffman code '1' for this single character
        return encoded_data, btree
        
        
    #Push a Node obj of list having characters with their frequency into priority queue
    for key, value in frequencies.items():
        p_queue.push(Node([value, key]))
    
    #Create a binary tree
    btree = binary_tree(p_queue)
    
    #Create a huffman codes dictionary having character as a key
    #and value as a code of that key
    codes = dict()
    huffman_codes(btree.get_root(), codes, code = '')
    
    #Encode data
    encoded_data = ''
    for char in data:
        encoded_data += codes[char]
    
    return encoded_data, btree
        
# Data Decoding
def huffman_decoding(encoded_data, tree):
    
    #Assign a variable to store the decoded data
    decoded_data = ''
    
    #Used for traversing
    current_node = tree.root
    
    # If the tree has only one node
    if not (current_node.has_left_child() and current_node.has_right_child()):
        for i in range(len(encoded_data)):
            decoded_data += current_node.value[0]
        return decoded_data
    
    for i in range(len(encoded_data)):
        
        #if edge value is 0 then traverse left of the tree
        if encoded_data[i] == '0':    
            current_node = current_node.left
        #if edge value is 1 then traverse right of the tree
        elif encoded_data[i] == '1':    
            current_node = current_node.right

        #if the current_node is a leaf node then it adds the character to the decoded_data
        #and make current_node pointer to point root node for re-traversing
        if current_node.left is None and current_node.right is None:
            decoded_data += current_node.value[1]
            current_node = tree.root
        
    return decoded_data

# Helper function to create Binary tree
def binary_tree(p_queue):
    
    binary_tree = BinaryTree()
    
    while True:
        
        #Run loop until the size or length of priority queue is > 1
        if p_queue.size() <= 1:
            p_queue.pop()
            return binary_tree
        
        #Pop nodes in priority queue as first and second nodes
        first_node = p_queue.pop()
        second_node = p_queue.pop()
    
        #Create parent node with "*" as a character and sum of both nodes as a value
        parent_node = [first_node.value[0] + second_node.value[0], "*"]
        parent_node = Node(parent_node)
        
        #Set left and right child of the parent node
        parent_node.set_left_child(first_node)
        parent_node.set_right_child(second_node)
        
        #Make parent node as root node
        binary_tree.set_root(parent_node)
        
        #Push parent node into priotity queue
        p_queue.push(parent_node)
        
# Helper function to retrieve huffman codes from Binary Tree 
def huffman_codes(root, codes, code):
    # If node is a leaf node
    if not (root.has_left_child() and root.has_right_child()):
        data = root.get_value()
        key = data[1]
        codes[key] = code
        return
    # Traversing left node
    huffman_codes(root.left, codes, code + '0')
    # Traversing right node
    huffman_codes(root.right, codes, code + '1')

# Helper function to find the frequencies of the characters
def find_frequency(data):   
    # frequencies with their character as key
    frequencies = {}
    for char in data:
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1
            
    return frequencies


# # Test Cases

# In[50]:


if __name__ == "__main__":
    
    a_great_sentence = "The bird is the word" #The bird is the word

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))


# In[51]:


a_great_sentence = "hello world"

print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
print ("The content of the data is: {}\n".format(a_great_sentence))

encoded_data, tree = huffman_encoding(a_great_sentence)

print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print ("The content of the encoded data is: {}\n".format(decoded_data))


# In[56]:


a_great_sentence = "aaaa"

print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
print ("The content of the data is: {}\n".format(a_great_sentence))

encoded_data, tree = huffman_encoding(a_great_sentence)

print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print ("The content of the encoded data is: {}\n".format(decoded_data))

