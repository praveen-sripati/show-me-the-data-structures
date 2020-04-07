# Problem 3: Huffman Coding
# Design Choice:
I've used a **Binary Tree** to store the characters of the data as leaf nodes and sum of frequencies of nodes to form parent nodes and sum of parent nodes to form a root node. The value of left edge of a node will be given 0 and right will be given 1. These edges are traversed until a leaf node, the combined edge value is called huffman code which is the encoded data. I've used **Recursion** to create this binary tree.

I've used **Priority Queue** to keep track of the BT Nodes and helps to create Binary Tree. The elements in this queue are sorted with their priorities which are frequencies in our case.

# Time complexity:
**O(n)** because i've constantly used data when determining frequencies, building binary tree, creating huffman codes, creating encoded data, creating decoded data.
**O(nlogn)** building priority queue as i've used sorted() function in append method of priority queue.

# Space complexity:
**O(n)** storing the binary tree, priority queue and lists.
**O(1)** for rest of the data.