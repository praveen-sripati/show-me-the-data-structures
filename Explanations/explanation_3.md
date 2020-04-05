# Problem 3: Huffman Coding
# Design Choice:
I've used a **Binary Tree** to store the characters of the data as leaf nodes and sum of frequencies of nodes to form parent nodes and sum of parent nodes to form a root node. The value of left edge of a node will be given 0 and right will be given 1. These edges are traversed until a leaf node, the combined edge value is called huffman code which is the encoded data. I've used **Recursion** to create this binary tree. The time complexity for creating Binary Tree is O(n).

I've used **Priority Queue** to keep track of the BT Nodes and helps to create Binary Tree. The elements in this queue are sorted with their priorities which are frequencies in our case. The time complexity for appending element in this priority queue is O(nlogn).

# Time complexity: O(n + nlogn)
# Space complexity: O(n)