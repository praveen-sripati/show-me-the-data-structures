# Problem 4: Active Directory
# Design Choice:
Directories are in the form of trees thus, I've used **Recursion** to traverse groups to find the user in a group. I've used recursion in a loop thus worst case time complexity would be O(2^n).

# Time complexity: O(2^n)
# Space complexity: O(maximum_depth * users)