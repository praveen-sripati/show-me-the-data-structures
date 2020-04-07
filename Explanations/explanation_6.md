# Problem 6: Union
# Design Choice:
I've used **Singly Linked List** to store the union or intersection of the two lists. To form a **Union**, first we have to make sets of the given linked lists and i've used set() in python to form sets. Iterating over two of these sets and appending unique values in a LL which are present in it will give us a union of the given lists. To form **Intersection**,Make sets of the given lists and Iterating over two of these sets and appending common values in a LL which are present in it will give us an LL of Intersection of the given lists.


# Time complexity:
**O(n)** for iterating linked lists to make sets, for iterating sets to form Linked Lists(Union or Intersection) and appending elements in a Linked List.
# Space complexity:
**O(n)** to Store linked list of Union or Intersection.