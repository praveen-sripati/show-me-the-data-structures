# Problem 6: Union
# Design Choice:
I've used **Singly Linked List** to store the union or intersection of the two lists. To form a **Union**, first we have to make sets of the given linked lists i.e(llist_1 and llist_2) to make a set it will take O(n^2) because to traverse the list and if value is unique appending into the newly formed linked list.
Traversing of set of linked lists and appending it to union linked list will take O(n^2) time. Time complexity for **Intersection** is also similar to **Union**.


# Time complexity: O(n^2) for Union as well as Intersection
# Space complexity: O(n)