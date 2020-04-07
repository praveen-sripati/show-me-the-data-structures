# Problem 1: File Recursion
# Design Choice:
I've used a **List** to store the paths of the file which are found and **Recursion** to traverse the directories of the given path. Recursion is useful for traversing tree like structures which is similar to directory structure.

# Time complexity:
**O(mn)** where m is the number of directories and n is the files in that directory

# Space complexity:
**O(mn)** where m directories to hold in memory and n files to hold in memory