# Problem 1: LRU Cache
# Design Choice:
I've used **Doubly Linked List Queue** to store the data because we can easily set the value by enqueueing the value in queue, if capacity of queue is full than we can dequeue the element present in the queue and enqueue the new element into the queue.

And Used **Dictionary** to track the elements present in the DLL queue. It has a key and value which is the DLLNode. Dictionary takes O(1) time to access the elements present in the DLL queue using keys. Thus, I've chosen this data structures to address this problem.

# Time complexity:
The time complexity of enqueueing and dequeueing of DLL Queue is **O(1)** and adding elements in a dictionary is **O(1)**.

# Space complexity:
**O(n)** because a DLL Queue is used to store elements and a Dictionary to keep track of that element.