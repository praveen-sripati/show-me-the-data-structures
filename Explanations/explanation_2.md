# Problem 1: File Recursion
# Design Choice:
I've used a **List** to store the paths of the file which are found. It takes O(n) time to append the path in the list.

I've used **Recursion** to traverse the directories of the given path. Recursion is useful for traversing tree like structures which is similar to directory structure. Thus, I've used recursion to traverse the directories. Time complexity is O(2^n) as i used recursion in a loop.

# Time complexity: O(2^n)
# Space complexity: O(n)