# Problem 4: Active Directory
# Design Choice:
Directories are in the form of trees and Active Directory consist of groups and users of that group which is similar to a directory structure. Thus, I've used **Recursion** to traverse groups to find the user in a group.

# Time complexity:
**O(mn)** where m is the number of users group and n is the number of sub-groups in a group
# Space complexity:
**O(mn)** to hold m users and n groups