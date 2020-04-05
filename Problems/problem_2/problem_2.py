import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    # list of paths which has the file
    file_path_list = list()
    file_recursion(suffix, path, file_path_list)
    return file_path_list

def file_recursion(suffix, path, file_path_list):

    try :
        for file in os.listdir(path):
            if os.path.isdir(os.path.join(path, file)):  # If directory is present traverse into that directory
                file_recursion(suffix, os.path.join(path, file), file_path_list)
            elif os.path.isfile(os.path.join(path, file)) and file.endswith(suffix): # If file is present than append path of file to the list
                file_path = os.path.join(path, file)
                file_path_list.append(file_path)
    except FileNotFoundError: # If file is not found
        file_path_list.append("Path Not Found!!")

#TEST CASE 1
print()
print(find_files('.c', '.'))
#EXPECTED OUTPUT - ['.\\subdir1\\a.c', '.\\subdir3\\subsubdir1\\b.c', '.\\subdir5\\a.c', '.\\t1.c']

#TEST CASE 2
print()
print(find_files('.h', '.'))
#EXPECTED OUTPUT - ['.\\subdir1\\a.h', '.\\subdir3\\subsubdir1\\b.h', '.\\subdir5\\a.h', '.\\t1.h']

print()
#TEST CASE 3
print(find_files('.py', '.'))
#EXPECTED OUTPUT - ['.\\problem_2.py']

print()
#TEST CASE 4
print(find_files('.txt', '.'))
#EXPECTED OUTPUT - []

print()
#TEST CASE 5
print(find_files('.txt', './something'))
#EXPECTED OUTPUT - ['Path Not Found!!']
